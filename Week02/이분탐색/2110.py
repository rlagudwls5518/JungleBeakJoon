n, c = map(int, input().split())  # n: 집의 수, c: 공유기 수

array = []
for i in range(n):
    array.append(int(input()))  # 집의 좌표를 입력받아 array에 저장
array.sort()  # 위치순으로 정렬

def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2  # 공유기 사이 거리의 후보
        current = array[0]        # 첫 번째 집에 무조건 설치
        count = 1                 # 첫 공유기 설치 count = 1

        for i in range(1, len(array)):
            # 현재 설치된 공유기에서 mid 이상 떨어졌다면 설치 가능
            if array[i] >= current + mid:
                count += 1
                current = array[i]  # 마지막 설치 위치 갱신

        if count >= c:
            # c개 이상 설치 가능 → 거리 늘릴 수 있음
            global answer
            answer = mid
            start = mid + 1
        else:
            # 너무 많이 설치 못함 → 거리 좁혀야 함
            end = mid - 1


start = 1                      # 가능한 최소 거리
end = array[-1] - array[0]     # 가능한 최대 거리 (가장 먼 집 간의 거리)
answer = 0                     # 최종 답


print(answer)
