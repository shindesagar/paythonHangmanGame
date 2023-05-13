# paythonHangmanGame
The first few lines of code import the random module, create a list of words, and randomly select one word from the list.
The next few lines of code create a variable called guessWord and initialize it to an empty string. They also create a list called blankSpaceIndex and initialize it to an empty list.
The next line of code prints a message asking the user to start guessing the word.
The next few lines of code iterate through the letters of the randomly selected word. For each letter, they check if the letter is a vowel. If the letter is a vowel, they print the letter to the console. If the letter is not a vowel, they print a "_" to the console and add the index of the letter to the blankSpaceIndex list.
The next line of code prints a blank line to the console.
The next few lines of code iterate through the blankSpaceIndex list. For each index in the list, they ask the user to guess a letter. They then check if the user's guess is correct. If the user's guess is correct, they update the guessWord variable to include the correct letter. They also print a message saying that the guess was correct. If the user's guess is incorrect, they print a message saying that the guess was incorrect and decrement the tries variable.
The next line of code checks if the tries variable is equal to 0. If the tries variable is equal to 0, the code prints a message saying that the user has lost the game.
I hope this explanation is helpful. Let me know if you have any other questions.