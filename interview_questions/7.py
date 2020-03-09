#monster 要喝水
#Description
#
#公司终于安好饮水机了，monster 迫不及待要去接水，但是他到那里才发现前面已经有n个同事了。他数了数，饮水机一共有m个接水口。所有的同事严格按照先来后到去接水（m个接水口同时工作，哪个水龙头有空人们就去哪里，如果 n \lt mn<m，那么就只有n个接水口工作）。每个人都有一个接水的时间，当一个人接完水后，另一个人马上去接，不会浪费时间。monster 着急要开会，所以他想知道什么时候才能轮到他。
#
#
#Input
#第一行两个整数n和m，表示 monster 前面有n个人，饮水机有m个接水口。n, m \lt 1100n,m<1100。第二行n个整数，表示每个同学的接水时间。
#
#
#Output
#一行，一个数，表示轮到 monster 接水的时间


def drinkWater(n, m, nums):
    time = 0
    if m == 1:
        time = sum(nums)
    else:
    	for i in range(m, n):
            idx = 0
            for j in range(1, m):
                if nums[j] < nums[idx]:
                    idx = j
            nums[idx] += nums[i]
            for k in range(m):
                time = time if time > nums[k] else nums[k]
    return time


if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    nums = list(map(int, input().strip().split()))
    print(drinkWater(n, m, nums))
