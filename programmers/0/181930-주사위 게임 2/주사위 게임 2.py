def solution(a, b, c):
    ret = 0
    
    if a != b != c != a:
        ret = a + b + c
        
    elif a == b != c or b == c != a or a == c != b:
        ret = (a + b + c) * (a**2 + b**2 + c**2)
    
    elif a == b == c:
         ret = (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    
            
    return ret