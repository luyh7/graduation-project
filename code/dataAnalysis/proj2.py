# coding: utf8
# 分析视频文件时长的概率分布特征
import numpy as np;
import math;
import myplot;
import matplotlib.pyplot as plt;
from scipy import stats as ss;
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
lengthOfLog = [];
index = 0;
for line in dataset:
    lengthOfInt = line['length'];
    if lengthOfInt >= np.power(10, powerRank) - 1:
        continue;

    # print(str(lengthOfInt) + ',' + length)
    countForLength[lengthOfInt] += 1;
    if index % (len(dataset)/10) == 0:
        print("running... " + str(index / (len(dataset)/10)) + "0%");
    index += 1;

    if lengthOfInt == 0:
        lengthOfLog.append(0);
    else:
        lengthOfLog.append(np.log10(lengthOfInt));

x = range(0, np.power(10, powerRank));
for i in range(0, np.power(10, powerRank)):
    if x[i] > 0:
        x[i] = np.log10(x[i]);

#使用累积值
# for i in reversed(range(0,np.power(10, powerRank) - 1)):
#     countForLength[i] = countForLength[i] + countForLength[i+1];

y = countForLength;

#归一化
print('normalizing...')
myplot.normalize(y);

# for i in range(0,np.power(10, powerRank)):
#     if y[i] > 0:
#         y[i] = np.log10(y[i]);

print('fitting...')
# 重新取样以拟合
sampleX = range(0, powerRank * 100);
for i in range(0, powerRank * 100):
    sampleX[i] = sampleX[i] * 0.01;

# sampleY = []
# for i in sampleX:
#     sampleY.append(y[int(math.pow(10, i))]);

sampleY = lengthOfLog;

# 拟合
params = ss.norm.fit(sampleY);
norm = ss.norm.pdf(sampleX, loc=params[0], scale=params[1]);
print (params);
sum = 0;
for i in range(0, len(norm)):
    norm[i] /= 100;
    sum += norm[i];
print sum;

# 画图
# myplot.plot(x, y, label='count', xlabel='Length', ylabel='Views', xAxieIsLog=True, yAxieIsLog=False);
print("plotting...");
plt.figure(figsize=(8,5));
plt.plot(x, y, label='Source data', linewidth=1);
plt.plot(sampleX, norm, label='Normal distribution', linewidth=1, color='red');
# plt.plot(sampleX, sampleY, color='green', label='count', linewidth=1);
plt.xlabel('Length');
# plt.ylabel('Count for length >= x');
plt.ylabel('Count');
plt.legend();
plt.show();