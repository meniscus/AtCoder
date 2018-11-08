# あ
numbers = [int(i) for i in input().split()]

left1 = max(numbers)
numbers.remove(left1)
left2 = max(numbers)
right = min(numbers)

left = str(left1) + str(left2)

print(int(left) + right)

