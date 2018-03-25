# coding: utf8
import numpy as np;
import matplotlib.pyplot as plt;

def plot(x, y, label='', linewidth=1, xlabel='', ylabel='', xAxieIsLog=False, yAxieIsLog=False, powerRank=8):
    # 画图
    print("plotting...");

    if xAxieIsLog:
        for i in range(0, len(x)):
            if x[i] > 0:
                x[i] = np.log10(x[i]);

    if yAxieIsLog:
        for i in range(0, len(y)):
            if y[i] > 0:
                y[i] = np.log10(y[i]);

    plt.figure(figsize=(8, 5));
    plt.plot(x, y, label=label, linewidth=linewidth);
    plt.xlabel(xlabel);
    plt.ylabel(ylabel);
    plt.legend();
    plt.show();
    return;