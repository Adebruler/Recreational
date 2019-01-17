def answer(count):
    soldiers=[i+1 for i in range(count)]
    alive=kill(soldiers)
    return alive

def kill(soldiers):
    count=len(soldiers)
    if (count==1 or count==2):
        alive = soldiers[0]
    else:
        newsoldiers=soldiers[2:count]
        newsoldiers.append(soldiers[0])
        alive = kill(newsoldiers)
    return alive

for count in range(1,512,1):
    # count=3
    soln=answer(count)
    print(f"In:{count} | Survivor:{soln}")
