#current problems:
#-does not work with double digit numbers because of bad input reading
#-no support for negative operators, but results may be negative
#-division results are aalways floats
ostr = "f, g, h = list(input())\ndef calc(num1, op, num2):\n    num1, num2 = int(num1), int(num2)\n"
for m in range(150):
    for n in range(150):
        ostr += f"    if num1 == {m} and op == \"+\" and num2 == {n}:\n        return {m + n}\n"
        ostr += f"    if num1 == {m} and op == \"-\" and num2 == {n}:\n        return {m - n}\n"
        ostr += f"    if num1 == {m} and op == \"*\" and num2 == {n}:\n        return {m * n}\n"
        if n == 0: g = "\"error\""
        else: g = m/n
        ostr += f"    if num1 == {m} and op == \"/\" and num2 == {n}:\n        return {g}\n"
        print(f"generated {m} for {n}")
ostr += "print(calc(f, g, h))"
f = open("calculator.py","w+")
f.write(ostr)
