#import tkinter as tk

#master = tk.Tk()
#master.title("Program Biodata")
#tk.Label(master, text="Nama ").grid(row=0)
#tk.Label(master, text="Alamat").grid(row=1)

#e1 = tk.Entry(master)
#e2 = tk.Entry(master)

#e1.grid(row=0, column=1)
#e2.grid(row=1, column=1)

#def show_data():
#    txt_nama = "Nama Saya : %s"%(e1.get())
#    txt_alamat = "Alamat Saya : %s"%(e2.get())
#    tk.Label(master, text=txt_nama).grid(row=4, columnspan=2)
#    tk.Label(master, text=txt_alamat).grid(row=5, columnspan=2)

#bt_show = tk.Button(master, text='Show', command=show_data)
#bt_show.grid(row=3, column=0, sticky=tk.W, pady=4)

#tk.mainloop( )

import tkinter as tk

master = tk.Tk()
master.title("Menghitung Segitiga")
tk.Label(master, text="Alas").grid(row=0)
tk.Label(master, text="Tinggi").grid(row=1)
tk.Label(master, text="Sisi Miring").grid(row=2)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

def show_luas ():
    txt_alas = "alas : %s"%(e1.get())
    txt_tinggi = "tinggi : %s"%(e2.get())
    txt_luas = 0.5*int(e1.get())*int(e2.get())
    tk.Label(master, text=txt_alas).grid(row=5, columnspan=2)
    tk.Label(master, text=txt_tinggi).grid(row=6, columnspan=2)
    tk.Label(master, text=txt_luas).grid(row=7, columnspan=2)
bt_show = tk.Button(master, text='Luas', command=show_luas)
bt_show.grid(row=4, column=0, sticky=tk.W, pady=4)

def show_keliling ():
    txt_sisimiring = "sisi miring : %s"%(e3.get())
    txt_keliling = int(e3.get())+int(e3.get())+int(e3.get())
    tk.Label(master, text=txt_sisimiring).grid(row=9, columnspan=2)
    tk.Label(master, text=txt_keliling).grid(row=10, columnspan=2)
bt_show = tk.Button(master, text='Keliling', command=show_keliling)
bt_show.grid(row=8, column=0, sticky=tk.W, pady=4)

def tampilkan_semua ():
    txt_alas = "alas : %s"%(e1.get())
    txt_tinggi = "tinggi : %s"%(e2.get())
    txt_luas = 0.5*int(e1.get())*int(e2.get())
    tk.Label(master, text=txt_alas).grid(row=12, columnspan=2)
    tk.Label(master, text=txt_tinggi).grid(row=13, columnspan=2)
    tk.Label(master, text=txt_luas).grid(row=14, columnspan=2)
    txt_sisimiring = "sisi miring : %s"%(e3.get())
    txt_keliling = int(e3.get())+int(e3.get())+int(e3.get())
    tk.Label(master, text=txt_sisimiring).grid(row=15, columnspan=2)
    tk.Label(master, text=txt_keliling).grid(row=16, columnspan=2)
bt_show = tk.Button(master, text='Tampilkan semua', command=tampilkan_semua)
bt_show.grid(row=11, column=0, sticky=tk.W, pady=4)

tk.mainloop( )

