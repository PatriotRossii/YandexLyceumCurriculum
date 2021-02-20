using System;
namespace Solution {
	class Program {
		static void Main() {
			String name = Console.ReadLine();
			String surname = Console.ReadLine();
			String favoriteAnimal = Console.ReadLine();
			String sign = Console.ReadLine();

			Console.WriteLine(String.Format("Индивидуальный гороскоп для пользователя {0} {1}", name, surname));
			Console.WriteLine(String.Format("Кем вы были в прошлой жизни: {0}", favoriteAnimal));
			Console.WriteLine(String.Format("Ваш знак зодиака - {0} , поэтому вы - тонко чувствующая натура.", sign));
		}
	}
}