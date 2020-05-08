import random
angka = random.randint(1,20)

print ('Saya mikirin satu angka nih (1-20)')
print ('Coba tebak')

for tebakan in range(1,7):
    print ('Yuk Tebak ' + str(tebakan) + '/7')
    tebakanangka = int(input())

    if tebakanangka < angka:
        print ('Terlalu kecil')
    elif tebakanangka > angka:
        print ('Kegedean bosq')
    else:
        break

if tebakanangka == angka:
    print ('Antum benar. Percobaan ke-' + str(tebakan) + "/7.")
else:
    print ('Salah bosq. Yang bener ' + str(angka) + '.')
