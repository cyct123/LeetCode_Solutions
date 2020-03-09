#Access Log 处理
#Description
#
#C 公司对一个即将上线的业务进行了测试，为了更好的评估该业务测试期间的运行状态，C 公司的 Alice 同学打算写一个工具来对该业务的 Access Log 进行处理，她希望能通过这个工具知道任意一个时间段内 (闭区间，精确到秒) 该业务有多少次访问。
#
#为了方便处理，机智的 Alice 同学写了个脚本将 Access Log 简化为了每条日志只有一个时间戳数据，即简化后的 Access Log 是一个 N 行的文本，每行是一个整数时间戳，代表该时刻有一次访问，如下图所示:
#
#1564900123
#1564934135
#1564934132
#1564934666
#1564931024
#但是 Alice 同学太忙了，所以需要请你帮她实现这个问题。
#
#
#Input
#第 1 行输入 1 个整数 TT (1 \le T \le 101≤T≤10)，表示一共有 TT 组数据；
#
#对于每一组数据:
#
#第 1 行输入 1 个整数 NN (1 \le N \le 100000001≤N≤10000000)，表示有 Access Log 有 NN 条数据；
#接下来 NN 行，每行输入一个整数 tt (0 \le t0≤t，且整数 t 不会超过uint64_t范围)，表示 Access Log 中的一条数据；
#接下来 1 行输入 1 个整数 M (1 \le M \le 10000001≤M≤1000000)，表示有 MM 次查询；
#接下来 MM 行，每行两个整数 bb，ee，表示查询 [b, e][b,e] 时间段内的访问次数 (0 \le b \le e)， 并且0≤b≤e)，并且b,,e$ 不会超过uint64_t范围)。
#注意： Access Log 中的时间戳并不能保证是有序的。
#
#
#Output
#
#对于每次询问输出一行，在该行输出一个整数 R，表示对应区间的访问次数。


def readInt():
    return int(input().strip())

def getTimeStamps(n):
    timestamps = []
    for _ in range(n):
        timestamps.append(readInt())
    timestamps.sort()
    return timestamps

def getTimeRanges(m):
    timeRanges = []
    for _ in range(m):
        timeRange = tuple(map(int, input().strip().split()))
        timeRanges.append(timeRange)
    return timeRanges

def getCounts():
    n = readInt()
    timeStamps = getTimeStamps(n)
    m = readInt()
    timeRanges = getTimeRanges(m)
    counter = [0] * m
    for i in range(len(timeRanges)):
        start, end = timeRanges[i]
        startIdx, startIsExist = getIndex(start, timeStamps)
        endIdx, endIsExist = getIndex(end, timeStamps)
        if startIsExist or endIsExist:
            counter[i] = endIdx - startIdx + 1
    return counter

def getIndex(num, nums):
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = low + int((high - low) / 2)
        if nums[mid] == num:
            return mid, 1
        elif nums[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
    return low, 0

def handleAccessLog():
    t = readInt()
    for _ in range(t):
        counter = getCounts()
        for c in counter:
            print(c)


if __name__ == "__main__":
    handleAccessLog()
