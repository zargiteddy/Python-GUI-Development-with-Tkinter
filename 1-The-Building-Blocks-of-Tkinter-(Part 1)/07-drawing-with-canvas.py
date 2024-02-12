import tkinter as tk

root = tk.Tk()
root.title("Drawing with Canvas")
root.minsize(300,200)

canvas = tk.Canvas(root, bg="yellow", height=500, width=500)

rect = 10,10,100,50
canvas.create_rectangle(rect, fill="green")

sqr = 10,10,50,50
canvas.create_rectangle(sqr, fill="blue")

line = 20,20,150,250
canvas.create_line(line, fill="red")

oval = 30,30,200,100
canvas.create_oval(oval, fill="pink")

coord = 50,50,120,250
canvas.create_arc(coord, start=0, extent=150, fill="orange")

pol = 45,10,200,350,100,240
canvas.create_polygon(pol, fill="purple")

canvas.pack()

root.mainloop()