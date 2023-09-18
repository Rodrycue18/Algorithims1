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

