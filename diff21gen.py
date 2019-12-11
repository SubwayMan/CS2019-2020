ostr = "f = int(input())\ndef dif21(x):\n"
def diff21(n):
  if n > 21: return (n - 21) * 2
  return 21 - n
for m in range(1201):
     ostr += f"    if x == {m}:\n        return {diff21(m)}\n"
ostr += "dif21(f)"
f = open("diff21.txt","w+")
f.write(ostr)
