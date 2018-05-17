
def divisor(N):
	return [n for n in range(1, N+1) if N %n == 0]


def Prime(n):
	return divisor (n) == [1,n]

def primes(n):
	return filter (Prime, range(1,n+1))

print "all primes:  ", primes(50)