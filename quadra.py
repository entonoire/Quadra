from math import sqrt

while True:
	print("")
	calc = input("calculation : ")

# --= Find A =--
	a_index = calc.find("x²") - 1 # if no -1 it return x
	a = 1

	parssedCalc = calc

	isNum = False
	try :
		float(calc[a_index])
		isNum = True
	except Exception :
		pass


	if (a_index < 0 or calc[a_index] == calc[len(calc) - 1] or not isNum) :
		# value is absent

		if (calc[a_index] == "-") : 
			# x is negative
			a = -1
			parssedCalc = calc.replace(f"-x²", "", 1)

		else : 
			# x is positive (don't replace x² with -)
			parssedCalc = calc.replace(f"+x²", "", 1)
			parssedCalc = calc.replace(f"x²", "", 1) # something x² won't have + in front of him

	else :
		# value is'nt absent

		if (calc[a_index] not in ["-", "+"]) :
			# a is a valid number
			i = a_index
			l = []

			# loop to get the full number
			while True:
				if (i > -1) :
					if (calc[i] in ["-", "+"]) : 
						if (calc[i] == "-") : l.append("-")
						break

					else :
						l.append(calc[i])
						i -= 1

				else :
						break


			l.reverse()
			a = float("".join(l))
				


			# remove {a} from calculation
			parssedCalc = calc.replace(f"{a:g}x²", "", 1)


	# trim the + that can still be there (not minus because i want to keep it for c)
	if (parssedCalc[0] == "+") : 
		parssedCalc = parssedCalc.replace(parssedCalc[0], "", 1)

	# print(f"{calc}\n{parssedCalc}\na : {a}")

	print(f": {parssedCalc}")

# --= Find B =--
	b_index = parssedCalc.find("x") - 1 # if no -1 it return x
	b = 1

	isNum = False
	try :
		float(parssedCalc[b_index])
		isNum = True
	except Exception :
		pass

	if (b_index < 0 or parssedCalc[b_index] == parssedCalc[len(parssedCalc) - 1] or not isNum) :
		# value is absent

		if (parssedCalc[b_index] == "-") : 
			# x is negative
			b = -1
			parssedCalc = parssedCalc.replace("-x", "", 1)

		else : 
			# x is positive (don't replace x with -)
			parssedCalc = parssedCalc.replace("+x", "", 1)


		if ("x" in parssedCalc) :
			parssedCalc = parssedCalc.replace("x", "", 1) # it can append so fixed i guess 


	else :
		# value is'nt absent

		if (parssedCalc[b_index] not in ["-", "+"]) :
			# b is a valid number
			i = b_index
			l = []

			# loop to get the full number
			while True:
				if (i > -1) :
					if (parssedCalc[i] in ["-", "+"]) : 
						if (parssedCalc[i] == "-") : l.append("-")
						break

					else :
						l.append(parssedCalc[i])
						i -= 1

				else :
						break


			l.reverse()
			b = float("".join(l))

			# remove {b} from calculation
			parssedCalc = parssedCalc.replace(f"{b:g}x", "", 1)


	# trim the + that can still be there (not minus because i want to keep it for c)
	if (parssedCalc[0] == "+") : 
		parssedCalc = parssedCalc.replace(parssedCalc[0], "", 1)
	
	# final trim for any - or + that can always be behing c
	if (parssedCalc[len(parssedCalc) - 1] in ["-", "+"]) :
		parssedCalc = parssedCalc.replace(parssedCalc[len(parssedCalc) - 1], "", 1)


	print(f"a : {a:g}")
	print(f"b : {b:g}")
	parssedCalc = parssedCalc.replace("+", "")
	c = float(parssedCalc)
	print(f"c : {c:g}")


# --= Find everything =--

	delta = (b ** 2) - (4 * a * c)

	print(f"\n△ = {b:g}² - 4 * {a:g} * {c:g} = {delta:g}")


	if (delta > 0):
		x1 = ((-b) - sqrt(delta)) / (2 * a)
		x2 = ((-b) + sqrt(delta)) / (2 * a)

		print("\n2 racines")
		print(f"x1 = ({-b:g} - \u221A{delta:g}) / 2 * {a:g} = {x1:g}")
		print(f"x2 = ({-b:g} + \u221A{delta:g}) / 2 * {a:g} = {x2:g}")

	if (delta == 0): 
		x = (-b) / (2 * a)
		print("\n1 racine")
		print(f"x = {-b:g} / 2 * {a:g} = {x:g}")


	if (delta < 0): 
		print("\npas de racine")