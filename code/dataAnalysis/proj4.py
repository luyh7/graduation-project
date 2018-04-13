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
        dataProcessed['ratings'] = int(line[3]);
        dataProcessed['stars'] = line[4].replace('\n','');
        dataset.append(dataProcessed);
print(dataset[0]);

# 提取特征属性views
viewTimes = np.zeros(np.power(10, powerRank));
countOfRatings = np.zeros(np.power(10, powerRank));

index = 0;
for line in dataset:
    ratings = line['ratings'];

    # 减少噪点
    # if lengthOfInt >= np.power(10, powerRank) - 1:
    #     continue;
    countOfRatings[ratings] += 1;
    viewTimes[ratings] += int(line['views']);
    if index % (len(dataset) / 10) == 0:
        print("running... " + str(index / (len(dataset) / 10)) + "0%");
    index += 1;

#使用累积值
sumy = list(viewTimes)
myplot.normalize(sumy)
for i in range(1, np.power(10, powerRank)):
    sumy[i] = sumy[i] + sumy[i-1];

# 取平均值
avrgY = list(viewTimes);
for i in range(0, np.power(10, powerRank)):
    if(not(countOfRatings[i] == 0)):
        avrgY[i] /= countOfRatings[i];

# 使用累积平均值
avrg_sumY = list(avrgY);
myplot.normalize(avrg_sumY)
for i in range(1, np.power(10, powerRank)):
    avrg_sumY[i] = avrg_sumY[i] + avrg_sumY[i - 1];

x = range(0, np.power(10, powerRank));

y = list(viewTimes);
print(y[0]);
print(y[1])

#fig4_1
# myplot.plot(x, y, label='', xlabel='Ratings', ylabel='Views', xAxieIsLog=True, yAxieIsLog=False, powerRank=powerRank);

#fig4_2
# myplot.plot(x, sumy, label='', xlabel='Ratings', ylabel='Aggregation of views with <= x ratings', xAxieIsLog=True, yAxieIsLog=False, powerRank=powerRank);


#fig4_3
# myplot.plot(x, avrgY, label='', xlabel='Ratings', ylabel='Average views', xAxieIsLog=True, yAxieIsLog=False, powerRank=powerRank);

#fig4_4
myplot.plot(x, avrg_sumY, label='', xlabel='Ratings', ylabel='Aggregation of average views', xAxieIsLog=True, yAxieIsLog=False, powerRank=powerRank);