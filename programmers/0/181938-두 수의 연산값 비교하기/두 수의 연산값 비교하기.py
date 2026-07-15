def solution(a, b):
    answer = 0
    
    ab = int(str(a) + str(b))
    n = 2 * a * b
    
    if ab > n:
        answer = ab
    else:
        answer = n
    
    
    return answer