#풀이1
def solution(my_string, is_prefix):
    string = ''
    while True:
        for i in my_string:
            string += i
            print(string)
            if is_prefix != string:
                pass
            elif is_prefix == string:
                return 1
        return 0

#풀이2
def solution(my_string, is_prefix):
    if my_string[:len(is_prefix)] == is_prefix:
        answer = 1
    else:
        answer = 0
    return answer