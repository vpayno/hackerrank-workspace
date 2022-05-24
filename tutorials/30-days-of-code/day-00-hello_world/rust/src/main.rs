use std::io::{self, BufRead, Write};

fn user_input<R, W>(mut reader: R, mut writer: W, question: &str) -> String
where
    R: BufRead,
    W: Write,
{
    write!(&mut writer, "{}", question).expect("Unable to write");

    let mut response = String::new();
    reader.read_line(&mut response).expect("Unable to read");

    response
} // user_input()

fn user_output<W>(mut writer: W, message: &str)
where
    W: Write,
{
    write!(&mut writer, "{}", message).expect("Unable to write");
} // user_output()

#[cfg(not(tarpaulin_include))]
fn main() {
    let stdio = io::stdin();
    let input = stdio.lock();

    let mut output = io::stdout();

    let banner: String = "Hello, World.\n".to_string();
    let message: String = user_input(input, &mut output, "");

    user_output(&mut output, &banner[..]);
    user_output(&mut output, &message[..]);
} // main()

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_user_input() {
        let input = b"Testing user input with dependency injection.";

        let mut output = Vec::new();

        let answer = user_input(&input[..], &mut output, "Enter message:");

        let output = String::from_utf8(output).expect("Not UTF-8");

        assert_eq!("Enter message:", output);
        assert_eq!("Testing user input with dependency injection.", answer);
    } // test_user_input()

    #[test]
    fn test_user_output() {
        let expected = "Testing user ouput with dependency injection.";

        let mut output = Vec::new();

        user_output(&mut output, &expected[..]);

        let output = String::from_utf8(output).expect("Not UTF-8");

        assert_eq!(expected, output);
    } // test_user_output()
} // mod tests

//  src/main.rs: 12, 22-24, 26, 28-29, 31-33
