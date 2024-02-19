function generatePi() {
    var piValueElement = document.getElementById("pi-value");
    piValueElement.innerHTML = "Calculating...";
    
    // Make a request to the server to compute pi
    fetch("/pi")
        .then(response => response.json())
        .then(data => {
            piValueElement.innerHTML = data.pi;
        })
        .catch(error => {
            console.error(error);
            piValueElement.innerHTML = "Error occurred.";
        });
}
console.log("YOLO!");
