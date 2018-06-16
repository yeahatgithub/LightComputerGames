# @Time    : 2018/6/16 8:14
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
number = 98
guess = input("你猜是什么数：")
guess = int(guess)

if guess == number:
    print("你猜中了！厉害！")
else:
    print("你没有猜中。")