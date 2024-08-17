# Markov Bigram Text Generator
This text generator uses the Markov bigram method which means that it can only calculate the frequencies for one word ahead and generate text based of one previous word. It hasn't been given much text to train, however, so it has a limited sentence generation scope.

# Files
## frequencies.json
frequencies.json contain the frequencies for each word that appears after each word of the text passed into train_data.txt

## main.py
main.py contains a very simple Flask API to get a list of generated words of whatever length is passed into the API url.

## /History
The history folder stores past versions of the frequencies.json file in case any progress in training the generator is lost.

# Usage
To use this generator, run <code>flask -app main run</code>. 
![Screenshot 2024-08-17 at 6 06 49 PM](https://github.com/user-attachments/assets/9cfa8926-324d-47bc-9ebb-399047955d0e)
This is will run the simple Flask API from which words can be generated by querying the /word-generation-api/<number> endpoint, where number is the amount of words to be generated in the sentence. Be aware that there may be repetitions in these words depending on how much the generator has been trained, i.e. how many different texts **train.py** has been run with.

![Screenshot 2024-08-17 at 6 12 38 PM](https://github.com/user-attachments/assets/6d085a92-c091-4194-afae-729a58ac2112)

The above response is what will be returned as JSON once the endpoint is called.
