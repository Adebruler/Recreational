def pluralize(count):
    if count == 1:
        return ''
    else:
        return 's'

wall_size = 99
on_the_wall = [i+1 for i in range (99)]
passed_around = []
bottles = len(on_the_wall)

while bottles > 0:
    s = pluralize(bottles)
    print(f'{bottles} bottle{s} of beer on the wall!')
    print(f'{bottles} bottle{s} of beer!')

    print("Take one down!")
    one_down = on_the_wall.pop()
    print("Pass it around!")
    passed_around.append(one_down)

    bottles = len(on_the_wall)
    s = pluralize(bottles)
    print(f'{bottles} bottle{s} of beer on the wall!\n')
