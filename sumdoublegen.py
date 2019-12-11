ostr = "f, g = int(input()), int(input())\ndef sumd(x, y):\n"
def sum_double(a, b):
  if a == b: return 2*(a+b)
  return a + b
for m in range(200):
    for n in range(200):
        ostr += f"    if x == {m} and y == {n}:\n        return {sum_double(m, n)}\n"
ostr += "sumd(f, g)"
f = open("sumdouble.txt","w+")
f.write(ostr)
