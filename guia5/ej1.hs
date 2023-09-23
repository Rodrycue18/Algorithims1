--Ejercicio 1
longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud(xs)
--longitud (x:xs) = length(x:xs) -- The noob way

--Ejercicio 2
ultimo :: [Int] -> Int
ultimo [] = 0
ultimo [x] = x 
ultimo (x:xs) = ultimo(xs)

--Ejercicio 3
principio :: [t] -> [t]
principio [] = []
principio [x] = []
principio (x:xs) = x : principio xs 

--Ejercicios 4

reverso :: [t] -> [t]
reverso [] = []
reverso (x:xs) = (reverso xs) ++ [x]

--Ejercicio 5

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece n (x:xs) | (n == x) || pertenece n xs = True
                   | otherwise = False
-- Alternativa : n (x:xs) =  elem(n (x:xs))

--Ejercicio 6
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [x] = True 
todosIguales (x:xs) | x == head(xs) && todosIguales xs = True
                    | otherwise = False

--Ejercicio 7
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [x] = True
todosDistintos (x:xs) = (auxiliarTodosDist x xs) && todosDistintos xs

auxiliarTodosDist :: (Eq t) => t -> [t] -> Bool
auxiliarTodosDist x xs = not(pertenece x xs)
            --alternativa: not(elem x xs)

-- Ejercicio 8
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [x] = False
hayRepetidos (x:xs) = auxiliarHayRepe x xs || hayRepetidos xs

auxiliarHayRepe :: (Eq t) => t -> [t] -> Bool
auxiliarHayRepe x xs = pertenece x xs

-- Ejercicio 9 
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar n (x:xs) | n == x = xs
                | otherwise = x : quitar n xs

quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos n (x:xs) | n == x = quitarTodos n xs
                     | otherwise = x : quitarTodos n xs

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) | elem x xs = x : (eliminarRepetidos(quitarTodos x xs))
                         | otherwise = x : eliminarRepetidos xs

-- mismosElementos :: (Eq t) => [t] -> [t] -> Bool
-- mismosElementos [] (y:ys) = True
-- mismosElementos (x:xs) (y:ys) | (auxMismosElementos x (y:ys) ) && (mismosElementos (xs) (y:ys)) = True
--                               | otherwise = False

-- auxMismosElementos :: (Eq t) => t -> [t] -> Bool
-- auxMismosElementos x (y:ys) = elem x (y:ys)

estaContenida :: (Eq t) => [t] -> [t] -> Bool
estaContenida [] ys = True
estaContenida (x:xs) ys = pertenece x ys && estaContenida xs ys

mismosElementos1 :: (Eq t) => [t] -> [t] -> Bool
mismosElementos1 xs ys = estaContenida xs ys && estaContenida ys xs

capicua :: (Eq t) => [t] -> Bool
capicua [] = False
capicua [x] = True
capicua list = list == reverse (list)

------------------------------    
--Pares de una lista
evens :: [Int] -> [Int]
evens [] = []
evens (x:xs) | mod x 2 == 0 = x : evens xs
             | otherwise = evens xs
--Elimina repetidos de una lista , solo deja uno
nub :: (Eq t) => [t] -> [t]
nub [] = []
nub (x:xs) | elem x xs = nub xs
           | otherwise = x : nub xs

agregarAtras :: Int -> [Int] -> [Int]
agregarAtras x [] = [x]
agregarAtras x lista = (head lista) : (agregarAtras x (tail lista))