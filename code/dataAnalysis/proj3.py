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
countOfLength = np.zeros(np.power(10, powerRank));
index = 0;
for line in dataset:
    lengthOfInt = line['length'];

    # 减少噪点
    if lengthOfInt >= np.power(10, powerRank) - 1:
        continue;

    countOfLength[lengthOfInt] += 1;
    viewTimes[lengthOfInt] += int(line['views']);
    if index % (len(dataset) / 10) == 0:
        print("running... " + str(index / (len(dataset) / 10)) + "0%");
    index += 1;

y = list(viewTimes);


#使用累积值
sumy = list(viewTimes);
myplot.normalize(sumy)
for i in range(1, np.power(10, powerRank)):
    sumy[i] = sumy[i] + sumy[i-1];

# 取平均值
avrgY = list(viewTimes);
for i in range(0, np.power(10, powerRank)):
    if(not(countOfLength[i] == 0)):
        avrgY[i] /= countOfLength[i];

# 使用累积平均值
avrg_sumY = list(avrgY);
myplot.normalize(avrg_sumY)
for i in range(1, np.power(10, powerRank)):
    avrg_sumY[i] = avrg_sumY[i] + avrg_sumY[i - 1];

x = range(0, np.power(10, powerRank));


#fig3_1
# myplot.bar(x, y, label='', xlabel='Length', ylabel='Views', xAxieIsLog=True, yAxieIsLog=False, powerRank=powerRank, deleteZero=True);

#fig3_2
# myplot.plot(x, sumy, label='', xlabel='Length', ylabel='Aggregation of views rate', xAxieIsLog=True, yAxieIsLog=False, powerRank=powerRank, deleteZero=False);

#fig3_3
# myplot.plot(x, avrgY, label='count', xlabel='Length', ylabel='Average views', xAxieIsLog=True, yAxieIsLog=False, powerRank=powerRank, deleteZero=True);

#fig3_4
myplot.plot(x, avrg_sumY, label='count', xlabel='Length', ylabel='Aggregation of average views rate', xAxieIsLog=True, yAxieIsLog=False, powerRank=powerRank, deleteZero=True);


