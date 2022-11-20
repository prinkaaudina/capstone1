dataNama = [
    {
        'ID' : 1234,
        'Nama' : 'Anggun',
        'Email' : 'anggun@gmail.com',
        'Alamat' : 'Jl. Anggrek No.1',
        'Telp' : '08123456789'
    },
    {   'ID' : 1235,
        'Nama' : 'Budi',
        'Email' : 'budi@gmail.com',
        'Alamat' : 'Jl. Bambu No.1',
        'Telp' : '08123456781'
    },
    {
        'ID' : 1236,
        'Nama' : 'Clara',
        'Email' : 'clara@gmail.com',
        'Alamat' : 'Jl. Cemara No.1',
        'Telp' : '08123456782'
    },
    {
        'ID' : 1237,
        'Nama' : 'Didi',
        'Email' : 'didi@gmail.com',
        'Alamat' : 'Jl. Damar No.1',
        'Telp' : '08123456783'
    },
    {
        'ID' : 1238,
        'Nama' : 'Elsa',
        'Email' : 'elsa@gmail.com',
        'Alamat' : 'Jl. Elang No.1',
        'Telp' : '08123456784'
    }
]

    

def daftarNama ():
    print('Daftar Nama\n')
    print('ID\t| Nama  \t| Email \t\t| Alamat \t\t| Telp')
    for i in range(len(dataNama)) :
        print('{}\t| {}  \t| {}\t| {}\t| {}'.format(dataNama[i]['ID'],dataNama[i]['Nama'],dataNama[i]['Email'],dataNama[i]['Alamat'],dataNama[i]['Telp']))

def cariNama ():
    idNama = int(input('Masukkan ID nama yang ingin Anda cari: '))
    exist = True
    for j in dataNama:
        if j['ID'] == idNama:
            indexData = dataNama.index(j)
            exist = True
            print('Data pada Yellow Pages: \n')
            print('ID\t| Nama  \t| Email \t\t| Alamat \t\t| Telp')
            print('{}\t| {}  \t| {}\t| {}\t| {}'.format(dataNama[indexData]['ID'],dataNama[indexData]['Nama'],dataNama[indexData]['Email'],dataNama[indexData]['Alamat'],dataNama[indexData]['Telp']))
            break
        else:
            exist = False
    if exist == False: 
        print('\nData tidak ditemukan!\n')          

def tambahNama ():
    idNama = int(input('Masukkan ID: '))
    for j in dataNama:
        if j['ID'] == idNama:
            print('\nData sudah ada!\n')
            break
        else:
            nama = input('Masukkan Nama: ')
            email = input('Masukkan Alamat Email: ')
            alamat = input('Masukkan Alamat: ')
            telp = input('Masukkan Nomor Telp: ')
            
            simpan = input('Apakah data baru mau disimpan (y/n)?')
            if simpan == 'y':
                print('\nData tersimpan!\n')
                dataNama.append({
                    'ID': idNama,
                    'Nama' : nama,
                    'Email': email,
                    'Alamat': alamat,
                    'Telp' : telp
                })
        daftarNama()
        break

def hapusNama ():
    daftarNama()
    idNama = int(input('Masukkan ID yang ingin dihapus: '))
    exist = True
    for j in dataNama:
        if j['ID'] == idNama:
            indexData = dataNama.index(j)
            exist = True
            ragu = input('Apakah Anda sungguh mau menghapus data (y/n)?')
            if ragu == 'y':
                del dataNama[indexData]
                print ('\nData telah dihapus!\n')
                daftarNama()
            else:
                daftarNama()
            break
        else: 
            exist = False
    if exist == False:
        print('\nData tidak ditemukan!\n')         

