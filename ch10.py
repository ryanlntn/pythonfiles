import string

def myreplace(old, new, s):
    print new.join(s.split(old))


# wordtools


def cleanword(word):
    """
      >>> cleanword('what?')
      'what'
      >>> cleanword('"now!"')
      'now'
      >>> cleanword('?+="word!,@$()"')
      'word'
    """
    return word.strip('?+="!,@$()-.')


def has_dashdash(s):
    """
      >>> has_dashdash('distance--but')
      True
      >>> has_dashdash('several')
      False
      >>> has_dashdash('critters')
      False
      >>> has_dashdash('spoke--fancy')
      True
      >>> has_dashdash('yo-yo')
      False
    """
    if '--' in s:
        return True
    else:
        return False


def extract_words(s):
    """
      >>> extract_words('Now is the time!  "Now", is the time? Yes, now.')
      ['now', 'is', 'the', 'time', 'now', 'is', 'the', 'time', 'yes', 'now']
      >>> extract_words('she tried to curtsey as she spoke--fancy')
      ['she', 'tried', 'to', 'curtsey', 'as', 'she', 'spoke', 'fancy']
    """
    words = s.split()
    temp = []
    extract = []

    for word in words:
        if has_dashdash(word):
            temp += word.split('--')
        else:
            temp.append(word)

    for word in temp:
        extract.append(cleanword(word.lower()))

    return extract


def wordcount(word, wordlist):
    """
      >>> wordcount('now', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
      ['now', 2]
      >>> wordcount('is', ['now', 'is', 'time', 'is', 'now', 'is', 'the', 'is'])
      ['is', 4]
      >>> wordcount('time', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
      ['time', 1]
      >>> wordcount('frog', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
      ['frog', 0]
    """
    return [word, wordlist.count(word)]


def wordset(wordlist):
    """
      >>> wordset(['now', 'is', 'time', 'is', 'now', 'is', 'is'])
      ['is', 'now', 'time']
      >>> wordset(['I', 'a', 'a', 'is', 'a', 'is', 'I', 'am'])
      ['I', 'a', 'am', 'is']
      >>> wordset(['or', 'a', 'am', 'is', 'are', 'be', 'but', 'am'])
      ['a', 'am', 'are', 'be', 'but', 'is', 'or']
    """
    for word in wordlist:
        count = wordcount(word, wordlist)

        if count[1] > 1:
            while count[1] > 1:
                wordlist.remove(word)
                count[1] -= 1

    wordlist.sort()

    return wordlist


def longestword(wordset):
    """
      >>> longestword(['a', 'apple', 'pear', 'grape'])
      5
      >>> longestword(['a', 'am', 'I', 'be'])
      2
      >>> longestword(['this', 'that', 'supercalifragilisticexpialidocious'])
      34
    """
    wordlength = []
    
    for word in wordset:
        wordlength.append(len(word))

    longest = max(wordlength)

    return longest
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
