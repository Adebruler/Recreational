# Code to solve explosion problem on Brilliant.org
# https://brilliant.org/daily-problems/exploding-dots/

input = [0,0,0,0,31]

def explode(input):
    boxes = len(input)
    newboxes = [input[i] for i in range(boxes)]
    if check_complete(input):
        return input
    else:
        for i in range(boxes):
            if input[i] > 1:
                if i > 0:
                    newboxes[i-1] +=1
                newboxes[i] -= 2
        return explode(newboxes)

def check_complete(input):
    is_complete = True
    for box in input:
        if box > 1:
            is_complete = False
    return is_complete

print(explode(input));

# Observations:
# I originally read the problem as the dots appearing in both the left and right newboxes
# For only left boxes, this very quickly becomes a binary expression
# That is, for cases where dots are only in the right box
