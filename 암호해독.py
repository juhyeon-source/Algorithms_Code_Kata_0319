#풀이1
def solution(cipher, code):
    answer = ''
    a = len(cipher)//code
    for i in range(1, a+1):
        answer += cipher[code*i - 1]
    return answer

#풀이2
def solution(cipher, code):
    answer = ''
    for i in range(code-1, len(cipher), code):
        answer += cipher[i]
    return answer