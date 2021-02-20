import Data.List
answer line
    | any (== True) $ map (flip isInfixOf line) redirect_words = neutral_answer
    | any (== True) $ map (flip isInfixOf line) good_words = "Отлично, у меня тоже всё хорошо :)"
    | any (== True) $ map (flip isInfixOf line) bad_words = "Ничего, скоро все наладится"
    | otherwise = neutral_answer
    where
        good_words = ["хорошо", "прекрасно", "чудесно"]
        bad_words = ["плохо", "ужасно"]
        redirect_words = ["?", "не"]
        neutral_answer = "Извините, я вас не понимаю"

main = do
    line <- getLine
    putStrLn "Как ваше настроение?"
    putStrLn (answer line)