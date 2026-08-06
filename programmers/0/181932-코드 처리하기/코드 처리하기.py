def solution(code):
    ret = ''
    idx = 0
    mode = 0
    
    for idx in range(len(code)):
        if mode == 0:
            if code[idx] != "1":
                if idx % 2 ==0:
                    ret = ret + code[idx]
                    
            if code[idx] == "1":
                mode = 1
                
        elif mode == 1:
            if code[idx] != "1":
                if idx % 2 != 0:
                    ret = ret + code[idx]
                    
            if code[idx] == "1":
                mode = 0  
    
    if ret == "":
        return "EMPTY"
    
    # 문자 1이면 모드 변경
    # 문자열 ret 만들기
    # 단, 시작할 때 mode는 0이며, return 하려는 ret가 만약 빈 문자열이라면 대신 "EMPTY"를 return

    
    return ret