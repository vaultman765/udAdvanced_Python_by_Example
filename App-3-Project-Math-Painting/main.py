from canvas import Canvas
from shapes import Square, Rectangle

# Get canvas width and height from the user
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

# Make a dict of color codes and prompt for color
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter canvas color (white or black): ")

# Create a canvas with user data
canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])


while True:
    shape_type = input("Would you like to draw a square or a rectangle? Enter quit to quit: ")
    # Ask for rectangle data and create rectangle if user entered 'rectangle'
    if shape_type.lower() == "rectangle":
        rec_x = int(input("Enter x of the rectangle: "))
        rec_y = int(input("Enter y of the rectangle: "))
        rec_width = int(input("Enter width of the rectangle: "))
        rec_height = int(input("Enter height of the rectangle: "))
        red = int(input("How much red should the rectangle have?: "))
        green = int(input("How much red should the rectangle have?: "))
        blue = int(input("How much red should the rectangle have?: "))

        r1 = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=(red, green, blue))
        r1.draw(canvas)

    if shape_type.lower() == "square":
        sq_x = int(input("Enter x of the square: "))
        sq_y = int(input("Enter y of the square: "))
        sq_size = int(input("Enter size of the square: "))
        red = int(input("How much red should the square have?: "))
        green = int(input("How much red should the square have?: "))
        blue = int(input("How much red should the square have?: "))

        s1 = Square(x=sq_x, y=sq_y, side=sq_size, color=(red, green, blue))
        s1.draw(canvas)

    if shape_type.lower() == 'quit':
        break

canvas.make("canvases/canvas.png")
