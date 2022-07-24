# Algorithm to determine if string has all unique characters

def is_unique(string: str) -> bool:
    return len(set(string)) == len(string)

def is_unique_dictionary(string: str) -> bool:
    seen = dict()
    for char in string:
        if char in seen:
            return False
        seen[char] = char
    return True

def main():
    test_str = "Helo"
    print(is_unique(test_str))
    print(is_unique_dictionary(test_str))

if __name__ == "__main__":
    main()
