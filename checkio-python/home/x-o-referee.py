def checkio(game_result):
    cross_lr = ""
    cross_rl = ""

    for i in range(0, 3):
        row = game_result[i]
        if row == "XXX" or row == "OOO":
            return row[0]

        col = game_result[0][i] + game_result[1][i] + game_result[2][i]
        if col == "XXX" or col == "OOO":
            return col[0]

        cross_lr += game_result[i][i]
        cross_rl += game_result[i][2 - i]

    if cross_lr == "XXX" or cross_lr == "OOO":
        return cross_lr[0]

    if cross_rl == "XXX" or cross_rl == "OOO":
        return cross_rl[0]

    return "D"