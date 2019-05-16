from tkinter import*
def checkered(canvas,line_distance):
 for x in range(line_distance,canvas_width,line_distance):
    canvas.create_line(x,0,x,canvas_height,fill="#476402")
 for y in range(line_distance,canvas_height,line_distance):
    canvas.(0,y,canvas_width,y,fill="#476402")
master=Tk()create_line
canvas_width=200
canvas_height=100
w=Canvas(master,width=canvas_width,height=canvas_height)
w.pack()
checkered(w,10)
mainloop()
    
