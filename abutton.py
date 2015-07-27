'''abutton'''
'''27 Jul 2015'''
from cStringIO import StringIO
import sys,io,os,time
global sys
import Tkinter as tk
from Tkinter import StringVar
from PIL import Image,ImageDraw,ImageFont,ImageTk
import numpy as np
global np,tk,Image,ImageDraw,ImageFont,ImageTk
global win,frame1,j,text,Picture1,Picture2,Picture2_1,Picture3,task,dotask,Font2,v
global Button,Button_im,Button_p,Button_im_p,Button_a,Button_im_a,Button_v,Button_im_v
if not os.path.isfile("9Things.mp4"):
	from pytube import YouTube
	yt=YouTube()
	yt.url="https://www.youtube.com/watch?v=4nP4PJL-9bg"
	video=yt.get('mp4')
	video.download()
FFMPEG_BIN = "ffmpeg.exe"
import subprocess as sp
Picture3=[]
old_stdout = sys.stdout
old_stderr = sys.stderr
sys.stdout = mystdout = StringIO()
sys.stderr = mystderr = StringIO()
for i in range(10):
	if os.path.isfile("out"+str(i)+".jpg"):
		# from StackOverflow.com Q#6996603 answer by RichieHindle 9 Aug 2011
		os.remove("out"+str(i)+".jpg")
	if i>5:
		ss=str((i-5)*10)
		mm='01'
	else:
		ss=str(i*10)
		mm='00'
	command = [ FFMPEG_BIN,
				'-ss', '00:'+mm+':'+ss,
				'-i', '9Things.mp4',
				'-frames:v','1','out'+str(i)+'.jpg']
	sp.call(command)
	Picture3.append(Image.open('out'+str(i)+'.jpg'))
	w,h = Picture3[i].size
	hh=int((w*40)/80)
	if hh>h:
		ww=int((h*80)/40)
		Picture3[i] = Picture3[i].crop((int((w-ww)/2.00),0,int((w-ww)/2.00)+ww,h))
	else:
		Picture3[i] = Picture3[i].crop((0,int((h-hh)/2.00),w,int((h-hh)/2.00)+hh))
	Picture3[i].thumbnail((80,40), Image.ANTIALIAS)

sys.stdout = old_stdout
sys.stderr = old_stderr
win=tk.Tk()
win.title('A_Button 1.0.0')
frame1 = tk.Frame(
	master = win,
	width = 840,
	height = 480,
	bg = '#808000'
)
frame1.pack(fill='both', expand='yes')
text='Enter'
Button=[]
Button_im=[]
Font1 = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 7)
Font2 = ImageFont.truetype("C:/Windows/Fonts/tahomabd.ttf", 24)
for i in range(1):
	image_pil = Image.new("RGB",(80,40),(0,0,0))
	draw = ImageDraw.Draw(image_pil)
	draw.text((5,5),text,(0,200,255),font=Font2)
	del draw
	Button_im.append(ImageTk.PhotoImage(image_pil))
	exec("Button.append(tk.Button(frame1,width=80,height=40,image=Button_im["+str(i)+"]))")
	if i==0:
		Button[i].place(x=10+(i*45),y=10)
v=StringVar()
v.set(text)
Entry1=tk.Entry(frame1,width=15,textvariable=v)
Entry1.place(x=10,y=50)
Picture1=Image.open('C:/Users/wisoot/Desktop/buttons2.jpg')
w,h = Picture1.size
hh=int((w*60)/80)
if hh>h:
	ww=int((h*80)/60)
	Picture1 = Picture1.crop((0,0,ww,h))
else:
	Picture1 = Picture1.crop((0,0,w,hh))
# From Stackoverflow.com Q#273946 answer by gnud 7 Nov 2008
Picture1.thumbnail((80,60), Image.ANTIALIAS)
Button_p=[]
Button_im_p=[]
for i in range(1):
	image_pil = Picture1.crop((0,0,80,40))
	Button_im_p.append(ImageTk.PhotoImage(image_pil))
	exec("Button_p.append(tk.Button(frame1,width=80,height=40,image=Button_im_p["+str(i)+"]))")
	if i==0:
		Button_p[i].place(x=10+(i*45),y=80)

Picture2=Image.open('C:/Users/wisoot/Desktop/Apple_gray_logo.png')
w,h = Picture2.size
hh=int((w*40)/80)
if hh>h:
	ww=int((h*80)/40)
	Picture2 = Picture2.crop((int((w-ww)/2.00),0,int((w-ww)/2.00)+ww,h))
else:
	Picture2 = Picture2.crop((0,int((h-hh)/2.00),w,int((h-hh)/2.00)+hh))
Picture2.thumbnail((80,40), Image.ANTIALIAS)
Picture2_1 = Image.new("RGB",(80,40),(50,200,55))
draw = ImageDraw.Draw(Picture2_1)
draw.text((5,5),'stock index',(255,255,255),font=Font1)
del draw
Button_a=[]
Button_im_a=[]
for i in range(1):
	Button_im_a.append(ImageTk.PhotoImage(Picture2))
	exec("Button_a.append(tk.Button(frame1,width=80,height=40,image=Button_im_a["+str(i)+"]))")
	if i==0:
		Button_a[i].place(x=10+(i*45),y=150)


Button_v=[]
Button_im_v=[]
for i in range(1):
	Button_im_v.append(ImageTk.PhotoImage(Picture3[0]))
	exec("Button_v.append(tk.Button(frame1,width=80,height=40,image=Button_im_v["+str(i)+"]))")
	if i==0:
		Button_v[i].place(x=10+(i*45),y=220)

def dotask():
	global win,frame1,text,v,j,task,Button,Button_im,Button_p,Button_im_p,Button_a,Button_im_a
	global Button_v,Button_im_v
	text=v.get()
	for i in range(1):
		image_pil = Image.new("RGB",(80,40),(0,0,0))
		draw = ImageDraw.Draw(image_pil)
		draw.text((5,5),text,(0,200,255),font=Font2)
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
		if j>80:
			jj=80
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

		last_image=ImageTk.PhotoImage(image_pil)
		image_pil=Image.fromarray(np.uint8(a_image))
		Button_im[i]=ImageTk.PhotoImage(image_pil)
		Button[i].configure(image=Button_im[i])

	for i in range(1):
		if j<=5:continue
		jx=j-5
		if jx>=0 and jx<80:
			if jx-(int(jx/4.00)*4)!=0:continue
			jj=int(j/4.00)
		elif jx>=80:
			continue
		jj=jj-1
		image_pil = Picture1.crop((0,jj,80,jj+40))
		Button_im_p[i]=ImageTk.PhotoImage(image_pil)
		Button_p[i].configure(image=Button_im_p[i])

	for i in range(1):
		if j==45:
			Button_im_a[i]=ImageTk.PhotoImage(Picture2_1)
			Button_a[i].configure(image=Button_im_a[i])
		elif j==89:
			Button_im_a[i]=ImageTk.PhotoImage(Picture2)
			Button_a[i].configure(image=Button_im_a[i])

	for i in range(1):
		if j-(int(j/10.00)*10)>0: continue
		Button_im_v[i]=ImageTk.PhotoImage(Picture3[int(j/10.00)])
		Button_v[i].configure(image=Button_im_v[i])
	j=j+1
	if j>=90: j=0
	task=win.after(10,dotask)

def on_closing():
	global win,task
	win.after_cancel(task)
	win.destroy()

j=1
task=win.after(10,dotask)
win.protocol("WM_DELETE_WINDOW", on_closing)
win.mainloop()
