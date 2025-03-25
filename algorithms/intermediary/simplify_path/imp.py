def solution(path):
    stack = ["/"]
    temp_word = ""

    for i, s in enumerate(path):
        if s == "/":
            if temp_word:
                stack.append(temp_word)
                temp_word = ""

            last_char = None
            penultimate_char = None

            try:
                if i - 1 > 0:
                    last_char = path[i - 1]

                if i - 2 > 0:
                    penultimate_char = path[i - 2]
            except IndexError:
                pass

            if last_char == "." and penultimate_char == ".":
                if len(stack) > 1:
                    stack.pop()
        elif s != ".":
            temp_word += s
    else:
        if temp_word:
            stack.append(temp_word)

    return "/" + "/".join(stack[1:])
