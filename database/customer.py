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