testcase = int(input())
a = []

for i in range(testcase):
    ticket = input()
    digits = []
    for digit in ticket:
        digits.append(int(digit))
        
    first3= digits[0:3]
    last3 = digits[3:7]
    
    sumfirst = sum(first3)
    sumlast = sum(last3)
    if sumfirst == sumlast:
        a.append('YES')
    else:
        a.append('NO')
for z in a:

    print(z)