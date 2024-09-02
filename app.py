import tkinter as tk
from PIL import Image,ImageOps,ImageGrab
from tensorflow.keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
import io


def capture():
    img =capture_canvas(canvas)
 

  
    img_array=np.array(img).reshape(1,28,28,1)/255.0

    prediction=model.predict(img_array)[0]
    predicted_digit=np.argmax(prediction)
    print(f"predicted digit: {predicted_digit}")


 


model=load_model("handwritten digit recognizer.h5")
canvas_size=280
grid_size=28

cell_size=canvas_size//grid_size

brush_size=8;

grid_visible=False





def capture_canvas(canvas):
    canvas.update()
    width= canvas.winfo_width()
    height = canvas.winfo_height()

    postscript = canvas.postscript(colormode='mono')

    img=Image.open(io.BytesIO(postscript.encode("utf-8")))
    img = img.resize((28,28))

    img = img.convert('L')
    return img


def clear_all(canvas):
    canvas.delete('all')
root=tk.Tk()
root.title("Drawing canvas")
root.geometry("320x360")


canvas=tk.Canvas(root,width=280,height=280,bg="white")
canvas.pack(pady=10)

def draw(event):
    x,y=event.x,event.y
    canvas.create_oval(x-brush_size,y-brush_size,x+brush_size,y+brush_size,fill='black',outline='')

canvas.bind("<B1-Motion>",draw)

capture_button= tk.Button(root,text="capture",
                          command=capture
                          )
capture_button.pack(pady=10)

clear_button=tk.Button(root,text="clear canvas",command=lambda:clear_all(canvas))
clear_button.pack(pady=10)

root.mainloop()


    
    
