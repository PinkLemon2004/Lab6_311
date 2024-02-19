from tkinter import *
def mainwindow():
    root = Tk()
    x = root.winfo_screenwidth() / 2 - (w / 2)
    y = root.winfo_screenheight() / 2 - (h / 2)
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))
    root.title("LAB6:Sweety Bakery Shop By Rujira Navaen")
    root.option_add('*font', 'Garamond 16 bold')
    menubar = Menu(root)
    menubar.add_command(label="Menu", command=loadwd1)
    menubar.add_command(label="Checkout", command=loadwd2)
    menubar.add_command(label="Exit", command=root.quit)
    root.config(bg="pink", menu=menubar)
    root.resizable(False, False)
    #ประกาศค่าในลิสต์ เพื่อเอาไปใช้ลูป
    menu_list = ['Strawberry Cake', 'Cheese Cake', 'Strawberry Mixed', 'Orange Mixed']
    price_list = ['85', '95', '120', '140']
    spin_vars = [IntVar() for _ in menu_list]  # Move this line here
    return root, menu_list, price_list, spin_vars
#หน้าแรก
def mainwin(root):
    bgm = Label(root, image=img1, bg="#FFFFFF")
    bgm.place(x=0, y=0, width=w, height=h)

    tm = Label(root, text='....Welcome to my restaurant....', bg='#FFFFFF')
    tm.place(x=200, y=650)
#sหน้าซื้อของ
def loadwd1():
    frm1 = Frame(root, bg="#FFFFFF") #ตั้งค่าหน้า
    frm1.place(x=0, y=0, width=w, height=h)
    frm1.columnconfigure((0, 1), weight=1)
    #เก็บรูปภาพไว้ในลิสต์เพื่อใช้ลูป
    img_list = [img2, img3, img4, img5]
    spinboxes = [] #ลิสต์ว่างเอาไว้เก็บค่าเพื่อคำนวณ
#ลูปเมนูสินค้า ทั้ง 4 ชิ้น ทั้งชื่อเมนู รูปภาพ ราคา การเพิ่มจำนวน
    for index, (title, img, price, spin_var) in enumerate(zip(menu_list, img_list, price_list, spin_vars)):
        row = index // 2 * 4 
        col = index % 2
        #ชื่อเมนู
        label = Label(frm1, text=title, font=('Garamond', 16, 'bold'),bg='#5E2D2D',width=15,fg="#FFFFFF")
        label.grid(row=row, column=col, padx=5, pady=10)
        #ภาพสินค้า
        imagmenu = Label(frm1, image=img)
        imagmenu.grid(row=row + 1, column=col, padx=1, pady=5)
        #เพิ่มจำนวนสินค้าที่ต้องการซื้อ
        spinbox = Spinbox(frm1, textvariable=spin_var, from_=0, to=10, width=5)
        spinbox.grid(row=row + 2, column=col, padx=1, pady=5)
        spinboxes.append(spinbox)
        #ราคาของสินค้า
        price_label = Label(frm1, text=('Price:', price), font=('Garamond', 11, 'bold'))
        price_label.grid(row=row + 3, column=col, padx=1, pady=25)
    return spinboxes

def loadwd2():
    frm2 = Frame(root, bg="#FFFFFF")
    frm2.place(x=0, y=0, width=w, height=h)
    frm2.columnconfigure((0, 1, 2, 3), weight=1)
    #ลูปหัวข้อ
    titlelist = ['Menu list', 'Amount', 'Price', 'Total (Bahts)']
    for index, title in enumerate(titlelist):
        label = Label(frm2, text=title, font=('Garamond', 11, 'bold'),fg='#FFFFFF',bg='#5E2D2D',width=25)
        label.grid(row=0, column=index, padx=5, pady=5)

    total = 0 # เซ้ทค่ายอดรวม
    #ลูปผลการคำนวณให้ออกมาโชวที่หน้า2
    for index, (title, price, spinbox) in enumerate(zip(menu_list, price_list, spin_vars)):
        # ชื่อสินค้าทั้ง4
        label = Label(frm2, text=title, font=('Garamond', 11, 'bold'),bg='#EBD7D7',width=25)
        label.grid(row=index + 1, column=0, padx=5, pady=5)
        #จำนวนที่สั่งซื้อ
        amount_label = Label(frm2, textvariable=spinbox, font=('Garamond', 11, 'bold'),bg='#EBD7D7',width=25)
        amount_label.grid(row=index + 1, column=1, padx=5, pady=5)
        #ราคาต่อชิ้น
        price_label = Label(frm2, text=price, font=('Garamond', 11, 'bold'),bg='#EBD7D7',width=25)
        price_label.grid(row=index + 1, column=2, padx=5, pady=5)
        #เก็บค่าจำนวนสินค้า
        quantity = int(spinbox.get())  # Get the quantity from the Spinbox
        #คำนวณผล ราคารวมสิ้นค่า 1 อย่าง
        total_product = quantity * int(price)  # Calculate the total for the current product
        total += total_product
        #แสดงผล
        total_label = Label(frm2, text=('Total:',total_product), font=('Garamond', 11, 'bold'),bg='#EBD7D7',width=25)
        total_label.grid(row=index + 1, column=3, padx=5, pady=5)
    #ผลรวมสินค้าทั้งหมด
    total_label = Label(frm2, text=('Total:',total), font=('Garamond', 11, 'bold'),bg='#99F3C9',width=25)
    total_label.grid(row=len(menu_list) + 1, column=0, columnspan=4, padx=5, pady=5)

w = 700
h = 700
root, menu_list, price_list, spin_vars = mainwindow()
img1 = PhotoImage(file='images/myshop.png')
img2 = PhotoImage(file='images/cake1.png')
img3 = PhotoImage(file='images/cake2.png')
img4 = PhotoImage(file='images/drink1.png')
img5 = PhotoImage(file='images/drink2.png')
mainwin(root)
root.mainloop()