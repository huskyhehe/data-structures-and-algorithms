# Backtracking
base case
choose - explore - un-choose

```java
// Prints all possible outcomes of rolling the given
// number of six-sided dice in {#, #, #} format.
void diceRolls(int dice) {
    Vector<int> chosen;
    diceRollHelper(dice, chosen);
}

// private recursive helper to implement diceRolls logic
void diceRollHelper(int dice, Vector<int>& chosen) {
    if (dice == 0) {
        cout << chosen << endl; // base case
    } else {
        for (int i = 1; i <= 6; i++) {
            chosen.add(i); // choose
            diceRollHelper(dice - 1, chosen); // explore
            chosen.remove(chosen.size() - 1); // un-choose
        }
    }
}
```
