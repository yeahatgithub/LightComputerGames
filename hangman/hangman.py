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

guessed_letters = ['_', '_', '_']
missed_letters = ''
num_guess_failure = 0
while num_guess_failure < len(HANGMAN_LIST) - 1:
    print(HANGMAN_LIST[num_guess_failure])
    print("当前空缺：")
    print(' '.join(guessed_letters))
    num_guess_failure = len(missed_letters)
    if num_guess_failure > 0:
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
        missed_letters += g

if num_guess_failure == len(HANGMAN_LIST) - 1:
    print("真不幸，你丢命了！")
    print(HANGMAN_LIST[num_guess_failure])
else:
    print("你猜对了！被猜测的单词是：" + target_word)
    print("棒棒哒！")


