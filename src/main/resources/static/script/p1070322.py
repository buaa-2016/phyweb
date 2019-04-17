# -*- coding:utf-8 -*-
"""
input:
    angle_A
    u_A
    angle_a1
    angle_a2
    angle_b1
    angle_b2
output:
    K
    ANGLE_A1
    ANGLE_A2
    ANGLE_B1
    ANGLE_B2
    ANGLE_I
    AVERAGE_I
    N
    UA_I
    U_I
    U_N
    RE_U
    RESULT_N
    RESULT_U_N
"""
import xml.dom.minidom
from math import sqrt
from jinja2 import Environment
from numpy import cos
from numpy import pi
from numpy import sin
from handler import texdir

env = Environment(line_statement_prefix="#", variable_start_string="%%", variable_end_string="%%")

angle_A = 0
u_A = 0
angle_a1 = []
angle_a2 = []
angle_b1 = []
angle_b2 = []

k = 0
angle_i = []
average_i_a = 0
average_i_r = 0
n = 0
ua_i = 0
u_i = 0
u_n = 0
re_u = 0
answer = []

K = 0
ANGLE_A1 = []
ANGLE_A2 = []
ANGLE_B1 = []
ANGLE_B2 = []
ANGLE_I = []
AVERAGE_I = ""
N = ""
UA_I = ""
U_I = ""
U_N = ""
U_A = ""
RE_U = ""
RESULT_N = ""
RESULT_U_N = ""


def handler(xml):
    global angle_a1
    global angle_a2
    global angle_b1
    global angle_b2
    global angle_A
    global u_A
    xmlReader(xml)
    niconiconi()
    regulation()
    file_object = open(texdir + "/Handle1070322.tex", "r")
    latex = file_object.read().decode('utf-8', 'ignore')
    return lexFiller(latex)


def niconiconi():
    global angle_A, u_A, angle_a1, angle_a2, angle_b1, angle_b2, k, angle_i, average_i_a, average_i_r, n, \
        ua_i, u_i, u_n, re_u
    k = len(angle_a1)
    if k == 0:
        print "illegal input: no data"
        return
    for i in range(k):
        angle_i.append((((angle_a2[i] - angle_a1[i]) + (angle_b2[i] - angle_b1[i])) % 360) / 2)
    average_i_a = sum(angle_i) / k
    average_i_r = average_i_a * pi / 180
    angle_A_r = angle_A * pi / 180
    u_A_r = u_A * pi / 180
    n = sqrt((pow(((cos(angle_A_r) + sin(average_i_r)) / sin(angle_A_r)), 2)) + 1)
    ua_i = Ua(angle_i, average_i_a, k)  # 角度值
    ub_i = 0.00962
    u_i = sqrt(pow(ua_i, 2) + pow(ub_i, 2)) * pi / 180
    ca = cos(angle_A_r)
    sa = sin(angle_A_r)
    ci = cos(average_i_r)
    si = sin(average_i_r)
    u_n = (ca + si) / n / si / si * sqrt(pow(ci * u_i, 2) + pow((ca * si + 1) * u_A_r / sa, 2))
    re_u = u_n / n
    bitAdapt(n, u_n, -1, -5)


def regulation():
    global angle_A, u_A, angle_a1, angle_a2, angle_b1, angle_b2, k, angle_i, average_i_a, average_i_r, n, \
        ua_i, u_i, u_n, re_u, K, ANGLE_A1, ANGLE_A2, ANGLE_B1, ANGLE_B2, ANGLE_I, AVERAGE_I, N, UA_I, U_I, \
        U_N, RE_U, RESULT_N, RESULT_U_N, U_A
    K = k
    for a1 in angle_a1:
        ANGLE_A1.append({'angle': str(int(a1)), 'minus': str(int((a1 - int(a1)) * 60 + 0.1))})
    for a2 in angle_a2:
        ANGLE_A2.append({'angle': str(int(a2)), 'minus': str(int((a2 - int(a2)) * 60 + 0.1))})
    for b1 in angle_b1:
        ANGLE_B1.append({'angle': str(int(b1)), 'minus': str(int((b1 - int(b1)) * 60 + 0.1))})
    for b2 in angle_b2:
        ANGLE_B2.append({'angle': str(int(b2)), 'minus': str(int((b2 - int(b2)) * 60 + 0.1))})
    for i in angle_i:
        ANGLE_I.append({'angle': str(int(i)), 'minus': str(int((i - int(i)) * 60 + 0.1))})
    AVERAGE_I = toScience(average_i_a)
    N = toScience(n)
    UA_I = toScience(ua_i)
    U_I = toScience(u_i)
    U_N = toScience(u_n)
    RE_U = toScience(re_u)
    RESULT_N = answer[0]
    RESULT_U_N = answer[1]
    U_A = toScience(u_A)


def xmlReader(sublab_root):
    global angle_a1, angle_a2, angle_b1, angle_b2, angle_A, u_A
    sublab_table_list = sublab_root.getElementsByTagName("table")
    table = sublab_table_list[0]
    table_tr_list = table.getElementsByTagName("tr")
    for tr in table_tr_list:
        tr_td_list = tr.getElementsByTagName("td")
        angle_a1.append(angleTransfer(float(tr_td_list[0].firstChild.nodeValue)))
        angle_b1.append(angleTransfer(float(tr_td_list[1].firstChild.nodeValue)))
        angle_a2.append(angleTransfer(float(tr_td_list[2].firstChild.nodeValue)))
        angle_b2.append(angleTransfer(float(tr_td_list[3].firstChild.nodeValue)))
    table_2 = sublab_table_list[1]
    tr_list = table_2.getElementsByTagName("tr")
    tr = tr_list[0]
    td_list = tr.getElementsByTagName("td")
    angle_A = float(td_list[0].firstChild.nodeValue)
    u_A = float(td_list[1].firstChild.nodeValue)


def lexFiller(source):
    global K, ANGLE_A1, ANGLE_A2, ANGLE_B1, ANGLE_B2, ANGLE_I, AVERAGE_I, N, UA_I, U_I, U_N, U_A, RE_U, RESULT_N, RESULT_U_N
    result = env.from_string(source).render(
        ANGLE_I=ANGLE_I,
        ANGLE_A1=ANGLE_A1,
        ANGLE_A2=ANGLE_A2,
        ANGLE_B1=ANGLE_B1,
        ANGLE_B2=ANGLE_B2,
        AVERAGE_I=AVERAGE_I,
        U_A=U_A,
        RE_U=RE_U,
        UA_I=UA_I,
        N=N,
        U_I=U_I,
        U_N=U_N,
        RESULT_N=RESULT_N,
        RESULT_U_N=RESULT_U_N
    )
    return result


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


# 将数字转化成可填入文件的字符串
def toScience(number):
    tempstr = format(number, '.5g')
    if 'e' in tempstr:
        index_str = tempstr.split('e')
        return index_str[0] + '{\\times}10^{' + str(int(index_str[1])) + '}'
    else:
        return tempstr


# a类不确定度计算
def Ua(x, aver, k):
    sumx = 0
    for i in range(k):
        sumx += (x[i] - aver) ** 2
    return sqrt(sumx / (k * (k - 1)))


# 将‘度.分’表示的角度转化成角度表示
def angleTransfer(raw):
    return int(raw) + (raw - int(raw)) * 100 / 60


if __name__ == '__main__':
    pass
