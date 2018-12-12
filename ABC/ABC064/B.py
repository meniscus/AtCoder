N = int(input())
place = [int(i) for i in input().split()]
place.sort()
print(place[-1] - place[0])