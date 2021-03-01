
def match(s, p):
    if len(p) == 0:
        return len(s) == 0
    ch = p[0]
    if ch == '?':
        return len(s) > 0 and match(s[1:], p[1:])
    elif ch == '*':
        return match(s, p[1:]) or len(s) > 0 and match(s[1:], p)
    else:
        return len(s) > 0 and s[0] == ch and match(s[1:], p[1:])


def match2(s, p, store=None):
    if len(p) == 0:
        return len(s) == 0
    if store is None:
        store = {}
    key = (s, p)
    if key in store:
        return key

    ch = p[0]
    if ch == '?':
        value = len(s) > 0 and match2(s[1:], p[1:], store)
    elif ch == '*':
        value = match2(s, p[1:], store) or len(s) > 0 and match2(s[1:], p, store)
    else:
        value = len(s) > 0 and s[0] == ch and match2(s[1:], p[1:], store)
    store[key] = value
    return value

print(match('abaab', 'a*b'), True)   # True
print(match('ab', 'a*b'), True)      # True
print(match('abaaba', 'a*b'), False)  #
print(match('abaab', 'a?aab'), True)
print(match('abaab', 'a?ab'), False)
print(match('abaaabba', 'a?a*bb*'), True)

# import time
# time.time()  # return seconds  3.12

print(match2(
    'abaaabbaabaaabbaabaaabbaabaaabbaabaaabbaabaaabbaabaaabbaabaaabbaabaaabbaabaaabbaabaaabbaabaaabbaabaaabbaabaaabbaabaaabbaabaaabbaabaaabbaabaaabbaabaaabbaabaaabbaabaaabbaabaaabbaabaaabbaabaaabbaabaaabbaabaaabbaabaaabbaabaaabbaabaaabbaabaaabba',
    'ababaababaaaabaaaabbbbb*aabaababababababababababaaaaabb*bbababaababaaaabaaa*abbbbbaabaababababababababababaaaaabbbb'), True)
