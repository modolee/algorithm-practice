def long_repeat(line):
    if len(line) == 0 :
        return 0
    else :
        max_count = 0
        count = 1
        for i in range(1, len(line)):
            if line[i-1] == line[i]:
                count += 1
            else :
                if max_count < count:
                    max_count = count
                count = 1
        return max_count if max_count > count else count