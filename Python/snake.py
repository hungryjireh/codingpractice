"""
Solution to the snake game.

Conditions:
1. If snake is able to clear specified movements, return 'YES'
2. Else, return last index which snake does not consume its own tail.

Sample input:
'2' # denotes number of tests which is a finite number
'6 EEEELL' # denotes test 1
'7 EEEELLL' # denotes test 2, which is independent of test 1

Sample output:
'YES'
6
"""

import copy

def next_coordinates(current_coordinates, front, step):
    if front == 'S':
        if step == 'L':
            front = 'E'
            current_coordinates[0] += 1
        elif step == 'R':
            front = 'W'
            current_coordinates[0] -= 1
        elif step == 'E' or step == 'F':
            current_coordinates[1] -= 1
    elif front == 'W':
        if step == 'L':
            front = 'S'
            current_coordinates[1] -= 1
        elif step == 'R':
            front = 'N'
            current_coordinates[1] += 1
        elif step == 'E' or step == 'F':
            current_coordinates[0] -= 1
    elif front == 'N':
        if step == 'L':
            front = 'W'
            current_coordinates[0] -= 1
        elif step == 'R':
            front = 'E'
            current_coordinates[0] += 1
        elif step == 'E' or step == 'F':
            current_coordinates[1] += 1
    elif front == 'E':
        if step == 'L':
            front = 'N'
            current_coordinates[1] += 1
        elif step == 'R':
            front = 'S'
            current_coordinates[1] -= 1
        elif step == 'E' or step == 'F':
            current_coordinates[0] += 1
    return {'current_coordinates': current_coordinates, 'front': front}

def main():
    number_tests = int(input().strip())
    for i in range(number_tests):
        current_steps = input().split(' ')
        movements = list(current_steps[1])
        snake_length = 1
        snake_body = [[0, 0]]
        prev_position = None
        front = 'S'
        duplicate = False
        for j in range(len(movements)):
            next_bearings = next_coordinates(copy.deepcopy(snake_body[0]), front, movements[j])
            front = next_bearings['front']
            if movements[j] == 'E':
                snake_length += 1
                snake_body.insert(0, next_bearings['current_coordinates'])
            else:
                snake_body.insert(0, next_bearings['current_coordinates'])
                snake_body = snake_body[:-1]
            for item in snake_body:
                if snake_body.count(item) != 1:
                    duplicate = True
                    print(j)
                    break
        if duplicate is False:
            print("YES")
        

if __name__ == '__main__':
    main()