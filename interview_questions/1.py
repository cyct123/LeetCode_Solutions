import time
import sys

def readInt(f):
    return int(f.readline().strip())

def getTimeStamps(f, n):
    timestamps = []
    for _ in range(n):
        timestamps.append(readInt(f))
    return timestamps

def getTimeRanges(f, m):
    timeRanges = []
    for _ in range(m):
        timeRange = tuple(map(int, f.readline().strip().split()))
        timeRanges.append(timeRange)
    return timeRanges

def getCounts(f):
    n = readInt(f)
    timeStamps = getTimeStamps(f, n)
    m = readInt(f)
    timeRanges = getTimeRanges(f, m)
    counter = [0] * m
    for i in range(n):
        timeStamp = timeStamps[i]
        for j in range(m):
            start, end = timeRanges[j]
            if start <= timeStamp <= end:
                counter[j] += 1
    return counter

def handleAccessLog(f):
    t = readInt(f)
    for _ in range(t):
        counter = getCounts(f)
        for c in counter:
            print(c)


if __name__ == "__main__":
    f = sys.stdin
    handleAccessLog(f)
