# coding: utf8
# 分析视频文件观看次数的概率分布特征
import numpy as np;
import matplotlib.pyplot as plt;
import myplot;

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

# 计算累积值
for i in reversed(range(0,np.power(10, powerRank) - 1)):
    viewTimes[i] = viewTimes[i] + viewTimes[i+1];

x = range(0,np.power(10, powerRank));

y = viewTimes;

# 画图
myplot.plot(x, y, label='count', xlabel='Views', ylabel='Number of views with >= x views', xAxieIsLog=True, yAxieIsLog=True);
