# Week 1 Programming Assignment 1
You begin with a stack of n boxes.

Then you make a sequence of moves. In each move, you divide one stack of boxes into two nonempty stacks. The game ends when you have n stacks, each containing a single box. You earn points for each move; in particular, if you divide one stack of height a + b into two stacks with heights a and b, then you score ab points for that move. Your overall score is the sum of the points that you earn for each move.

What strategy should you use to maximize your total score?

As an example, suppose that we begin with a stack of n = 10 boxes. Then the game might proceed as follows:
```
At the start: one stack of height 10 

The next steps show the stack sizes first followed by the score earned by the split.

5 5 25 points
5 3 2 6 points
4 3 2 1 4 points
2 3 2 1 2 4 points
2 2 2 1 2 1 2 points
1 2 2 1 2 1 1 1 points
1 1 2 1 2 1 1 1 1 points
1 1 1 1 2 1 1 1 1 1 points
1 1 1 1 1 1 1 1 1 1 1  points
```

The total score in the example above is 45 points. Can you find a better strategy?

Input Format

The first line is T, the number of test cases.
The next T lines have one test case each.
Each test case is a number 1 <= N <= 10000, which is the size of the first stack of boxes.

Output Format

For each test case, output the best possible score that you can earn with an optimal strategy.
Your output should have N lines, with the i-th line containing the answer for the i-th test case.
