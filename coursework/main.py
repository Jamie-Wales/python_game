temperatures = [4.7, 3, 4.8]

best_position = 0

for x in range(0, 2):
    if temperatures[best_position] < temperatures[x]:
        best_position = x

print(best_position)