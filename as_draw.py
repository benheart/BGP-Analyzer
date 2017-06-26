# coding=utf-8
# !/usr/bin/python
import matplotlib.pyplot as plt
import math

AS = []
ip_num = []
prefix_num = []
degree_num = []
x = []
y = []
x_y = {}

ip_dic = {}
prefix_dic = {}
degree_dic = {}

as_file = open("result.txt")
for line in as_file:
    as_data = line.split('|')
    AS.append(int(as_data[0]))
    ip_num.append(int(as_data[1]))
    prefix_num.append(int(as_data[2]))
    y.append(math.log(int(as_data[3]) + 1))
    degree_num.append(int(as_data[3]))
    x.append(math.log(int(as_data[2]) + 1))
    if int(math.log(int(as_data[2]) + 1) + 1) not in x_y:
        x_y.setdefault(int(math.log(int(as_data[2]) + 1) + 1), math.log(int(as_data[3]) + 1))
    else:
        x_y[int(math.log(int(as_data[2]) + 1) + 1)] += math.log(int(as_data[3]) + 1)

for ip in ip_num:
    if (ip not in ip_dic) and (ip != 0):
        ip_dic.setdefault(math.log(ip), math.log(ip_num.count(ip)))

for prefix in prefix_num:
    if (prefix not in prefix_dic) and (prefix != 0):
        prefix_dic.setdefault(math.log(prefix), math.log(prefix_num.count(prefix)))

for degree in degree_num:
    if (degree not in degree_dic) and (degree != 0):
        degree_dic.setdefault(math.log(degree), math.log(degree_num.count(degree)))

# IP数量分布图
plt.xlabel('log(ip_num)')
plt.ylabel('log(as_num)')
plt.plot(ip_dic.keys(), ip_dic.values(), 'o')
plt.show()

# IP前缀分布图
plt.xlabel('log(prefix_num)')
plt.ylabel('log(as_num)')
plt.plot(prefix_dic.keys(), prefix_dic.values(), 'o')
plt.show()

# 节点度分布图
plt.xlabel('log(degree_num)')
plt.ylabel('log(as_num)')
plt.plot(degree_dic.keys(), degree_dic.values(), 'o')
plt.show()

# 节点度与前缀的关系图
plt.xlabel('log(degree_num)')
plt.ylabel('log(prefix_num)')
plt.plot(x, y, 'o')
plt.show()

# 节点度与前缀的关系图
plt.xlabel('log(degree_num)')
plt.ylabel('log(prefix_num)')
plt.plot(x_y.keys(), x_y.values(), 'o')
plt.show()
