import turtle

#This is a function to construct the table
def table(table_length,table_color):
 """
 In this function, we will prompt the user to input the desired length of the the table and will take them as parameters 
 """

 """
 The if statement is used to constraint user to enter table length value between 10 and 100
 """
 if 10<=table_length<=100:
    """
    We are constructing the base of the table
    """
    table_length = table_length * 4
    turtle.fillcolor(table_color)
    turtle.begin_fill()
    turtle.pencolor(table_color)
    turtle.goto(0,0)
    turtle.left(180)
    turtle.forward(table_length/2)
    turtle.left(90)
    turtle.forward(table_length/10)
    turtle.left(90)
    turtle.forward(table_length)
    turtle.left(90)
    turtle.forward(table_length/10)
    turtle.left(90)
    turtle.forward(table_length/2)
    turtle.end_fill()

    """
    Constructing the First leg of the table
    """
    turtle.fillcolor(table_color)
    turtle.begin_fill()
    turtle.forward(table_length / 2)
    turtle.left(90)
    turtle.forward(table_length / 10)
    turtle.pendown()
    turtle.forward(table_length / 2)
    turtle.left(90)
    turtle.forward(table_length / 10)
    turtle.left(90)
    turtle.forward(table_length/2)
    turtle.end_fill()

    """
    Constructing second leg of table
    """
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.pencolor("black")
    turtle.penup()
    turtle.right(90)
    turtle.forward(table_length / 10)
    turtle.right(90)
    turtle.pendown()
    turtle.forward((table_length / 2)-(table_length / 10))
    turtle.right(90)
    turtle.forward(table_length / 10)
    turtle.end_fill()

    """
    Constructing third leg of table
    """
    turtle.penup()
    turtle.goto(0,0)
    turtle.right(180)
    turtle.forward(table_length/2)
    turtle.right(90)
    turtle.forward(table_length/10)
    turtle.pendown()
    turtle.pencolor(table_color)
    turtle.fillcolor(table_color)
    turtle.begin_fill()
    turtle.forward(table_length/2)
    turtle.right(90)
    turtle.forward(table_length/10)
    turtle.right(90)
    turtle.forward(table_length/2)
    turtle.end_fill()

    """
    Constructing the fourth leg of the table
    """
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.penup()
    turtle.left(90)
    turtle.forward(table_length / 10)
    turtle.left(90)
    turtle.pendown()
    turtle.pencolor("black")
    turtle.forward((table_length / 2)-(table_length/10))
    turtle.left(90)
    turtle.forward(table_length / 10)
    turtle.end_fill()

    """
    Going back to where the turtle started
    """
    turtle.penup()
    turtle.goto(0,0)

 else:
    print("Error! PLease try again and enter a table length between (10-100).")
    main()
    """
    End of table function
    """


#This is a function that contructs the cake
def cake(cake_size,cake_color1,cake_color2,cake_color3):
   cake_size = cake_size * 2
   """
   In this function, we will prompt the user to input the size of the cake and desired colors and will take them as parameters 
   """

   """
   This code constructs the first layer of the cake
   """
   turtle.left(180)
   turtle.pendown()
   turtle.pencolor(cake_color1)
   turtle.fillcolor(cake_color1)
   turtle.begin_fill()
   turtle.forward(cake_size/2)
   turtle.right(90)
   turtle.forward(cake_size/2)
   turtle.right(90)
   turtle.forward(cake_size)
   turtle.right(90)
   turtle.forward(cake_size/2)
   turtle.right(90)
   turtle.forward(cake_size/2)
   turtle.end_fill()

   """
   Constructing the second layer of the cake
   """
   turtle.hideturtle()
   turtle.penup()
   turtle.forward(cake_size/2)
   turtle.right(90)
   turtle.forward(cake_size/2)
   turtle.right(90)
   turtle.forward(cake_size/2)
   turtle.left(180)
   turtle.showturtle()
   turtle.pendown()
   turtle.fillcolor(cake_color2)
   turtle.begin_fill()
   turtle.pencolor(cake_color2)
   turtle.forward(cake_size/3)
   turtle.right(90)
   turtle.forward(cake_size/3)
   turtle.right(90)
   turtle.forward(cake_size/1.5)
   turtle.right(90)
   turtle.forward(cake_size/3)
   turtle.right(90)
   turtle.forward(cake_size/1.5)
   turtle.end_fill()

   """
   Constructing third and last layer of the cake
   """
   turtle.hideturtle()
   turtle.penup()
   turtle.right(90)
   turtle.forward(cake_size/3)
   turtle.right(90)
   turtle.forward(cake_size/3)
   turtle.left(180)
   turtle.showturtle()
   turtle.pendown()
   turtle.fillcolor(cake_color3)
   turtle.begin_fill()
   turtle.pencolor(cake_color3)
   turtle.forward(cake_size/4)
   turtle.right(90)
   turtle.forward(cake_size/4)
   turtle.right(90)
   turtle.forward(cake_size/2)
   turtle.right(90)
   turtle.forward(cake_size/4)
   turtle.end_fill()

   """
   End of cake function
   """


