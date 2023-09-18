sumaExt::Int-> Int->Int
sumaExt i j | i==0 = 0
            | otherwise = sumInt (i) (j) + sumaExt (i-1) (j)

sumInt :: Int -> Int-> Int
sumInt i j | j ==0 = 0
           | otherwise = (i^j) + sumInt (i) (j-1)

testSumatoria = (sumaExt 1 2) == 2 :: Bool

-- ejercico 14 sumaPotencias q^(a+b)
-- sumaGrande :: Int->Int-> Int
-- sumaGrande a b | a==0 = 0
--                | otherwise = sumaPeque (a) (b) + sumaGrande (a-1) (b)

-- sumaPeque :: Int -> Int ->Int
-- sumaPeque a b | b==0 = 0
--               | otherwise = (a+b) + sumaPeque (a) (b-1)

-- sumaPotencias :: Int->Int->Int->Int
-- sumaPotencias q a b | a==1 && b ==1 = q^2
--                     | otherwise = q^(a+b) + q^(sumaGrande (a-1) (b))+ sumaPotencias 

sumaPotencias :: Int->Int-> Int-> Int
sumaPotencias q a b | a==0 =0
                    |otherwise = sumaPeque (q) (a) (b) + sumaPotencias (q) (a-1) (b)

sumaPeque :: Int -> Int ->Int-> Int
sumaPeque q a b | b==0 = 0
                | otherwise = q^(a+b) + sumaPeque (q) (a) (b-1)
