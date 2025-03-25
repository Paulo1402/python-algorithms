def solution_1(string):
    temp_str = ""
    string = string.lower()

    for i in range(len(string) - 1, -1, -1):
        temp_str += string[i]

    return temp_str == string


def solution_2(string):
    reversed_index = len(string) - 1

    for index in range(len(string)):
        if index == reversed_index:
            return True

        if string[index] != string[reversed_index]:
            return False

        reversed_index -= 1

    return True


def solution_3(string):
    return string.lower() == string[::-1].lower()
