# -*- coding:utf-8 -*-
# 1080215 钠光双棱镜干涉
"""
input:
output:

"""
import math
import xml.dom.minidom
from math import sqrt
from jinja2 import Environment
from handler import texdir

# input data
x = []
light_small_big = []
data_big = []
data_small = []

average_delta_x = 0
s_small = 0
s_big = 0
b_big = 0
b_small = 0
lam = 0
ua_10delta_x = 0
u_10delta_x = 0
u_delta_x = 0
u_b1 = 0
u_b2 = 0
u_lam = 0
re_u = 0
answer = 0

X = []
AVERAGE_DELTA_X = []
UA_10DELTA_X = ""
U_10DELTA_X = ""
U_DELTA_X = ""
LIGHT_SMALL_BIG = []
DATA_BIG = []
DATA_SMALL = []
B_BIG = ""
B_SMALL = ""
U_B1 = ""
U_B2 = ""
S_SMALL = ""
S_BIG = ""
LAMBDA = ""
U_LAMBDA = ""
RE_U = ""
RESULT_LAMBDA = ""
RESULT_U_LAMBDA = ""

env = Environment(line_statement_prefix="#", variable_start_string="%%", variable_end_string="%%")


def handler(xml):
    xmlReader(xml)
    niconiconi()
    regulation()
    file_object = open(texdir + "/Handle1080215.tex", "r")
    latex = file_object.read().decode('utf-8', 'ignore')
    return lexFiller(latex)


def niconiconi():
    global x, average_delta_x, light_small_big, data_big, data_small, s_small, s_big, b_big, b_small, lam, \
        ua_10delta_x, u_10delta_x, u_delta_x, u_b1, u_b2, u_lam, re_u, answer
    delta_x = []
    for i in range(len(x) / 2):
        delta_x.append(abs(x[i + len(x) / 2] - x[i]))
    average_delta_x = sum(delta_x) / len(delta_x) / len(delta_x)
    ua_10delta_x = Ua(delta_x, 10 * average_delta_x, len(delta_x))
    ub_10delta_x = 0.00289
    u_10delta_x = sqrt(pow(ua_10delta_x, 2) + pow(ub_10delta_x, 2))
    u_delta_x = u_10delta_x / 10

    b_small = (data_small[0] - data_small[1] + data_small[2] - data_small[3]) / 2
    b_big = (data_big[0] - data_big[1] + data_big[2] - data_big[3]) / 2

    s_small = abs(light_small_big[0] - light_small_big[1])  # cm
    s_big = abs(light_small_big[0] - light_small_big[2])  # cm

    lam = (average_delta_x * sqrt(b_big * b_small) / (s_small + s_big) / 10) * 1000000  # nm

    # 计算不确定度
    u_b1 = 0.025 * b_small / math.sqrt(3)
    u_b2 = 0.025 * b_big / math.sqrt(3)

    u_s1 = 0.5 / sqrt(3)
    u_s1s2 = sqrt(2) * u_s1
    u_lam = sqrt(
        pow(u_delta_x / average_delta_x, 2) + 1 / 4 * pow(u_b1 / b_small, 2) + 1 / 4 * pow(u_b2 / b_big, 2) + pow(
            u_s1s2 / (s_small + s_big), 2)) * lam
    re_u = u_lam / lam
    bitAdapt(lam, u_lam, 2, -3)


def regulation():
    global x, average_delta_x, light_small_big, data_big, data_small, s_small, s_big, b_big, b_small, lam, \
        ua_10delta_x, u_10delta_x, u_delta_x, u_b1, u_b2, u_lam, re_u, answer, X, AVERAGE_DELTA_X, LIGHT_SMALL_BIG, \
        DATA_BIG, DATA_SMALL, S_SMALL, S_BIG, B_BIG, B_SMALL, LAMBDA, UA_10DELTA_X, \
        U_10DELTA_X, U_DELTA_X, U_B1, U_B2, U_LAMBDA, RE_U, RESULT_LAMBDA, RESULT_U_LAMBDA
    X = x
    LIGHT_SMALL_BIG = light_small_big
    DATA_SMALL = data_small
    DATA_BIG = data_big

    AVERAGE_DELTA_X = ToScience(average_delta_x)
    S_SMALL = ToScience(s_small)
    S_BIG = ToScience(s_big)
    B_SMALL = ToScience(b_small)
    B_BIG = ToScience(b_big)
    LAMBDA = ToScience(lam)
    UA_10DELTA_X = ToScience(ua_10delta_x)
    U_10DELTA_X = ToScience(u_10delta_x)
    U_DELTA_X = ToScience(u_delta_x)
    U_B1 = ToScience(u_b1)
    U_B2 = ToScience(u_b2)
    U_LAMBDA = ToScience(u_lam)
    RE_U = ToScience(re_u)
    RESULT_LAMBDA = answer[0]
    RESULT_U_LAMBDA = answer[1]
    pass


