from sys import stdin

def isPossible(candidate, defect_button):
    for ch in candidate:
        if int(ch) in defect_button:
            return 0

    return len(candidate)

if __name__ == '__main__':
    default_channel = 100
    hopping_channel = stdin.readline()
    num_of_defect_button = int(stdin.readline())

    if num_of_defect_button > 0:
        defect_button = list(map(int, stdin.readline().rstrip().split()))
    else:
        defect_button = []

    min_press = abs(int(hopping_channel) - default_channel)
    for candidate in range(1000001):
        press = isPossible(str(candidate), defect_button)
        if press > 0:
            press += abs(candidate - int(hopping_channel))
            if min_press > press:
                min_press = press

    print(min_press)