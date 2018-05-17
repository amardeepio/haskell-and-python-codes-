main :: IO ()

main = print ((fibo 8),(factorial 4))


factorial 0 = 1  
factorial n = n * factorial (n - 1)  






fibo 1 = 0 

fibo 2 = 1


fibo n = fibo(n-1) +fibo(n-2)