# coding: utf8
# 分析视频文件时长的概率分布特征
import myplot;
import numpy as np;
from scipy import stats as ss
# 数据数量级
powerRank = 2;
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
        dataProcessed['stars'] = int(float(line[4].replace('\n', '')) * 10);
        dataset.append(dataProcessed);
print(dataset[0]);

# 提取特征属性views
viewTimes = [];
index = 0;
for line in dataset:
    views = line['views'];

    # 减少噪点
    # if lengthOfInt >= np.power(10, powerRank) - 1:
    #     continue;

    viewTimes.append(int(line['views']));
    if index % (len(dataset) / 10) == 0:
        print("running... " + str(index / (len(dataset) / 10)) + "0%");
    index += 1;

viewTimes.sort();
viewTimes.reverse();
#使用累积值
# for i in reversed(range(0,np.power(10, powerRank) - 1)):
#     viewTimes[i] = viewTimes[i] + viewTimes[i+1];

x = range(0, len(viewTimes));

y = viewTimes;
myplot.plot(x, y, label='count', xlabel='Rank', ylabel='Views', xAxieIsLog=True, yAxieIsLog=True);


