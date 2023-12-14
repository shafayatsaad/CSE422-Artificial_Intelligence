import random

def alpha_beta_pruning(alpha, beta, node_index, depth, maximizing_player, values):
    if depth == 3:
        return values[node_index]

    if maximizing_player:
        max_value = float('-inf')
        for i in range(0, 2):
            value = alpha_beta_pruning(alpha, beta, node_index * 2 + i, depth + 1, False, values)
            max_value = max(max_value, value)
            alpha = max(alpha, max_value)
            if beta <= alpha:
                break
        return max_value
    else:
        min_value = float('inf')
        for i in range(0, 2):
            value = alpha_beta_pruning(alpha, beta, node_index * 2 + i, depth + 1, True, values)
            min_value = min(min_value, value)
            beta = min(beta, min_value)
            if beta <= alpha:
                break
        return min_value

def task1(id):
    min_point = int(id[4])
    max_point = round(int(id[-2:][::-1]) * 1.5)
    total_points_to_win = int(id[-2:][::-1])
    values = [random.randint(min_point, max_point) for _ in range(8)]
    print(f"Generated 8 random points between the minimum and maximum point limits: {values}")
    print(f"Total points to win: {total_points_to_win}")
    achieved_point = alpha_beta_pruning(float('-inf'), float('inf'), 0, 0, True, values)
    print(f"Achieved point by applying alpha-beta pruning = {achieved_point}")
    if achieved_point >= total_points_to_win:
        print("The winner is Optimus Prime")
    else:
        print("The winner is Megatron")

def task2(id):
    min_point = int(id[4])
    max_point = round(int(id[-2:][::-1]) * 1.5)
    total_points_to_win = int(id[-2:][::-1])
    shuffle_times = int(id[3])
    win_times = 0
    for _ in range(shuffle_times):
        values = [random.randint(min_point, max_point) for _ in range(8)]
        achieved_point = alpha_beta_pruning(float('-inf'), float('inf'), 0, 0, True, values)
        if achieved_point >= total_points_to_win:
            win_times += 1
    print(f"Won {win_times} times out of {shuffle_times} number of shuffles")

id = input("Enter your student ID: ")
task1(id)
task2(id)
