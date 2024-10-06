---
layout: none
---
{%- include navbar.html -%}

<html>
    <form id="form">
    Organization Name: <input id="orgname" type="text">
    <br>
    Type: <input id="type" type="text">
    <br>
    Tags: <input id="tags" type="text">
    <br>
    Description: <input id="description" type="text">
    <br>
    Twitter Followers: <input id="twitterfollowers" type="text">
    <br>
    Facebook Followers: <input id="facebookfollowers" type="text">
    <br>
    Funding (2015): <input id="funding2015" type="text">
    <br>
    Funding (2016): <input id="funding2016" type="text">
    <br>
    Funding (2017): <input id="funding2017" type="text">
    <br>
    Three Year Funding:  <input id="threeyearfunding" type="text">
    <br>
    Social Reach: <input id="socialreach" type="text">
    <br>
    Impact: <input id="impact" type="text">
    <br>
    Scale: <input id="scale" type="text">
    <br>
    URL: <input id="url" type="text">
    <br>
    Image URL: <input id="image" type="text">
    <br>
    Interdependence: <input id="interdependence" type="text">
    <br>
    Polarization: <input id="polarization" type="text">
    <br>
    Holistic: <input id="holistic" type="text">
    <br>
    Cultural Isolation: <input id="culturalisolation" type="text">
    <br>
    Mindset: <input id="mindset" type="text">
    <br>
    Behavior: <input id="behavior" type="text">
    <br>
    <input id="submit" type="submit">
    </form>
</html>

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