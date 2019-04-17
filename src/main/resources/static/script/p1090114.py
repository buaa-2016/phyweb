# -*- coding:utf-8 -*-
"""
input:
    d_list
output:
    D_LIST = []
    DELTA_D = []
    AVERAGE_DELTA_D = ""
    LAM = ""
    UA_DELTA_D = ""
    U_DELTA_D = ""
    U_LAM = ""
    RE_U = ""
    RESULT_LAM = ""
    RESULT_U_LAM = ""
"""
d_list = []

delta_d = []
average_delta_d = 0
lam = 0
ua_delta_d = 0
u_delta_d = 0
u_lam = 0
re_u = 0
answer = []

D_LIST1 = []
D_LIST2 = []
DELTA_D = []
AVERAGE_DELTA_D = ""
LAM = ""
UA_DELTA_D = ""
U_DELTA_D = ""
U_LAM = ""
RE_U = ""
RESULT_LAM = ""
RESULT_U_LAM = ""

import xml.dom.minidom
from math import sqrt
from jinja2 import Environment
from handler import texdir

env = Environment(line_statement_prefix="#", variable_start_string="%%", variable_end_string="%%")


def handler(xml):
    global d_list
    d_list = []
    xmlReader(xml)
    niconiconi()
    regulation()
    file_object = open(texdir + "/Handle1090114.tex", "r")
    latex = file_object.read().decode('utf-8', 'ignore')
    return lexFiller(latex)


def niconiconi():
    global d_list, delta_d, average_delta_d, lam, ua_delta_d, u_delta_d, u_lam, re_u
    for i in range(5):
        delta_d.append(d_list[i + 5] - d_list[i])
    average_delta_d = sum(delta_d) / 5
    N = 500
    lam = 2 * average_delta_d / N * 1000000  # nm
    ua_delta_d = Ua(delta_d, average_delta_d, 5)
    ub_delta_d = 0.0000289
    u_delta_d = sqrt(pow(ua_delta_d, 2) + pow(ub_delta_d, 2))
    u_N = 0.577
    u_lam = lam * sqrt(pow(u_delta_d / average_delta_d, 2) + pow(u_N / N, 2))  # nm
    re_u = u_lam / lam
    bitAdapt(lam, u_lam, 2, -3)


def regulation():
    global d_list, delta_d, average_delta_d, lam, ua_delta_d, u_delta_d, u_lam, re_u, \
        D_LIST1, D_LIST2, DELTA_D, AVERAGE_DELTA_D, LAM, UA_DELTA_D, U_DELTA_D, U_LAM, RE_U, RESULT_LAM, RESULT_U_LAM
    for i in range(5):
        D_LIST1.append(toScience(d_list[i]))
        D_LIST2.append(toScience(d_list[i + 5]))
    for delta in delta_d:
        DELTA_D.append(toScience(delta))
    AVERAGE_DELTA_D = toScience(average_delta_d)
    LAM = toScience(lam)
    UA_DELTA_D = toScience(ua_delta_d)
    U_DELTA_D = toScience(u_delta_d)
    U_LAM = toScience(u_lam)
    RE_U = toScience(re_u)
    RESULT_LAM = answer[0]
    RESULT_U_LAM = answer[1]
    pass


def xmlReader(sublab_root):
    global d_list
    sublab_table_list = sublab_root.getElementsByTagName("table")
    for table in sublab_table_list:
        table_tr_list = table.getElementsByTagName("tr")
        for tr in table_tr_list:
            tr_td_list = tr.getElementsByTagName("td")
            for td in tr_td_list:
                d_list.append(float(td.firstChild.nodeValue))


def lexFiller(lex):
    global D_LIST1, D_LIST2, DELTA_D, AVERAGE_DELTA_D, LAM, UA_DELTA_D, U_DELTA_D, U_LAM, RE_U, RESULT_LAM, RESULT_U_LAM
    result = env.from_string(lex).render(
        D_LIST1=D_LIST1,
        D_LIST2=D_LIST2,
        DELTA_D=DELTA_D,
        AVERAGE_DELTA_D=AVERAGE_DELTA_D,
        LAM=LAM,
        UA_DELTA=UA_DELTA_D,
        U_DELTA=U_DELTA_D,
        U_LAM=U_LAM,
        RE_U=RE_U,
        RESULT_LAM=answer[0],
        RESULT_U_LAM=answer[1]
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
    tempstr = format(number, '.7g')
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


if __name__ == '__main__':
    d_list = [51.05257, 51.08570, 51.11871, 51.15150, 51.18287, 51.21456, 51.25132, 51.28370, 51.31506, 51.34883]
    fileTex = open('./1090114test/1090114test.tex', 'w')
    text = handler("").encode('utf-8')
    fileTex.write(text)
    fileTex.close()
    print delta_d
    print average_delta_d
    print lam
    print ua_delta_d
    print u_delta_d
    print u_lam
    print answer
