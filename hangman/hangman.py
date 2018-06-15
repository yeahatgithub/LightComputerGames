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
guessed_letters = ['_', '_', '_']
missed_letters = ''
while guess_error < len(HANGMAN_LIST) - 1:
    print(HANGMAN_LIST[guess_error])
    print("当前空缺：")
    print(' '.join(guessed_letters))
    if len(missed_letters) > 0:
        print("没猜中的字母：" + missed_letters)
    g = input("\n你猜的下一个字母是：")
    hit = False
    for i in range(len(target_word)):
        if target_word[i] == g:
            guessed_letters[i] = g
            hit = True
    if hit:
        if '_' not in guessed_letters:
            break
    else:
        guess_error += 1
        missed_letters += g

if guess_error == len(HANGMAN_LIST) - 1:
    print("真不幸，你丢命了！")
    print(HANGMAN_LIST[guess_error])
else:
    print("你猜对了！被猜测的单词是：" + target_word)
    print("棒棒哒！")


