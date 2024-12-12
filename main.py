def countWords(fileContent):
    return len(fileContent.split())

def countLetters(fileContent):
    count = {}
    for c in fileContent:
        lower = c.lower()
        if lower in count:
            count[lower] += 1
        else:
            count[lower] = 1
    return count

def main():
    with open("books/frankenstein.txt") as f:
        fileContent = f.read()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{countWords(fileContent)} words found in the document")
    sortedDict = sorted(countLetters(fileContent).items(), key=lambda x:x[1])
    for c in sortedDict:
        if c.isalpha():
            print(f"The {c} character was found {sortedDict[c]} times")
    print("--- End report ---")

main()