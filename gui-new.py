from tkinter import *
from Lissajous_Figures import *

def Get_and_Make():
    global E1
    global E2
    global E3
    global E4
    global E5
    a1 = E2.get()
    num1 = E1.get()
    a2 = E4.get()
    num2 = E3.get()
    Chr = E5.get()
    return make1(a1, num1,a2, num2, Chr)


root = Tk()
frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)
frame5 = Frame(root)
frame6 = Frame(root)
frame7 = Frame(root)
root.title("Lissajous Figures")
'''chr1 = "0"
chr2 = "0"
chr3 = "0"
chr4 = "0"
Chr = "0"'''

label1 = Label(frame1,text="This program can give the GIF of the Lissajous Figures you want to see.\nThis program can analog the Oscilloscope.",font = 'consolas',justify=CENTER)
label1.pack(side=LEFT)

label2 = Label(frame2,text="Frequency of CH1",font = 'consolas',justify=LEFT)
label2.pack(side=LEFT)
E1 = Entry(frame2, bd = 2)
E1.pack(side = LEFT)
 
label3 = Label(frame3,text="Amplitude of CH1",font = 'consolas',justify=LEFT)
label3.pack(side=LEFT)
E2 = Entry(frame3, bd = 2)
E2.pack(side = LEFT)

label4 = Label(frame4,text="Frequency of CH2",font = 'consolas',justify=LEFT)
label4.pack(side=LEFT)
E3 = Entry(frame4, bd = 2)
E3.pack(side = LEFT)

label5 = Label(frame5,text="Amplitude of CH2",font = 'consolas',justify=LEFT)
label5.pack(side=LEFT)
E4 = Entry(frame5, bd = 2)
E4.pack(side = LEFT)


label6 = Label(frame6,text="Give a Name of this Gif(eg. hello.gif)",font = 'consolas', justify=LEFT)
label6.pack(side=LEFT)
E5 = Entry(frame6, bd = 2)
E5.pack(side = LEFT)

#def make_the_Gif(chr1,chr2,chr3,chr4, chr5):
 #   a1 = float(chr2)
  #  num1 = float(chr1)
   # a2 = float(chr4)   
    # num2 = float(chr3)
#    Chr = chr5
#    return make(a1, num1,a2, num2, Chr)
#def get(chr):
 #   global Entry
    # chr=Entry.get()
    # entry.get()
    # 其次，您可以将其绑定到tkinter.Variable（它使用自动生成的名称创建和包装Tcl全局变量）。通常，使用它的子类StringVar-
    # 它str在获取/设置时将值转换为。
    # v = tkinter.StringVar()
    # entry = tk.Entry(root1, textvariable=v)
    # return chr
    # global Entry
   # v = StringVar()
 #   entry = Entry(root, textvariable = v)
  #  # chr = StringVar()
 #   chr = v.get()
 #   return chr'''


make_the_gif = Button(frame7, text="Make!", font = 'consolas', command=Get_and_Make())
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
