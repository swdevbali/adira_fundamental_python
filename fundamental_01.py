"""
Author: Eko
Purposes: Fundamental of Python
"""
"""
Fundamental ada tiga:
- Sequential
- Branching
- Loop / Perulangan
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
customer1_gaji = 3000000
customer1_existing = True
customer1_occupation = FIX

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

if customer2_existing:
    print(f'{customer2_nama} sedang memiliki pinjaman')

if customer3_existing:
    print(f'{customer3_nama} sedang memiliki pinjaman')