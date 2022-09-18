from ast import operator


angka1 = int(input("Masukkan Angka =>"))
angka2 = int(input("Masukkan Angka =>"))
operator = input("Masukkan opertor =>")
if(operator == "+"):
    hasil = angka1+angka2
    print("Hasil", angka1,"+", angka2,"=", hasil)
elif(operator == "-"):
    hasil = angka1-angka2
    print("Hasil", angka1,"-", angka2,"=", hasil)