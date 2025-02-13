def solution(string):
    temp_str = ""
    string = string.lower()

    for i in range(len(string) - 1, -1, -1):
        temp_str += string[i]

    return temp_str == string
