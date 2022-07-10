#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""filler game bot"""
import logging


def main():
    """the main function"""
    logging.getLogger().setLevel(logging.DEBUG)

    player = input()
    if "p1 :" in player:
        player = "O"
    else:
        player = "X"
    try:
        while True:
            print(*step(player))
    except EOFError:
        logging.debug("No more available moves!")


def step(player):
    """bot step"""
    enemy = "X" if player == "O" else "O"
    board, b_size = board_parsing()
    figure, f_size = figure_parsing()
    player_counter, enemy_counter, figure_counter = 0, 0, 0

    for rows in range(1, len(board)):
        for column in range(4, len(board[rows])):
            if board[rows][column] is player:
                player_counter += 1
            elif board[rows][column] is enemy:
                enemy_counter += 1
    for rows, _ in enumerate(figure):
        for col in range(len(figure[rows])):
            if figure[rows][col] == "*":
                figure_counter += 1

    for row in range(1, len(board)):
        for col in range(4, len(board[row])):
            if col - 4 + f_size[1] <= b_size[1] and\
                    row - 1 + f_size[0] <= b_size[0]:
                symbol_c_player, symbol_c_enemy, r_temp = 0, 0, row
                f_temp = figure.copy()
                b_temp = board.copy()

                while len(f_temp) > 0:
                    for check in range(len(f_temp[0])):
                        temp_b, temp_f = \
                            board[r_temp][col:col +
                                          len(f_temp[0])][check],\
                            f_temp[0][check]
                        if temp_b == player and temp_f == "*":
                            symbol_c_player += 1
                        elif temp_b == enemy and temp_f == "*":
                            symbol_c_enemy += 1

                    b_temp[r_temp] = \
                        board[r_temp][:col] + f_temp[0].\
                        replace("*", player) + \
                        b_temp[r_temp][len(f_temp[0]) + col:]
                    r_temp += 1
                    f_temp.pop(0)

                if symbol_c_player == 1 and symbol_c_enemy == 0:
                    return [row - 1, col - 4]

    return [0, 0]


def board_parsing():
    """field parsing"""
    board = []
    b_size = list(map(int, input()[:-1].split(" ")[1:]))
    for _ in range(b_size[0] + 1):
        board.append(input())

    return list(map(str.upper, board)), b_size


def figure_parsing():
    """figure parsing"""
    figure = []
    f_size = list(map(int, input()[:-1].split()[1:]))
    for _ in range(f_size[0]):
        figure.append(input())

    return figure, f_size


if __name__ == "__main__":
    main()
