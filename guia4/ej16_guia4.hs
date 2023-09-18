--A)
menorDivisor :: Int ->Int
menorDivisor n = divisor(n) (2)

divisor :: Int->Int->Int
divisor n d | mod n d == 0 = d
            | (n==d) && (mod n d==0) = d --primos --Creo que no es necesaria este caso, ya que cuando es primo d suma hasta que se haga n 
            | otherwise = divisor(n) (d+1)

--B)

esPrimo :: Int -> Bool
esPrimo n | (n == (divisor (n) (2))) = True
          | otherwise = False

rt