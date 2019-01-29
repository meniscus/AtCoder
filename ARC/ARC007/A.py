X = input()
s = input()

a = [s_ for s_ in list(s) if s_ != X]
print(''.join(a))