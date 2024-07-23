from collections import deque


def is_palindrome(s):
    s = ''.join(s.split()).lower()

    d = deque(s)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True


input_string = "qWe rTyuio Poi uY trew q"
print(is_palindrome(input_string))
