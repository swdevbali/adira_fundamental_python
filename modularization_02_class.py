"""
OOP = Object Oriented Programming
OOP:
    - Encapsulation: membuat class yang terdiri dari variabel dan fungsi
    - Inheritance: encapsulation dari class yang sudah ada=> penurunan
    - Polymorphism: bentuk yang sama, akan beraksi berbeda tergantung kelas anaknya (inheritance)
"""

# ENCAPSULATION
PRIA, WANITA = range(2) #TIPE DATA ENUMERASI, konstanta sebaiknya huruf besar
NON_FIX, FIX = range(2)


# CETAKAN (class) untuk customer
class Customer:
    def __init__(self, nama, jenis_kelamin, gaji, existing, occupation, alamat): #constructor
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.gaji = gaji
        self.existing = existing
        self.occupation = occupation
        self.alamat = alamat

    def __str__(self):
        return f'{self.nama} bergaji {self.gaji}'

    def __repr__(self): #dibutuhkan tipe data string unicode
        return f'{self.nama} bergaji {self.gaji}'

    def check_status_peminjaman(self):
        if self.existing:
            print(f'{self.nama} sedang memiliki pinjaman')
        else:
            print(f'{self.nama} sedang tidak memiliki pinjaman')

    def check_gaji(self):
        result = ''
        if self.gaji < 3000000:
            result = 'Terlalu kecil gajinya'
        elif self.gaji >= 3000000 and self.gaji < 6000000:
            result = 'Kelas menengah'
        elif self.gaji >= 6000000 and self.gaji < 9000000:
            result = 'Kelas atas'
        else:
            result = 'Dewaaa'
        print(f'Pengecekan gaji {self.nama} sebesar {self.gaji}, status = {result}')


# PROSES MENCETAK KUSTOMER (OBJECT)
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


#INHERITANCE DAN POLYMORPHISM
class CustomerBandel(Customer):
    def __str__(self):
        return f'Kustomer ini Bandel: {Customer.__str__(self)}'

    def __repr__(self):
        return f'Kustomer ini Bandel: {Customer.__repr__(self)}'




customerX = CustomerBandel('WatiX', WANITA, 2000000, False, NON_FIX, {})
print(customerX)