def solution(my_string, k):
    answer = ''
    
    # in 뒤에 여기서 꺼내쓰기 k라고 적으면 3이기에 꺼낼수없음 range(K) 사용해서 0 , 1, 2 에서 꺼내서 사용
    for n in range(k):
        answer += my_string
    
    return answer