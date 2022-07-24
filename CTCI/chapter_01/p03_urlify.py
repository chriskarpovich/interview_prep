# Write method to replace all spaces in string with "%20". Assume string has enough space at end to hold the additional characters
# and you are given the true length of the string. Remove trailing whitespace

def urlify(string: str, length: int) -> str:
    return string.rstrip().replace(" ", "%20")

def urlify_new_string(string, length):
    new_str = []
    for char in string.rstrip():
        if char == " ":
            new_str.append("%20")
        else:
            new_str.append(char)
    return "".join(new_str)


def main():
    string = "Hello my name is Bob.     "
    length = len(string.rstrip())
    print(urlify(string, length))
    print(urlify_new_string(string, length))

if __name__ == "__main__":
    main()