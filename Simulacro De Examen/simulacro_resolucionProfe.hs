relacionesValidas :: [(String,String)] -> Bool
relacionesValidas [] = True
relacionesValidas (x:xs) = not(amigaDeMiMisma x) && (amistadNoSeRepite x xs) && relacionesValidas(xs)


amigaDeMiMisma :: (String,String) -> Bool
amigaDeMiMisma (x,y) = x==y

amistadNoSeRepite :: (String,String) -> [(String,String)] -> Bool
amistadNoSeRepite x [] = True -- no es necesario este caso base ya que no estamos usando recursion
amistadNoSeRepite (x,y) xs = (not(elem (x,y) xs)) && (not (elem(y,x) xs))

--Ejercicio Personas

personas :: [(String,String)]->[String]
personas xs = sacarRepetidos (aplanarLaListaDeTuplas xs)

aplanarLaListaDeTuplas :: [(String,String)]->[String]
aplanarLaListaDeTuplas [] = []
aplanarLaListaDeTuplas (x:xs) = (fst x : snd x : aplanarLaListaDeTuplas xs)
--alternativa 1: [fst x, snd x] ++ aplanarLaListaDeTuplas xs
--alternativa 2: aplanarLaListaDeTuplas ((a,b):xs) = (a:b:aplanarLaListaDeTuplas xs)

sacarRepetidos :: [String] -> [String]
sacarRepetidos [] = []
sacarRepetidos (x:xs) | elem x xs = sacarRepetidos xs
                      | otherwise = (x: sacarRepetidos xs)

--Ejercicio amigosDe

--amigosDe :: String -> [(String,String)] -> [String]
--amigosDe _ [] = []
--amigosDe n (x:xs)

