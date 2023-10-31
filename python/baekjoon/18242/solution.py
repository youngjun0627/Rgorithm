def solution():
    N, M = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(input())

    len_y = N
    len_x = M
    rectangle_coords = []

    for i in range(len_y):
        for j in range(len_x):
            if board[i][j] == '#':
                rectangle_coords.append([j, i])
    left_top_coord = sorted(rectangle_coords, key=lambda x: [x[0], x[1]])[0]
    right_bottom_coord = sorted(rectangle_coords, key=lambda x: [-x[0], -x[1]])[0]
    right_top_coord = [right_bottom_coord[0], left_top_coord[1]]
    left_bottom_coord = [left_top_coord[0], right_bottom_coord[1]]

    if search(board, right_top_coord, right_bottom_coord):
        print('RIGHT')
    if search(board, left_top_coord, left_bottom_coord):
        print('LEFT')
    if search(board, left_top_coord, right_top_coord):
        print('UP')
    if search(board, left_bottom_coord, right_bottom_coord):
        print('DOWN')


def search(board, start_coord, end_coord):
    start_x, start_y = start_coord
    end_x, end_y = end_coord

    if start_y == end_y:
        for x in range(start_x, end_x):
            if board[start_y][x] != '#':
                return True
    if start_x == end_x:
        for y in range(start_y, end_y):
            if board[y][start_x] != '#':
                return True
    return False
