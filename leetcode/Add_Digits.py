def addDigits(num):
	"""
	:type num: int
	:rtype: int
	"""
	sum = 0
	while num > 0:
		num, mod = divmod(num, 10)
		print "num=", num
		print "mod=", mod
		sum = sum + mod
		print "sum=", sum
addDigits(1234)
