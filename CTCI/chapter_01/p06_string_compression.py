# Method to perform string compression using the counts of repeated characters. E.g. aabccccaaa becomes a2b1c5a3. 
# If the compressed string would not become smaller than the original it should return the original. Assume upper/lower letters only.

def string_compression(string: str) -> str:
    
    counter = 0
    result = []
    last_char = None
    for ind in range(len(string)):
        if ind == 0:
            last_char = string[0]
        if last_char != string[ind]:
            result.append(last_char)
            result.append(str(counter))
            last_char = string[ind]
            counter = 0
        counter += 1
    if counter > 0:
        result.append(last_char)
        result.append(str(counter))

    
    return_str = "".join(result)
    print(return_str)
    if len(return_str) < len(string): 
        return return_str
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
    