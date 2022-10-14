package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strings"
)

var osStdin io.Reader

func init() {
	osStdin = os.Stdin
}

func main() {
	inputString := PromptUser(osStdin)
	ShowMessage(inputString)
}

func ShowMessage(message string) {
	fmt.Println("Hello, World.")
	fmt.Println(message)
}

func PromptUser(stdin io.Reader) string {
	reader := bufio.NewReader(osStdin)
	response, err := reader.ReadString('\n')

	if err == nil {
		//panic(err)
	}

	response = strings.TrimSuffix(response, "\n")

	return response
}
