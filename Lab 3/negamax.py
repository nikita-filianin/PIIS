import evaluation as eval


def negamax(depth, board):
    if depth == 0:
        return eval.getEvaluation(board)
    max = -9999
    for move in board.legal_moves:
        board.push(move)
        res = -negamax(depth - 1, board)
        if res > max:
            max = res
        board.pop()
    return max


def controller(depth, board):
    best = None
    bv = -9998

    for move in board.legal_moves:
        board.push(move)
        value = -negamax(depth - 1, board)
        if value > bv:
            bv = value
            best = move
        board.pop()

    return best
