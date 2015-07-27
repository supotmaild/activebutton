'''Active Button'''
'''version 1.0.0'''
import sys,io,os,time
global sys
if sys.version_info[0] < 3:
	import Tkinter as tk
	from Tkinter import Menu,Canvas,Scrollbar
	from Tkinter import StringVar,PhotoImage
	from Tkinter import ALL, TOP, END, RIGHT, LEFT, X, Y, N, BOTH, VERTICAL
	import tkMessageBox as msgbox
	import ScrolledText as tkst
else:
	import tkinter as tk
	from tkinter import Menu,Canvas,Scrollbar
	from tkinter import StringVar,PhotoImage
	from tkinter import ALL, TOP, END, RIGHT, LEFT, X, Y, N, BOTH, VERTICAL
	from tkinter import messagebox as msgbox
	from tkinter import scrolledtext as tkst
from PIL import Image,ImageDraw,ImageFont,ImageTk
import numpy as np
global np,tk,Image,ImageDraw,ImageFont,ImageTk
global win,frame1,j,task,dotask,Font2
global Button,Button_im
win=tk.Tk()
win.title('Active Button 1.0.0')
frame1 = tk.Frame(
	master = win,
	width = 840,
	height = 480,
	bg = '#808000'
)
frame1.pack(fill='both', expand='yes')
Button=[]
Button_im=[]
Font2 = ImageFont.truetype("C:/Windows/Fonts/tahomabd.ttf", 24)
for i in range(10):
	image_pil = Image.new("RGB",(40,40),(0,0,0))
	draw = ImageDraw.Draw(image_pil)
	draw.text((5,5),str(i),(0,200,255),font=Font2)
	del draw
	Button_im.append(ImageTk.PhotoImage(image_pil))
	exec("Button.append(tk.Button(frame1,width=40,height=40,image=Button_im["+str(len(Button_im)-1)+"]))")
	if i>=1 and i<=3:
		Button[i].place(x=10+((i-1)*45),y=10)
	elif i>=4 and i<=6:
		Button[i].place(x=10+((i-4)*45),y=55)
	elif i>=7 and i<=9:
		Button[i].place(x=10+((i-7)*45),y=100)
	elif i==0:
		Button[i].place(x=10+((i+1)*45),y=145)


def dotask():
	global win,frame1,j,task,Button,Button_im
	for i in range(10):
		image_pil = Image.new("RGB",(40,40),(0,0,0))
		draw = ImageDraw.Draw(image_pil)
		draw.text((5,5),str(i),(0,200,255),font=Font2)
		del draw
		a_image = np.array(image_pil)
		l=0
		for k in range(len(a_image)):
			if l==1:
				l=0 
				continue
			l=1
			for kk in range(len(a_image[k])):
				a_image[k,kk]=(0,0,0)
		if j>40:
			jj=40
		else:
			jj=j
		if j>=2:
			l=1
			for k in range(len(a_image)):
				if l==1:
					l=0 
					continue
				l=1
				for kk in range(jj):
					if kk<(j-10): continue
					if a_image[k,kk][1]==0 and a_image[k,kk][2]==0:
						a_image[k,kk]=(0,200,255)
					else:
						a_image[k,kk]=(0,0,0)

		image_pil=Image.fromarray(np.uint8(a_image))
		Button_im[i]=ImageTk.PhotoImage(image_pil)
		exec("Button[i]=tk.Button(frame1,width=40,height=40,image=Button_im["+str(i)+"])")
		Button[i].place_forget()
		if i>=1 and i<=3:
			Button[i].place(x=10+((i-1)*45),y=10)
		elif i>=4 and i<=6:
			Button[i].place(x=10+((i-4)*45),y=55)
		elif i>=7 and i<=9:
			Button[i].place(x=10+((i-7)*45),y=100)
		elif i==0:
			Button[i].place(x=10+((i+1)*45),y=145)
	j=j+1
	if j>=50: j=0
	task=win.after(100,dotask)

def on_closing():
	global win,task
	win.after_cancel(task)
	win.destroy()

j=1
task=win.after(100,dotask)
win.protocol("WM_DELETE_WINDOW", on_closing)
win.mainloop()
