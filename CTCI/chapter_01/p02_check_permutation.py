# Given two strings, write a method to decide if one is a permutation of another

def check_permutation(str1: str, str2: str) -> bool:
    if set(str1) == set(str2):
        return True
    else:
        return False

def check_permutation_by_count(str1, str2):
    count_arr = [0] * 256
    for char in str1:
        count_arr[ord(char)] += 1
    for char in str2:
        if count_arr[ord(char)] == 0:
            return False
        count_arr[ord(char)] -= 1
    return True

def check_permutation_by_sort(str1, str2):
    if len(str1) != len(str2):
        return False
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    for ind in range(len(str1)):
        if sorted_str1[ind] != sorted_str2[ind]:
            return False
    return True

def main():
    str1 = "Hello"
    str2 = "lleoH"
    print(check_permutation(str1, str2))
    print(check_permutation_by_count(str1, str2))
    print(check_permutation_by_sort(str1, str2))

if __name__ == "__main__":
    main()