'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    
    count = 0
    if len(word) <= 1:
        return count
    elif word[0] + word[1] == 'th':
        count = count_th(word[1:]) + 1
    else:
        count = count_th(word[1:])
    print(count)
    return count

count_th('thooth')
