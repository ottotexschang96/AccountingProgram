# an ideal function should only do one thing a time
# Refactor: rewrite your code into fcn

import os # operating system
# To set up fcn, check if filename or product and set it as coin slot or pass in

# Read a file
def read_file(filename): # insert any filename to read it; simply to read file only
	product = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f: 
			if 'Name名子, Price價格' in line: 
				continue 
			name, price = line.strip().split(',') 
			product.append([name, price])
	return product # there is a new append file, and it needs to be saved
		
# User input
def user_input(product): # input new product and append
	while True:
		name = input('Please input product name:')
		if name == 'q':
			break
		price = input('Please input product price:') 
		product.append([name, price])
	print(product)
	return product # there is a new append file, and it needs to be saved

# Print all buying record
def print_product(product): # input new product 
	for p in product:
		print(p)
		print(p[0], 's price is', p[1]) 

# Write into a file
def write_file(filename, product):
	with open(filename, 'w', encoding = 'utf-8') as f: 
		f.write('Name名子, Price價格\n')
		for p in product:
			f.write(p[0] + ',' + p[1] + '\n') 

def main(): # usually we write the main running code into main fcn where can enter our code and run it
	filename = '20210331RefactorAccountingProgramIntoFcn.csv'
	if os.path.isfile(filename): 
		print('Yes, there is the file')
		product = read_file(filename) # product = for append
	else:
		print('No such file')
	product = user_input(product) # product = for append
	print_product(product)
	write_file('20210331RefactorAccountingProgramIntoFcn.csv', product)

main()


## Find \t (tab), replaced by    (four space)
## ctr+[:将空格减去