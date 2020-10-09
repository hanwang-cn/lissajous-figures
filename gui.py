from tkinter import *
import Lissajous_Figures

def make_the_Gif(chr1,chr2,chr3,chr4, chr5):
    a1 = float(chr2)
    num1 = float(chr1)
    a2 = float(chr4)   
    num2 = float(chr3)
    Chr = chr5
    return Lissajous_Figures.make(a1, num1,a2, num2, Chr)
def get(E, chr):
    global Entry
    chr=Entry.get()
    return chr

root = Tk()
frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)
frame5 = Frame(root)
frame6 = Frame(root)
frame7 = Frame(root)
root.title("Lissajous Figures")

label1= Label(frame1,text="This program can give the GIF of the Lissajous Figures you want to see.\nThis program can analog the Oscilloscope.",font = 'consolas',justify=CENTER)
label1.pack(side=LEFT)

label2= Label(frame2,text="Frequency of CH1",font = 'consolas',justify=LEFT)
label2.pack(side=LEFT)
E1 = Entry(frame2, bd = 2)
E1.pack(side = LEFT)
get1 = Button(frame2, text="Get!", font = 'consolas', command=get(E1, chr1))
get1.pack(side=LEFT)
 
label3= Label(frame3,text="Amplitude of CH1",font = 'consolas',justify=LEFT)
label3.pack(side=LEFT)
E2 = Entry(frame3, bd = 2)
E2.pack(side = LEFT)
get2 = Button(frame3, text="Get!", font = 'consolas', command=get(E2,chr2))
get2.pack(side=LEFT )

label4= Label(frame4,text="Frequency of CH2",font = 'consolas',justify=LEFT)
label4.pack(side=LEFT)
E3 = Entry(frame4, bd = 2)
E3.pack(side = LEFT)
get3 = Button(frame4, text="Get!", font = 'consolas', command=get(E3,chr3))
get3.pack(side=LEFT)

label5= Label(frame5,text="Amplitude of CH2",font = 'consolas',justify=LEFT)
label5.pack(side=LEFT)
E4 = Entry(frame5, bd = 2)
E4.pack(side = LEFT)
get4 = Button(frame5, text="Get!", font = 'consolas', command=get(E4,chr4))
get4.pack(side=LEFT)

label6= Label(frame6,text="Give a Name of this Gif(eg. hello.gif)",font = 'consolas', justify=LEFT)
label6.pack(side=LEFT)
E5 = Entry(frame6, bd = 2)
E5.pack(side = LEFT)
chr = E5.get()
get5 = Button(frame6, text="Get!", font = 'consolas', command=get(E5,chr5))
get5.pack(side=LEFT)

make_the_gif = Button(frame7, text="Make!", font = 'consolas') # command=make_the_Gif(chr,chr,chr,chr))
make_the_gif.pack(side=LEFT)
# make_the_Gif(chr1,chr2,chr3,chr4)

frame1.pack(padx=20,pady=20)
frame2.pack(padx=20,pady=20)
frame3.pack(padx=20,pady=20)
frame4.pack(padx=20,pady=20)
frame5.pack(padx=20,pady=20)
frame6.pack(padx=20,pady=20)
frame7.pack(padx=20,pady=20)
root.mainloop()


# 注释和相应的解答


'''手动
按照该Tkinter的Entry控件：

首先，你可以阅读从价值Entry与

entry.get()
其次，您可以将其绑定到tkinter.Variable（它使用自动生成的名称创建和包装Tcl全局变量）。通常，使用它的子类StringVar- 它str在获取/设置时将值转换为。

v = tkinter.StringVar()
entry = tk.Entry(root1, textvariable=v)

<...>
value = v.get()
你可以看到，没有太大的区别，只增加了一个间接层。这两种方法都会让你得到一个str所以你需要解析它int()。
但你可以使用一个IntVar而不是Variable（或StringVar）来解析它.get()（ValueError如果它不是一个有效的整数，它将会提升）。
def guess():
    global entry
    guess = entry.get()
    guessN = int(guess)'''
