from sys import stdin

ja = 'bcdfghjklmnpqrstvwxyz'
mo = 'aeiou'


def is_possible_password(pwd):
    ja_cnt = 0
    mo_cnt = 0
    for val in pwd:
        if val in ja:
            ja_cnt += 1
        if val in mo:
            mo_cnt += 1

    return ja_cnt >= 2 and mo_cnt >= 1


def find_password(pwd_len, idx, password, cand_list):
    if pwd_len == len(password):
        if is_possible_password(password):
            print(password)
        return

    if idx >= len(cand_list):
        return

    find_password(pwd_len, idx+1, password + cand_list[idx], cand_list)
    find_password(pwd_len, idx+1, password, cand_list)


if __name__ == '__main__':
    password_length, candidate_number = list(map(int, stdin.readline().rstrip().split()))
    candidate_list = list(map(str, stdin.readline().rstrip().split()))
    candidate_list.sort()

    find_password(password_length, 0, '', candidate_list)