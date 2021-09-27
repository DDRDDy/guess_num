import random
r = random.randint(1, 100)
while True:
	u = input('請輸入1-100間的數字:')
	u = int(u)
	if u == r:
		print('終於猜對了!')
		break
	else:
		if u < r:
			print('比答案小')
		elif u > r:
			print('比答案大')