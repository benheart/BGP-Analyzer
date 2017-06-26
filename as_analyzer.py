# coding=utf-8
# !/usr/bin/python

# 变量声明
as_ip_num = {}
as_prefix_num = {}
prefix = {}
as_node = {}
as_sum = 0
prefix_sum = 0

as_file = open("as.txt")  # 打开测试文件test.txt
out = open("result.txt", "wb")  # 将统计结果保存在result.txt

for line in as_file:
    as_data = line.split('|')
    as_path = as_data[6].split(' ')  # as_data[6]表示路径，每个节点存在as_path中

    i = 0
    while i < len(as_path) & len(as_path) != 1:
        if int(as_path[i]) in as_ip_num.keys():  # as存在,数目不变
            if i < len(as_path) - 1:
                if int(as_path[i]) != int(as_path[i + 1]):
                    # 采用字典的嵌套来统计as的节点度
                    as_node.setdefault(int(as_path[i]), {})
                    as_node[int(as_path[i])].setdefault(int(as_path[i + 1]), 0)
                    as_node.setdefault(int(as_path[i + 1]), {})
                    as_node[int(as_path[i + 1])].setdefault(int(as_path[i]), 0)
            i += 1
        else:
            as_sum += 1  # as不存在，数目加一
            # print (as_Sum)

            as_ip_num.setdefault(int(as_path[i]), 0)
            as_prefix_num.setdefault(int(as_path[i]), 0)
            if i < len(as_path) - 1:
                if int(as_path[i]) != int(as_path[i + 1]):
                    # 采用字典的嵌套来统计as的节点度
                    as_node.setdefault(int(as_path[i]), {})
                    as_node[int(as_path[i])].setdefault(int(as_path[i + 1]), 0)
                    as_node.setdefault(int(as_path[i + 1]), {})
                    as_node[int(as_path[i + 1])].setdefault(int(as_path[i]), 0)
            i += 1

    if as_data[5] not in prefix.keys():  # 前缀不存在,as_data[5]表示前缀
        prefix_sum += 1
        prefix.setdefault(as_data[5], as_path[len(as_path) - 1])  # 添加到前缀字典，{前缀->自治域}
        temp = as_data[5].split('/')
        as_ip_num[int(as_path[len(as_path) - 1])] += pow(2, (32 - int(temp[1])))
        as_prefix_num[int(as_path[len(as_path) - 1])] += 1

as_file.close()

# 每个as对应的ip前缀数目、ip数目、节点度进行排序
as_ip_num = sorted(as_ip_num.items(), key=lambda d: d[0], reverse=False)
as_prefix_num = sorted(as_prefix_num.items(), key=lambda d: d[0], reverse=False)
as_node = sorted(as_node.items(), key=lambda d: d[0], reverse=False)

# 将结果保存在result.txt中
for index in range(len(as_ip_num)):
    out.write((str(as_ip_num[index][0]) + '|' + str(as_ip_num[index][1]) + '|' + str(
        as_prefix_num[index][1]) + '|' + str(len(as_node[index][1])) + '|' + '\r\n').encode())
out.close()

# 打印as数目、前缀总数目
print ('as_sum: ', as_sum)
print ('prefix_sum: ', prefix_sum)
