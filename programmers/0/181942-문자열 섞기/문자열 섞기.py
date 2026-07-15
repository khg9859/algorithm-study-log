# 문자열의 인덱스는 0부터 시작한다.
# str1[0], str2[0] → 첫 번째 문자들
# str1[1], str2[1] → 두 번째 문자들

# 반복문으로 처음부터 끝까지 이동하면서
# str1의 문자 하나를 먼저 추가하고,
# 같은 위치의 str2 문자 하나를 다음에 추가한다.

# answer는 결과를 저장할 빈 문자열이다.
# answer += 문자 를 사용하면 기존 문자열 뒤에 문자가 추가된다.

# 모든 문자를 번갈아 추가한 뒤 answer를 return 한다.

def solution(str1, str2):
    answer = ''
    
    # range()는 끝 숫자를 포함하지 않음
    for n in range(len(str1)):
        answer += str1[n] + str2[n]
    
    return answer

