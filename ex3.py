import re

def wordset(fname):
    """Returns the set of words corresponding to the given file"""
    # Create regexp for character filtering
    regex = re.compile('[^a-zA-Z ]')
    # Create wordset
    wordlist = []
    wordset = set()
    # open file
    file = open(fname, "r").read()
    # filter the file for alphanumeric characters and strip punctuation
    #file = regex.sub('', file)
    file = re.sub(r'[^\w\s]', '', file)
    # lowercase all words in the string and split words by spaces
    file = file.lower()
    wordlist = file.split()
    # iterate through the list of words in the wordlist, to add unique words to the wordset
    for word in wordlist:
        if word not in wordset:
            wordset.add(word)
    #print(wordset)
    return wordset

def jaccard(fname1, fname2):
    """Calculate Jaccard index"""
    # Your code here - call wordset()
    file1set = wordset(fname1)
    file2set = wordset(fname2)

    intersec = file1set.intersection(file2set)
    union = file1set.union(file2set)

    jindex = len(intersec)/len(union)
    print(jindex)
    return jindex


#wordset("/home/ben/Artifical_Intelligence/Homework_1/alice_ascii.txt")

jaccard("/home/ben/Artifical_Intelligence/Homework_1/alice_ascii.txt", "/home/ben/Artifical_Intelligence/Homework_1/alice_ascii.txt")
jaccard("/home/ben/Artifical_Intelligence/Homework_1/alice_ascii.txt", "/home/ben/Artifical_Intelligence/Homework_1/looking_glass_ascii.txt")