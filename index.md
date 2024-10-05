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
<body>
    <input id="searchbar" class="searchbar" type="text" placeholder="type here">
    <br><br>
    <div class="container">
        <div class="square" style="background-color: red;">BLM</div>
        <div class="square" style="background-color: lightblue;">lgbgqt</div>
        <div class="square" style="background-color: yellow;">politechnika</div>
    </div>
</body>
</html>

<style>
    .square {
    width: 150px;
    height: 150px;
    border-radius: 10px;
    padding:5px;
    }

    .container {
        display:flex;
        align-items: center;
        justify-content: space-evenly;
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