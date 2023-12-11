import tkinter as tk


# master = tk.Tk()
# master.title("Program Menampilkan Nama Lengkap")


# tk.Label(master, text="Nama Depan                  :").grid(row=0)
# tk.Label(master, text="Nama Tengah                :").grid(row=1)
# tk.Label(master, text="Nama Belakang             :").grid(row=2)

# namad = tk.Entry(master)
# namat = tk.Entry(master)
# namab= tk.Entry(master)

# namad.grid(row=0, column=2)
# namat.grid(row=1, column=2)
# namab.grid(row=2, column=2)

# def namalengkap():
#     namaa = 'Nama Saya : %s'%(namad.get())+(' ')+(namat.get())+(' '+(namab.get()))
#     #lengkap=(namad.get(    )+namat.get(   )+namab.get(  ))
#     #hasil=f'Nama Saya  : {lengkap}'
#     tk.Label(master, text=namaa).grid(row=4, column=1)
# bt_show=tk.Button(master,text='show', command=namalengkap)
# bt_show.grid(row=3, column=0, sticky=tk.W, pady=4)
# tk.mainloop()

master = tk.Tk()
master.title('mahasiswa')

tk.Label(master, text='nama : ').grid(row=0)
tk.Label(master, text='nim : ').grid(row=1)
tk.Label(master, text='prodi : ').grid(row=2)

nam= tk.Entry(master)
n=tk.Entry(master)
pd=tk.Entry(master)

nam.grid(row=0, column=2)
n.grid(row=1, column=2)
pd.grid(row=2, column=2)

def tampil():
    txt_nama = 'nama : %s'%(nam.get())
    txt_nim = 'nim : %s'%(n.get())
    txt_pd = 'prodi : %s'%(pd.get())
    tk.Label(master, text=txt_nama).grid(row=4, columnspan=2)
    tk.Label(master, text=txt_nim).grid(row=5, columnspan=2)
    tk.Label(master, text=txt_pd).grid(row=6, columnspan=2)

btampil = tk.Button(master, text='tampil', command=tampil)
btampil.grid(row=3, column=0, sticky=tk.W, pady=4)

tk.mainloop()


# versi output diterminal
master = tk.Tk()
master.title('mahasiswa')

tk.Label(master, text='nama : ').grid(row=0)
tk.Label(master, text='nim : ').grid(row=1)
tk.Label(master, text='prodi : ').grid(row=2)

nam= tk.Entry(master)
n=tk.Entry(master)
pd=tk.Entry(master)

nam.grid(row=0, column=2)
n.grid(row=1, column=2)
pd.grid(row=2, column=2)

def tampil():
    print('nama : %s'%(nam.get()))
    print('nim : %s'%(n.get()))
    print('prodi : %s'%(pd.get()))


btampil = tk.Button(master, text='tampil', command=tampil)
btampil.grid(row=3, column=0, sticky=tk.W, pady=4)

tk.mainloop()