def lexFiller(latex):
    global X, AVERAGE_DELTA_X, LIGHT_SMALL_BIG, DATA_BIG, DATA_SMALL, S_SMALL, S_BIG, B_BIG, B_SMALL, LAMBDA, UA_10DELTA_X, \
        U_10DELTA_X, U_DELTA_X, U_B1, U_B2, U_LAMBDA, RE_U, RESULT_LAMBDA, RESULT_U_LAMBDA
    result = env.from_string(latex).render(
        X_10811=X,
        DATA_BIG=DATA_BIG,
        DATA_SMALL=DATA_SMALL,
        DELTA_X=AVERAGE_DELTA_X,
        UA_10DELTA_X=UA_10DELTA_X,
        U_10DELTA_X=U_10DELTA_X,
        U_DELTA_X=U_DELTA_X,
        LIGHT_SMALL_BIG=LIGHT_SMALL_BIG,
        B_SMALL=B_SMALL,
        B_BIG=B_BIG,
        S_SMALL=S_SMALL,
        S_BIG=S_BIG,
        LAMDA_LAB=LAMBDA,
        U_B1=U_B1,
        U_B2=U_B2,
        RE_LAMDA=RE_U,
        RESULT_LAMDA=RESULT_LAMBDA,
        RESULT_U_LAMDA=RESULT_U_LAMBDA,
        U_LAMDA=U_LAMBDA
    )
    return result


def ToScience(number):
    Tempstr = format(number, '.4g')
    # 如果发现Tempstr中含有e的话，说明是科学计数法
    if 'e' in Tempstr:
        index_str = Tempstr.split('e')
        return index_str[0] + '{\\times}10^{' + str(int(index_str[1])) + '}'
    else:
        return Tempstr


# 计算a类不确定度
def Ua(x, aver, k):
    sumx = 0
    for i in range(k):
        sumx += (x[i] - aver) ** 2
    return sqrt(sumx / (k * (k - 1)))


# 最终结果的对齐
def bitAdapt(x, u_x, up, low):
    global answer
    answer = [0, 0, 0]
    maxu = 10 ** up
    minu = 10 ** low
    if u_x > maxu:
        print ("误差过大")
        return
    if u_x < minu:
        print ("误差过小")
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


def xmlReader(item):
    global x, light_small_big, data_big, data_small

    tablelist = item.getElementsByTagName('table')
    table_1 = tablelist[0]
    datalist = table_1.getElementsByTagName('td')
    # 获取光源及小像大像位置
    light_small_big = (float(datalist[0].firstChild.nodeValue), float(datalist[3].firstChild.nodeValue),
                       float(datalist[4].firstChild.nodeValue))
    table_2 = tablelist[1]
    datalist = table_2.getElementsByTagName('td')
    # 获取大像位置
    data_b2 = (float(datalist[0].firstChild.nodeValue), float(datalist[1].firstChild.nodeValue),
               float(datalist[2].firstChild.nodeValue), float(datalist[3].firstChild.nodeValue))
    for b in data_b2:
        data_big.append(b)

    # 获取小像位置
    data_b1 = (float(datalist[4].firstChild.nodeValue), float(datalist[5].firstChild.nodeValue),
               float(datalist[6].firstChild.nodeValue), float(datalist[7].firstChild.nodeValue))
    for b in data_b1:
        data_small.append(b)

    table_3 = tablelist[2]
    datalist = table_3.getElementsByTagName('td')
    # 获取条纹位置
    for i in range(len(datalist)):
        x.append(float(datalist[i].firstChild.nodeValue))
    print x


if __name__ == '__main__':
    def ReadXmlTop():
        latex_head_file = open('./Head.tex', 'r')
        latex_head = latex_head_file.read().decode('utf-8', 'ignore')
        latex_tail = "\n\\end{document}"
        latex_body = ""
        dom = xml.dom.minidom.parse('./1080114test/1081.xml')
        root = dom.documentElement
        sublab_list = root.getElementsByTagName('sublab')
        for sublab in sublab_list:
            sublab_status = sublab.getAttribute("status")
            sublab_id = sublab.getAttribute("id")
            if (sublab_status == 'true') & (sublab_id == '10811'):
                latex_body += handler(sublab)
        return latex_head + latex_body + latex_tail


    fileTex = open('./1080114test/1080114test.tex', 'w')
    text = ReadXmlTop().encode('utf-8')
    fileTex.write(text)
    fileTex.close()
    print lam
    print u_lam
# -*- coding:utf-8 -*-
