def special_pythagorean_triplet():
	
	total_sum = 1000
	
	a = 1
	b = 2
	c = 3
	
	permutations = []
	
	for a in range(1, total_sum):
		for b in range(a + 1, total_sum):
			for c in range(b + 1, total_sum):
				if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
					print(a, b, c)
					print(a * b * c)

					
special_pythagorean_triplet()