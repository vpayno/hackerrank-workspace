package main

import (
	"bytes"
	"io"
	"os"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestHelloWorld(t *testing.T) {
	testStdout, writer, err := os.Pipe()
	if err != nil {
		t.Errorf("os.Pipe() err %v; want %v", err, nil)
	}

	osStdout := os.Stdout // keep backup of the real stdout
	os.Stdout = writer

	defer func() {
		// Undo what we changed when this test is done.
		os.Stdout = osStdout
	}()

	// The stdout we're looking for.
	input := "Welcome to 30 Days of Code!"
	want := "Hello, World.\n" + input + "\n"

	// Write to stdin.
	var stdin bytes.Buffer
	b := []byte(input)
	b = append(b, '\n')
	inSize, inErr := stdin.Write(b)

	// Run the function who's output we want to capture.
	osStdin = &stdin
	main()

	// Stop capturing stdout.
	writer.Close()

	var buf bytes.Buffer
	_, err = io.Copy(&buf, testStdout)
	if err != nil {
		t.Error(err)
	}
	got := buf.String()
	if got != want {
		t.Errorf("main(); want %q, got %q", want, got)
	}

	assert.NoError(t, inErr) // stdin.Write() always returns nil for error. It panics when it encounters an error.
	assert.Equal(t, len(input+"\n"), inSize)
	assert.Equal(t, want, got)

}

func TestPromptUser(t *testing.T) {
	input := "Welcome to 30 Days of Code!"
	want := input

	// Write to stdin.
	var stdin bytes.Buffer
	b := []byte(input)
	b = append(b, '\n')
	inSize, inErr := stdin.Write(b)

	// Run the function that reads user input.
	got := PromptUser(&stdin)

	assert.NoError(t, inErr) // stdin.Write() always returns nil for error. It panics when it encounters an error.
	assert.Equal(t, len(input)+1, inSize)
	assert.Equal(t, want, got)
}
