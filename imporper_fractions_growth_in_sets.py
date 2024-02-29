import math
import matplotlib.pyplot as plt
import warnings

class Fraction: 
	def __init__(self, numerator, denominator): 
		self.numerator = numerator 
		self.denominator = denominator
	def __add__(self, other):
		newnumerator = self.numerator + other.numerator
		newdenominator = self.denominator + other.denominator
		return Fraction(newnumerator, newdenominator)

	def invert(self): 
		return Fraction(self.denominator, 2 * self.numerator)

	def __repr__(self): 
		return f"{self.numerator}/{self.denominator}"


	def __eq__(self, other): 
		return (self.numerator == other.numerator) and (self.denominator == other.denominator)


	def isImproper(self): 
		return (self.numerator) > (self.denominator)

 
def simplify(myFrac: Fraction) -> Fraction: 
	return Fraction(int(myFrac.numerator/math.gcd(myFrac.numerator, myFrac.denominator)), int(myFrac.denominator/math.gcd(myFrac.numerator, myFrac.denominator)))
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main(initialElement):
	warnings.warn("Please note: This is a non-terminating process. Please use control + C to terminate at your discretion.")
	impropercount = 0
	S = [initialElement]

	for currentFrac in S: 
		added = 0
		# Operation 1: catering to rule 2. 
		if simplify(currentFrac.invert()) not in S: 
			S.append(simplify(currentFrac.invert()))
			if simplify(currentFrac.invert()).isImproper(): 
				impropercount += 1
			added += 1
		

		# Operation 2: catering to rule 3. Add the given fraction to everything before it.
		currentIndex = S.index(currentFrac)
		for previndex in range(currentIndex): 
			if (currentFrac != S[previndex]) and (simplify(currentFrac + S[previndex]) not in S): 
				S.append(simplify(currentFrac + S[previndex]))
				added += 1
				if simplify(currentFrac + S[previndex]).isImproper(): 
					impropercount += 1

	
		if len(S) % 100 == 0: 
			# print(f"\n\n\n {S}")
			print(f"\nTotal number of improper fractions: {impropercount}")
			print(f"Total number of fractions in set: {len(S)}\n")

		if len(S) > 1000000: 
			print(f"Stopping execution as length has crossed 10000")
			print(f"Total number of improper fractions: {impropercount}")
			break 

		replayBufferLen.append(len(S))
		replayBuffernumImproper.append(impropercount)

try:
	replayBufferLen = []
	replayBuffernumImproper = []
	initialElement = Fraction(1, 1)
	initialElementNumerator = int(input("Enter the numerator of the starting fraction of S: "))
	initialElementDenominator = int(input("Enter the denominator of the starting fraction of S: "))
	initialElement = Fraction(initialElementNumerator, initialElementDenominator)
	main(initialElement)
except KeyboardInterrupt: 
	plt.xlabel('Length of S')
	plt.ylabel('Number of improper fractions')
	plt.title(f'Rate of improper fraction growth with initial condition S = [{initialElement}]')
	plt.plot(replayBufferLen, replayBuffernumImproper, color='blue', marker='o')
	plt.show()
else: 
	exit()

	


