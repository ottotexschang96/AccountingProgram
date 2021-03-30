# we can tell there is a list by seeing []

product = []
while True:
	name = input('Please input product name:')
	if name == 'q':
		break
	price = input('Please input product price:') # price is string
	# p = []
	# p.append(name)
	# p.append(price)
	## p = [name, price]
	# product.append(p)
	product.append([name, price])
print(product)

for p in product:
	print(p)
	print(p[0], 's price is', p[1]) # p[1] is string

# +* can be applied on string, but not -/
# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'

# the following with can be reviewed in Chapter4\20210327\Read
# encoding = 'utf-8': UTF-8（8-bit Unicode Transformation Format）
with open('AccountingProgram.csv', 'w', encoding = 'utf-8') as f: # use more common .csv, which can be opened by excel, to replace .txt
	f.write('Name名子, Price價格\n')
	for p in product:
		f.write(p[0] + ',' + p[1] + '\n') # p[1] is string, + can only combine string with string and int with int 
#f's function 'write' should only include one argument/srting like append() takes exactly one argument (1 given)

# test
data = [1, 3, 5, 7, 9]
with open('test.txt', 'w') as f:
	for d in data: # d is still int
		f.write(str(d) + '\n') #write() argument must be str, not int
		# print(d)
