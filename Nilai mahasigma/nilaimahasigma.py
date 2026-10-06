import json

try:
    with open("nilaimahasigma.json", "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    data = []
except json.JSONDecodeError:
    data = []


def tambah_data(nama, nim, nilai):
    data.append({"nama": nama, "nim": nim, "nilai": nilai})
    return "data dah nambah"


def ubah_nilai(index, nilai_baru):
    data[index]["nilai"] = nilai_baru
    return "nilai diganti"


def hapus_data(index):
    data.pop(index)
    return "data dihapus"


def lihat_data():
    if not data:
        print("Data masih kosong.")
        return

    print("\nData saat ini:")
    for i, item in enumerate(data, start=1):
        print(f"{i}. nama: {item['nama']} , nim: {item['nim']} , nilai: {item['nilai']}")


def simpan_data():
    with open("nilaimahasigma.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    return "data tersimpan bos (bos,bos)"

while True:
    print("\nMenu:")
    print("1. Tambah data")
    print("2. Ubah nilai")
    print("3. Hapus data")
    print("4. Lihat data")
    print("5. Simpan data")
    print("6. Keluar")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        nama = input("nama: ")
        nim = input("nim: ")
        nilai = input("nilai: ")
        print(tambah_data(nama, nim, nilai))
    elif pilihan == "2":
        lihat_data()
        if data:
            index = int(input("pilih akun yang ingin diubah: ")) - 1
            nilai_baru = input("nilai baru: ")
            print(ubah_nilai(index, nilai_baru))
    elif pilihan == "3":
        lihat_data()
        if data:
            index = int(input("pilih akun yang ingin dihapus: ")) - 1
            print(hapus_data(index))
    elif pilihan == "4":
        lihat_data()
    elif pilihan == "5":
        print(simpan_data())
    elif pilihan == "6":
        break
    else:
        print("Pilihan tidak valid.")