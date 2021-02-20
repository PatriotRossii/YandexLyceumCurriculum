using System;
namespace Solution {
	class Program {
		static void Main() {
			String title = Console.ReadLine();
			String cinema = Console.ReadLine();
			String time = Console.ReadLine();

			Console.WriteLine($"Билет на \" {title} \" в \" {cinema} \" на {time} забронирован.");
		}
	}
}