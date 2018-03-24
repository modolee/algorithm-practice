def checkio(data):
    # replace this for solutionreturn True or False
    is_longer_than_ten = True if len(data) >= 10 else False
    have_alpha = not data.isdigit()
    have_digit = not data.isalpha()
    have_upper = not data.islower()
    have_lower = not data.isupper()

    if is_longer_than_ten and have_alpha and have_digit and have_upper and have_lower:
        return True
    return False