import spacy
import pandas as pd
from pymilvus import MilvusClient, connections, CollectionSchema, FieldSchema, DataType, Collection, utility
from milvus import default_server

default_server.start()

nlp = spacy.load("en_core_web_md")

df = pd.read_csv('npodatabase.csv')  

def get_vector(text):
    if isinstance(text, str):  # Check if the input is a string
        doc = nlp(text)
        return doc.vector
    else:
        return None  # or return a default vector, or handle as needed

df['vector1'] = df['Tags'].apply(get_vector)
df['vector1'] = df['vector1'].apply(lambda x: x.tolist())

df['id'] = None
for i in range(len(df['vector1'])):
    df.at[i, 'id'] = i

item_names = df['id'].tolist() 
vectors1 = df['vector1'].tolist()

#######

connections.connect("default", host='localhost', port='19530')  # Adjust host and port as necessary

fields = [
    FieldSchema(name="npo_id", dtype=DataType.INT64, is_primary=True),
    FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=300)  # Dim should match the spaCy model
]

schema = CollectionSchema(fields=fields, description="npo recommendations")
collection_name = "npos"

# Step 2: Check if the collection exists
if utility.has_collection(collection_name):
    # Drop the existing collection
    utility.drop_collection(collection_name)

collection = Collection(name=collection_name, schema=schema)

####

collection.create_index("vector", {"metric_type":"COSINE",})

collection.insert([item_names, vectors1])

collection.flush()

def get_recommendations(item_tags, top_k):
    vector = [get_vector(item_tags)]
    search_params = {"metric_type":"COSINE", "params":{"nprobe": 10}}
    results = collection.search(vector, "vector", search_params, limit=top_k)
    return results

collection.load()
recommendations = get_recommendations("Criminal Justice Technology", 5)

results = [None] * 5
i = 0

for result in recommendations[0]:
    results[i] = df['Name'][int(result.id)]
    i = i + 1

for item in results:
    print(item)