import function

haikal = True
while haikal:
    function.judul()

    panjang, lebar = function.inputan()

    # luas dan lebar
    kel, luas = function.hitung(panjang, lebar)

    # Display
    function.tampil('luas', luas)
    function.tampil('keliling', kel)

    a = function.pilihan()