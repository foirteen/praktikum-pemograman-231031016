nama = 'nama lengkap'
nim  = '231031016'
meet = 'praktikum 3'
prodi = 'sistem informasi A'
email = 'achmadhaikal1405@gmail.com'
 
sp = 40
print('-'*sp)
print(nama.upper().center(sp))
print(nim.center(sp))
print('\n'*2)
print(meet.capitalize().rjust(sp))
print(prodi.title().rjust(sp))
print(email.rjust(sp))
print('-'*sp)



Nama = 'Achmad haikal fikri'
NIM = '231031016'
meet = 'Praktikum 3'
Prodi = 'Sistem Informasi'
TTL = 'Makassar, 14-mei-2005'
Alamat = 'Bumi Lestari'
Asal = 'Makassar'
Hobi = 'Game'
Tinggi= '163'

print(f'''Halo,nama saya {Nama} dengan NIM {NIM} dari prodi {Prodi},ini adalah file {meet.capitalize()}. Terima kasih''') 

print(f'''Biodata saya,
Nama\t: {Nama.title()}
Nim\t: {NIM}
Prodi\t: {Prodi.title()}
TTL\t: {TTL}
Alamat\t: {Alamat}
Asal\t: {Asal}
Hobi\t: {Hobi}
inggi\t: {Tinggi}cm      
        ''')
stat = 'sir issac newton'
up = stat.upper()
print(up)
up = up.split()
print(up)
print(up[2][0],up[0],up[1])

print(up[2],up[0] [0],up[1] [0])



stat2 = '&sir$ @issac# *newton.'
up2 = stat2.upper()
print(up2)
up2 = up2.split()
print(up2[0] [1:-1],up2[1][1:-1],up2[2] [1:-1])
print(up2[0].strip('&$'),up2[1].strip('@#'),up2[2].strip('*.'))

