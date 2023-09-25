contarPalabras1 :: [Char] -> Int
contarPalabras1 [] = 0
contarPalabras1 (xs) = (contarEspacios (quitarEspaciosIniFin (sacarBlancosRepetidos xs))) + 1

sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos (x:[]) = [x]
sacarBlancosRepetidos (x:y:xs) | x==y && x==' ' = sacarBlancosRepetidos (y:xs)
                             | otherwise = [x] ++ sacarBlancosRepetidos (y:xs) 

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

palabras :: [Char] -> [[Char]]
palabras xs = armarListaPalabras (quitarEspaciosIniFin xs)

armarListaPalabras :: [Char] -> [[Char]]
armarListaPalabras [] = []
armarListaPalabras xs = [primerPalabra xs] ++ armarListaPalabras (sacarPrefijo (primerPalabra xs) xs)

primerPalabra :: [Char] -> [Char]
primerPalabra [] = []
primerPalabra [' '] = []
primerPalabra [x] = [x]
primerPalabra (x:' ':xs) = [x] 
primerPalabra (x:y:xs) = [x] ++ primerPalabra (y:xs)

sacarPrefijo :: [Char] -> [Char] -> [Char]
sacarPrefijo [] [] = []
sacarPrefijo [] (y:ys) | y==' ' = ys
                        | otherwise = (y:ys)
sacarPrefijo (x:xs) (y:ys) | x==y = sacarPrefijo xs ys
                           | y==' ' = ys
                           | otherwise = ys
