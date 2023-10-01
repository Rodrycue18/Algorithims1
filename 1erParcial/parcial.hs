module Solucion where

-- Ejercicio 1
golesDeNoGoleadores :: [(String, String)] -> [Int] -> Int  -> Int
golesDeNoGoleadores _ goles totalGolesTorneo = totalGolesTorneo - sumatoriaDeGoles goles  


sumatoriaDeGoles :: [Int] -> Int
sumatoriaDeGoles [] = 0
sumatoriaDeGoles (x:xs) = x + sumatoriaDeGoles xs 


-- Ejercicio 2 
equiposValidos :: [(String, String)] -> Bool 
equiposValidos [] = True
equiposValidos (x:xs) = (revisamosTupla x) && not (equiposRepetidos x xs) && not (nombresyEquiposrepetidos x (aplanar xs)) &&  equiposValidos xs

revisamosTupla :: (String,String) -> Bool  --Revisamos si hay 2 equipos en una tupla o dos 2 jugadores en una tuplas
revisamosTupla (equipo,jugador) = not (equipo == jugador)

equiposRepetidos :: (String,String) -> [(String,String)] -> Bool --Equipos repetidos
equiposRepetidos (a,b) xs = elem (a,b) xs || elem (b,a) xs 

nombresyEquiposrepetidos :: (String,String) -> [String] -> Bool --Revisa si hay nombres o equipos repetidos
nombresyEquiposrepetidos (a,b) (xs) = elem a xs || elem b xs

aplanar :: [(String, String)] -> [String]
aplanar [] = []
aplanar (x:xs) = fst x : snd x : aplanar xs


-- Ejercicio 3

porcentajeDeGoles :: String -> [(String, String)] -> [Int] -> Float
porcentajeDeGoles jugador ((equipos,jugadores):xs) (y:ys) | jugador == jugadores = (sacarPromedio (y) (totalDeGoles(y:ys)))
                                                          | otherwise = porcentajeDeGoles (jugador) (xs) (ys ++ [y])

sacarPromedio :: Int->Int -> Float
sacarPromedio a b = (division a b) * 100.0

totalDeGoles :: [Int] -> Int
totalDeGoles [] = 0
totalDeGoles (x:xs) = x + totalDeGoles xs

division :: Int -> Int -> Float
division a b = (fromIntegral a) / (fromIntegral b)


-- Ejercicio 4
botinDeOro :: [(String, String)] -> [Int] -> String
botinDeOro ((equipo,jugador):xs) [] = " "
botinDeOro ((equipo,jugador):xs) (y:ys) | maximo(y:ys) == y = jugador
                                        | otherwise = botinDeOro (xs) (ys)

maximo :: [Int] -> Int
maximo [] = 0
maximo (x:xs) | x > maximo xs = x
              | otherwise = maximo xs