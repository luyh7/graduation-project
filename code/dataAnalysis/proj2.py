# coding: utf8
# 分析视频文件时长的概率分布特征
import numpy as np;
import matplotlib.pyplot as plt;

# 数据数量级
powerRank = 7;
# 数据预处理
dataset = [];
with open('dataset.txt', 'r') as f:
    for line in f.readlines():
        line = line.split('|');
        dataProcessed = {};
        dataProcessed['url'] = line[0];

        # 将时长字符串转换为整型，单位为秒
        lengthOfInt = 0;
        for l in line[1].split(':'):
            lengthOfInt *= 60;
            lengthOfInt += int(l);
        dataProcessed['length'] = lengthOfInt;

        dataProcessed['views'] = int(line[2]);
        dataProcessed['ratings'] = int(line[3]);
        dataProcessed['stars'] = int(float(line[4].replace('\n','')) * 10);
        dataset.append(dataProcessed);
print(dataset[0]);


# 提取特征属性length
countForLength = np.zeros(np.power(10, powerRank));
index = 0;
for line in dataset:
    lengthOfInt = line['length'];
    if lengthOfInt >= np.power(10, powerRank) - 1:
        continue;

    # print(str(lengthOfInt) + ',' + length)
    countForLength[lengthOfInt] += line['views'];
    if index % (len(dataset)/10) == 0:
        print("running... " + str(index / (len(dataset)/10)) + "0%");
    index += 1;

x = range(0, np.power(10, powerRank));
for i in range(0, np.power(10, powerRank)):
    if x[i] > 0:
        x[i] = np.log10(x[i]);

y = countForLength;
# for i in range(0,np.power(10, powerRank)):
#     if y[i] > 0:
#         y[i] = np.log10(y[i]);

# 画图
print("plotting...");
plt.figure(figsize=(8,5));
plt.plot(x, y, label='count', linewidth=1);
plt.xlabel('Length');
plt.ylabel('Views');
plt.legend();
plt.show();