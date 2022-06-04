#!/bin/bash

shopt -s nullglob

declare EXE="../src/challenge/main"

declare -a INPUTS
declare INPUT

declare expected_sum
declare expected_out
declare captured_sum
declare captured_out
declare test_name
declare -i passed=0
declare -i failed=0

main()
{
	INPUTS=( ../../resources/test*input.txt )

	printf "Running tests (%d)\n" "${#INPUTS[@]}"
	printf "\n"

	for INPUT in "${INPUTS[@]}"; do
		expected_out="${INPUT//input/output}"

		expected_sum="$(sha512sum "${expected_out}" | awk '{ print $1 }')"
		captured_out="$("${EXE}" < "${INPUT}")"
		captured_sum="$(echo "${captured_out}" | sha512sum | awk '{ print $1 }')"

		test_name="${INPUT%-*}"
		test_name="${test_name##*/}"

		printf "[%s]: " "${test_name}"

		if [[ "${expected_sum}" == "${captured_sum}" ]]; then
			(( passed++ ))

			printf "pass\n"
		else
			(( failed++ ))

			printf "fail\n"
			printf "\n"
			printf "\tExpected:\n"
			awk '{printf "\t\t%s\n", $0}' < "${expected_out}"
			printf "\n"
			printf "\tGot:\n"
			echo "${captured_out}" | awk '{printf "\t\t%s\n", $0}'
		fi
		printf "\n"
	done

	printf "Passed Tests: %d\n" "${passed}"
	printf "Failed Tests: %d\n" "${failed}"
} # main()

time main "$@" | tee ../run-tests-integration.txt
