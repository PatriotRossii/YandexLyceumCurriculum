fn main() {
    let stdin = std::io::stdin();

    let mut title = String::new();
    let mut cinema = String::new();
    let mut time = String::new();

    stdin.read_line(&mut title).expect("Failed to read a line");
    stdin.read_line(&mut cinema).expect("Failed to read a line");
    stdin.read_line(&mut time).expect("Failed to read a line");

    println!(r#"Билет на " {} " в " {} " на {} забронирован."#, title.trim(), cinema.trim(), time.trim());
}
