# variable global untuk menyimpan data bu
buku = []

# fungsi menampilkan data
def show_data():
    if len(buku) <= 0:
        print("BELUM ADA DATA")
    else:
        for index in range(len(buku)):
            print(("[%d] %s" % (index, buku[index])))

# fungsi untuk tambah data
def insert_data():
    buku_baru = input("Judul Buku: ")
    buku.append(buku_baru)

# fungsi edit
def edit_data():
    show_data()
    index = eval(input("Masukkan ID buku: "))
    if(index > leng(buku)):
        print("ID salah")
    else:
        judul_baru = input("Judul Baru: ")
        buku[index] = judul_baru

# fungsi hapus data
def delete_data():
    show_data()
    index = eval(input("Masukkan ID buku: "))
    if(index > len(buku)):
        print("ID salah")
    else:
        buku.remove(buku[index])

# fungsi tampilkan menu
def show_menu():
    print("\n")
    print("-------------- MENU --------------")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit")

    menu = eval(input("PILIH MENU> "))
    print("\n")

    if menu == 1:
        show_data()
    elif menu == 2:
        insert_data()
    elif menu == 3:
        edit_data()
    elif menu == 4:
        delete_data()
    elif menu == 5:
        exit()
    else:
        print("Salah Pilih!")

if __name__ == "__main__":
    while(True):
        show_menu()