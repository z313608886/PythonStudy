import random


def secret_word():       # 生成随机单词
    words = 'apple pen play game sun hello happy sad red go'.split()
    i = random.randint(0, len(words)-1)
    return words[i]


def shuru(guessed_words):    # 获得用户输入的值
    print('Please enter a letter:')
    while True:
        i = input()
        i = i.lower()
        if i == 'end':  # 输入end 结束程序
            return i
        elif len(i) != 1:
            print("you can only guess one letter,guess again")
        elif i not in "abcdefghijklmnopqrstuvwxyz":
            print('must be a letter,guess again')
        elif i in guessed_words:
            print('you have guessed the letter, guess another')
        else:
            guessed_words = guessed_words + i
            return i, guessed_words    #利用函数返回值传递参数


def judge(k, secret, miss, blanks):
    if k not in secret:
        miss = miss + 1
    else:
        for i in range(0, len(secret)):
            if k == secret[i]:
                blanks = blanks[:i] + k + blanks[i+1:]   #注意拼接用到的字母 [1:5]不包括5
    return miss, blanks

secret = secret_word()
print('HANGMAN GAME')
hangman_pics = ['''      
+ --- +
|     |
      |
      |
      |
      |
========''', '''
+ --- +
|     |
O     |
      |
      |
      |
========''', '''
 + --- + 
 |     |
 O     |
 |     |
       |
       |
 ========''', '''
 + --- +
 |     |
 O     |
/|     |
       |
       |
 ========''', '''
 + --- +
 |     |
 O     |
/|\    |
       |
       |
 ========''', '''
  + --- +
 |     |
 O     |
/|\    |
/      |
       |
 ========''', '''
  + --- +
 |     |
 O     |
/|\    |
/ \    |
       |
 ========''']
miss = 0  # 猜错的次数
guess = 0  # 猜测总次数
blanks = '_'*len(secret)  # 打印空格
guessed_words = ''
while True:
    print(hangman_pics[miss])
    print(blanks)
    k = shuru(guessed_words)
    guessed_words = k[1]
    if k[0] == 'end':
        print('GAME OVER')
        exit()
    else:
        z = judge(k[0], secret, miss, blanks)
        miss = z[0]
        blanks = z[1]
    guess = guess + 1
    if guess == 6:
        print('you have run out of chances. Game over')
        print(hangman_pics[6])
        exit()
    if blanks == secret:
        print('you got the word! It is ', secret, ' ! Congratulations!')
        exit()
