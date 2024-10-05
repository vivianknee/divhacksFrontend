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
    <div class="search-wrapper">
        <div id="search">
            <img src="images/searchicon.png" style="width: 30px">
            <input id="searchbar" class="searchbar" type="text" placeholder="Type here">
        </div>
    </div>
    <div id="filters">
        <button class="filter" onclick="filterObjects('all')">Show All</button>
        <button class="filter" onclick="filterObjects('race')">Race</button>
        <button class="filter" onclick="filterObjects('climate')">Climate</button>
        <button class="filter" onclick="filterObjects('gender')">Gender</button>
        <button class="filter" onclick="filterObjects('humanRights')">Human Rights</button>
    </div>
    <div id="filters">
        <button class="filter" onclick="filterObjects('all')">Show All</button>
        <button class="filter" onclick="filterObjects('race')">Race</button>
        <button class="filter" onclick="filterObjects('climate')">Climate</button>
        <button class="filter" onclick="filterObjects('gender')">Gender</button>
        <button class="filter" onclick="filterObjects('humanRights')">Human Rights</button>
    </div>
    <br><br>
    <div class="container objects">
        <div class="square race">BLM</div>
        <div class="square gender">lgbgqt</div>
        <div class="square climate">politechnika</div>
        <div class="square">one</div>
        <div class="square">another one</div>
        <div class="square">and another one</div>
        <div class="square">one more</div>
        <div class="square">two more</div>
    </div>
</body>
</html>

<style>
    .search-wrapper {
        position: relative;
    }
    .search-wrapper img {
        position: absolute;
        top: 5px;
        left: 40.8%;
    }
    .search-wrapper input {
        padding-left: 50px;
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
    .searchbar {
        background-color: white;
        border-color: #5c48ee;
        border-radius: 20px;
        padding: 10px;
        width: 300px;
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
            const dataArray = parseCSV(data);
            console.log(dataArray);
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
</script>
