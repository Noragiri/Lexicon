
var employee = {
    name: "John Smith",
    job: "Programmer",
    age: 31,

    // Method to print the length of the employee's name to the console
    nameLength: function() {
        console.log("Name length:", this.name.length);
    },

    // Method to create an alert with each key-value pair
    displayInfo: function() {
        alert("Name is " + this.name);
        alert("Job is " + this.job);
        alert("Age is " + this.age);
    },

    // Method to print the last name to the console
    lastName: function() {
        console.log("Last name:", this.name.split(" ")[1]);
    }
};

// Call the methods
employee.nameLength();  // Prints the length of the name to the console
employee.displayInfo(); // Alerts each key-value pair
employee.lastName();    // Prints the last name to the console
