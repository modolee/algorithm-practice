def safe_pawns(pawns):
    count = 0
    for pawn in pawns :
        left_brother = chr(ord(pawn[0]) - 1) + str((int(pawn[1]) - 1))
        right_brother = chr(ord(pawn[0]) + 1) + str((int(pawn[1]) - 1))

        if (left_brother in pawns) or (right_brother in pawns) :
            count += 1
    return count