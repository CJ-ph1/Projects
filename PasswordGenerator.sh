#!/bin/bash

printf "\nWelcome to password Generator\n"

read -p "Please enter the length of the password: " pass

if ! [[ $pass =~ ^[0-9]+$ ]]; then
	echo "Error: Please enter a valid number."
	exit 1
fi

passwords=()

for p in $(seq 1 3); do
	password=$(openssl rand -base64 48 | tr -dc "a-zA-Z0-9" | head -c "$pass")
	passwords+=("$password")
done

printf "\n"
echo "Here are the generated passwords: " "%s\n" "${passwords[@]}"

read -p "Do you want to save these passwords to a file? (y/n): " choice

if [ "$choice" = "y" ]; then
	
	read -sp "Enter a passphrase for encryption: " PASSPHRASE
	echo
	
	> passwords.txt

	for password in "${passwords[@]}"; do
		echo "$password" >> passwords.txt
	done

	echo "$PASSPHRASE" | gpg --batch --yes --passphrase-fd 0 -c passwords.txt
	rm passwords.txt
	echo "Passwords saved securely to passwords.txt.gpg"

elif [ "$choice" = "n" ]; then
	echo "Passwords not saved."
fi

