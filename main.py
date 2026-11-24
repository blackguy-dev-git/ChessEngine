import chess

board = chess.Board()

while not board.is_game_over():
    move_str = input("Enter your move (e.g., e2e4): ").strip().lower()
    if move_str == "end":
        break   
    try:
        move = chess.Move.from_uci(move_str)

        if move in board.legal_moves:
            board.push(move)
            print("Move played!")
            print(board)
        else:
            print("Illegal move!")
        
    
    except ValueError:
        print("Wrong format! Use UCI notation like 'e2e4'.")
    

print("Game over!")
print(board.result())
