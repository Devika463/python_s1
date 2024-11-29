sentence = input("Enter a sentence: ")
words=sentence.split()
count=len(words)
print(f"Number of words={count}")
search=input("Enter the word to be searched:")
if search in words:
    print(f"'{search}' is found in the sentence")
else:
     print(f"'{search}' is not found in the sentence")
