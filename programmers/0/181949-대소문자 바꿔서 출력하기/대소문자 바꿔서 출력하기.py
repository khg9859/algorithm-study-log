str = input()
result = ""

# 문자열은 여러 개의 문자로 이루어져 있으므로 한 글자씩 확인한다.

# length가 아니라 len
for n in range(len(str)):
    if str[n].islower():
        result += str[n].upper()

# 힌트 1: else 뒤에는 조건을 쓰지 않아
    else:
        result += str[n].lower()
    
print(result)
    
# isupper()는 해당 문자가 대문자인지 확인한다.
# islower()는 해당 문자가 소문자인지 확인한다.

# upper()는 소문자를 대문자로 바꾼다.
# lower()는 대문자를 소문자로 바꾼다.

# 변환한 문자들을 하나의 문자열로 이어 붙인 뒤 출력한다.

