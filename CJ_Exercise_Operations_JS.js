#!/usr/bin/env node

const readline = require('readline');

const input = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

function getNumber(prompt, callback) {
	input.question(prompt, (value) => {
		const number = parseFloat(value);
		if (isNaN(number)) {
			console.log("Try again.");
			getNumber(prompt, callback);
		} else {
			callback(number);
		}
	});
}

function calculate() {
	showChoices();
	input.question("Enter your choice (1-5): ", (choice) => {
		const operation = parseInt(choice);

		if (operation === 5){
			input.close();
			return;
		}
		
		if (operation < 1 || operation > 4) {
			console.log("Try Again");
			return calculate();
		}

		const operations = {
			1: (a, b) => a + b,
			2: (a, b) => a - b,
			3: (a, b) => a / b, 
			4: (a, b) => a * b
		};

		getNumber("Enter first number: ", (num1) => {
			getNumber("Enter second number: ", (num2) => {
				if (operation === 3 && num2 === 0) {
					console.log("Error: Division by zero!");
				} else {
					const result = operations[operation](num1, num2);
					console.log(`Result: ${result}`);
				}

				calculate();
			});
		});
	});
}

function showChoices() {
	console.log("============");
	console.log("1.Add");
	console.log("2.Subtract");
	console.log("3.Divide");
	console.log("4.Multiply");
	console.log("5.Exit");
	console.log("============");
}

calculate();
