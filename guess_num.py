import random
i = 0 #猜的次數
start = input('請決定隨機數字的開始值:')
end = input('請決定隨機數字的結束值:')
start = int(start)
end = int(end)
r = random.randint(start, end)
while True:
	u = input('請輸入數字:') #使用者輸入之數字
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
