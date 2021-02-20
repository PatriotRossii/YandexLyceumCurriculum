good_words = ["хорошо", "прекрасно", "чудесно"]
bad_words = ["плохо", "ужасно"] 
redirect_words = ["?", "не"]

neutral_answer = "Извините меня, пожалуйста, глупую железяку, я вас не понимаю"

print("Каково у вас настроение?")
userInput = input()

if any(word in userInput for word in redirect_words):
    print(neutral_answer)
elif any(word in userInput for word in good_words):
    print("Отлично, у меня тоже все хорошо :)")
elif any(word in userInput for word in bad_words):
    print("Ничего, скоро все наладится")
else:
    print(neutral_answer)