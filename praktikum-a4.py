nim = ['2','3','1','0','3','1','0','1','6']
# nim2 = ('231031016')
print(nim[1:3])
# print(nim2[1:3])

print(f'item indeks 0 adalah {nim[0]}   ')
print(f'item indeks 4 adalah {nim[4]}   ')
print(f'item indeks terakhir adalah {nim[len(nim)-1]}')

# akses indeks negatif

print(f'item indeks terakhir {nim[-1]}')
print(f'item indeks pertama adalah {nim[-len(nim)]}')
print(f'item indeks 6 [-3] {nim[-3]}')
print(f'item indeks 4 [-5] {nim[-5]}')
print(f'item indeks 7 [-2] {nim[-2]}')

# akses indeks batas

print(f'item indeks 1,2,...: \n {nim[1:]}')
print(f'item indeks 3,4,...: \n {nim[3:]}')
print(f'item indeks 0,1,2,...: \n {nim[3:]}')
print(f'item indeks 0,1,2,3...: \n {nim[4:]}')
print(f'item indeks semua...: \n {nim[:]}')
print(f'item indeks [:8]: \n {nim[:-1]}')
print(f'item indeks [:6]: \n {nim[:-3]}')

# pengirisan

print(f'item indeks 1,2 : \n {nim[1:3]}')
print(f'item indeks 2,3,4: \n {nim[2:5]}')
print(f'item indeks kosong :\n {nim[3:3]}')
print(f'item indeks [8:8] kosong : \n {nim[-1:-1]}')
print(f'item indeks  [1:8]: \n {nim[:-1]}')
print(f'item indeks  [2:7]: \n {nim[:-2]}')

# latihan list

data = ['haikal fikri',2023,'aktif']
nilai = [90,100,96,60]

print('Nama '+ data[0], 'status kuliah' , data[2])
print('Data terbesar nilai adalah :',{max(nilai)})
print('Data terbesar nilai adalah :',{min(nilai)})
print('Data terbesar nilai adalah :',{sum(nilai)/len(nilai)})

# latihan tuple

data = ('haikal fikri',2023,'aktif')
nilai = (90,80,93,100)
print(f'jumlah nilai : {len(nilai)}\n')
print(f'Data terbesar : {max(nilai)}\n')
print(f'data terkecil : {min(nilai)}\n')
print(f'nilai  rata-rata : {sum(nilai)/len(nilai)}\n')

# latihan nested list

data = [['Haikal fikri', 2032, 'Aktif'],
        [90,87,91,90],
        [20,22],
        ['Si-reguler', 'Ganjil']
        ]

print(f'\nProgram pendidikan {data[0][0]}: {data[3][0]}\n')
print(f'Angkatan {data[0][1]}-{data[3][1]}\n')
print(f'Jumlah Nilai {data[0][0]} : adalah : {len(data[1])}\n')
print(f'Data tebesar {data[0][0]} adalah : {max(data[1])}\n')
print(f'Data terkecil nilai adalah : {min(data[1])}\n')
print(f'rata-rata nilai nilai adalah : {sum(data[1])/len(data[1])}\n')
