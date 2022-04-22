use std::io;

fn get_user_input() -> String {
    let mut buffer: String = String::new();

    let stdin = io::stdin();

    stdin.read_line(&mut buffer).ok();

    return buffer;
}

fn print_user_message(message: String) {
    // Don't print an extra new line since the new line the input has one.
    print!("{message}", message = message);
}

fn print_hello_world() {
    let mut message: String = String::new();

    message.push_str("Hello, World.");

    println!("{greeting}", greeting = message);
}

fn main() {
    let message = get_user_input();

    print_hello_world();
    print_user_message(message);
}
