# -*- coding: utf-8 -*-
"""ハノイの塔 非再帰版
"""
import sys
import itertools

def move_disk(pegs, idx1, idx2):
    # 初期状態と最終状態を除き、任意の2つのペグどちらか一方に必ずディスクがある
    if not pegs[idx1]:
        src = pegs[idx2]
        dst = pegs[idx1]
    elif not pegs[idx2]:
        src = pegs[idx1]
        dst = pegs[idx2]
    else:
        if pegs[idx1][0] > pegs[idx2][0]:
            src = pegs[idx2]
            dst = pegs[idx1]
        else:
            src = pegs[idx1]
            dst = pegs[idx2]
    v = src.pop(0)
    dst.insert(0, v)

def hanoi(n):
    pegs = [list(range(n)), [], []]
    print(pegs)

    if (n % 2) == 0:
        order = itertools.cycle([(0, 1), (0, 2), (1, 2)])
    else:
        order = itertools.cycle([(0, 2), (0, 1), (1, 2)])
    for idx1, idx2 in order:
        move_disk(pegs, idx1, idx2)
        print(pegs)
        if len(pegs[2]) == n:
            break


if __name__ == "__main__":
    n = int(sys.argv[1])
    hanoi(n)
