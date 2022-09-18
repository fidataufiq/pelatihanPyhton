def penjumlahan():
  angka1 = int(input("Masukkan Angka => "))
  angka2 = int(input("Masukkan Angka => "))
  operator = input("Masukkan operator => ")
  if(operator == "+"):
    hasil = angka1+angka2
    print("Hasil", angka1, "+", angka2, "=", hasil)
  elif(operator == "-"):
    hasil = angka1-angka2
    print("Hasil", angka1, "-", angka2, "=", hasil)
  else:
    print("Else")
penjumlahan()