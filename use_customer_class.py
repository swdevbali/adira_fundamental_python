from database.customer import Customer

PRIA, WANITA = range(2) #TIPE DATA ENUMERASI, konstanta sebaiknya huruf besar
NON_FIX, FIX = range(2)

customer1 = Customer('Budi', PRIA, 30000000, True, FIX, {
    'Line 1': 'Glagah Kidul RT 3',
    'Kelurahan': 'Tamanan',
    'Kecamatan': 'Banguntapan',
    'City': 'Bantul',
    'Province': 'Yogyakarta',
    'Zip Code': '55191',
    'Country': 'Indonesia'
})
customer2 = Customer('Wati', WANITA, 6000000, False, NON_FIX, {})
customer3 = Customer('Paman', PRIA, 9000000, True, FIX, {})

print(customer1)
print(customer2)
print(customer3)

customer1.check_status_peminjaman()
customer1.check_gaji()
