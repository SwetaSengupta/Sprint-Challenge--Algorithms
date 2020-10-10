'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    if len(word) < 2: # Base Case
        return 0

    elif word[0:2] == 'th': # Add to the count and recurse for an instance of th
        return 1 + count_th(word[1:])

    else: # Recurse and move forward  
        return count_th(word[1:])


if __name__ == '__main__':
    word = 'fifth'
    print(count_th(word))
    word2 = 'ththth'
    print(count_th(word2))
    word3 = "FifTH"
    print(count_th(word3))
