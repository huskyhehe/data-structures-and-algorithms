# Backtracking
base case
choose - explore - un-choose

## template
```python
result = []
def backtrack(Path, Seletion List):
    if meet the End Conditon:
        result.add(Path)
        return

    for seletion in Seletion List:
        select
        backtrack(Path, Seletion List)
        deselect
```
## Subset
The subset problem can use the idea of mathematical induction: assuming that the results of a smaller problem are known, and thinking about how to derive the results of the original problem. You can also use the backtracking algorithm, using the `start` parameter to exclude selected numbers.

## Combination
The combination problem uses the backtracking idea, and the results can be expressed as a tree structure. We only need to apply the backtracking algorithm template. The key point is to use a `start` to exclude the selected numbers.

## Permutation
The permutation problem uses the backtracking idea, and it can also be expressed as a tree structure to apply the algorithm template. The key point is to use the `contains` method to exclude the selected numbers. There is detailed analysis previously. Here we mainly compare it with the combination problem.

#### Combination VS Permutation
In the code we can see:
- the permutation problem uses the `contains` method to exclude the numbers that have been selected in track each time;
- the combination problem passes a `start` parameter to exclude the numbers before the start index.


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
