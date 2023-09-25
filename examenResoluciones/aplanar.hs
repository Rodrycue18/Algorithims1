aplanar :: [(String, String)] -> [String]
aplanar [] = []
aplanar ((p,vp):xs) = p : vp : aplanar xs