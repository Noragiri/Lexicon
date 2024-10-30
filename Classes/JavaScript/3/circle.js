class Circle {
    constructor(radius) {
      this.radius = radius;
    }
  
    // Getter for diameter
    get diameter() {
      return this.radius * 2;
    }
  
    // Setter for diameter
    set diameter(diameter) {
      this.radius = diameter / 2;
    }
  
    // Method to calculate the area
    area() {
      return Math.PI * Math.pow(this.radius, 2);
    }
  }
  
  // Example usage
  let c = new Circle(2);
  console.log(`Radius: ${c.radius}`);       // Output: 2
  console.log(`Diameter: ${c.diameter}`);   // Output: 4
  console.log(`Area: ${c.area()}`);         // Output: 12.566370614359172
  
  // Changing diameter
  c.diameter = 1.6;
  console.log(`Radius: ${c.radius}`);       // Output: 0.8
  console.log(`Diameter: ${c.diameter}`);   // Output: 1.6
  console.log(`Area: ${c.area()}`);         // Output: 2.0106192982974678
  