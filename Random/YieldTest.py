def YieldSomething():
	yield 1
	yield 2
	yield 3
	yield 4
	yield 5

asd = YieldSomething()
for d in asd:
	print(d)