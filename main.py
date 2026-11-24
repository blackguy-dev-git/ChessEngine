import chess

PIECE_VALUES = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 0,
}

def evaluate(board):
    
    if board.is_checkmate():
        
        return -99999 if board.turn == chess.WHITE else 99999
    if board.is_stalemate() or board.is_insufficient_material():
        return 0

    score = 0
    for square, piece in board.piece_map().items():
        value = PIECE_VALUES[piece.piece_type]
        if piece.color == chess.WHITE:
            score += value
        else:
            score -= value
    return score


board = chess.Board()

while not board.is_game_over():
    move_str = input("Enter your move (e.g., e2e4): ").strip().lower()
    if move_str == "end":
        break
    try:
        move = chess.Move.from_uci(move_str)
        if move in board.legal_moves:
            board.push(move)
            print(board)
            print("Evaluation:", evaluate(board))
        else:
            print("Illegal move!")
    except ValueError:
        print("Wrong format! Use UCI notation like 'e2e4'.")

print("Game over!")
print(board.result())