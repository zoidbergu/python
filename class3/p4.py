
#randrange(0, 3): 0~2까지 무작위 수 만듦
import random

com= random.randrange(3)
user= int(input('가위0 바위1 보2 선택: '))
print('user= %d, com= %d' % (user, com))

if user == com :
    print('비겼습니다')
elif(user == 0 == 2) or (user == 1 and com == 0) or (user == 2 and com == 1) :
    print('user 승!')
else :
    print('com 승!')