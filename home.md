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
    <div id="search">
        <input id="searchbar" class="searchbar" type="text" placeholder="type here">
    </div>
    <br><br>
    <img src="/images/searchicon.png">
    <div class="container">
        <div class="square">BLM</div>
        <div class="square">lgbgqt</div>
        <div class="square">politechnika</div>
        <div class="square">one</div>
        <div class="square">another one</div>
        <div class="square">and another one</div>
        <div class="square">one more</div>
        <div class="square">two more</div>
    </div>
</body>
</html>

<style>
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
    .searchbar::placeholder {
        text-align:center;
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
</script>
