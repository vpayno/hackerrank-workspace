//
// test/cli.rs
//

extern crate assert_cli;

// use std::process::Command;  // Run programs
// use assert_cmd::prelude::*; // Add methods on commands
// use predicates::prelude::*; // Used for writing assertions

#[cfg(test)]
#[cfg(not(tarpaulin))]
mod integration {
    use assert_cli;

    #[test]
    fn test_challenge() {
        assert_cli::Assert::main_binary()
            .succeeds()
            .stdin("Welcome to 30 Days of Code!")
            .stdout()
            .is("Hello, World.\nWelcome to 30 Days of Code!\n")
            .unwrap();
    } // test_challenge()
} // mod integration
