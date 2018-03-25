# coding: utf8
# 分析视频文件时长的概率分布特征
import myplot;
import numpy as np;
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

        dataProcessed['views'] = line[2];
        dataProcessed['ratings'] = line[3];
        dataProcessed['stars'] = line[4].replace('\n','');
        dataset.append(dataProcessed);
print(dataset[0]);

# 提取特征属性views
viewTimes = np.zeros(np.power(10, powerRank));
index = 0;
for line in dataset:
    lengthOfInt = line['length'];

    # 减少噪点
    if lengthOfInt >= np.power(10, powerRank) - 1:
        continue;

    viewTimes[lengthOfInt] += int(line['views']);
    if index % (len(dataset) / 10) == 0:
        print("running... " + str(index / (len(dataset) / 10)) + "0%");
    index += 1;

#使用累积值
for i in reversed(range(0,np.power(10, powerRank) - 1)):
    viewTimes[i] = viewTimes[i] + viewTimes[i+1];

x = range(0, np.power(10, powerRank));

y = viewTimes;
myplot.plot(x, y, label='count', xlabel='Length', ylabel='Views', xAxieIsLog=True, yAxieIsLog=False, powerRank=powerRank);

