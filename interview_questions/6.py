#数组运算
#Description
#
#给你一个 nn 个数的数组 a_1 ,a_2, ..., a_na
#1
#​
# ,a
#2
#​
# ,...,a
#n
#​
#  (无序)一次操作可以把两个数替换成这两个数的和。
#
#比如数组 [2, 1, 4][2,1,4] 可以变成: [3, 4], [1, 6], [2, 5][3,4],[1,6],[2,5] 。
#
#请问，在不限次合并操作之后，数组中最多能有多少个数可以被 33 整除。
#
#
#Input
#第一行包含一个整数 t(1\leq t \leq 1000)t(1≤t≤1000) ,表示有 tt 个样例每个样例的第一行有一个整数 n(1 \leq n \leq 100)n(1≤n≤100) 表示数组中数的个数, 第二行有 nn 个整数 a_1 ,a_2, ..., a_n (1 \leq a_i \leq 1e9)a
#1
#​
# ,a
#2
#​
# ,...,a
#n
#​
# (1≤a
#i
# ≤1e9) 为数组元素。
#
#
#Output
#每个样例输出一行包含 mm 表示该数组中在操作之后最多能有 mm 个数可以被 3整除


def getMostThree(lenOfNums, nums):
    count = 0
    total = 0
    for num in nums:
      num %= 3
      if not num:
        count += 1
      else:
        total += num
    count += int(total / 3)
    return count

if __name__ == "__main__":
  t = int(input().strip())
  for _ in range(t):
    lenOfNums = int(input().strip())
    nums = map(int, input().strip().split())
    count = getMostThree(lenOfNums, nums)
    print(count)
