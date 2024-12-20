class Point {
    constructor(x, y) {
      this.x = x;
      this.y = y;
    }
  
    // Static method to calculate distance between two points
    static distance(p1, p2) {
      return Math.sqrt(Math.pow(p2.x - p1.x, 2) + Math.pow(p2.y - p1.y, 2));
    }
  }
  
  // Example usage
  let p1 = new Point(5, 5);
  let p2 = new Point(9, 8);
  console.log(Point.distance(p1, p2));  // Output: 5
  