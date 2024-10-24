#!python3
"""
String handling is important.  We can break a string into pieces to help us look at parts one at a time using the string.split function.
Have the user enter a sentence or paragraph and gives a word count.
"""
#input: sentance or paragraph
#output: word count

def wordCounter(sentance):
    modSentance = str(sentance)
    words = modSentance.split(' ')
    wordCount = len(words)
    print(wordCount)

    return wordCount

def main():
    paragraph = input("Enter a sentence or paragraph:")
    numberWords = wordCounter(paragraph)
    print(f"There are {numberWords} words.")

if __name__ == '__main__':
    main()