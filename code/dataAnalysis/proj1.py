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
    viewTimes[views] += 1;
    if index % (len(dataset)/10) == 0:
        print("running... " + str(index / (len(dataset)/10)) + "0%");
    index += 1;

# 计算累积值
# for i in reversed(range(0,np.power(10, powerRank)-1 )):
#     viewTimes[i] = viewTimes[i] + viewTimes[i+1];
# for i in range(1, np.power(10, powerRank)):
#     viewTimes[i] = viewTimes[i] + viewTimes[i-1];

x = range(0,np.power(10, powerRank));

y = viewTimes;

z = range(0,np.power(10, powerRank));

for i in x:
    z[i] = y[i] * i;

# 计算累积值
for i in range(1, np.power(10, powerRank)):
    z[i] = z[i] + z[i-1];

# 去掉 y = 0 的点,加快绘图速度
xx = [];
yy = [];
for i in x:
    if y[i] != 0:
        xx.append(x[i]);
        yy.append(y[i]);

print("data size: " + len(xx).__str__())
# 画图

#fig1_1
myplot.plot(xx, yy, label='', xlabel='Views', ylabel='Number of videos', xAxieIsLog=True, yAxieIsLog=False);

#fig1_2
# myplot.plot(x, y, label='', xlabel='Views', ylabel='Aggregation of views where views <= x', xAxieIsLog=True, yAxieIsLog=False);

# myplot.scatter(x, z, label='count', xlabel='Views', ylabel='Number of video', xAxieIsLog=True, yAxieIsLog=False);