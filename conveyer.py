import numpy as np
from main import print_picture
from colorama import Fore


# details_number = 15
details_number = input('\nInput integer number of positions. (Example: 1 or 2 or 3...or 10 or 25): ')
details_number = int(details_number)
non_blow_positions = input('Input positions separated by commas where Blower is deactivated. (Example: 0,3,7,10): ')
non_blow_positions = [int(el) for el in non_blow_positions.split(',')]
# BlowOutUnitActive = list(np.random.choice(a=[False, True], size=(1, details_number))[0])
# BlowOutUnitActive = [True, True, True, True, False]
BlowOutUnitActive = [True]*details_number
for i in non_blow_positions:
    BlowOutUnitActive[i] = False
_WpcDataEmArray_AT = [False]*details_number
_WpcDataEmArray_ON = [False]*details_number

move_or_not = []
empty_positions = 0
print(f"BlowOutUnitActive: {BlowOutUnitActive}")
print_picture(_WpcDataEmArray_AT, _WpcDataEmArray_ON, BlowOutUnitActive)
input("For next step press ENTER")
while True:
    if any(_WpcDataEmArray_ON):  # если есть детали которые выезжают со своей позиции
        # перемещаем детали которые выехали на следующую позицию
        for ind in range(details_number):
            if _WpcDataEmArray_ON[ind]:
                _WpcDataEmArray_AT[ind+1] = True
                _WpcDataEmArray_ON[ind] = False
        if move_or_not[0]:
            _WpcDataEmArray_AT[0] = True

    else:  # нет выезжающих деталей. Они либо стоят на своих позиция АТ или деталей воодще нет
        move_or_not = []
        empty_positions = 0
        for ind in reversed(range(details_number)):
            blow = BlowOutUnitActive[ind]
            at, at_prev = _WpcDataEmArray_AT[ind], _WpcDataEmArray_AT[ind - 1]
            on, on_prev = _WpcDataEmArray_ON[ind], _WpcDataEmArray_ON[ind - 1]

            if ind == 0:
                if (blow and not at) or (not blow and empty_positions > 0) or (blow and move_or_not[0]):  # and not at
                    move_or_not.insert(0, True)
                    empty_positions -= 1
                else:
                    move_or_not.insert(0, False)
            else:
                if ind != details_number - 1:
                    MoN = move_or_not[0]
                else:
                    MoN = False
                if blow and (not at or MoN) and at_prev and not on_prev:  # дует + пусто + есть деталь на предыдущей позиции + она еще не в пути -> едем
                    move_or_not.insert(0, True)
                elif blow and not at and not at_prev and not on_prev:  # дует + пусто + нет детали на предыдущей позиции + она не в пути -> не едем
                    empty_positions += 1
                    move_or_not.insert(0, False)
                elif not blow and empty_positions == 0:
                    move_or_not.insert(0, False)  # не дует + нет пустых позиций после
                elif not blow and at_prev and not on_prev and empty_positions > 0:
                    move_or_not.insert(0, True)  # не дует + есть пустые позиции после
                    empty_positions -= 1
                else:
                    # print(f"Unknown Case: {blow} + {at} + {at_prev} + {on_prev}")
                    move_or_not.insert(0, False)

        if not any(_WpcDataEmArray_AT) and len(BlowOutUnitActive) != 0:
            _WpcDataEmArray_AT[0] = True

        for ind, el in enumerate(move_or_not[1:]):
            if el:
                _WpcDataEmArray_ON[ind] = True
                _WpcDataEmArray_AT[ind] = False

    print_picture(_WpcDataEmArray_AT, _WpcDataEmArray_ON, BlowOutUnitActive)
    input("For next step press ENTER")
    if _WpcDataEmArray_AT == BlowOutUnitActive:
        print(Fore.WHITE + "\nALL DETAILS ARE ON THEIR PLACES. CLEAR ALL PLACES")
        _WpcDataEmArray_AT = [False] * len(_WpcDataEmArray_AT)
        _WpcDataEmArray_ON = [False] * len(_WpcDataEmArray_ON)
        print_picture(_WpcDataEmArray_AT, _WpcDataEmArray_ON, BlowOutUnitActive)
        input()
        break
