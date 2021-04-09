import time

start_time = time.time()
sudoku = [
    [2, "x", "x", 3, "x", 8, 6, 1, "x"],
    ["x", "x", 6, "x", "x", "x", "x", 8, "x"],
    [9, "x", 8, 6, "x", "x", 7, 5, 4],
    [8, "x", "x", "x", "x", "x", "x", "x", 5],
    [3, "x", 9, "x", 8, "x", "x", 7, 6],
    [5, "x", "x", 2, "x", "x", "x", "x", "x"],
    [7, "x", 4, "x", 5, 3, 9, "x", 2],
    ["x", "x", 3, "x", 2, 7, 5, 4, "x"],
    ["x", "x", "x", "x", 6, 9, "x", 3, "x"],
]

solution = [
    [2, 7, 5, 3, 4, 8, 6, 1, 9],
    [4, 1, 6, 7, 9, 5, 2, 8, 3],
    [9, 3, 8, 6, 1, 2, 7, 5, 4],
    [8, 4, 7, 9, 3, 6, 1, 2, 5],
    [3, 2, 9, 5, 8, 1, 4, 7, 6],
    [5, 6, 1, 2, 7, 4, 3, 9, 8],
    [7, 8, 4, 1, 5, 3, 9, 6, 2],
    [6, 9, 3, 8, 2, 7, 5, 4, 1],
    [1, 5, 2, 4, 6, 9, 8, 3, 7],
]


def solver():
    prev_num = 0
    previous = []
    i = 0
    while i < len(sudoku):
        j = 0
        while j < len(sudoku[i]):
            checker = True
            if sudoku[i][j] == "x":
                for num in range(1, 10):  # check row
                    if num not in sudoku[i] and num > prev_num:
                        if column_check(
                            num, i, j, prev_num
                        ):  # Returns True if column valid
                            if boxcheck(
                                num, i, j, prev_num
                            ):  # Returns True if Box valid
                                previous.append(
                                    [i, j]
                                )  # Use a stack to store the positions
                                sudoku[i][
                                    j
                                ] = num  # Becomes num when both condition returns true
                                prev_num = 0
                                checker = False
                                break  # Breaks, prevents a looping again where the larger valid number replaces
                if (
                    checker
                ):  # Goes back to the previous position when current position can't be filled
                    prev_num = sudoku[previous[-1][0]][previous[-1][1]]
                    sudoku[previous[-1][0]][previous[-1][1]] = "x"
                    i = previous[-1][0]
                    j = previous[-1][1] - 1
                    previous.pop()
            j += 1
        i += 1


def column_check(num, i, j, prev_num):  # check column
    checker = True
    for k in range(len(sudoku)):
        if str(num) in str(sudoku[k][j]) and num > prev_num:
            return False
    return True


def boxcheck(num, i, j, prev_num):  # check boxes
    checker = True
    for h in range(0, 3):
        for z in range(0, 3):
            if int(i / 3) == h:
                if int(j / 3) == z:
                    for hz in range(h * 3, h * 3 + 3):  # check for which box
                        for kz in range(z * 3, z * 3 + 3):
                            if (
                                str(num) in str(sudoku[hz][kz]) and num > prev_num
                            ):  # check for num in box
                                checker = False
                                return checker
    return checker


solver()
for i in range(len(sudoku)):
    print(sudoku[i])
print("--- %s seconds ---" % (time.time() - start_time))  # Time taken
