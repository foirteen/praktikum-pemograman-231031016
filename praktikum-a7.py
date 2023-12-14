Ubah  = 3
katasandi = 'haikal14'

while True:
    inp = input('Silahkan masukkan password : ')
    if inp != 'haikal14':
        Ubah -= 1
        print(f'Password salah!')
        print(f'anda punya {Ubah} kesempatan tersisa ')
        if Ubah == 0:
            print('anda kehabisan kesempatan!')
            break
    else:
        print('selamat datang!')
        break
