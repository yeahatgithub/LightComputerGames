# @Time    : 2018/6/8 20:48
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
import random

HANGMAN_LIST = [
'''
  +---+
      |
      |
      |
     === 
''',
'''
  +---+
  o   |
      |
      |
     === 
''',
'''
  +---+
  o   |
  |   |
      |
     === 
''',
'''
  +---+
  o   |
 /|   |
      |
     === 
''',
'''
  +---+
  o   |
 /|\  |
      |
     === 
''',
'''
  +---+
  o   |
 /|\  |
 /    |
     === 
''',
'''
  +---+
  o   |
 /|\  |
 / \  |
     === 
'''
        ]

def input_guess(guessed_letters):
    '''输入猜测的字母。把重复的猜测，非字母，非单个字母的输入，视为无效输入，要求重新输入。'''
    while True:
        g = input("你猜的下一个字母是：")
        g = g.lower()
        if len(g) != 1:
            print("只能输入1个字母！")
        elif not g.isalpha():
            print("必须输入*字母*！")
        elif g in guessed_letters:
            print("你已经猜过这个字母。再猜一次...")
        else:
            return g


def play_set(target_word):
    hitted_letters = ['_'] * len(target_word)
    missed_letters = ''
    num_guess_failure = 0
    print("H A N G M A N")
    while num_guess_failure < len(HANGMAN_LIST) - 1:
        print(HANGMAN_LIST[num_guess_failure])
        print("当前空缺：")
        print(' '.join(hitted_letters))
        num_guess_failure = len(missed_letters)
        if num_guess_failure > 0:
            print("没猜中的字母：" + missed_letters)

        guessed_letters = ''.join(hitted_letters) + missed_letters
        g = input_guess(guessed_letters)
        hit = False
        for i in range(len(target_word)):
            if target_word[i] == g:
                hitted_letters[i] = g
                hit = True
        if hit:
            if '_' not in hitted_letters:
                break
        else:
            missed_letters += g
    if num_guess_failure == len(HANGMAN_LIST) - 1:
        print("真不幸，你丢命了！")
        print(HANGMAN_LIST[num_guess_failure])
        print("被猜的单词是：" + target_word)
    else:
        print("你猜对了！被猜测的单词是：" + target_word)
        print("棒棒哒！")

def continue_to_play():
    '''继续玩吗？'''
    print()
    print("你要继续玩吗？(yes or no)")
    return input().lower().startswith('y')

target_words_str = "apple banana berry lemon lichee mango orange pear"
target_words = target_words_str.split()

start_game = True
while start_game:
    target_word = random.choice(target_words)
    play_set(target_word)

    start_game = continue_to_play()

print("拜拜！")


