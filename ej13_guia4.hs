import Test.HUnit

sumGrande :: Float -> Float ->Float
sumGrande p q | p == 0 = 0
               | otherwise = sumPeq (p) (q) + sumGrande (p-1) (q)

sumPeq :: Float -> Float ->Float
sumPeq p q | q == 1 = p
           | otherwise = p/q + sumPeq (p) (q-1)

testSuiteSumaGrande = test [
    "test1" ~:(sumGrande 2 1) ~?=3,
    "casobase" ~:(sumGrande 1 1) ~?=1
 ]

correrTests = runTestTT testSuiteSumaGrande