class User:
    nama_depan = "Adiputera"
    nama_belakang = "Indra"
    umur = 17

    def nama_lengkap(self):
        return self.nama_depan+" "+self.nama_belakang

pengguna = User()

print(pengguna.umur)
print(pengguna.nama_lengkap())