#This is a function to decorate the cake with cherries
def cherries_decoration(y):
   """
   The turtle.circle() command is used to create the round shape of the cherries
   """
   """ 
   Adjusting position of cherry 1
   """
   turtle.hideturtle()
   turtle.penup()
   turtle.right(90)
   turtle.forward(y)
   turtle.right(90)
   turtle.forward(y/2)
   turtle.right(90)
   turtle.forward(y/8)
   turtle.showturtle()
   turtle.pendown()
   """
   Drawing cherry
   """
   turtle.fillcolor("Red")
   turtle.begin_fill()
   turtle.pencolor("Red")
   turtle.circle(y/10)
   turtle.end_fill()
   turtle.hideturtle()
   turtle.penup()
   turtle.circle(y/10,180)
   turtle.right(90)
   turtle.showturtle()
   turtle.pendown()
   turtle.pencolor("green")
   turtle.forward(y/7)

   """
   Adjusting position of cherry 2
   """
   turtle.hideturtle()
   turtle.penup()
   turtle.backward(y/7)
   turtle.left(90)
   turtle.circle(y/10, 180)
   turtle.backward(y/8)
   turtle.forward(y)
   turtle.backward(y/8)

   """
   Drawing cherry 2
   """
   turtle.showturtle()
   turtle.pendown()
   turtle.pencolor("Red")
   turtle.fillcolor("Red")
   turtle.begin_fill()
   turtle.circle(y/10)
   turtle.end_fill()
   turtle.hideturtle()
   turtle.penup()
   turtle.circle(y/10,180)
   turtle.right(90)
   turtle.showturtle()
   turtle.pendown()
   turtle.pencolor("green")
   turtle.forward(y/7)

   """
   Re-adjusting position on to the midpoint of the cake to draw candle next
   """
   turtle.hideturtle()
   turtle.penup()
   turtle.backward(y/7)
   turtle.left(90)
   turtle.circle(y/10, 180)
   turtle.forward(y/8)
   turtle.left(180)
   turtle.forward(y/2)
   turtle.right(90)
   

def candle(y):
   """
   Drawing candle
   """
   turtle.showturtle()
   turtle.pendown()
   turtle.pencolor("black")
   turtle.forward(y/4)
   turtle.fillcolor("red")
   turtle.begin_fill()
   turtle.pencolor("red")
   turtle.right(90)
   turtle.circle(y/12)
   turtle.end_fill()
   turtle.fillcolor("orange")
   turtle.pencolor("orange")
   turtle.begin_fill()
   turtle.circle(y/22)
   turtle.end_fill()

   """
   Setting turtle back to starting position
   """
   turtle.penup()
   turtle.goto(0,0)


#Defining the main function
def main():
    """
    Prompting the user to enter desired values such as length, color, and size
    """
    table_length = int(input("Please enter the length of one side of a table (between 10-100): "))
    table_color = input("Please enter the color of the table: ")
    cake_size = int(input("Please enter the size of the cake (between 10-100) Note that the cake size should be equal to or smaller than the table size: "))
    cake_color1= input("Please enter the first flavor of the cake as a color: ")
    cake_color2= input("Please enter the second flavor of the cake as a color: ")
    cake_color3= input("Please enter the third flavor of the cake as a color: ")
    print("Your cake is loading! Happy Birthday!")
    turtle.speed(7)

    """
    calling functions to be executed
    """
    table(table_length,table_color)
    cake(cake_size,cake_color1,cake_color2,cake_color3)
    cherries_decoration(cake_size)
    candle(cake_size)

    """
    Using the input() command to pause the window screen of the drawing until user presses any key
    """
    input("Press any key to exit...")

main() #calling the main function

