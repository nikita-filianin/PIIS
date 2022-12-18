import chess
import evaluation as eval
import negamax as ai


def main():
    board = chess.Board()
    board.legal_moves
    n = 0
    print(board)
    while n < 100:
        if n % 2 == 0:
            move = input("Your move: ")
            move = chess.Move.from_uci(str(move))
            board.push(move)
        else:
            print("Wait for opponent`s move:")
            move = ai.controller(eval.maxDepth(), board)
            move = chess.Move.from_uci(str(move))
            board.push(move)
        print(board)
        n += 1


if __name__ == "__main__":
    main()
