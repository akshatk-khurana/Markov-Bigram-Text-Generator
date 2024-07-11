# Markov Bigram Text Generator
A text generator that uses the simplified Markov bigram method.

This text generator uses the Markov bigram method which means that it can only calculate the frequencies for one word ahead and generate text based of one previous word. 

# frequencies.json
frequencies.json contain the frequencies for each word that appears after each word of the text passed into train_data.txt

NOTE: I am currently just training the program on George Orwell's 1984

# main.py
main.py contains a very simple Flask API to get a list of generated words of whatever length is passed into the API url.

# History
The history folder stores past versions of the frequencies.json file in case any progress in training the generator is lost.