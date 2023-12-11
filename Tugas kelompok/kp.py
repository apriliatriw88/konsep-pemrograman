#OPERATOR READ
#membuka file data.txt dengan mode read
tugas = open ("tugas.txt", "r")

#mencetak isi data.txt
print(tugas.read())

#OPERATOR APPEND
#membuka file data.txt dengan mode append untuk menambah data
tugas = open('tugas.txt','a')

#menambah kalimat
tugas.write("Belajar python \n")
tugas.write("Yuk ngerjain tugas \n")
tugas.write("Semangat nugasnya \n")
tugas.close() 

#OPERATOR WRITE
#membaca file databaru.txt dengan mode write
file = open('databaru.txt','w') 

#menulis kalimat di file databaru.txt
file.write("Belajar nulis di file \n") 
file.write("nulis di file dengan mode write \n") 
file.close() 