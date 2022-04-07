# lotto picker by manny juan  (juanm@wellsfargo.com or manny@bdt.com)
from random import randint


def get_number():
    return int(randint(1, 69))


def get_power():
    return int(randint(1, 26))


def pick_lotto():
    regular = []
    ticket = []
    for i in range(0, 5):
        number = get_number()
        while regular.count(number) > 0:
            number = get_number()
        regular.append(number)
        regular.sort()
    ticket.append(get_power())
    return tuple(regular + ticket)


def run():
    done = 0
    while not done:
        try:
            x = input('\npress Enter for Lotto picks (Q to quit). ')
        except EOFError:
            x = 'q'
        if x and (x[0] == 'q' or x[0] == 'Q'):
            done = 1
            print('done')
        else:
            print(pick_lotto())


# immediate-mode commands, for drag-and-drop or execfile() execution
if __name__ == '__main__':
    run()
else:
    print("Module lotto imported.")
    print("To run, type: lotto.run()")
    print("To reload after changes to the source, type: reload(lotto)")
# end of lotto.py
