print("total belanja")
total_belanja=int(input("masukan total belanja : "))
if total_belanja >=5000 :
	diskon=0.1
	total=int(total_belanja*(1-diskon))
	print("total belanja", total)
else :
	total_bayar=total_belanja
	print("total bayar", total_belanja)