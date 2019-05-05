b=1;d=1
while d==1:
    while b==1:
        a=input('please input 字符串:')
        if a.isalpha():
            b=0
        else:
            print('输入错误,重新输入')

    b=1
    c=len(a)
    if a=='quit':
        exit()
    print('这是一个长度为',c,'的字符串')
