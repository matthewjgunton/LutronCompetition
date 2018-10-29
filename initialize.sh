#!/bin/bash

#DO NOT MODIFY THIS SCRIPT.
#Modifying this script will incorrectly initialize your project competition repo.

echo "Welcome to the Lutron Coding Competition!"

echo "This script is intended to get you started with the coding competiton - if you are already coding, please do not run this script again."

read -p "Please enter your first and last name with NO SPACES (eg, JohnSmith): " name

branchName="lurton-coding-comp-2018-$name"

echo "Creating and checking out branch $branchName"

git branch $branchName

if [ $? -ne 0 ]; then 
	echo "There was an error in making branch $branchName - are you running this script again?"
	exit 2
fi

git checkout $branchName

if [ $? -ne 0 ]; then 
	echo "There was an error in checking out branch $branchName - do you have the right permissions?"
	exit 2
fi


chmod 777 ./submission.sh
