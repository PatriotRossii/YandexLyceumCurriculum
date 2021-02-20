using System;
namespace Solution {
	class Program {
		static void Main() {
			Console.WriteLine("1 бит - минимальная единица количества информации.");
			Console.WriteLine("1 байт = 8 бит.");
			Console.WriteLine("1 Килобайт = 1024 байта.");
			Console.WriteLine(String.Format("1 Килобайт = {0} бит.", 8 * 1024));
		}
	}
}