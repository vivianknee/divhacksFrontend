---
layout: none
baseurl: /requests
---
{%- include navbar.html -%}


<html>
    <header>
    <h1>Organization Request Form</h1>
    </header>
    <div class="container">
        <form id="form">
            <div class="form-row">
                <div class="form-group">
                    <label for="orgname">Organization Name:</label>
                    <input id="orgname" type="text" required>
                </div>
                <div class="form-group">
                    <label for="type">Type:</label>
                    <input id="type" type="text" required>
                </div>
            </div>
            <div class="form-group">
                <label for="tags">Tags:</label>
                <input id="tags" type="text">
            </div>
            <div class="form-group">
                <label for="description">Description:</label>
                <textarea id="description"></textarea>
            </div>
            <div class="form-row">
                <div class="form-group">
                    <label for="twitterfollowers">Twitter Followers:</label>
                    <input id="twitterfollowers" type="number">
                </div>
                <div class="form-group">
                    <label for="facebookfollowers">Facebook Followers:</label>
                    <input id="facebookfollowers" type="number">
                </div>
            </div>
            <div class="form-group">
                <label>Funding:</label>
                <div class="form-row">
                    <input id="funding2015" type="number" placeholder="2015">
                    <input id="funding2016" type="number" placeholder="2016">
                    <input id="funding2017" type="number" placeholder="2017">
                </div>
            </div>
            <div class="form-row">
                <div class="form-group">
                    <label for="threeyearfunding">Three Year Funding:</label>
                    <input id="threeyearfunding" type="number">
                </div>
                <div class="form-group">
                    <label for="socialreach">Social Reach:</label>
                    <input id="socialreach" type="number">
                </div>
            </div>
            <div class="form-row">
                <div class="form-group">
                    <label for="impact">Impact:</label>
                    <input id="impact" type="text">
                </div>
                <div class="form-group">
                    <label for="scale">Scale:</label>
                    <input id="scale" type="text">
                </div>
            </div>
            <div class="form-group">
                <label for="url">URL:</label>
                <input id="url" type="url">
            </div>
            <div class="form-group">
                <label for="image">Image URL:</label>
                <input id="image" type="url">
            </div>
            <div class="form-row">
                <div class="form-group">
                    <label for="interdependence">Interdependence:</label>
                    <input id="interdependence" type="text">
                </div>
                <div class="form-group">
                    <label for="polarization">Polarization:</label>
                    <input id="polarization" type="text">
                </div>
            </div>
            <div class="form-row">
                <div class="form-group">
                    <label for="holistic">Holistic:</label>
                    <input id="holistic" type="text">
                </div>
                <div class="form-group">
                    <label for="culturalisolation">Cultural Isolation:</label>
                    <input id="culturalisolation" type="text">
                </div>
            </div>
            <div class="form-row">
                <div class="form-group">
                    <label for="mindset">Mindset:</label>
                    <input id="mindset" type="text">
                </div>
                <div class="form-group">
                    <label for="behavior">Behavior:</label>
                    <input id="behavior" type="text">
                </div>
            </div>
            <input id="submit" type="submit" value="Submit">
        </form>
    </div>
</html>

<style>
    header {
        text-align: center;
        padding: 10px 0;
        font-size: 1.5em;
        color: #5c48ee;
    }
    body{
        font-family: Poppins, sans-serif;
        margin: 0;
        padding: 20px;
        line-height: 1.6;
        color: #333;
    }
    .container{
        max-width: 800px;
        margin: 0 auto;
        background-color: #CBC5EA;
        padding: 30px;
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    .form-group{
        display: grid;
        gap: 10px;
    }
    .form-row{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
        gap: 20px;
    }
    label{
        font-weight: bold;
    }
    input, textarea{
        wideth: 100%;
        padding 10px;
        border: 1px solid var(#ddd);
        border-radius: 4px;
        font-size: 16px;
    }
    textarea{
        height: 100px;
        resize: vertical;
    }
    input[type="submit"]{
        background-color: #5c48ee;
        color: white;
        border: none;
        padding: 12px 20px;
        cursor: pointer;
        font-size: 18px;
        transition: background-color 0.3s ease;
        display: block;
        margin: 0 auto;
        width: 200px;
    }
    input[type="submit"]: hover{
        background-color: #CBC5EA;
    }
    @media(max-width: 600px){
        input[type="submit"] {
            width: 100%;
        }
    }
</style>


<script>
    let form = document.querySelector("#form");
    form.addEventListener("submit", event => {
        event.preventDefault();
        let orgname = document.getElementById("orgname").value;
        let type = document.getElementById("type").value;
        let tags = document.getElementById("tags").value;
        let desc = document.getElementById("description").value;
        let twitter = document.getElementById("twitterfollowers").value;
        let facebook = document.getElementById("facebookfollowers").value;
        let funding2015 = document.getElementById("funding2015").value;
        let funding2016 = document.getElementById("funding2016").value;
        let funding2017 = document.getElementById("funding2017").value;
        let year3 = document.getElementById("threeyearfunding").value;
        let reach = document.getElementById("socialreach").value;
        let impact = document.getElementById("impact").value;
        let scale = document.getElementById("scale").value;
        let url = document.getElementById("url").value;
        let image = document.getElementById("image").value;
        let interdependence = document.getElementById("interdependence").value;
        let polarization = document.getElementById("polarization").value;
        let holistic = document.getElementById("holistic").value;
        let isolation = document.getElementById("culturalisolation").value;
        let mindset = document.getElementById("mindset").value;
        let behavior = document.getElementById("behavior").value;

        let data = {
            label: orgname,
            typeoforg: type,
            tags: tags,
            descript: desc,
            twitter_followers: twitter,
            fb_followers: facebook,
            three_year_funding: year3,
            social_reach: reach,
            impact: impact,
            scale: scale,
            url: url,
            image: image,
            interdependence: interdependence,
            polarization: polarization,
            holistic: holistic,
            cultural_isolation: isolation,
            mindset: mindset,
            behavior: behavior
        }
        fetch("http://10.207.73.150:8080/api/divhacks/post", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        }).then(response => {
            console.log(response);
        })
})
</script>