def updateNama() :
    while True:
        idNama = int(input('Masukkan ID nama data yang ingin diganti: '))
        exist = True
        for j in dataNama:
            if j['ID'] == idNama:
                indexData = dataNama.index(j)
                exist = True
                print('Data pada Yellow Pages: \n')
                print('ID\t| Nama  \t| Email \t\t| Alamat \t\t| Telp')
                print('{}\t| {}  \t| {}\t| {}\t| {}'.format(dataNama[indexData]['ID'],dataNama[indexData]['Nama'],dataNama[indexData]['Email'],dataNama[indexData]['Alamat'],dataNama[indexData]['Telp']))
                break
            else:
                exist = False
        if exist == False: 
            print('\nData tidak ditemukan!\n')          
        update = int(input('''
            Data apakah yang ingin Anda update?
            
            1. Nama
            2. Email
            3. Alamat
            4. Telp
            5. Semua Data
            
            Masukkan angka Menu yang ingin dijalankan: '''))
        if update == 1:
            nama = input('Masukkan Nama: ')
            simpan = input('Apakah data mau diperbaharui (y/n)?')
            if simpan == 'y':
                print('\nData telah diperbaharui!\n')
                for j in dataNama:
                    if j['ID'] == idNama:
                        indexData = dataNama.index(j)
                        dictNama = dataNama[indexData]
                        dictNama['Nama'] = nama
                        daftarNama()
                        break
            break
        elif update == 2:
            email = input('Masukkan Email: ')
            simpan = input('Apakah data mau diperbaharui (y/n)?')
            if simpan == 'y':
                print('\nData telah diperbaharui!\n')
                for j in dataNama:
                    if j['ID'] == idNama:
                        indexData = dataNama.index(j)
                        dictNama = dataNama[indexData]
                        dictNama['Email'] = email
                        daftarNama()
                        break
            break
        elif update == 3:
            alamat = input('Masukkan Alamat: ')
            simpan = input('Apakah data mau diperbaharui (y/n)?')
            if simpan == 'y':
                print('\nData telah diperbaharui!\n')
                for j in dataNama:
                    if j['ID'] == idNama:
                        indexData = dataNama.index(j)
                        dictNama = dataNama[indexData]
                        dictNama['Alamat'] = alamat
                        daftarNama()
                        break
            break
        elif update == 4:
            telp = input('Masukkan Nomor Telepon: ')
            simpan = input('Apakah data mau diperbaharui (y/n)?')
            if simpan == 'y':
                print('\nData telah diperbaharui!\n')
                for j in dataNama:
                    if j['ID'] == idNama:
                        indexData = dataNama.index(j)
                        dictNama = dataNama[indexData]
                        dictNama['Telp'] = telp
                        daftarNama()
                        break
            break
        elif update == 5:
            nama = input('Masukkan Nama: ')
            email = input('Masukkan Email: ')
            alamat = input('Masukkan Alamat: ')
            telp = input('Masukkan Nomor Telepon: ')
            simpan = input('Apakah data mau diperbaharui (y/n)?')
            if simpan == 'y':
                print('\nData telah diperbaharui!\n')
                for j in dataNama:
                    if j['ID'] == idNama:
                        indexData = dataNama.index(j)
                        dictNama = dataNama[indexData]
                        dictNama['Nama'] = nama
                        dictNama['Email'] = email
                        dictNama['Alamat'] = alamat
                        dictNama['Telp'] = telp
                        daftarNama()
                        break
            break   

def utama ():
    while True :
            menuUtama = input('''
                Selamat Datang di Yellow Pages

                Pilihan Menu:
                1. Menampilkan Data
                2. Menambahkan Data Baru
                3. Mengupdate Data
                4. Menghapus Data
                5. Exit Program

                Masukkan angka Menu yang ingin dijalankan: ''')

            while (menuUtama == '1') :
                satu = int(input('''
                    Selamat Datang di Menu Menampilkan Data

                    Pilihan Menu:
                    1. Tampilkan seluruh data
                    2. Tampilkan salah satu data saja
                    3. Kembali ke Menu Utama
            
                    Masukkan angka Menu yang ingin dijalankan: '''))
                if satu == 1:
                    daftarNama()
                elif satu == 2:
                    cariNama()
                elif satu == 3:
                    utama()
                    break
            
            while (menuUtama == '2') :
                dua = input('''
                    Selamat Datang di Menu Menambahkan Data Baru
            
                    Apakah Anda ingin menambahkan data baru (y/n)? ''')
                if dua == 'y':
                    tambahNama()
                elif dua == 'n':
                    utama()
                    break
            
            while (menuUtama == '3') :
                tiga = input('''
                    Selamat Datang di Menu Update Data
                    
                    Apakah ada data yang ingin Anda update (y/n)? ''')
                if tiga == 'y':
                    updateNama()
                elif tiga == 'n':
                    utama()
                    break

            while (menuUtama == '4') :
                empat = input('''
                    Selamat Datang di Menu Penghapusan Data
            
                    Apakah Anda ingin menghapus data (y/n)? ''')
                if empat == 'y':
                    hapusNama()
                elif empat == 'n':
                    utama()
                    break

            while (menuUtama == '5'):
                exit()

            else:
                False
                print('\nPilihan yang Anda Masukkan Salah!\n')
                utama()

            break
        
        
utama()