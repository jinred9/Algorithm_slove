def solution(command):
    x, y = 0, 0
    dx, dy = 0, 1  # robot is facing upwards at the start

    for c in command:
        if c == 'R':
            dx, dy = dy, -dx  # rotate clockwise by 90 degrees
        elif c == 'L':
            dx, dy = -dy, dx  # rotate counterclockwise by 90 degrees
        elif c == 'G':
            x, y = x + dx, y + dy  # move one step forward
        elif c == 'B':
            x, y = x - dx, y - dy  # move one step backward

    return [x, y]