print('praktikum-a2\n')

print('nama  :Achmad Haikal Fikri ')
print('kelas :SI23-A ')
print('NIM   :231031016 ')
print('Prodi :Sistem Informasi A\n\n')

# INI OPERATOR ASSIGNMENT

a = 19
print('Nilai a adalah',a)
a += 3
print('Nilai a sekarang adalah',a)

print()
a = 19
print('Nilai a adalah',a)
a -= 3
print('Nilai a sekarang adalah',a)

print()
a = 19
print('Nilai a adalah',a)
a *=2
print('Nilai a sekarang adalah',a)

print()
a = 19
print('Nilai a adalah',a)
a /= 2
print('Nilai a sekarang adalah',a)

a = 19
print('Nilai a adalah',a)
a **= 2
print('Nilai a sekarang adalah',a)


print()
a = 35
print('Nilai a adalah',a)
a %= 32
print('Nilai a sekarang adalah',a)

print()
a = 35
print('Nilai a adalah',a)
a //= 32
print('Nilai a sekarang adalah',a)


#tugas melanjutkan untuk operator selanjutnya

#OR
b = True
print('Nilai b =',b)
b|=False
print('Nilai b|=False  akan menjadi',b)
print()
#AND
b = True
print('Nilai b =',b)
b&=False
print('Nilai b&=False  akan menjadi',b)
b=False
print('Nilai b',b)
b&=False
print('Nilai b&=False  akan menjadi',b)
#XOR
b=True
print('Nilai b',b)
b^=False
print('Nilai b^=False akan menjadi',b)
b=False
print('Nilai b',b)
b^=False
print('Nilai b^=False akan menjadi',b)
#shifting
c=0b0100
print('Nilai c =',format(c, '04b'))
c>>=1
print('Nilai c>>=1 akan menjadi',format(c, '04b'))
c=0b0100
c<<=1
print('Nilai c<<=1 akan menjadi',format(c, '04b'))

#operator perbandingan


a= 9
b = 13
print('\n------ besar dari 13')
hasil = a>13
print(a,'> 13 adalah',hasil)

print('\n------ besar dari 13')
hasil = a<13
print(a,'< 13 adalah',hasil)

print('\n------ besar dari 13')
hasil = a>16
print(a,'> 16 adalah',hasil)

print('\n------ besar dari 13')
hasil = a<16
print(a,'< 16 adalah',hasil)
print('\n--------- Besar atau sama dari 13 #ujung nim')
hasil = a > 16
hasil = b > 16
print('hasil dari a', hasil)
print('hasil dari b', hasil)


print('\n--------- kecil  atau sama dari 13 #ujung nim')
hasil = a < 16
hasil = b < 16
print('hasil dari a', hasil)
print('hasil dari b', hasil)


print('\n--------- sama dari 13 #ujung nim')
hasil = a = 16
hasil = b = 16
print('hasil dari a', hasil)
print('hasil dari b', hasil)

print('\n--------- Tidak  sama dari 13 #ujung nim')
hasil = a != 16
hasil = b != 16
print('hasil dari a', hasil)
print('hasil dari b', hasil)


#operator  logika

a = True
b = False
print('\n--------AND-------')
hasil = a and a
print(a, 'and',a,'hasilnya=',hasil)

a = True
b = False
print('\n--------AND-------')
hasil = a and b
print(a, 'and',b,'hasilnya=',hasil)

a = True
b = False
print('\n--------AND-------')
hasil = b and a
print(b, 'and',a,'hasilnya=',hasil)

a = True
b = False
print('\n--------AND-------')
hasil = b and b
print(b, 'and',b,'hasilnya=',hasil)


print('\n--------OR-------')
hasil = a or a
print(a, 'or',a,'hasilnya=',hasil)

a = True
b = False
print('\n--------OR-------')
hasil = a or b
print(a, 'OR',b,'hasilnya=',hasil)

a = True
b = False
print('\n--------OR-------')
hasil = b or a
print(b, 'OR',a,'hasilnya=',hasil)

a = True
b = False
print('\n--------OR-------')
hasil = b or b
print(b, 'OR',b,'hasilnya=',hasil)

print('\n--------XOR-------')

hasil = a ^ a
print(a, 'XOR',a,'hasilnya=',hasil)

a = True
b = False
print('\n--------XOR-------')
hasil = a ^ b
print(a, 'XOR',b,'hasilnya=',hasil)

a = True
b = False
print('\n--------XOR-------')
hasil = b ^ a
print(b, 'XOR',a,'hasilnya=',hasil)

a = True
b = False
print('\n--------XOR-------')
hasil = b ^ b
print(b, 'XOR',b,'hasilnya=',hasil)

print('\n--------NOT-------')

hasil = not a
print('not',a,'hasilnya adalah=',hasil)
hasil = not b
print('not',b,'hasilnya adalah=',hasil)

#operator mwmbership
print('\n---------------IN')
nama = 'Achmad Haikal Fikri'
test = 'ri'
cek = test in nama
print(test,'terdapat di',nama,'adalah',cek)

test = 'ir'
cek = test in nama
print(test,'terdapat di',nama,'adalah',cek)
print()
test1= 'a'
test2= 'i'
test3= 'u'
test4= 'e'
test5= 'o'

cek = test1 in nama
print(test1,'terdapat di',nama,'adalah',cek)

cek = test2 in nama
print(test2,'terdapat di',nama,'adalah',cek)

cek = test3 in nama
print(test3,'terdapat di',nama,'adalah',cek)

cek = test4 in nama
print(test4,'terdapat di',nama,'adalah',cek)

cek = test5 in nama
print(test5,'terdapat di',nama,'adalah',cek)

print('\n---------------NOT IN')












