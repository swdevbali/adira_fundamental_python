"""
Author: Eko
Purposes: Fundamental of Python
"""
"""
Fundamental ada tiga:
- Sequential
- Branching
- Loop / Perulangan
- Tipe data penting: List (array) dan Dictionary (kamus/json)
- Modularization:
    - Dengan Fungsi
    - Dengan Class
    - Dengan Package    

Kasus:
Advis jenis motor bagi kustomer tertentu

Nama Program:
Customer Advisor Management System - CAMS
"""

versi = "0.1" #tipe data string/text
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

if customer1_existing:
    print(f'{customer1_nama} sedang memiliki pinjaman')
else:
    print(f'{customer1_nama} sedang tidak memiliki pinjaman')

if customer2_existing:
    print(f'{customer2_nama} sedang memiliki pinjaman')
else:
    print(f'{customer2_nama} sedang tidak memiliki pinjaman')

if customer3_existing:
    print(f'{customer3_nama} sedang memiliki pinjaman')
else:
    print(f'{customer3_nama} sedang tidak memiliki pinjaman')


#kasus customer 1 jenjang gaji: <3jt, 3jt - 6jt, 6jt - 9jt
print(f'Pengecekan gaji {customer1_nama} sebesar {customer1_gaji}')
if customer1_gaji < 3000000 :
    print('Terlalu kecil gajinya')
elif customer1_gaji >= 3000000 and customer1_gaji < 6000000:
    print('Kelas menengah')
elif customer1_gaji >= 6000000 and customer1_gaji < 9000000:
    print('Kelas atas')
else:
    print('Dewaaa')

#COBA CETAK SEMUA NAMA CUSTOMER
#tanpa list
print(customer1_nama)
print(customer2_nama)
print(customer3_nama)

#dengan list
print()
print('Daftar customers')
customers = [customer1_nama, customer2_nama, customer3_nama]
for i in range(0, len(customers)):
    print(f'{i+1}. {customers[i]}')

print(customer1_alamat)
print(customer1_alamat['Line 1'])
print(customer1_alamat['Kelurahan'])
print(customer1_alamat['Kecamatan'])
print(customer1_alamat['City'])
print(customer1_alamat['Province'])
print(customer1_alamat['Zip Code'])