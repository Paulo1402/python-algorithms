def solution(str_to_decode):
    def parse_str(str_to_decode, index=0, number=None):
        str_decoded = ""

        while index < len(str_to_decode):
            str = str_to_decode[index]

            if str == "]":
                break

            if str == "[":
                index += 1
                continue

            if str.isdigit():
                if number:
                    _number = f"{number}{str}"
                else:
                    _number = str

                _number = int(_number)
                number = None

                content, index = parse_str(str_to_decode, index + 1, number=_number)
                str_decoded += content
            else:
                str_decoded += str
                index += 1

        if number:
            str_decoded = str_decoded * number

        return str_decoded, index + 1

    str_decoded, _ = parse_str(str_to_decode)
    return str_decoded
