using System;
using System.Linq;
namespace Solution {
	class Program {
		static void Main() {
			String[] good_words = {"хорошо", "прекрасно", "чудесно"};
			String[] bad_words = {"плохо", "ужасно"};
			String[] redirect_words = {"?", "не"};

			String neutral_answer = "Извините меня, пожалуйста, глупую железяку, я вас не понимаю";

			Console.WriteLine("Каково у вас настроение?");
			String answer = Console.ReadLine();

			if (redirect_words.Where(x => answer.Contains(x)).Any()) {
				Console.WriteLine(neutral_answer);
			} else if(good_words.Where(x => answer.Contains(x)).Any()) {
				Console.WriteLine("Отлично, у меня все тоже хорошо :)");
			} else if(bad_words.Where(x => answer.Contains(x)).Any()) {
				Console.WriteLine("Ничего, скоро все наладится");
			} else {
				Console.WriteLine(neutral_answer);
			}
		}
	}
}