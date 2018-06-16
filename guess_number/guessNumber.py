# @Time    : 2018/6/14 11:11
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
import random

number = random.randint(1, 20)
print("我已经想好了1到20之间的一个数。")

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


