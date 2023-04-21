import sys

N, M = map(int, sys.stdin.readline().split())
lesson_list = list(map(int, sys.stdin.readline().split()))

start = max(lesson_list)
end = sum(lesson_list)
ans = sum(lesson_list)

while start <= end:
    mid = (start + end) // 2

    cnt = 1
    lesson_sum = 0
    for lesson in lesson_list:
        if lesson_sum + lesson > mid:
            lesson_sum = lesson
            cnt += 1
        else:
            lesson_sum += lesson

    if cnt <= M:
        end = mid - 1
        ans = min(ans, mid)
    else:
        start = mid + 1
print(ans)
