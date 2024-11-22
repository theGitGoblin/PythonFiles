from tkinter import *

window = Tk()

canvas = Canvas(window, width=500, height=500, background="black")

canvas.pack()

 

def get_star_pixel_x(s):
    split = s.split(",")
    cord_x_1 = split[0]

    formula = 250 + (250 * float(cord_x_1))

    return formula

 


 

def get_star_pixel_y(s):
    split = s.split(",")
    cord_y_1 = split[1]

    formula = 250 - (250 * float(cord_y_1))

    return formula

 

def get_star_size(s):
    split = s.split(",")
    magnitude = float(split[4])

    formula = 10.0/(magnitude + 2)

    return formula


def get_star_name(s):
    list = s.split(",")
   
    if len(list) == 7:

        return list[-1]

    else:

        return ""
 

def draw_star(s):

    x_pixel= get_star_pixel_x(s)

    y_pixel= get_star_pixel_y(s)

    name= get_star_name(s)

    size = get_star_size(s)

    left_x = (x_pixel - (size/2))

    right_x = (x_pixel + (size/2))

    bottom_y = (y_pixel +(size/2))

    top_y = (y_pixel - (size/2))

    canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill="white", width=0)

 
 

def draw_all_stars():

    text = open("stars.txt")

    f = text.read()

    lines = f.split("\n")

    for constellation in lines:
        draw_star(constellation)
 

def get_star_string(starname):
    f = open("stars.txt")
    big_str = f.read()
    lines = big_str.split("\n")
 
    for line in lines:
        line_name = get_star_name(line)
        if line_name == starname:
            return line    
    a = get_star_name(starname)
    return a,"ERROR: No star called "+ starname + " could be found."



def draw_star_by_name(s):
    x = get_star_string(s)
    draw_star(x)

def draw_constellation_line(star1, star2):
    a = get_star_string(star1)    
    b = get_star_string(star2)
    x1 = get_star_pixel_x(a)
    y1 = get_star_pixel_y(a)
    x2 = get_star_pixel_x(b)
    y2 = get_star_pixel_y(b)
    canvas.create_line(x1, y1, x2, y2, fill="yellow")

def draw_constellation_file(filename):
    f = open(filename)
    stars = f.read()
    line = stars.split("\n")
    for star in line:
        x = star.split(",")
        draw_constellation_line(x[0], x[1])
draw_all_stars()
draw_constellation_file("BigDipper_lines.txt")
draw_constellation_file("Bootes_lines.txt")
draw_constellation_file("Cas_lines.txt")
draw_constellation_file("Cyg_lines.txt")
draw_constellation_file("Gemini_lines.txt")
draw_constellation_file("Hydra_lines.txt")
draw_constellation_file("UrsaMajor_lines.txt")
draw_constellation_file("UrsaMinor_lines.txt")

mainloop()