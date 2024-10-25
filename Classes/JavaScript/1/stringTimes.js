// PROBLEM 3: STRING TIMES
// Given a string and a non-negative int n, return a larger string that is n copies of the original string.
// Example input and output:

function stringTimes(str, n) {
    let strAnswer = "";
    for (let x = 0; x < n; x++) {
      strAnswer += str;
    }
    return strAnswer;
}

console.log(stringTimes("Hi", 2)) //→ "HiHi"
console.log(stringTimes("Hi", 3)) //→ "HiHiHi"
console.log(stringTimes("Hi", 1)) //→ "Hi"
