import os

qna = {}
#ask which class I am in and which week (of this class) it is
current_class = input("Which class are you in right now?: ")
week = input("Which week or topic is this?: ")
prefix = f".\\TI 2023-2024\\{current_class}"

#check whether directory for class already exists
#if not then create it
if not os.path.exists(prefix):
    os.mkdir(prefix)
#check if directory for this week exists, if not then create it
if not os.path.exists(prefix+f"\\{week}"):
    os.mkdir(prefix+f"\\{week}")
while True:
    q = input("Please give a question: ")
    #to stop the script
    if q == "STOP":
        break
    a = input("Please give the answer: ")
    #look if the question is already present in the dictionary
    # if it is it will print out a message saying so
    try:
        qna[q]
        print("This question is already in the deck")
    except KeyError:
        qna[q] = a

#create the tsv-file if it doesn't yet exist

if not os.path.exists(f"{prefix}\\{week}\\Q&A.tsv"):
    open(f"{prefix}\\{week}\\Q&A.tsv").close()

#add question-answer pairs to tsv file (flashcard for Anki)
with open(f"{prefix}\\{week}\\Q&A.tsv", 'r+', encoding='utf-8') as flashcard:
    #take the contents of the textfile
    flash = flashcard.readlines()
    # loop over all the question-answer pairs and only add them if they are not already in the flashcard file
    for i, j in qna.items():
        if f"{i}:{j}\n" not in flash:
            flashcard.write(f"{i}:{j}\n")