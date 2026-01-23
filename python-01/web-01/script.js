alert("js terhubung");

function ambilquote() {
    fetch("https://api.quotable.io/random")
        then(response => response.json())
        then(data => {

document.getElementById("quote").innerHTML =data.content;
        })
        .catch(error => {
            console.log(error);
        });
}
