num = 30
fibonacci = []

n = 1
while len(fibonacci)<num:
  if n == 1 or n == 2:
    fibonacci.append(1)
  else:
    fibonacci.append(sum(fibonacci[-2:]))
  n = n + 1

print(fibonacci)