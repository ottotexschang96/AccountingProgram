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