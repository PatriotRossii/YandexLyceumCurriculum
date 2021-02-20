fn main() {
    println!("Каково у вас настроение?")
    let mut answer = String::new();
    std::io::stdin().read_line(&mut answer).expect("Failed to read a line");

    let good_words = ["хорошо", "прекрасно", "чудесно"];
    let bad_words = ["плохо", "ужасно"];
    let redirect_words = ["?", "не"];

    let neutral_answer = "Извините меня, пожалуйста, глупую железяку, я вас не понимаю";

    println!("{}",
        if redirect_words.iter().filter(|&x| answer.find(x).is_some()).count() != 0 { neutral_answer }
        else if good_words.iter().filter(|&x| answer.find(x).is_some()).count() != 0 { "Отлично, у меня тоже все хорошо :)" }
        else if bad_words.iter().filter(|&x| answer.find(x).is_some()).count() != 0 { "Ничего, скоро все наладится" } 
        else { neutral_answer }
    )
}