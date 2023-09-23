sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria(xs)

productoria :: [Integer] -> Integer
productoria [] = 1
productoria (x:xs) = x * productoria(xs)

maximo :: [Int] -> Int
maximo [] = 0
maximo [x] = x
maximo (x:xs) | x > maximo xs = x
              | otherwise = maximo xs


sumarN :: Int -> [Int] -> [Int]
sumarN _ [] = []
sumarN n (x:xs) = (x+n) : (sumarN n xs)

sumarElPrimero :: [Int] -> [Int]
sumarElPrimero [] = []
sumarElPrimero (x:xs) = sumarN x (x:xs) 

sumarElUltimo :: [Int] -> [Int]
sumarElUltimo [] = []
sumarElUltimo (x:xs) = reverse(sumarN x (reverse(x:xs)))

pares :: [Int] -> [Int]
pares [] = []
pares (x:xs) | mod x 2 == 0 = x : pares xs
             | otherwise = pares xs

multiplosdeN :: Int->[Int]->[Int]
multiplosdeN _ [] = []
multiplosdeN n (x:xs) | mod x n == 0 = x : multiplosdeN n xs
                      | otherwise = multiplosdeN n xs

ordenar :: [Int] -> [Int]
ordenar [] = []
ordenar [x] = [x]
ordenar (x:xs) | x < ordenar xs = [x] ++ ordenar xs
               | otherwise = ordenar xs

--Vemos quienes son menores
compararCadaElemento :: Int -> [Int] -> Int
compararCadaElemento _ [] = []
compararCadaElemento x (y:ys) |  x < compararCadaElemento y (ys) = x
                          | otherwise = compararCadaElemento ()

-- no edsta terminado , pensar mejor la solucion
