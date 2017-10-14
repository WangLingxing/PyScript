#!/usr/bin/python3

def printTable(tableDate):
    #当前列的长度存在colwiths中
    colWiths = [0] * len(tableDate)
    for i in range(len(tableDate)):
        maxLen = 0
        for j in range(len(tableDate[i])):
            if len(tableDate[i][j]) > maxLen:
                maxLen = len(tableDate[i][j])
            colWiths[i] = maxLen

    #跟据colwiths中的最长长度作为rjust右对齐的长度
    for j in range(len(tableDate[0])):
        for i in range(len(tableDate)):
            print(tableDate[i][j].rjust(colWiths[i]),end = ' ')
        print()


if __name__ == '__main__':
    tableDate = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]

    printTable(tableDate)



