#!/usr/bin/env node

const readline = require('readline');

const userInput = process.argv[2];

function cardNumber(userInput) {
    if (userInput && userInput.length === 16) {
        cardCalculation(userInput);
    } else {
        console.log("Number is not 16 digits.");
        askForCardNumber();
    }
}

function cardCalculation(userInput) {
    let evenSum = 0;
    let oddSum = 0;

    for (let i = 0; i < userInput.length; i += 2) {
        let number = parseInt(userInput[i], 10);
        let doubleNum = number * 2;

        if (doubleNum >= 10) {
            evenSum += Math.floor(doubleNum / 10) + (doubleNum % 10);
        } else {
            evenSum += doubleNum;
        }
    }

    for (let i = 1; i < userInput.length; i += 2) {
        oddSum += parseInt(userInput[i], 10);
    }

    const total = evenSum + oddSum;
    console.log(`Total sum of all numbers: ${total}`);

    if (total % 10 === 0) {
        console.log("This is a valid Card.");
    } else {
        console.log("This is not a valid Card.");
        askForCardNumber();
    }
}

function askForCardNumber() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question('Please enter a 16-digit card number: ', (input) => {
        rl.close();
        if (input.length === 16) {
            cardCalculation(input);
        } else {
            console.log("Number is not 16 digits.");
            askForCardNumber();
        }
    });
}

if (userInput) {
    cardNumber(userInput);
} else {
    askForCardNumber();
}
