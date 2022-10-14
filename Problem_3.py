def finish(arg, mark):
    if arg[mark] == 'Finish':
        return True
    return False


def flights(*args):
    destination = {}
    for index in range(len(args)):
        is_finish = finish(args, index)
        if is_finish:
            return destination

        elif index % 2 == 0:
            key = args[index]
            if key in destination:
                destination[key] += args[index +1]
            else:
                value = args[index + 1]
                destination[key] = value

    return destination


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))