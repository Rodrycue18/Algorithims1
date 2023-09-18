sumaDistintos :: Int -> Int -> Int ->Int
sumaDistintos x y z | (x/=y) && (x/=z) && (y/=z) = x+y+z --cuando son los 3 distintos
                    | x==y && x==z && y==x && y==z && z==x && z==y = 0
                    | x==y = x+y 
                    | x==z = x+z
                    | y==x = x+y 
                    | y==z = y+z
                    | z==x = z+x 
                    | z==y = z+y
                    