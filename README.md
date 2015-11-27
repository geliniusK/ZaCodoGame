## Za Codo Game

A reversi game simulator.

### Functions

These are the functions that must be defined in the
strategy python file.

##### GetMove

This function will need two parameters:

- The board;
- The history of plays;

It must return which play it will do. Specifically, a
tuple (x, y). Where "x" represents the line number and
"y" the column number.

##### Result

It will inform whether the position informed was valid.
If it was not valid, it will wait for the next move of
the strategy.


### TODO

- [ ] Create a function that turns all the pieces that it 
is possible. The played piece is the parameter.
- [ ] Create a function that validates the position played
by the strategy.
- [ ] Create a function that updates the board and the history.
- [ ] Create a function that verifies which player's turn it is.

