# -*- coding:utf-8 -*-
# 1070212测量三棱镜顶角
'''
input:
    angle_a1 = []
    angle_a2 = []
    angle_b1 = []
    angle_b2 = []
output:
    N
    ANGLE_A 二元组{'angle','minus'}的集合
    ANGLE_THETA 二元组{'angle','minus'}的集合
    ANGLE_A1 二元组{'angle','minus'}的集合
    ANGLE_A2 二元组{'angle','minus'}的集合
    ANGLE_B1 二元组{'angle','minus'}的集合
    ANGLE_B2 二元组{'angle','minus'}的集合
    AVERAGE_A 二元组{'angle','minus'}的集合
    UA_A 字符串
    U_A 字符串
    RE_U 字符串
    RESULT_A 字符串
    RESULT_UA 字符串
'''
import xml.dom.minidom
from math import sqrt
from jinja2 import Environment
from handler import texdir
from handler import scriptdir
# 原始数据
n = 0
angle_a1 = []
angle_a2 = []
angle_b1 = []
angle_b2 = []
# 数据处理得到的数据
angle_theta = []
angle_A = []
average_angle_A = 0
ua_A = 0
ub_A = 0
re_u = 0
answer = []  # 三元组，经过位数处理的(期望真值，误差， 幂次)
# 输出数据
N = 0
ANGLE_A = []
ANGLE_THETA = []
ANGLE_A1 = []
ANGLE_A2 = []
ANGLE_B1 = []
ANGLE_B2 = []
AVERAGE_A = ""
UA_A = ""
U_A = ""
RE_U = ""
RESULT_A = ""
RESULT_UA = ""

# 定义模板
env = Environment(line_statement_prefix="#", variable_start_string="%%", variable_end_string="%%")


# 入口函数
def handler(xml):
    global n, angle_theta, angle_A, average_angle_A, ua_A, ub_A, u_A, re_u
    readXML(xml)
    sumA = 0
    # 数据处理
    n = len(angle_a1)
    for i in range(n):
        angle_theta.append((((angle_a2[i] - angle_a1[i]) + (angle_b2[i] - angle_b1[i])) % 360) / 2)
        angle_A.append(angle_theta[i] / 2)
        sumA += angle_A[i]
    print angle_A
    average_angle_A = sumA / n
    ua_A = Ua(angle_A, average_angle_A, n)
    ub_A = 0.009622
    u_A = sqrt(ua_A ** 2 + ub_A ** 2)
    re_u = u_A / average_angle_A
    bitAdapt(average_angle_A, u_A, 1, -3)
    # 数据规范化
    regulation()
    # 数据填入模板
    file_object = open(texdir + "/Handle1070212.tex", "r")
    latexAddress = file_object.read().decode('utf-8', 'ignore')
    latex_body = LatexFiller(latexAddress)
    return latex_body


# 将计算得到的结果，转化成符合格式要求的字符串
def regulation():
    global n, angle_theta, angle_A, average_angle_A, ua_A, ub_A, u_A, re_u, N, ANGLE_A, ANGLE_A1, ANGLE_A2, ANGLE_B1, \
        ANGLE_B2, ANGLE_THETA, UA_A, U_A, RE_U, RESULT_A, RESULT_UA, AVERAGE_A
    for a1 in angle_a1:
        ANGLE_A1.append({'angle': str(int(a1)), 'minus': str(int((a1 - int(a1)) * 60 + 0.1))})
    for a2 in angle_a2:
        ANGLE_A2.append({'angle': str(int(a2)), 'minus': str(int((a2 - int(a2)) * 60 + 0.1))})
    for b1 in angle_b1:
        ANGLE_B1.append({'angle': str(int(b1)), 'minus': str(int((b1 - int(b1)) * 60 + 0.1))})
    for b2 in angle_b2:
        ANGLE_B2.append({'angle': str(int(b2)), 'minus': str(int((b2 - int(b2)) * 60 + 0.1))})
    for a in angle_A:
        ANGLE_A.append({'angle': str(int(a)), 'minus': str(int((a - int(a)) * 60 + 0.1))})
    for theta in angle_theta:
        ANGLE_THETA.append({'angle': str(int(theta)), 'minus': str(int((theta - int(theta)) * 60 + 0.1))})
    N = n
    AVERAGE_A = toScience(average_angle_A)
    UA_A = toScience(ua_A)
    U_A = toScience(u_A)
    RE_U = toScience(re_u)
    RESULT_A = answer[0]
    RESULT_UA = answer[1]


# xml文件的解析
def readXML(sublab_root):
    global angle_a1, angle_a2, angle_b1, angle_b2
    sublab_table_list = sublab_root.getElementsByTagName("table")
    for table in sublab_table_list:
        # table_name = table.getAttribute("name")
        table_tr_list = table.getElementsByTagName("tr")
        for tr in table_tr_list:
            # tr_index = tr.getAttribute("index")
            # index = int(tr_index)
            tr_td_list = tr.getElementsByTagName("td")
            angle_a1.append(angleTransfer(float(tr_td_list[0].firstChild.nodeValue)))
            angle_a2.append(angleTransfer(float(tr_td_list[1].firstChild.nodeValue)))
            angle_b1.append(angleTransfer(float(tr_td_list[2].firstChild.nodeValue)))
            angle_b2.append(angleTransfer(float(tr_td_list[3].firstChild.nodeValue)))


# 将得到的结果填入模板
def LatexFiller(latex_address):
    result = env.from_string(latex_address).render(
        N=N,
        ANGLE_A=ANGLE_A,
        ANGLE_THETA=ANGLE_THETA,
        ANGLE_A1_VERT=ANGLE_A1,
        ANGLE_A2_VERT=ANGLE_A2,
        ANGLE_B1_VERT=ANGLE_B1,
        ANGLE_B2_VERT=ANGLE_B2,
        AVERAGE_A=AVERAGE_A,
        UA_A=UA_A,
        U_A=U_A,
        RE_U=RE_U,
        RESULT_A=RESULT_A,
        RESULT_UA=RESULT_UA
    )
    return result


# a类不确定度计算
def Ua(x, aver, k):
    sumx = 0
    for i in range(k):
        sumx += (x[i] - aver) ** 2
    return sqrt(sumx / (k * (k - 1)))


# 将‘度.分’表示的角度转化成角度表示
def angleTransfer(raw):
    return int(raw) + (raw - int(raw)) * 100 / 60


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


def toScience(number):
    tempstr = format(number, '.5g')
    if 'e' in tempstr:
        index_str = tempstr.split('e')
        return index_str[0] + '{\\times}10^{' + str(int(index_str[1])) + '}'
    else:
        return tempstr


if __name__ == '__main__':


    def ReadXmlTop():
        latex_head_file = open(texdir+'Head.tex', 'r')
        latex_head = latex_head_file.read().decode('utf-8', 'ignore')
        latex_tail = "\n\\end{document}"
        latex_body = ""
        dom = xml.dom.minidom.parse(scriptdir+'test/1070212test/1071.xml')
        root = dom.documentElement
        sublab_list = root.getElementsByTagName('sublab')
        for sublab in sublab_list:
            sublab_status = sublab.getAttribute("status")
            sublab_id = sublab.getAttribute("id")
            if (sublab_status == 'true') & (sublab_id == '10711'):
                latex_body += handler(sublab)
        return latex_head + latex_body + latex_tail
    fileTex = open(scriptdir+'test/1070212test/1070212test.tex', 'w')
    text = ReadXmlTop().encode('utf-8')
    fileTex.write(text)
    fileTex.close()
    print u_A, U_A

