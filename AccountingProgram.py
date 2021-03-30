# we can tell there is a list by seeing []

product = []
while True:
	name = input('Please input product name:')
	if name == 'q':
		break
	price = input('Please input product price:')
	# p = []
	# p.append(name)
	# p.append(price)
	## p = [name, price]
	# product.append(p)
	product.append([name, price])
print(product)

for p in product:
	print(p)
	print(p[0], 's price is', p[1])

# +* can be applied on string, but not -/
# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'

# can be reviewed in Chapter4\20210327\Read
with open('AccountingProgram.csv', 'w') as f: # use more common .csv, which can be opened by excel, to replace .txt
	for p in product:
		f.write(p[0] + ',' + p[1] + '\n') 
#f's function 'write' should only include one argument/srting like append() takes exactly one argument (1 given)