hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False --caso base
hayRepetidos (x:[]) = False
hayRepetidos (x:xs) | pertenece x xs = True
                    | otherwise = hayRepetidos xs
                    

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece x (y:[]) = x==y
pertenece x (y:ys) | x==y = True
                   | otherwise = pertenece x ys

testPertenece = (pertenece 2 [1,2,3])  == True :: Bool
testhayRepetidos = (hayRepetidos [1,2,3,4,5,5,6]) == True :: Bool
testhayRepetidos1= (hayRepetidos ['a', 'x', 'x', 'c', 'd', 'b']) == True :: Bool

maximo :: [Int] -> Int
maximo [] = 0
maximo [x] = x
maximo (x:xs) | x > maximo xs = x
              | otherwise = maximo xs 

testmaximo = (maximo [1,2,3,2]) == 3 :: Bool
testmaximo1 = (maximo [3,2,1]) == 3 :: Bool
testmaximo2 = (maximo [3]) == 3 :: Bool
------------------------------
ordenar :: [Int] -> [Int]
ordenar []=[]
ordenar [x]=[x]
ordenar (x:xs) = agregarAtras maximo(x:xs)

agregarAtras :: Int -> [Int] -> [Int]
agregarAtras x [] = [x]
agregarAtras x lista = (head lista) : (agregarAtras x (tail lista))
