# -*- coding: utf-8 -*-

from math import sqrt


# 将二维列表x中的每一个值保留b位小数（带四舍五入）
def RoundTwo(x, b=2):
    for i in range(len(x)):
        for j in range(len(x[i])):
            x[i][j] = round(x[i][j], b)
            x[i][j] = "%.*f" % (b, x[i][j])


# 将一维列表x中的每一个值保留b位小数（带四舍五入）
def RoundOne(x, b):
    for i in range(len(x)):
        x[i] = round(x[i], b)
        x[i] = "%.*f" % (b, x[i])


# 计算a类不确定度：x是一个列表，aver是x的平均值，k是数据的组数（不一定等于len(x)，
#               因为x后面可能添加了x的平均值）
def Ua(x, aver, k):
    if (k <= 1):
        return 0
    sumx = 0
    for i in range(k):
        sumx += (x[i] - aver) ** 2
    return sqrt(sumx / (k * (k - 1)))


# 匹配最终结果：(f+u_f)
# 输入算出来的最终结果和它的不确定度，可以返回最终结果的形式
def BitAdapt(x, u_x):
    ten = 0
    ften = 0
    if (u_x >= 10):
        temp = x
        while (temp >= 10):
            temp = temp / 10
            ten += 1
        x = float(x) / 10 ** ten
        u_x = float(u_x) / 10 ** ten
    elif (x < 0.001):
        temp = x
        ften = 0
        while (temp < 1):
            temp = temp * 10
            ften += 1
        x = float(x) * 10 ** ften
        u_x = float(u_x) * 10 ** ften
    Tempbit = 0
    bit = 0
    while (1):
        i = 0
        while (1):
            temp = float(u_x) * (10 ** i)
            if (temp >= 1):
                bit = i
                break
            else:
                i += 1
        u_x = round(float(u_x), bit)
        x = round(float(x), bit)
        u_x = ("%.*f" % (bit, u_x))
        x = ("%.*f" % (bit, x))
        i = 0
        while (1):
            temp = float(u_x) * (10 ** i)
            if (temp >= 1):
                Tempbit = i
                break
            else:
                i += 1
        if Tempbit == bit:
            break
    if ten > 0:
        x = "(" + str(x) + "\\pm"
        u_x = str(u_x) + "){\\times}10^{" + str(ten) + "}"
    elif ften > 0:
        x = "(" + str(x) + "\\pm"
        u_x = str(u_x) + "){\\times}10^{-" + str(ften) + "}"
    else:
        x = "(" + str(x) + "\\pm"
        u_x = str(u_x) + ")"
    return x + u_x


# 转换为科学计数法表示
def ToScience(number):
    Tempstr = format(number, '.4g')
    # 如果发现Tempstr中含有e的话，说明是科学计数法
    if 'e' in Tempstr:
        index_str = Tempstr.split('e')
        if (index_str[1][0] == '+'):
            index_str[1] = index_str[1][1:]
        if index_str[0] == '1':
            return '10^{' + str(int(index_str[1])) + '}'
        else:
            return index_str[0] + '{\\times}10^{' + str(int(index_str[1])) + '}'
    else:
        return Tempstr


# 对于x和y两个一维列表进行一元线性处理：y = a + bx
# 返回列表[b,r]
def ULR(x, y):
    size = len(x) - 1
    x_2 = []
    y_2 = []
    xy = []
    for i in range(size):
        x_2.append(x[i] ** 2)
        y_2.append(y[i] ** 2)
        xy.append(x[i] * y[i])
    x_2.append(sum(x_2) / size)
    y_2.append(sum(y_2) / size)
    xy.append(sum(xy) / size)

    b = (x[size] * y[size] - xy[size]) / (pow(x[size], 2) - x_2[size])
    r = (xy[size] - x[size] * y[size]) / sqrt((x_2[size] - pow(x[size], 2)) * (y_2[size] - pow(y[size], 2)))
    res = [b, r]
    return res


# 求仪器误差限
def DELTA_R(R):
    res = 0.02 + R % 1 * 5 / 100.0
    R = R - R % 1
    res = res + R % 10 * 5 / 1000.0
    R = R - R % 10
    res = res + R % 100 * 2 / 1000.0
    R = R - R % 100
    res = res + R / 1000.0
    return res


# 逐差法求
def DWM(x):
    res = []
    size = len(x) / 2
    for i in range(size):
        temp = abs(x[i] - x[i + size])
        res.append(temp)
    return res


# 测试时的误差要求，误差范围内就返回1，否则就返回0
def Mistake(x, y):
    x = abs(x)
    y = abs(y)
    r1 = x + x / 100
    r2 = x - x / 100
    if (y > r1) | (y < r2):
        return 0
    else:
        return 1


# 规约最终结果，进行有效位数限定
def bitAdapt(x, u_x, up, low):
    global answer
    answer = [0, 0, 0]
    maxu = 10 ** up
    minu = 10 ** low
    if u_x > maxu:
        print ("误差过大233")
        return
    if u_x < minu:
        print ("误差过小233")
        return
    for i in range(low, up):
        if 10 ** i < u_x < 10 ** (i + 1):
            break
    if u_x > (10 ** (i + 1) - 10 ** i):
        bit = i + 1
        u_x = 10 ** bit
    else:
        bit = i
        u_x += 10 ** bit
    if int(x / (10 ** (bit - 1))) % 10 > 5:
        x += 10 ** bit
    elif int(x / (10 ** (bit - 1))) % 10 == 5 and int(x / (10 ** bit)) % 2 == 1:
        x += 10 ** bit
    if bit < 0:
        answer[0] = str(int(x / (10 ** bit)) * (10 ** bit))[0:len(str(10 ** bit)) + len(str(int(x))) - 1]
        answer[1] = str(int(u_x / (10 ** bit)) * (10 ** bit))[0:len(str(10 ** bit))]
        answer[2] = 0
    else:
        answer[0] = str(int(x / (10 ** bit)))
        answer[1] = str(int(u_x / (10 ** bit)))
        answer[2] = bit
    return
