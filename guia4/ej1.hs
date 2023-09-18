f :: Int -> Int
f 1=8
f 4=131
f 16=16

f2 :: Int -> Int
f2 x  | x == 1 = 8
      | x == 4 = 131              
      | x == 16 = 16

    
g :: Int -> Int
g x   | x == 8 = 16
      | x == 16 = 4              
      | x == 131 = 1


h :: Int -> Int
h x = f2(g(x))

k :: Int -> Int
k x = g(f2(x))
