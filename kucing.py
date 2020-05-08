namaKucing = []
while True:
    nomor = 1
    print ('Enter the name of cat ' + str(len(namaKucing)+  1) + ' or enter nothing to stop.' )
    nama = input()
    if nama == '':
        break
    namaKucing = namaKucing + [nama]

print('Nama kucingnya :')
for nama in namaKucing:
    print (' ' + nama)
