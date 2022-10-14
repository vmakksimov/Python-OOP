from collections import deque

def check_who(f_all, m_all, female, male):
    if 0 >= female:
        f_all.popleft()
    if 0 >= male:
        m_all.pop()

    return f_all, m_all


def check(female, male):
    if 0 >= female or 0 >= male:
        return False
    return True


males = [int(el) for el in input().split()]
females = deque([int(el) for el in input().split()])

matches = 0
while True:
    if len(males) <= 0:
        break
    if len(females) <= 0:
        break

    current_male = males[-1]
    current_female = females[0]

    if check(current_female, current_male):
        if current_female % 25 == 0:
            females.popleft()
            females.popleft()
            continue

        elif current_male % 25 == 0:
            males.pop()
            males.pop()
            continue

        if current_female == current_male:
            matches += 1
            females.popleft()
            males.pop()

        elif current_female != current_male:
            females.popleft()
            males[-1] -= 2
            if 0 >= males[-1]:
                males.pop()

    else:
        females, males = check_who(females, males, current_female, current_male)


print(f'Matches: {matches}')
if 0 >= len(males):
    print("Males left: none")
elif len(males) > 0:
    result = list(map(str, males))
    print(f'Males left: {", ".join(reversed(result))}')

if 0 >= len(females):
    print("Females left: none")
elif len(females) > 0:
    print(f'Females left: {", ".join((map(str, females)))}')


