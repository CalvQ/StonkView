CRED = '\033[91m'
CGREEN = '\033[92m'
CYEL = '\033[93m'
CEND = '\033[0m'

def red_s(s):
    return CRED + s + CEND

def green_s(s):
    return CGREEN + s + CEND

def yel_s(s):
    return CYEL + s + CEND