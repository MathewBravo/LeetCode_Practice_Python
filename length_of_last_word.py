def length_of_last_word(s: str) -> int:
    if s == "":
        return 0
    parsed_s = s.split()
    return len(parsed_s[-1])


if __name__ == "__main__":
    print(length_of_last_word("   fly me   to   the moon  "))