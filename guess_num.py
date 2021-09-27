import random
r = random.randint(1, 100)
i = 0 #猜的次數
while True:
	u = input('請輸入1-100間的數字:') #使用者輸入之數字
	u = int(u)
	i = i + 1 #同 i += 1 
	if u == r:
		print('終於猜對了!')
		print('已經猜了', i, '次')
		break
	elif u < r:
		print('比答案小')
	elif u > r:
		print('比答案大')
	print('已經猜了', i, '次')
