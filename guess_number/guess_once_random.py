# @Time    : 2018/6/16 8:21
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
import random

number = random.randint(1, 100)
guess = input("我想好了1到100之间的一个整数。你猜是什么数：")
guess = int(guess)

if guess == number:
    print("你猜中了！厉害！")
else:
    print("你没有猜中。这个数是：" + str(number))


#扩展功能：
#  若玩家没有猜中，给出“你猜的数大了”或“你猜的数小了”的输出。