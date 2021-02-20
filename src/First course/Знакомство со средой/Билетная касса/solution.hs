main = do
    title <- getLine
    cinema <- getLine
    time <- getLine
    putStrLn $ "Билет на \" " ++ title ++ " \" в \" " ++ cinema ++ " \" на " ++ time ++ " забронирован."