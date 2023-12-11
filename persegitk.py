import tkinter as tk

master = tk.Tk()
master.title("Menghitung Persegi Panjang")
tk.Label(master, text="Panjang").grid(row=0)
tk.Label(master, text="Lebar").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

def show_luas () :
    txt_panjang = "panjang : %s"%(e1.get())
    txt_lebar = "lebar : %s"%(e1.get())
    txt_luas = int(e1.get())*int(e2.get())
    tk.Label(master, text=txt_panjang).grid(row=4, columnspan=2)
    tk.Label(master, text=txt_lebar).grid(row=5, columnspan=2)
    tk.Label(master, text=f"luas : {txt_luas}").grid(row=6, columnspan=2)
bt_show = tk.Button(master, text='Luas', command=show_luas)
bt_show.grid(row=3, column=0, sticky=tk.W, pady=4)

def show_keliling () :
    txt_panjang = "panjang : %s"%(e1.get())
    txt_lebar = "lebar : %s"%(e1.get())
    txt_keliling = 2*(int(e1.get())+int(e2.get()))
    tk.Label(master, text=txt_panjang).grid(row=8, columnspan=2)
    tk.Label(master, text=txt_lebar).grid(row=9, columnspan=2)
    tk.Label(master, text=f"keliling : {txt_keliling}").grid(row=10, columnspan=2)
bt_show = tk.Button(master, text='Keliling', command=show_keliling)
bt_show.grid(row=7, column=0, sticky=tk.W, pady=4)

tk.mainloop( )

