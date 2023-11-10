def isSubsequence(s: str, t:str) -> bool:
    t1, t2 = 0, 0
    while t1 < len(s) and t2 < len(t):
        if s[t1] == t[t2]:
            t1 += 1
            t2 += 1
        else:
            t2 += 1
    return len(s) == t1

if __name__ == "__main__":
    isSubsequence("b", "abc")