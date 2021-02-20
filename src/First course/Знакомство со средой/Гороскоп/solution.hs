main = do
    name <- getLine
    surname <- getLine
    animal <- getLine
    sign <- getLine

    putStrLn $ "Индивидуальный гороскоп для пользователя " ++ name ++ " " ++ surname
    putStrLn $ "Кем вы были в прошлой жизни: " ++ animal
    putStrLn $ "Ваш знак зодиака - " ++ sign ++ " , " ++ "поэтому вы - тонко чувствующая натура."