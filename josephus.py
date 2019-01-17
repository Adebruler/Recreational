# Code for iteratively simulating the Josephus (mutual suicide) problem
# https://en.wikipedia.org/wiki/Josephus_problem

max_soldiers = 512;

def answer(count):
    # create circle of numbered soldiers
    soldiers=[i+1 for i in range(count)]
    alive=kill(soldiers)
    return alive

def kill(soldiers):
    count=len(soldiers)
    if (count==1 or count==2):
        alive = soldiers[0]
    else:
        # kill second soldier by not adding to new list
        newsoldiers=soldiers[2:count]
        # add first soldier to end of rotation
        newsoldiers.append(soldiers[0])
        # iterate
        alive = kill(newsoldiers)
    return alive

for count in range(1,512,1):
    soln=answer(count)
    print(f"In:{count} | Survivor:{soln}")

# Observed results:
# 1) Even-positioned soldiers never survive.
# 2) The position of the survivor generally increases by 2 (sequential odd numbers)
# 3) The position of the survivor resets to 1 when there are 2^n soldiers

# y = 1 + 2 * (x - 2^(round(log(x,2))))
