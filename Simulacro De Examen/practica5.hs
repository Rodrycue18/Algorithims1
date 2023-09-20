--Ejercicio 1
longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud(xs)
--longitud (x:xs) = length(x:xs) -- The noob way

--Ejercicio 2
ultimo :: [t] -> Int
ultimo [] = 0
--ultimo [x] = x
ultimo (x:xs) = ultimo(xs)

principio :: [Int] -> [Int]
principio [] = []
principio [x] = []
principio (x:xs) = x : principio xs 

agregarAtras :: Int -> [Int] -> [Int]
agregarAtras x [] = [x]
agregarAtras x lista = (head lista) : (agregarAtras x (tail lista))

--tail, init , head, last son 4 comandos para una lista
