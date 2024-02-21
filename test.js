function greetUser() {
    // Ask the user for their name using prompt
    var userName = prompt("Please enter your name:");

    // Check if the user entered a name
    if (userName !== null && userName !== "") {
        // Display a greeting message
        alert("Hello, " + userName + "! Welcome to our platform.");
    } else {
        // If the user didn't enter a name, display a generic greeting
        alert("Hello! Welcome to our platform.");
    }
}

// Call the greetUser function
greetUser();
