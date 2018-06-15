# @Time    : 2018/6/8 20:48
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT

target_word = "cat"
print("H A N G M A N")

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

guess_error = 0
guessed_letter = ['_', '_', '_']
while guess_error < len(HANGMAN_LIST) - 1:
    print(HANGMAN_LIST[guess_error])
    print("缺失的字母：")
    print(' '.join(guessed_letter))
    g = input("输入下一个字母：")
    hit = False
    for i in range(len(target_word)):
        if target_word[i] == g:
            guessed_letter[i] = g
            hit = True
    if hit:
        if '_' not in guessed_letter:
            break
    else:
        guess_error += 1

if guess_error == len(HANGMAN_LIST) - 1:
    print("真不幸，你丢命了！")
    print(HANGMAN_LIST[guess_error])
else:
    print("你猜对了！")
    print("棒棒哒！")


