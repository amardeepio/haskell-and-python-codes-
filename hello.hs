main = print(prime 24)

doubleme  x = x+x 

doubleus x y = x*2 + y*2 

doubleus x y = doubleme x + doubleme y 

double_of_small_num x = if x > 100 then x else x *2 

evenfornow x = [x*2 | x <- [1..x]]

oddfornow x =[x | x <- [1..x] , x `mod` 2 ==1]

factors n =[x | x <- [1..n] , n `mod` x ==0] -- finding factors 

prime n = factors(n)==[1,n]

[ [[ x | x <- xs, even x ]] | xs <- xxs]

[[[[[a|a <- z, even a ]| z <- y]  | y <- x] | x <- xs] | xs <- xxs] 
mod_of_array m n =  [x `mod` n  | x <- m]
[[[ y | y <- x , even y | x <- xs | xs <- xxs ]]

[[[[z | z <- y , even z ] | y <- x] | x <- xs] | xs <- xxs] 

[[[[[a|a <- z, even a ]| z <- y]  | y <- x] | x <- xs] | xs <- xxs] 

[ [[ x | x <- xs, even x ]] | xs <- xxs]



