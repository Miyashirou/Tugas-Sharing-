
import random as tebakan
angka = tebakan.randint(0, 100)
tebakan = angka
kesempatan = 1 
while kesempatan <= 10 :
    Inputantebakan = int(input("Masukin Tebakan Anda : "))
    if Inputantebakan>tebakan :
        print("Angka Terlalu Besar")
        kesempatan += 1
    if Inputantebakan<tebakan :
        print("Angka Terlalu Kecil")
        kesempatan += 1   
    if kesempatan >=10:
        print("Kesempatan Anda Telah Habis")
        break 
    if Inputantebakan == tebakan:
        print("Tebakan Anda benar")
        break        
    
        
    