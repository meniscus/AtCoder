N = int(input())
cards = [int(i) for i in input().split()]
cards.sort(reverse=True)

alice = cards[0::2]
bob = cards[1::2]
print(sum(alice) - sum(bob))
