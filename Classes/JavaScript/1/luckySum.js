// PROBLEM 4: LUCKY SUM
// Given 3 numerical values, a b c, return their sum. However, if one of the values is 13 then it does not
// count towards the sum and values to its right do not count.
// So for example, if b is 13, then both b and c do not count.
// Hint (Explore using multiple return statements inside a single function!)
// Example input and output

function luckySum(a, b, c){
    let sum = 0;
    if (a !== 13) sum += a;
    if (b !== 13 && a !== 13) sum += b;
    if (c !== 13 && b !== 13 && a !== 13) sum += c;
    return sum;
}

console.log(luckySum(1, 2, 3)) //→ 6
console.log(luckySum(1, 2, 13)) //→ 3
console.log(luckySum(1, 13, 3)) //→ 1