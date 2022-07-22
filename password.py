password = 'a123456'
y = 3
while True:
	pwd = input('請輸入密碼: ')
	if pwd != password:
		y = y - 1
		if y <= 0:
			break
		print('密碼錯誤! 還有', y,"次機會")
	elif pwd == password:
		print("登入成功")
		break