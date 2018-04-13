# coding: utf8
import numpy as np;
import matplotlib.pyplot as plt;

#画折线图
def plot(x, y, label='', linewidth=1, xlabel='', ylabel='', xAxieIsLog=False, yAxieIsLog=False, deleteZero=False, powerRank=8):
    # 画图
    print("plotting...");

    print("\tdelete zero...")
    # 去掉 y = 0 的点,加快绘图速度
    if deleteZero:
        xx = [];
        yy = [];
        for i in x:
            if not(y[i] == 0):
                xx.append(x[i]);
                yy.append(y[i]);
        x = xx;
        y = yy;

    print("\tdata size is %d" % (len(x)))

    # plt.figure(figsize=(8, 5));
    plt.plot(x, y, label=label, linewidth=linewidth);

    process(xlabel, ylabel, xAxieIsLog, yAxieIsLog)

    return;

# 画散点图
def scatter(x, y, label='', linewidth=1, xlabel='', ylabel='', xAxieIsLog=False, yAxieIsLog=False, powerRank=8):
    # 画图
    print("plotting...");

    # plt.figure(figsize=(8, 5));
    plt.scatter(x, y, c='r', marker='+', alpha=0.5)
    process(xlabel, ylabel,xAxieIsLog, yAxieIsLog)
    return;

def bar(x, y, label='', linewidth=1, xlabel='', ylabel='', xAxieIsLog=False, yAxieIsLog=False, deleteZero=False, powerRank=8):
    print("\tdelete zero...")
    # 去掉 y = 0 的点,加快绘图速度
    if deleteZero:
        xx = [];
        yy = [];
        for i in x:
            if not(y[i] == 0):
                xx.append(x[i]);
                yy.append(y[i]);
        x = xx;
        y = yy;
    plt.bar(x, y, alpha=1, width=linewidth, facecolor='b', edgecolor='b', label=label,lw=0)
    process(xlabel, ylabel, xAxieIsLog, yAxieIsLog)

# 图像统一处理
def process(xlabel, ylabel, xAxieIsLog, yAxieIsLog):
    plt.xlabel(xlabel);
    plt.ylabel(ylabel);

    plt.xlim(xmin=0)
    plt.ylim(ymin=0)

    if xAxieIsLog:
        plt.xscale('log')
        plt.xlim(xmin=1)
        # for i in range(0, len(x)):
        #     if x[i] > 0:
        #         x[i] = np.log10(x[i]);

    if yAxieIsLog:
        plt.yscale('log')
        plt.ylim(ymin=1)
        # for i in range(0, len(y)):
        #     if y[i] > 0:
        #         y[i] = np.log10(y[i]);

    # plt.grid();
    plt.legend();
    plt.show();

#定义归一化方法
def normalize(y):
    sumy = 0;
    for i in range(0, len(y)):
        sumy += y[i];
    for i in range(0, len(y)):
        y[i] = float(y[i]) / sumy;
    return;




