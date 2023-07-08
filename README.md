# q-and-a
I wrote this script so that I can make flashcards of things said in class.

First the script asks which class I'm in, then which week it is.
It creates the directories if they don't yet exist.

Then I can start typing the questions and providing the answers.

When I input "STOP" the question-answer pairs get written to a tsv-file, which I can use to make flashcards in Anki.

The questions and answers only get written to the file if they are not already in the file.

If you'd like to use this script, you can edit the variable "prefix" with the path of your desired directory.