def countWords(fileContent):
    return len(fileContent.split())

def countLetters(fileContent):
    count = {}
    for c in fileContent:
        if c.isalpha():
            lower = c.lower()
            if lower in count:
                count[lower] += 1
            else:
                count[lower] = 1
    return count

def sortList(d):
    return d["num"]

def main():
    with open("books/frankenstein.txt") as f:
        fileContent = f.read()
    numberOfWords = countWords(fileContent)
    numberOfLetters = countLetters(fileContent)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{numberOfWords} words found in the document")
    sortedList = []
    for c in numberOfLetters:
        sortedList.append({"char" : c, "num" : numberOfLetters[c]})
    sortedList.sort(reverse=True, key=sortList)
    for w in sortedList:
        print(f"The {w['char']} character was found {w['num']} times")

main()