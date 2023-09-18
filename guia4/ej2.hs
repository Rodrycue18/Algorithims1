maximo :: Int -> Int -> Int -> Int
maximo x y z | x>=y && x>=z = x
             | y>=x && y>=z= y
             | otherwise = z
