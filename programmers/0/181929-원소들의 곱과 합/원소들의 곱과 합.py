def solution(num_list):
    a = 1
    b = 0
    
    for n in num_list:
        a *= n
        b += n
        
    c = b ** 2
    
    if a < c:
        return 1
    else:
        return 0