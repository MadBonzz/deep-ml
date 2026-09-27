def phi_corr(x: list[int], y: list[int]) -> float:
	"""
	Calculate the Phi coefficient between two binary variables.

	Args:
	x (list[int]): A list of binary values (0 or 1).
	y (list[int]): A list of binary values (0 or 1).

	Returns:
	float: The Phi coefficient rounded to 4 decimal places.
	"""
	# Your code here
	x00 = x11 = x01 = x10 = 0
	for x1, y1 in zip(x, y):
		if(x1 == 0 and y1 == 0):
			x00 += 1
		elif(x1 == 0 and y1 == 1):
			x01 += 1
		elif(x1 == 1 and y1 == 0):
			x10 += 1
		else:
			x11 += 1
	val = ((x00*x11) - (x01 * x10))
	denominator = (((x00 + x01) * (x10 + x11) * (x00 + x10) * (x01 + x11)) ** 0.5)
	if denominator == 0:
		return 0
	return round(val/denominator,4)