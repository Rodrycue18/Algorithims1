relacionesValidas :: [(String,String)] -> Bool
relacionesValidas [] = True
--relacionesValidas (x:[]) = []
--relacionesValidas [x] = x
relacionesValidas (x:xs)  | (fst(x) == snd(x)) && relacionesValidas(xs) = False
                          | otherwise = True
-- | ((x == y) && ((snd(y),fst(y))== x)) && relacionesValidas(xs) = False

--relacionesValidas(x:y:xs) | (fst(x)==snd(y) && snd(x)==fst(y)) && relacionesValidas(xs) = False
--                          | otherwise = relacionesValidas(xs)

--relacionesValidas (x:y:xs)| (fst(x) == snd(x)) || (fst(y)==snd(y)) = False
--                          | otherwise = True
verificarTuplas :: (String,String) -> [(String,String)] -> Bool
verificarTuplas x [] = True
verificarTuplas x (xs) | (fst(x) == snd(x)) && relacionesValidas(xs) = False
                       | ((fst(x)==snd(verificarTuplas(xs))) && (snd(x) == fst(verificarTuplas(xs)))) && verificarTuplas(xs) = False
                       | otherwise = True
                        
-- | ((x==y) && (reverse(y)==x)) || relacionesValidas(xs) = False
 elem