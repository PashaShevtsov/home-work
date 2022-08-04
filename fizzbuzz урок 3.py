def fizzbuzz(f, b, n):
  l = []
  for i in range(1, n+1):
    if not i%f and not i%b:
      l.append("FB")
    elif not i%f:
      l.append("F")
    elif not i%b:
      l.append("B")
    else:
      l.append(str(i))

  return " ".join(l) + "\n"

filename = "date.txt"
filename2 = "results.txt"

f = open(filename)
f2 = open(filename2, 'w')

for string in f:
  a, b, c = map(int, string.split())
  f2.write(fizzbuzz(a, b, c))

f.close()
f2.close()