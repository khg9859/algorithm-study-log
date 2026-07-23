def solution(ineq, eq, n, m):
    answer = 0
    
    # 문자열은 비어 있지 않으면 True로 취급되어서 결국 or에서 첫 번째 값만 들어감
    
    
    if ineq == "<" and eq == "=":
        if n <= m:
            answer = 1
        else:
            answer = 0
        
        
    if ineq == "<" and eq == "!":
        if n > m:
            answer = 0
        else:
            answer = 1
        
    if ineq == ">" and eq == "=":
        if n >= m:
            answer = 1
        else:
            answer = 0
        
    if ineq == ">" and eq == "!":
        if n > m:
            answer = 1
        else:
            answer = 0
    
    
    return answer