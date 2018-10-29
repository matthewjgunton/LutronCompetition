#!/bin/bash

#DO NOT MODIFY THIS SCRIPT.
#The grading server logs all information on each game - if any of your information is unexpected, you will earn 0 points on your submission.

echo Welcome to the Lutron Programming Competition!

echo "Did you update your user ID to have \"-SUBMISSION\" appended to it?"

read -p "Type Y or y for yes and anything else for no: " updatedID

if [ "$updatedID" == "y" ] || [ "$updatedID" == "Y" ]; then
	date=$(date '+%Y-%m-%d %H:%M:%S');
	echo "Submitting your solution..."
	git add .
	git commit -a -m "Programming competition submission $date"
	git push
	if [ $? -ne 0 ]; then 
		echo "Git push failed. Did you enter the right credentials? Are you still on master branch?"
		exit 2
	fi
	echo "Submission complete. Grading solution now - output will be stored in submissionOutput.txt"
	echo "Grading easy."
	echo "---EASY SOLUTION---" > submissionOutput.txt	
	python3 main.py easy >> submissionOutput.txt
	if [ $? -ne 0 ]; then 
		echo "There was an error in grading your easy solution. Check submissionOutput.txt"
		exit 3
	fi
	echo "Grading medium."
	echo "---MEDIUM SOLUTION---" >> submissionOutput.txt	
	python3 main.py medium >> submissionOutput.txt
	if [ $? -ne 0 ]; then 
		echo "There was an error in grading your medium solution. Check submissionOutput.txt"
		exit 3
	fi
	echo "Grading hard."
	echo "---HARD SOLUTION---" >> submissionOutput.txt	
	python3 main.py hard >> submissionOutput.txt
	if [ $? -ne 0 ]; then 
		echo "There was an error in grading your hard solution. Check submissionOutput.txt"
		exit 3
	fi
	echo "Grading complete!"
else
	echo "Please update your ID and then run this script again."
fi


