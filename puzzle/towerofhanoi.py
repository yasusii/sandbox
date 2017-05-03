from itertools import cycle

def move_disk(pegs, src, dst):
    v = pegs[src].pop(0)
    pegs[dst].insert(0, v)

def solution(n):
    pegs = [list(range(n)), [], []] # [ペグA, ペグB, ペグC]
    # 最小ディスクの移動パターン
    if (n % 2) == 0:
        order = cycle([1, 2, 0])
    else:
        order = cycle([2, 1, 0])
    print(pegs)
    idx_smallest = 0 # 最小ディスクの現在位置
    for idx_smallest_next in order:
        # 最小ディスクを移動
        move_disk(pegs, idx_smallest, idx_smallest_next)
        idx_smallest = idx_smallest_next
        print(pegs)
        if len(pegs[2]) == n: # ペグCにすべてのディスクが揃ったら終了
            break
        # 最小ではないディスクを移動
        idx_other1 = (idx_smallest + 1) % 3
        idx_other2 = 3 - (idx_smallest + idx_other1)
        if pegs[idx_other1] and pegs[idx_other2]:
            if [idx_other1][0] < pegs[idx_other2][0]:
                move_disk(pegs, idx_other1, idx_other2)
            else:
                move_disk(pegs, idx_other2, idx_other1)
        elif pegs[idx_other1]:
            move_disk(pegs, idx_other1, idx_other2)
        else:
            move_disk(pegs, idx_other2, idx_other1)
        print(pegs)


if __name__ == "__main__":
    solution(4)
        
