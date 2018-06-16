# @Time    : 2018/6/16 8:26
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
import random

continuing = True
while continuing:
    number = random.randint(1, 100)
    print("我已经想好了1到100之间的一个数。")
    for i in range(6):
        print("你猜一猜看是什么数：")
        guess = int(input())

        if guess == number:
            print("你猜对了。恭喜！")
            break
        elif guess < number:
            print("猜小了")
        else:
            print("猜大了")

    if guess != number:
        print("你猜的都不对。我想的数字是" + str(number) + ".")

    print("再猜一轮？(yes/no)")
    continuing = input().lower().startswith('y')

#扩展程序功能：
#1. 修改“你猜一猜看是什么数：”为：
#   如果是一轮里头的第一次，提示“你猜一猜看是什么数：”，否则提示”你再猜："