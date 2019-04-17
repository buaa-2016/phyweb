# -*- coding:utf-8 -*-
"""
input:
    angle_a1
    angle_a2
    angle_b1
    angle_b2
output:
    ANGLE_DELTA_MIN
    ANGLE_A1_MIN
    ANGLE_A2_MIN
    ANGLE_B1_MIN
    ANGLE_B2_MIN
    AVERAGE_A
    AVERAGE_MIN
    U_A
    RE_U_MIN
    UA_MIN
    N1
    U_MIN
    U_N1
    RESULT_N1
    RESULT_U_N1
"""
import xml.dom.minidom
from math import sqrt
from jinja2 import Environment
from numpy import cos
from numpy import pi
from numpy import sin
from handler import texdir
from handler import scriptdir

# 输入数据
angle_a1 = []
angle_a2 = []
angle_b1 = []
angle_b2 = []
angle_A = 0
u_A = 0
# 数据处理得到数据
k = 0
angle_delta = []
average_delta_a = 0
average_delta_r = 0
n1 = 0

ua_delta_a = 0
ua_delta_r = 0
u_delta = 0
u_n1 = 0
re_u = 0

answer = []
# 经过规范化的输出数据
ANGLE_DELTA_MIN = []
ANGLE_A1_MIN = []
ANGLE_A2_MIN = []
ANGLE_B1_MIN = []
ANGLE_B2_MIN = []
AVERAGE_A = ""
AVERAGE_MIN = ""
U_A = ""
RE_U_MIN = ""
UA_MIN = ""
N1 = ""
U_MIN = ""
U_N1 = ""
RESULT_N1 = ""
RESULT_U_N1 = ""

env = Environment(line_statement_prefix="#", variable_start_string="%%", variable_end_string="%%")


def handler(xml):
    xmlReader(xml)
    niconiconi()
    regulation()
    file_object = open(texdir + "/Handle1070312.tex", "r")
    latex = file_object.read().decode('utf-8', 'ignore')
    return lexFiller(latex)


def niconiconi():
    global angle_a1, angle_a2, angle_b1, angle_b2, angle_A, u_A, \
        k, angle_delta, average_delta_a, average_delta_r, n1, ua_delta_a, ua_delta_r, u_delta, u_n1, re_u
    angle_A_r = angle_A * pi / 180
    u_A_r = u_A * pi / 180
    k = len(angle_a1)
    if k == 0:
        print "illegal input"
        return
    for i in range(k):
        angle_delta.append((((angle_a2[i] - angle_a1[i]) + (angle_b2[i] - angle_b1[i])) % 360) / 2)
    average_delta_a = sum(angle_delta) / k
    average_delta_r = average_delta_a / 180 * pi
    n1 = sin((average_delta_r + angle_A_r) / 2) / sin(angle_A_r / 2)
    ua_delta_a = Ua(angle_delta, average_delta_a, k)
    ub_delta = 0.009622
    u_delta = sqrt(pow(ua_delta_a, 2) + pow(ub_delta, 2))
    u_delta_r = u_delta*pi/180
    temp1 = cos((average_delta_r + angle_A_r) / 2) * u_delta_r / 2 / sin(angle_A_r / 2)
    temp2 = sin(average_delta_r / 2) * u_A_r / 2 / pow(sin(angle_A_r / 2), 2)
    u_n1 = sqrt(pow(temp1, 2) + pow(temp2, 2))
    re_u = u_n1 / n1
    bitAdapt(n1, u_n1, -1, -5)


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
    global ANGLE_A1_MIN, ANGLE_A2_MIN, ANGLE_B1_MIN, ANGLE_B2_MIN, ANGLE_DELTA_MIN, AVERAGE_A, AVERAGE_MIN, U_A, \
        RE_U_MIN, UA_MIN, N1, U_MIN, U_N1, RESULT_N1, RESULT_U_N1
    result = env.from_string(source).render(
        ANGLE_DELTA_MIN=ANGLE_DELTA_MIN,
        ANGLE_A1_MIN=ANGLE_A1_MIN,
        ANGLE_A2_MIN=ANGLE_A2_MIN,
        ANGLE_B1_MIN=ANGLE_B1_MIN,
        ANGLE_B2_MIN=ANGLE_B2_MIN,
        AVERAGE_A=AVERAGE_A,
        AVERAGE_MIN=AVERAGE_MIN,
        U_A=U_A,
        RE_U_MIN=RE_U_MIN,
        UA_MIN=UA_MIN,
        N1=N1,
        U_MIN=U_MIN,
        U_N1=U_N1,
        RESULT_N1=RESULT_N1,
        RESULT_U_N1=RESULT_U_N1
    )
    return result


def regulation():
    global ANGLE_A1_MIN, ANGLE_A2_MIN, ANGLE_B1_MIN, ANGLE_B2_MIN, ANGLE_DELTA_MIN, AVERAGE_A, AVERAGE_MIN, U_A, \
        RE_U_MIN, UA_MIN, N1, U_MIN, U_N1, RESULT_N1, RESULT_U_N1, angle_a1, angle_a2, angle_b1, angle_b2, angle_A, \
        u_A, k, angle_delta, average_delta_a, average_delta_r, n1, ua_delta_a, ua_delta_r, u_delta, u_n1, re_u
    for a1 in angle_a1:
        ANGLE_A1_MIN.append({'angle': str(int(a1)), 'minus': str(int((a1 - int(a1)) * 60 + 0.1))})
    for a2 in angle_a2:
        ANGLE_A2_MIN.append({'angle': str(int(a2)), 'minus': str(int((a2 - int(a2)) * 60 + 0.1))})
    for b1 in angle_b1:
        ANGLE_B1_MIN.append({'angle': str(int(b1)), 'minus': str(int((b1 - int(b1)) * 60 + 0.1))})
    for b2 in angle_b2:
        ANGLE_B2_MIN.append({'angle': str(int(b2)), 'minus': str(int((b2 - int(b2)) * 60 + 0.1))})
    for delta in angle_delta:
        ANGLE_DELTA_MIN.append({'angle': str(int(delta)), 'minus': str(int((delta - int(delta)) * 60 + 0.1))})
    AVERAGE_A = toScience(angle_A)
    AVERAGE_MIN = toScience(average_delta_a)
    U_A = toScience(u_A)
    RE_U_MIN = toScience(re_u)
    UA_MIN = toScience(ua_delta_a)
    N1 = toScience(n1)
    U_MIN = toScience(u_delta)
    U_N1 = toScience(u_n1)
    RESULT_N1 = answer[0]
    RESULT_U_N1 = answer[1]


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
    dom = xml.dom.minidom.parse(scriptdir + 'test/1070312test/1070312.xml')
    root = dom.documentElement
    sublab_list = root.getElementsByTagName('sublab')
    for sublab in sublab_list:
        handler(sublab)
    print(answer)
