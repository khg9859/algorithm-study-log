# 문자열은 인덱스로 원하는 구간을 잘라낼 수 있다.

# my_string[:s]
# → 인덱스 s 이전까지의 문자열

# overwrite_string
# → 새로 덮어쓸 문자열

# my_string[s + len(overwrite_string):]
# → 덮어쓴 부분 이후에 남아 있는 문자열

# 위 세 부분을 +로 이어 붙이면 된다.

# 문자열 슬라이싱 형식
# 문자열[시작:끝]
# 시작은 포함하고, 끝은a 포함하지 않는다.

def solution(my_string, overwrite_string, s):
    answer = ''
    
    #전
    f = my_string[:s]
    
    #index
    e = s + len(overwrite_string)
    
    #후 = d and ""
    b = my_string[e:]
    
    answer = f + overwrite_string + b
    
    
    
    return answer