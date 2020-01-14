# ai_develop
Zero Knowledge(chess engine)

establish the search tree
Use neural net to prune the search tree


should we fix the value of initial board state?

what is the value of about to lose?

simpler:
All positions where white wins =1 
All positions where black wins = -1 
All positions where draw =0 

Definition:

Value network V- f(board)
V = f(state)

what is v?
v = -1 Black wins board state
V = 1 white wins board state
v = 0 draw board state

State:

Pieces(2-7*2-16)

*  Universal
** Blank
** Blank(En passant)
** En passant
*  Pieces
** Pawn
** Bishop
** Knight
** Rook
** Rook (can castle)
** Queen
** King

Extra state: = To move

8x8x5 =257 bits( vector of 0 or 1)