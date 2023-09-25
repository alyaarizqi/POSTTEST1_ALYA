#program membuat login sederhana dan percabangan volume bangun ruang (bola, tabung, limas segitiga)

print("program login sederhana")
print("-----------------------")


# Fungsi menghitung volume bola
def hitung_volume_bola(jari_jari):
    return (4/3) * 3.14 * jari_jari ** 3 #rumus volume bola

# Fungsi menghitung volume tabung
def hitung_volume_tabung(jari_jari, tinggi):
    return 3.14 * jari_jari ** 2 * tinggi #rumus volume tabung dengan phi 3.14
# Fungsi menghitung volume limas segitiga
def hitung_volume_limas_segitiga(alas, tinggi):
    return (1/3) * (1/2 * alas) * tinggi #rumus volume limas segitiga

# Fungsi login
def login():
    nama = "alya_rizqi"
    nim = "2309116008"
#Memasukkan Nama dan NIM
    inputNama = input("Masukkan Nama: ")
    inputPassword = input("Masukkan NIM: ")

#Tampilan saat login berhasil atau gagal
    if inputNama == nama and inputPassword == nim:
        print("Login berhasil!\n")
        return True
    else:
        print("Login gagal. Nama atau NIM salah.\n")
        return False

#Tampilan saat login berhasil,muncul pilihan operasi bangun datar
while True:
    print("Selamat datang di Program Menghitung Volume Bangun Ruang")
    if login():
        print("Pilih bangun ruang yang ingin dihitung:")
        print("1. Bola")
        print("2. Tabung")
        print("3. Limas Segitiga")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan == "1":
            jari_jari = float(input("Masukkan jari-jari bola: "))
            volume = hitung_volume_bola(jari_jari)
            print(f"Volume bola adalah {volume:.2f} satuan kubik\n")
        elif pilihan == "2":
            jari_jari = float(input("Masukkan jari-jari tabung: "))
            tinggi = float(input("Masukkan tinggi tabung: "))
            volume = hitung_volume_tabung(jari_jari, tinggi)
            print(f"Volume tabung adalah {volume:.2f} satuan kubik\n")
        elif pilihan == "3":
            alas = float(input("Masukkan panjang alas segitiga: "))
            tinggi = float(input("Masukkan tinggi limas segitiga: "))
            volume = hitung_volume_limas_segitiga(alas, tinggi)
            print(f"Volume limas segitiga adalah {volume:.2f} satuan kubik\n")
        elif pilihan == "4":
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.\n")
