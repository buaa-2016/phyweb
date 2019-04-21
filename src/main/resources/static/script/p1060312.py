# -*- coding:utf-8 -*-
# 实验三 共轭法测量透镜焦距
"""
mm
input:
    s_pos
    p_pos
    big_1_1
    big_1_2
    big_2_1
    big_2_2
    small_1_1
    small_1_2
    small_2_1
    small_2_2
output:

"""
import xml.dom.minidom
from jinja2 import Environment
from handler import texdir
from handler import scriptdir
from phylab import *

env = Environment(line_statement_prefix="#", variable_start_string="%%", variable_end_string="%%")


s_pos = 0
p_pos = 0
big_1_1 = []
big_1_2 = []
big_2_1 = []
big_2_2 = []
small_1_1 = []
small_1_2 = []
small_2_1 = []
small_2_2 = []

b = 0
a = []
average_a = 0
ua_a = 0
ub_a = 0
u_a = 0
ua_b = 0
ub_b = 0
u_b = 0
f = 0
u_f = 0

S_POS = ""
P_POS = ""
BIG11 = []
BIG12 = []
BIG21 = []
BIG22 = []
SMALL11 = []
SMALL12 = []
SMALL21 = []
SMALL22 = []
B = ""
A = []
AVERAGE_A = ""
UA_A = ""
U_A = ""
answer = []


def handler(sublab_root):
    xmlReader(sublab_root)
    niconiconi()
    regulation()
    # file_object = open(texdir + "/Handle1060312.tex", "r")
    # latex = file_object.read().decode('utf-8', 'ignore')
    # return lexFiller(latex)


def xmlReader(sublab_root):
    global p_pos, s_pos, big_1_1, big_1_2, big_2_1, big_2_2, small_1_1, small_2_1, small_1_2, small_2_2
    table_list = sublab_root.getElementsByTagName("table")
    table1 = table_list[0]
    table2 = table_list[1]
    row1 = (table1.getElementsByTagName("tr"))[0]
    row1_elements = row1.getElementsByTagName("td")
    s_pos = float(row1_elements[0].firstChild.nodeValue)
    p_pos = float(row1_elements[1].firstChild.nodeValue)
    row_list = table2.getElementsByTagName("tr")
    row1 = row_list[0]
    row1_tds = row1.getElementsByTagName("td")
    for td in row1_tds:
        big_1_1.append(float(td.firstChild.nodeValue))
    row2 = row_list[1]
    row2_tds = row2.getElementsByTagName("td")
    for td in row2_tds:
        big_1_2.append(float(td.firstChild.nodeValue))
    row3 = row_list[2]
    row3_tds = row3.getElementsByTagName("td")
    for td in row3_tds:
        small_1_1.append(float(td.firstChild.nodeValue))
    row4 = row_list[3]
    row4_tds = row4.getElementsByTagName("td")
    for td in row4_tds:
        small_1_2.append(float(td.firstChild.nodeValue))
    row5 = row_list[4]
    row5_tds = row5.getElementsByTagName("td")
    for td in row5_tds:
        big_2_1.append(float(td.firstChild.nodeValue))
    row6 = row_list[5]
    row6_tds = row6.getElementsByTagName("td")
    for td in row6_tds:
        big_2_2.append(float(td.firstChild.nodeValue))
    row7 = row_list[6]
    row7_tds = row7.getElementsByTagName("td")
    for td in row7_tds:
        small_2_1.append(float(td.firstChild.nodeValue))
    row8 = row_list[7]
    row8_tds = row8.getElementsByTagName("td")
    for td in row8_tds:
        small_2_2.append(float(td.firstChild.nodeValue))


def niconiconi():
    global p_pos, s_pos, big_1_1, big_1_2, big_2_1, big_2_2, small_1_1, small_2_1, small_1_2, small_2_2, \
        b, a, average_a, f, ua_a, ua_b, ub_a, ub_b, u_f, u_a, u_b
    size = len(big_1_1)
    sum_a = 0
    for i in range(size):
        a.append(abs(small_1_1[i] + small_1_2[i] + small_2_1[i] + small_2_2[i] - big_1_1[i] - big_1_2[i] - big_2_1[i] \
                     - big_2_2[i]) / 4)
        sum_a += a[i]
    if size > 0:
        average_a = sum_a / size
    else:
        print "no data!"
    b = abs(p_pos - s_pos)
    f = (pow(b, 2) - pow(average_a, 2))/(4*b)
    ua_a = Ua(a, average_a, size)
    ub_a = 0.5774
    u_a = sqrt(ua_a*ua_a+ub_a*ub_a)
    ua_b = 0
    ub_b = 0.5774
    u_b = sqrt(ua_b*ua_b+ub_b*ub_b)
    u_f = sqrt(pow(((pow(b, 2) + pow(average_a, 2))/(4*pow(b, 2))*u_a), 2)+pow((average_a/b/2*u_b), 2))


def regulation():
    global S_POS, P_POS, BIG11, BIG12, BIG21, BIG22, SMALL11, SMALL12, SMALL21, SMALL22, B, AVERAGE_A, UA_A, U_A,\
        p_pos, s_pos, big_1_1, big_1_2, big_2_1, big_2_2, small_1_1, small_2_1, small_1_2, small_2_2, \
        b, a, average_a, f, ua_a, ua_b, ub_a, ub_b, u_f, u_a, u_b
    P_POS = ToScience(p_pos)
    S_POS = ToScience(s_pos)
    for d in big_1_1:
        BIG11.append(ToScience(d))
    for d in big_1_2:
        BIG12.append(ToScience(d))
    for d in big_2_1:
        BIG21.append(ToScience(d))
    for d in big_2_2:
        BIG22.append(ToScience(d))
    for d in small_1_1:
        SMALL11.append(ToScience(d))
    for d in small_1_2:
        SMALL12.append(ToScience(d))
    for d in small_2_1:
        SMALL21.append(ToScience(d))
    for d in small_2_2:
        SMALL22.append(ToScience(d))
    for d in a:
        A.append(ToScience(d))
    B = ToScience(b)
    AVERAGE_A = ToScience(average_a)
    UA_A = ToScience(ua_a)
    U_A = ToScience(u_a)
    bitAdapt(f, u_f, 2, -3)


def lexFiller(source):
    complete_file = env.from_string(source).render(
        S_POS=S_POS,
        P_POS=P_POS,
        BIG11=BIG11,
        BIG12=BIG12,
        BIG21=BIG21,
        BIG22=BIG22,
        SMALL11=SMALL12,
        SMALL21=SMALL22,
        SMALL12=SMALL12,
        SMALL22=SMALL22,
        UA_A=UA_A,
        U_A=U_A,
        F=answer[0],
        UF=answer[1],
    )
    return complete_file


# 规约最终结果，进行有效位数限定
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



if __name__ == '__main__':
    dom = xml.dom.minidom.parse(scriptdir + 'test/1060312test/1060312.xml')
    root = dom.documentElement
    sublab_list = root.getElementsByTagName('sublab')
    for sublab in sublab_list:
        sublab_status = sublab.getAttribute("status")
        sublab_id = sublab.getAttribute("id")
        if (sublab_status == 'true') & (sublab_id == '10613'):
            handler(sublab)
    print(big_1_1)
    print(f)
    print(u_f)
    print(answer)