def generateMatrix():
    data = open("data.csv", "r")
    return [row.split('\t') for row in data.read().split('\n')][:-1]