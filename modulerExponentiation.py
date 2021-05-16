'''Tutorial for modular exponentiation --> Calculating modular exponentiation using python
given a, n and mod values return what would be ( a ^ n) % mod
this is quite useful for calculating power for big numbers as that big number
wouldn't fit properly in int/long'''

#calculation power exponentiation using python3
#euler modulus power exp


def expPower(a, n, mod):
	'''calculate a ^ n % mod
	we will use recursive approach which will do this calculation 
	in log(n), we can write a^n as a^n/2 * a^n/2 if n is even 
	else a^n as a^n/2 * a^n/2 * a '''

	#base condition to break the recursion
	if n == 0:
		return 1

	#print(n)

	#don't calculate power twice just calculate once and use it
	half = expPower(a, n//2, mod)
 
	#if n is odd ( n & 1) is n % 2
	if( n & 1 ):
		return( half * half * a) % mod

	#calculate power for even n
	return( half * half) % mod


if __name__ == '__main__':
	#input
	''' change input parameters .. make them interactive as well
	a = 2
	n = 5'''
	a = int(input('enter value of a: '))
	n = int(input('enter value of n: '))

	#change value of mod if required
	#this will work only when mod is prime
	#for non prime their are special ways which could be used to
	#calculate modulus exponentiation
	mod = 1000*1000*1000 + 7;

	ans = expPower(a, n, mod)

	print(" %d ^ %d %s %d = %d" %(a, n, '%', mod, ans) )

