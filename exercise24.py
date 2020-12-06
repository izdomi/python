# Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s
# print statement.

def board_draw(height, width):
    top = "┌" + "┬".join(["─"*4]*width) + "┐\n"
    bottom = "└" + "┴".join(["─"*4]*width) + "┘"
    middle = "├" + "┼".join(["─"*4]*width) + "┤\n"
    print(top +
          middle.join(
              "│" +
              "│".join('    '.format(x * width + y + 1)
                       for y in range(width)) +
              "│\n"
              for x in range(height)) +
          bottom)
print(board_draw(4,3))


def board_draw(height, width):
    square = 0
    print(" --- " * width)
    for x in range(height):
        line = "| "
        for i in range(0, width):
            line += format(square, '02d') + " | "
            square += 1
        print(line)
    print(" --- " * width)

heightinp= int(input("Enter the height of the board: "))
widthinp= int(input("Enter the width of the board: "))

board_draw(heightinp,widthinp)



def drawboard(size):
    size = int(size)
    i = 0
    top = "--- "
    middle = "|   "
    top = top * size
    middle = middle * (size+1)
    while i < size+1:
        print(top)
        if not (i == size):
            print(middle)
        i += 1
print(drawboard(4))



a = '---'.join('    ')
b = '   '.join('||||')
print('\n'.join((a, b, a, b, a, b, a)))