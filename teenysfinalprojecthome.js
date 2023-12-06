function check() {

    // sets a variable equal to the age entered by the user
    let fruit = document.getElementById("fruit").value;

    let output = document.getElementById("output");

    if (!isNaN(fruit)) {
        // checks if the user entered a valid string
        output.innerHTML="User has failed to enter a valid fruit"
        output.style.display="block"
        document.getElementById("hide").style.visibility="hidden";
    }
    else {
        // changes the visibility if string is good
        document.getElementById("hide").style.visibility="visible";
        output.style.display = "none";
        document.getElementById("temphide").style.visibility="hidden";
    }

}

