import tkinter as tk
import random
import matplotlib.pyplot as plt

root= tk.Tk()
canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()
label1=tk.Label(root,text='LAW OF LARGE NUMBERS')
label1.config(font=('helvetica',14))
canvas1.create_window(200, 25, window=label1)
label2 = tk.Label(root, text='Enter number of times to flip the coin:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)
entry1=tk.Entry(root)
canvas1.create_window(200,140,window=entry1)
head,tail,flip=[],[],[]
coin_outcomes=["heads","tails"]

def flipping(n):
	i=0
	for _ in range(n):
		if str(random.choice(coin_outcomes))=="heads":i+=1
	return i

Hx,Hy=[],[]
def main():
	n=int(entry1.get())
	i=flipping(n)
	head.append(i)
	flip.append(n)
	head_value=sum(head)/sum(flip)
	Hx.append(sum(flip))
	Hy.append(head_value)
	label3=tk.Label(root,text="Expected Value of heads=0.50")
	label3.config(font=('helvetica', 10))
	canvas1.create_window(200, 200, window=label3)
	label4=tk.Label(root,text="Current mean Value of heads={}".format(head_value))
	label4.config(font=('helvetica', 10))
	canvas1.create_window(200, 220, window=label4)
	plt.hlines(0.5,min(Hx),max(Hx))
	plt.plot(Hx, Hy, color='green', linestyle='dashed', linewidth = 1,marker='o',markerfacecolor='blue', markersize=8)
	plt.ylim(0,1)
	plt.xlim(min(Hx),max(Hx))
	plt.xlabel('number of flips done')
	plt.ylabel('heads occurred')
	plt.title('LAW OF LARGE NUMBERS')
	plt.show()	

button1 = tk.Button(text='Flip!!!!', command=main, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()