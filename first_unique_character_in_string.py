def firstUniqChar(s: str) -> int:
    non_repeated_char = {}
    for i in range(len(s)):
        if s[i] not in non_repeated_char:
            non_repeated_char[s[i]] = 1
        else:
            non_repeated_char[s[i]] = non_repeated_char[s[i]] + 1
    for i in range(len(s)):
        if s[i] in non_repeated_char and non_repeated_char[s[i]] == 1:
            return i
    return -1


if __name__ == "__main__":
    print(firstUniqChar("leetcode"))
    print(firstUniqChar("loveleetcode"))
    print(firstUniqChar("aabb"))
