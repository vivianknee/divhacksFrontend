---
layout: none
---

{%- include navbar.html -%}

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<br><br>
<body>
    <p class="instructions" >Use the search or filter tools to find the groups you're interested in!</p>
    <br>
    <div class="search-wrapper">
        <div id="search">
            <input class="searchbar" id="searchbar" type="text" placeholder="Type here" >
        </div>
    </div>
    <br>
    <div class="filters" id="filters">
        <button class="searchbutton" id="search_button">Search</button>
        <div class="filter-item">
            <input class="box_pos" type="checkbox" id="community" name="community" value="Community">
            <label for="community">Community</label>
        </div>
        <div class="filter-item">
            <input class="box_pos" type="checkbox" id="antiHate" name="antiHate" value="Anti-Hate">
            <label for="antiHate">Anti-Hate</label>
        </div>
    </div>
    <br><br>
    <div id="result" class="container objects">
    </div>
</body>
</html>

<style>
    .instructions {
        display: flex;
        font-size: 16px;
        justify-content: center;
    }
    
    .search-wrapper {
        position: relative;
    }

    .search-wrapper input {
        padding-left: 50px;
    }

    .searchbar {
        width: 300px;
        padding: 12px 15px;
        border: 2px solid #ddd;
        border-radius: 30px;
        font-size: 16px;
        outline: none;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); 
    }

    .searchbar::placeholder {
        color: #aaa;
        font-style: italic;
    }

    .searchbar:focus {
        border-color: #5c48ee;
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }

    .square {
        width: 350px;
        height: 350px;
        border-radius: 10px;
        padding:5px;
        display: flex;
        justify-content: center;
        align-items: center;
        border-color: black;
        border-style: solid;
        background-color: #CBC5EA;
    }

    .container {
        display:flex;
        align-items: center;
        justify-content: space-evenly;
        flex-wrap: wrap;
        row-gap: 30px
    }

    #search {
        display:flex;
        justify-content: center;
    }

    .searchbutton {
        padding: 10px 15px;
        margin-bottom: 15px;
        background-color: #5c48ee;
        color: white;
        border: none;
        border-radius: 4px;
        font-size: 16px;
        cursor: pointer;
    }

    .searchbutton:hover {
        background-color: #CBC5EA;
    }

    .filters {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin: 0 auto;
    }

    .filter-item {
        display: flex;
        align-items: center;
    }

    .box_pos {
        margin-top: -6px;
    }

    .filters input[type="checkbox"] {
        appearance: none;
        width: 20px;
        height: 20px;
        border: 2px solid #5c48ee;
        border-radius: 4px;
        margin-right: 10px;
        position: relative;
        cursor: pointer;
    }

    .filters input[type="checkbox"]:checked::before {
        content: '✔';
        color: white;
        font-size: 16px;
        position: relative;
        left: 3px;
        top: -1px;
    }

    .filters input[type="checkbox"]:checked {
        background-color: #5c48ee;
        border-color: #5c48ee;
    }

    .filters label {
        font-size: 16px;
        color: #555;
        cursor: pointer;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
    }

</style>

<script>

    let form = document.querySelector("#searchbar")
    form.addEventListener("keyup", search)
    function search() {
        let input = form.value.toUpperCase();
        console.log(input);
        let squares = document.getElementsByClassName("square");
        for(square of squares) {
            let topic = square.textContent.toUpperCase();
            if(topic.indexOf(input) > -1) {
                square.style.display = "";
            }
            else {
                square.style.display = "none";
            }
        }
    }

    let dataArray;

    function parseCSV(csvString) {
        const rows = csvString.trim().split('\n');
        return rows.map(row => row.split(','));
    }

    // Fetch the CSV file
    fetch('interdependence-orgs.csv')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(data => {
            dataArray = parseCSV(data);
            console.log(dataArray);
            console.log("data set to all_groups");
            for(let i = 1; i < dataArray.length; i++) {
                let container = document.querySelector(".container");
                let child = document.createElement("div");
                child.classList.add("square");
                child.textContent = dataArray[i][0];
                container.appendChild(child);
            }
        })
        .catch(error => {
            console.error('Error fetching the file:', error);
        });

    const btnSearch = document.getElementById("search_button");
    const resultContainer = document.getElementById("result");
    const comm_filter = document.getElementById("community");
    const antiHate_filter = document.getElementById("antiHate");

    btnSearch.addEventListener('click', (event) => {
          console.log("Search Clicked!");
          clearCards();
          const values = [];

          var community_value = comm_filter.value;
          var antiHate_value = antiHate_filter.value; 
          
          if (document.getElementById('community').checked) {
            console.log("community is checked");
            values.push(community_value);
          } else {
            console.log("didn't check community");
          }

          if (document.getElementById('antiHate').checked) {
            console.log("antiHate is checked");
            values.push(antiHate_value);
          } else {
            console.log("didn't check antiHate");
          }
          
          console.log(values);
          var group_list = getFilterResults(values); 

          if (group_list.length === 0) {
            alert('No Groups Found')
            return
          }

          console.log("Filtered groups retrieved!");
          console.log(group_list);
          console.log("Creating cards!");
          console.log(values);

          for (const group of group_list) {
            console.log(group);

            let container = document.querySelector(".container");
            let child = document.createElement("div");
            child.classList.add("square");
            child.textContent = group[0];
            container.appendChild(child);
          }

    });

    function getFilterResults(types) {
        var result = [];
        console.log(types);
        for (const group of dataArray){
              console.log(group);
              console.log("group type is: " + group[1])
            for (type of types){
                if (group[1] === type)
                    {
                    result.push(group);
                }
            }
        }

        if (result.length === 0) {
            console.log('No Groups Found');
        }

        else {
            console.log(result.length + 'Groups Found');
        }

        return result;
    }

    function clearCards() {
        var tableRows = resultContainer.getElementsByTagName('div');
        var rowCount = tableRows.length;

        for (var x=rowCount-1; x>=0; x--) {
            resultContainer.removeChild(tableRows[x]);
        }
    }
</script>
