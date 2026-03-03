N = int(input())
M = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]

# Step 1: Compute subject averages
averages = []
for col in range(M):
    col_sum = 0
    for row in range(N):
        col_sum += matrix[row][col]
    averages.append(col_sum / N)

# Step 2: Count passing students
count = 0

for row in range(N):
    for col in range(M):
        if matrix[row][col] > averages[col]:
            count += 1
            break   # Student counted once

print(count)