import numpy as np
import csv
import datetime
import pandas as pd
import os

def removeEmptyRows(fname):
    df = pd.read_csv(fname)
    df.to_csv("dummy_" + fname, index=False)
    os.remove(fname)
    os.rename("dummy_" + fname, fname)

def exportData(fname, data, dname):
    date = datetime.datetime.now()
    fname = fname + '_{:%Y-%m-%d_%H-%M-%S}.csv'.format(date)

    with open(fname, 'w') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(dname)
        n = np.size(data, 0)
        sizes = np.zeros(n)
        for i in range(0, n):
            sizes[i] = np.size(data[i])
            maxsize = int(np.max(sizes))
        mat = np.zeros([n, maxsize])
        for i in range(0, n):
                for j in range(0, int(sizes[i])):
                    mat[i, j] = 1

        for i in range(0, maxsize):
            row = []
            for j in range(0, n):
                if (mat[j, i] == 1):
                    row.extend([data[j][i]])

                else:
                    row.extend("")
            csv_writer.writerow(row)
    removeEmptyRows(fname)
    return fname