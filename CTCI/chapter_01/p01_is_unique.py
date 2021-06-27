# Algorithm to determine if string has all unique characters

def is_unique(string: str) -> bool:
    if len(set(string)) == len(string):
        return True
    else:
        return False

def is_unique_dictionary(string: str) -> bool:
    char_dict = {}
    for char in string:
        if char in char_dict:
            return False
        char_dict[char] = 1
    return True

def main():
    test_str = "Helo"
    print(is_unique(test_str))
    print(is_unique_dictionary(test_str))

if __name__ == "__main__":
    main()
