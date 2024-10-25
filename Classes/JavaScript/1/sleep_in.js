//Write a function called sleepIn that takes in two boolean parameters: weekday and vacation.
//The parameter weekday is true if it is a weekday, and the parameter vacation is true if we are on
//vacation. We sleep in if it is not a weekday or we're on vacation. Return true if we sleep in. So some
//example input and output:

function sleepIn(weekday, vacation) {
    if (!weekday) {
        return true;
      }
      if (weekday) {
        if (vacation) {
          return true;
        } else {
          return false;
        }
      }
}
console.log(sleepIn(false, false)) //→ true
console.log(sleepIn(true, false)) //→ false
console.log(sleepIn(false, true)) //→ true