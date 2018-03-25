# coding: utf8
# 分析视频文件观看次数的概率分布特征
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
        dataProcessed['length'] = line[1];
        dataProcessed['views'] = line[2];
        dataProcessed['ratings'] = line[3];
        dataProcessed['stars'] = line[4].replace('\n','');
        dataset.append(dataProcessed);
print(dataset[0]);

# 提取特征属性views
viewTimes = np.zeros(np.power(10, powerRank));
index = 0;
for line in dataset:
    views = int(line['views']);
    viewTimes[views/10] += 1;
    if index % (len(dataset)/10) == 0:
        print("running... " + str(index / (len(dataset)/10)) + "0%");
    index += 1;

for i in reversed(range(0,np.power(10, powerRank) - 1)):
    viewTimes[i] = viewTimes[i] + viewTimes[i+1];

x = range(0,np.power(10, powerRank));
for i in range(0,np.power(10, powerRank)):
    if x[i] > 0:
        x[i] = np.log10(x[i]);

y = viewTimes;
for i in range(0,np.power(10, powerRank)):
    if y[i] > 0:
        y[i] = np.log10(y[i]);

# 画图
print("plotting...");
plt.figure(figsize=(8,5));
plt.plot(x, y, label='count', linewidth=1);
plt.xlabel('Views');
plt.ylabel('Number of views with >= x views');
plt.legend();
plt.show();