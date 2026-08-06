def solution(a, d, included):
    answer = 0

    # included의 인덱스를 처음부터 끝까지 반복
    for i in range(len(included)):

        # included[i]가 True라면
        if included[i]:
            # i에 해당하는 등차수열 값을 answer에 더하기
            answer += a + (i*d)

    return answer