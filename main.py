from colorama import Fore


def print_picture(AT, ON, BlowOutUnitActive):
    BlowOutUnit = ''
    for blow, at, on in zip(BlowOutUnitActive, AT, ON):
        if blow:
            BlowOutUnit += Fore.GREEN + '['
            if at:
                BlowOutUnit += Fore.BLUE + '0' + Fore.GREEN + ']'
            else:
                BlowOutUnit += Fore.GREEN + ' ]'
        else:
            BlowOutUnit += Fore.RED + '['
            if at:
                BlowOutUnit += Fore.BLUE + '0' + Fore.RED + ']'
            else:
                BlowOutUnit += Fore.RED + ' ]'
        if on:
            BlowOutUnit += Fore.BLUE + ' 0 '
        else:
            BlowOutUnit += '   '
    numbers = [i for i in range(len(BlowOutUnitActive))]
    numbers_str = ""
    for i in numbers:
        if len(str(i)) == 1:
            numbers_str += f" {i}    "
        else:
            numbers_str += f" {i}   "
    print(Fore.WHITE + numbers_str)
    print(BlowOutUnit)
    print(Fore.RED + "---------->")
    print(Fore.WHITE)


def main():
    AT = [False, False, False, False]  # on position
    ON = [False, False, False, False]  # in motion
    BlowOutUnitActive = [True, True, False, True]
    num_wpc_required = sum(BlowOutUnitActive)
    num_wpc = 0

    print_picture()
    input()

    while True:
        if AT == BlowOutUnitActive or AT[-1]:
            print("All WPC on their Place. Replace everything")
            AT = [False] * len(AT)
            ON = [False] * len(ON)
            num_wpc = 0
        else:
            # queue = deque([x for el in zip(_WpcDataEmArray_TS_AT_MS,
            #                                _WpcDataEmArray_TS_ON_MS) for x in el])
            if any(ON):
                for ind in reversed(range(len(ON), 1)):
                    print(ind)
                    if BlowOutUnitActive[ind] and not AT[ind]:
                        AT[ind] = ON[ind-1]
                        ON[ind-1] = False
                        if not AT[0] and num_wpc < num_wpc_required:
                            AT[0] = True
                            num_wpc += 1
            elif any(AT):
                    for ind, el in enumerate(AT):
                        wpc_after_ind = sum(AT[ind:]) + sum(ON[ind:])
                        if el and wpc_after_ind < sum(BlowOutUnitActive[ind:]):
                            ON[ind] = True
                            AT[ind] = False
            else:
                AT[0] = True
                num_wpc += 1
                # queue.pop()
                # if not _WpcDataEmArray_TS_AT_MS[0] and num_wpc < num_wpc_required:
                #     queue.appendleft(True)
                #     num_wpc += 1
                # else:
                #     queue.appendleft(False)
                #
                # _WpcDataEmArray_TS_AT_MS = []
                # _WpcDataEmArray_TS_ON_MS = []
                # while queue:
                #     _WpcDataEmArray_TS_AT_MS.append(queue.popleft())
                #     _WpcDataEmArray_TS_ON_MS.append(queue.popleft())

        print_picture(AT, ON, BlowOutUnitActive)
        input()


if __name__ == '__main__':
    main()
