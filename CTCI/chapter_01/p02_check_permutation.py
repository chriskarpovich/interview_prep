# Given two strings, write a method to decide if one is a permutation of another

def check_permutation_by_count(str1, str2):
    str1_dict = dict()
    for char in str1:
        if char not in str1_dict:
            str1_dict[char] = 0
        str1_dict[char] += 1
    for char in str2:
        if char not in str1_dict:
            return False
        str1_dict[char] -= 1
    for key in str1_dict:
        if str1_dict[key] != 0:
            return False
    return True

def main():
    str1 = "Hellol"
    str2 = "lleoHH"
    print(check_permutation_by_count(str1, str2))

if __name__ == "__main__":
    main()