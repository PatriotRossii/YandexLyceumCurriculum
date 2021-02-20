fn main() {
    let stdin = std::io::stdin();
    
    let mut name = String::new();
    let mut surname = String::new();
    let mut animal = String::new();
    let mut sign = String::new();

    stdin.read_line(&mut name).expect("Failed to read a line");
    stdin.read_line(&mut surname).expect("Failed to read a line");
    stdin.read_line(&mut animal).expect("Failed to read a line");
    stdin.read_line(&mut sign).expect("Failed to read a line");

    println!("Индивидуальный гороскоп для пользователя {} {}", name.trim(), surname.trim());
    println!("Кем вы были в прошлой жизни: {}", animal.trim());
    println!("Ваш знак зодиака - {} , поэтому вы - тонко чувствующая натура.", sign.trim());
}
