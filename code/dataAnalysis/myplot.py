# coding: utf8
import numpy as np;
import matplotlib.pyplot as plt;

def plot(x, y, label='', linewidth=1, xlabel='', ylabel='', xAxieIsLog=False, yAxieIsLog=False, powerRank=8):
    # 画图
    print("plotting...");



    # plt.figure(figsize=(8, 5));
    plt.plot(x, y, label=label, linewidth=linewidth);
    plt.xlabel(xlabel);
    plt.ylabel(ylabel);

    if xAxieIsLog:
        plt.xscale('log')
        # for i in range(0, len(x)):
        #     if x[i] > 0:
        #         x[i] = np.log10(x[i]);

    if yAxieIsLog:
        plt.yscale('log')
        # for i in range(0, len(y)):
        #     if y[i] > 0:
        #         y[i] = np.log10(y[i]);

    plt.xlim(xmin=1)
    plt.ylim(ymin=1)
    # plt.grid();
    plt.legend();
    plt.show();
    return;

def scatter(x, y, label='', linewidth=1, xlabel='', ylabel='', xAxieIsLog=False, yAxieIsLog=False, powerRank=8):
    # 画图
    print("plotting...");



    # plt.figure(figsize=(8, 5));
    plt.scatter(x, y, c='r', marker='+', alpha=0.5)
    plt.xlabel(xlabel);
    plt.ylabel(ylabel);

    if xAxieIsLog:
        plt.xscale('log')
        # for i in range(0, len(x)):
        #     if x[i] > 0:
        #         x[i] = np.log10(x[i]);

    if yAxieIsLog:
        plt.yscale('log')
        # for i in range(0, len(y)):
        #     if y[i] > 0:
        #         y[i] = np.log10(y[i]);

    plt.xlim(xmin=1)
    plt.ylim(ymin=1)
    # plt.grid();
    plt.legend();
    plt.show();
    return;

# def (y):
#     sumy = 0;
#     for i in range(0, len(y)):
#         sumy += y[i];
#     for i in range(0, len(y)):
#         y[i] = float(y[i]) / sumy;
#     return;




