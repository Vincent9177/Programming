import math
count = 0
total = 0

while True:
    numberlist = []
    sum = 0
    count = 0
    total = 0
    numbers = int (input('输入数字数量:'))
    while count <= numbers - 1 :
        count = count + 1
        inputs = float (input("输入第%d个数的数值:" %(count)))
        total = total + inputs
        numberlist.append(inputs)
    mean = total / numbers
    print('平均数为:',mean)
    for x in numberlist:
        deviation = (x - mean) * (x - mean)
        sum = sum + deviation
    print("方差为:",sum/numbers)
    print("标准差为:",math.sqrt(sum/numbers))
    continue
        