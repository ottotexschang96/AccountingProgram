# Read a file
product = []
with open('AccountingProgram.csv', 'r', encoding = 'utf-8') as f:
	for line in f: 
		if 'Name名子, Price價格' in line: # make sure if a word is in specific line, use 'in'
			continue # skip the current line and move to second loop. continue usually comes with loop like break
		# s = line.strip().split(',') 
		name, price = line.strip().split(',') 
		#remove str \n or space by strip; cut the line by split, which will make it become a list
		# name = s[0]
		# price = s[1]
		product.append([name, price])
		# print(s)
print(product)

# User input
## we can tell there is a list by seeing []
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

# Print all buying record
for p in product:
	print(p)
	print(p[0], 's price is', p[1]) # p[1] is string


#Write into a file
## the following with can be reviewed in Chapter4\20210327\Read
## encoding = 'utf-8': UTF-8（8-bit Unicode Transformation Format）, it helps to be read in sublime and loading csv from excel
with open('AccountingProgram.csv', 'w', encoding = 'utf-8') as f: # use more common .csv, which can be opened by excel, to replace .txt
	f.write('Name名子, Price價格\n')
	for p in product:
		f.write(p[0] + ',' + p[1] + '\n') # p[1] is string, + can only combine string with string and int with int 
#f's function 'write' should only include one argument/srting like append() takes exactly one argument (1 given)
# +* can be applied on string, but not -/
# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'

# test
data = [1, 3, 5, 7, 9]
with open('test.txt', 'w') as f:
	for d in data: # d is still int
		f.write(str(d) + '\n') #write() argument must be str, not int
		# print(d)
