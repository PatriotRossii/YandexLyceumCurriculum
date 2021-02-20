use std::io::Read;

fn main() {
    let mut stdin = std::io::stdin();
    
    let mut string1 = String::new();
    let mut string2 = String::new();
    let mut string3 = String::new();

    stdin.read_line(&mut string1).expect("Failed to read a line");
    stdin.read_line(&mut string2).expect("Failed to read a line");
    stdin.read_line(&mut string3).expect("Failed to read a line");

    println!("{}", string1.trim());
    println!("{}", string2.trim());
    println!("{}", string3.trim());
}
