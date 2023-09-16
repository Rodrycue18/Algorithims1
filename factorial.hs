factorial :: Float->Float
factorial 1 = 1
factorial n = n * factorial(n-1)

--fibonacci

fibonacci :: Int->Int
fibonacci 1 = 0
fibonacci 2 = 1
fibonacci n = fibonacci(n-1)+fibonacci(n-2)

--fibonacci 5 = fibonacci(5-1)+fibonacci(5-2)
--                fibo 4 + fibo 3
--                fibo 3 + fibo 2
--                fibo 2 + 1
--                1
--sumaImpares :: Int->Int
--sumaImpares 1 = 1
--sumaImpares n = sumaImpares(n-1) +  (2*n+1)

sumaImpares :: Int -> Int
sumaImpares 1 = 1
sumaImpares n = (2*n-1)+sumaImpares(n-1)

--1 + 3 + 5 + 7 + 9 + 11
--1   2   3   4   5   6

--sacar el ultimo impar se hace 2*n-1
-- ejm 2*6-1

medioFactorial :: Int ->Int
medioFactorial 0 = 1
medioFactorial 1 = 1
medioFactorial n = n * medioFactorial(n-2)

sumaDigitos :: Int -> Int
sumaDigitos n | n<10 = n
sumaDigitos n = (sacarUltimoDig n) + sumaDigitos(otrosDigitos n) 

sacarUltimoDig :: Int -> Int
sacarUltimoDig n = mod n 10

otrosDigitos :: Int -> Int
otrosDigitos n = div n 10

todosDigitosIguales :: Int -> Bool
todosDigitosIguales n | n<10 = True
                      | otherwise= ((sacarUltimoDig n) == sacarUltimoDig(otrosDigitos n)) && todosDigitosIguales(otrosDigitos n)

numeroCapicua :: Int -> Bool
numeroCapicua n | n<10 = True
                | otherwise = n == numeroInvertido(n)

numeroInvertido :: Int -> Int
numeroInvertido n | n <10 = n
numeroInvertido n = (10^(cantDigitos(n)-1)) * sacarUltimoDig(n) + numeroInvertido (otrosDigitos(n)) 

cantDigitos :: Int -> Int
cantDigitos n | n<10 = 1
              | otherwise = 1 + cantDigitos(otrosDigitos(n))

sumatoriaA :: Int->Int
sumatoriaA n | n==0 = 1
             | otherwise = 2^(n)+sumatoriaA(n-1) 

sumatoriaB :: Int -> Float -> Float
sumatoriaB n q | n <= 1 = q^n
               | otherwise = q^(n)+sumatoriaB(n-1) q

sumatoriaC :: Int -> Float -> Float
sumatoriaC n q | n == 1 = q^(1) + q^(2)
               | otherwise = q^(2*n)+ q^((2*n)-1)+sumatoriaC(n-1) q

-- sumatoriaD :: Integer -> Float -> Float
-- sumatoriaD n q | n == 0 = 1
--                | otherwise = q ^ (2 * n) + sumatoriaD (2 * n - 1) q

-- no logre resolverlo
sumatoriaD :: Int -> Float -> Float
sumatoriaD n q | n == 1 = q^(1) + q^(2)
               | otherwise = q^(2*n)+ q^((2*n)-1)+sumatoriaD(n-1) q

eAprox :: Float->Float
eAprox n | n==0=1
         | n==1=1
         | otherwise = (1/(factorial (n-1))) + eAprox(n-1)