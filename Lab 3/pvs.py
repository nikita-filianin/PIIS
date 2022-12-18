import evaluation as eval


def pvs(depth, board, alpha, beta):
    if depth == 0:
        return eval.getEvaluation(board)
    bSearchPv = True
    for move in board.legal_moves:
        board.push(move)
        if bSearchPv:
            score = -pvs(depth - 1, board, -beta, -alpha)
        else:
            score = -pvs(depth - 1, board, -alpha - 1, -alpha)
            if score > alpha:
                score = -pvs(depth - 1, board, -beta, -alpha)
        board.pop()
        if score >= beta:
            return beta
        if score > alpha:
            alpha = score
            bSearchPv = False
    return alpha


def checkValue(depth, board):
    best = None
    bv = -9998
    alpha = -9999
    beta = 9999

    for move in board.legal_moves:
        board.push(move)
        value = -pvs(depth - 1, board, -beta, -alpha)

        if value > bv:
            bv = value
            best = move
        alpha = max(bv, alpha)

        board.pop()

    return best
