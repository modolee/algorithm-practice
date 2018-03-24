def checkio(game_result):
    serialized = "".join(game_result)
    result_list = game_result + [serialized[i:9:3] for i in range(3)] + [serialized[2:8:2], serialized[0:9:4]]

    return "X" if "XXX" in result_list else "O" if "OOO" in result_list else "D"