# 결과를 저장할 빈 문자열을 만든다.
# arr의 문자를 앞에서부터 하나씩 꺼낸다.
# 꺼낸 문자를 결과 문자열 뒤에 계속 붙인다.
# 완성된 문자열을 반환한다.

def solution(arr):
    answer = ''
    
    for n in arr:
        answer += n

    return answer