digitoUnidades :: Int -> Int
digitoUnidades x = x  `mod` (10)

digitoDecenas :: Int->Int
digitoDecenas y = y  `div` (10)

x :: Int->Int
x y = y `mod` (10)

k :: Int->Int
k y= x(digitoDecenas(y))
--Guia 3 - Ejercicio 4:
todoMenor :: (Int,Int) -> (Int,Int) -> Bool
todoMenor (x,y) (a,b) | (x<a && y<b) = True
                      | otherwise = False
--Guia 3 - Ejercicio 4 e):
sumarSoloMultiplos :: (Int,Int,Int)-> Int -> Int
sumarSoloMultiplos (x,y,z) w | (x`mod`w==0) && (y`mod`w==0) && (z`mod`w==0) = x+y+z
                             | (x`mod`w/=0) && (y`mod`w/=0) && (z`mod`w/=0) = 0
                             | (x`mod`w/=0) && (y`mod`w==0) && (z`mod`w==0) = y+z
                             | (x`mod`w==0) && (y`mod`w==0) && (z`mod`w/=0) = x+y
                             | (x`mod`w==0) && (y`mod`w/=0) && (z`mod`w==0) = x+z
                             | (x`mod`w/=0) && (y`mod`w/=0) && (z`mod`w==0) = z
                             | (x`mod`w/=0) && (y`mod`w==0) && (z`mod`w/=0) = y
                             | (x`mod`w==0) && (y`mod`w/=0) && (z`mod`w/=0) = x
                            
sumarSoloMultiplos1 :: (Int, Int, Int) -> Int -> Int --hat gpt mode
sumarSoloMultiplos1 (x, y, z) w = sum [n | n <- [x, y, z], n `mod` w == 0]

--main :: IO ()
--main = do
--    let resultado1 = sumarSoloMultiplos1 (10, -8, -5) 2
--    let resultado2 = sumarSoloMultiplos1 (66, 21, 4) 5
--    let resultado3 = sumarSoloMultiplos1 (-30, 2, 12) 3
--    putStrLn ("Resultado 1: " ++ show resultado1)
--    putStrLn ("Resultado 2: " ++ show resultado2)
--    putStrLn ("Resultado 3: " ++ show resultado3)
