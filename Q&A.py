import os

qna = {}
#ask which class I am in and which week (of this class) it is
current_class = input("Which class are you in right now?: ")
week = input("Which week or topic is this?: ")

#check whether directory for class already exists
#if not then create it
if not os.path.exists('.'):
    os.mkdir('.')
#check if directory for this week exists, if not then create it
if not os.path.exists(f".\\{week}"):
    os.mkdir(f".\\{week}")
print("Please don't put colons (:) in the questions or answers. This will cause problems when converting to actual flashcards in Anki. If you do use them, they will be replaced with a dash (-).")
while True:
    q = input("Please give a question: ").replace(':', '-')
    #to stop the script
    if q == "STOP":
        break
    a = input("Please give the answer: ").replace(':', '-')
    #look if the question is already present in the dictionary
    # if it is it will print out a message saying so
    try:
        qna[q]
        print("This question is already in the deck")
    except KeyError:
        qna[q] = a

#create empty set
existing_content = set()

#create the file if it doesn't yet exist
open(f".\\{week}\\Q&A.tsv", 'a+', encoding='utf-8').close()

#add current content of the flashcard in the set (this eliminates duplicates)
with open(f".\\{week}\\Q&A.tsv", 'r', encoding='utf-8') as flashcard:
    existing_content = set(flashcard.readlines())

# open the file in append mode
with open(f".\\{week}\\Q&A.tsv", 'w', encoding='utf-8') as flashcard:
    # add all question-answer pairs to the file
    for i in existing_content:
        flashcard.write(i)
    for i, j in qna.items():
        #this is a double check that we don't accidently add any duplicate questions to the file
        if f"{i}:{j}\n" not in existing_content:
            flashcard.write(f"{i}:{j}\n")
