# Write method to replace all spaces in string with "%20". Assume string has enough space at end to hold the additional characters
# and you are given the true length of the string. Remove trailing whitespace

def urlify(string: str, length: int) -> str:
    return string.rstrip().replace(" ", "%20")

def urlify_new_string(string, length):

    string_arr = [None] * length
    for ind in range(length):
        if string[ind] == " ":
            string_arr[ind] = "%20"
        else:
            string_arr[ind] = string[ind]
    return ''.join([str(elem) for elem in string_arr])


def main():
    string = "Hello my name is Bob.     "
    length = len(string.rstrip())
    print(urlify(string, length))
    print(urlify_new_string(string, length))

if __name__ == "__main__":
    main()