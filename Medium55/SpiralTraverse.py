def spiralTraverse(array):
    """
    O(nm)
    """
    res = []
    up, down = 0, len(array) - 1
    left, right = 0, len(array[0]) - 1
    row, col = up, left
    while left <= right or up <= down:
        # Move right
        while col <= right:
            res.append(array[row][col])
            col += 1
        up += 1
        row, col = up, right
        if down < up:
            return res
        # Move down
        while row <= down:
            res.append(array[row][col])
            row += 1
        right -= 1
        row, col = down, right
        if right < left:
            return res
        # Move left
        while col >= left:
            res.append(array[row][col])
            col -= 1
        down -= 1
        row, col = down, left
        if down < up:
            return res
        # Move up
        while row >= up:
            res.append(array[row][col])
            row -= 1
        left += 1
        row, col = up, left
        if right < left:
            return res
    return res






