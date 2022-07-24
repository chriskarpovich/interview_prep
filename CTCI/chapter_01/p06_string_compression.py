# Method to perform string compression using the counts of repeated characters. E.g. aabccccaaa becomes a2b1c5a3. 
# If the compressed string would not become smaller than the original it should return the original. Assume upper/lower letters only.

def string_compression(string: str) -> str:
    i = 0
    result = []
    while i < len(string):
        result.append(string[i])
        j = i + 1
        ct = 1
        while j < len(string) and string[j] == string[i]:
            ct += 1
            j += 1
        result.append(str(ct))
        i = j

    if len(result) < len(string):
        return "".join(result)
    else:
        return string

def main():
    test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", ""),
    ]
    for case in test_cases:
        assert(case[1] == string_compression(case[0]))

if __name__ == "__main__":
    main()
    