"""
Modularisasi:

- Functions
- Class
- Package => PIP => VirtualEnvironment
"""

"""
Author: Eko
Purposes: Fundamental of Python
"""
versi = "0.15" #tipe data string/text
nama_program = 'Customer Advisor Management System'
author = 'Eko Wibowo'

PRIA, WANITA = range(2) #TIPE DATA ENUMERASI, konstanta sebaiknya huruf besar
NON_FIX, FIX = range(2)

customer1_nama = 'Budi'
customer1_jenis_kelamin = PRIA
customer1_gaji = 30000000
customer1_existing = True
customer1_occupation = FIX
customer1_alamat = {
    'Line 1': 'Glagah Kidul RT 3',
    'Kelurahan': 'Tamanan',
    'Kecamatan': 'Banguntapan',
    'City': 'Bantul',
    'Province': 'Yogyakarta',
    'Zip Code': '55191',
    'Country': 'Indonesia'
}

customer2_nama = 'Wati'
customer2_jenis_kelamin = WANITA
customer2_gaji = 6000000
customer2_existing = False
customer2_occupation = NON_FIX

customer3_nama = 'Paman'
customer3_jenis_kelamin = PRIA
customer3_gaji = 9000000
customer3_existing = True
customer3_occupation = FIX

print(f'{nama_program} versi {versi} oleh {author}')

#FUNGSI PENGECEKAN STATUS PEMINJAMAN
def check_status_peminjaman(nama, is_existing):
    if is_existing:
        print(f'{nama} sedang memiliki pinjaman')
    else:
        print(f'{nama} sedang tidak memiliki pinjaman')

check_status_peminjaman(customer1_nama, customer1_existing)
check_status_peminjaman(customer2_nama, customer2_existing)
check_status_peminjaman(customer2_nama, customer2_existing)

#FUNGSI PENGECEKAN GAJI

def check_gaji(name, gaji):
    result = ''
    if gaji < 3000000 :
        result = 'Terlalu kecil gajinya'
    elif gaji >= 3000000 and gaji < 6000000:
        result = 'Kelas menengah'
    elif gaji >= 6000000 and gaji < 9000000:
        result = 'Kelas atas'
    else:
        result = 'Dewaaa'
    print(f'Pengecekan gaji {name} sebesar {gaji}, status = {result}')

check_gaji(customer1_nama, customer1_gaji)
check_gaji(customer2_nama, customer2_gaji)
check_gaji(customer3_nama, customer3_gaji)