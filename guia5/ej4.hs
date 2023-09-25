sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos (x:[]) = [x]
sacarBlancosRepetidos (x:y:xs) | (x==y) && (x==' ') = sacarBlancosRepetidos (y:xs)
                               | otherwise = x : sacarBlancosRepetidos(y:xs)
             -- ALTERNATIVA: otherwise = [x] ++ sacarBlancosRepetidos (y:xs)

contarPalabras :: [Char] -> Integer
contarPalabras [] = 0
contarPalabras (x:xs) = auxContarPalabras x + contarPalabras xs

auxContarPalabras ::  Char -> Integer
auxContarPalabras x | x==' ' = 0
                    | otherwise = 1

eliminarBlancos :: [Char]->[Char]
eliminarBlancos []=[]
eliminarBlancos (x:xs) | x == ' ' = eliminarBlancos (xs)
                       | otherwise = x : eliminarBlancos(xs)

palabras :: [Char] -> [[Char]]
palabras [] = [[]]
palabras (x:[]) = [[x]]










contarPalabras1 :: [Char] -> Int
contarPalabras1 [] = 0
contarPalabras1 (xs) = (contarEspacios (quitarEspaciosIniFin (sacarBlancosRepetidos xs))) + 1

contarEspacios :: [Char] -> Int
contarEspacios [] = 0
contarEspacios (x:xs) | x==' '= 1+contarEspacios xs
                      | otherwise = contarEspacios xs

quitarEspaciosIniFin :: [Char] -> [Char]
quitarEspaciosIniFin [] = []
quitarEspaciosIniFin (x:xs) | x==' ' && head(reverse(xs))==' ' = (quitarUltimo xs)
                        | x==' ' = xs
                        | head(reverse(xs))==' ' = quitarUltimo (x:xs)
                        | otherwise = x:xs

quitarUltimo :: [Char] -> [Char]
quitarUltimo [] = []
quitarUltimo [x] = []
quitarUltimo (x:xs) = [x]++(quitarUltimo xs)