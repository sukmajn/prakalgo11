# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 05:43:53 2022

@author: Sukma Julia Nada
"""

nama_file = ""
temp_update = ""
indeks = 0


def cek_file():
    global nama_file
    while True:
        nama_file = input("Masukkan nama file: ")
        try:
            open(nama_file)
            print("")
            break
        except FileNotFoundError:
            print("File tidak ditemukan\n")


def baca_data():
    print("[1. BACA DATA]\n NAMA | PRAK 1 | PRAK 2 | PRAK 3\n--------------------------------")
    baca_data1 = open(nama_file)
    print(baca_data1.read())


def cari_rerata_prak_mhs():
    print("[2. MENCARI RATA-RATA NILAI PRAK TIAP MAHASISWA]")
    data_nilai = []
    baca_data2 = open(nama_file).readlines()
    nama = input("Masukkan nama mahasiswa: ").capitalize()
    for nilai in range(len(baca_data2)):
        data_nilai.append(baca_data2[nilai].split())
        if nama in data_nilai[nilai][0]:
            prak1, prak2, prak3 = int(data_nilai[nilai][1]), int(data_nilai[nilai][2]), int(data_nilai[nilai][3])
            print(" NAMA | PRAK 1 | PRAK 2 | PRAK 3\n--------------------------------")
            print("{} \t {} \t {} \t {}\n".format(nama, prak1, prak2, prak3))
            print("Rerata nilai praktikum {} =".format(nama), (prak1 + prak2 + prak3) / 3, "\n")
            break


def update_nilai_prak():
    global temp_update, indeks
    print("[3. UPDATE NILAI PRAK MAHASISWA]")
    data_nilai = []
    baca_data3 = open(nama_file).readlines()
    nama = input("Masukkan nama mahasiswa: ").capitalize()
    for nilai in range(len(baca_data3)):
        data_nilai.append(baca_data3[nilai].split())
        if nama in data_nilai[nilai][0]:
            indeks = nilai
            prak_ke = int(input("Ingin update nilai praktikum ke-: "))
            if 0 < prak_ke < 4:
                nilai_baru = input("Nilai baru: ")
                data_nilai[nilai][prak_ke] = nilai_baru
                prak1, prak2, prak3 = data_nilai[nilai][1], data_nilai[nilai][2], data_nilai[nilai][3]
                temp_update = "{} \t {} \t {} \t {}\n".format(nama, prak1, prak2, prak3)
                print("")
                break


def simpan_perubahan():
    print("[4. SIMPAN UPDATE NILAI]")
    baca_data4 = open("Data Nilai.txt", "r")
    data_nilai = baca_data4.readlines()
    data_nilai[indeks] = temp_update

    baca_data4 = open("Data Nilai.txt", "w")
    baca_data4.writelines(data_nilai)
    baca_data4.close()
    print("PERUBAHAN BERHASIL DISIMPAN\n")


def mulai():
    cek_file()

    while True:
        pilihan = input("MENU\n"
                        "1. Baca Data\n"
                        "2. Mencari Nilai Rata-Rata Praktikum Mahasiswa\n"
                        "3. Update Nilai Praktikum Mahasiswa\n"
                        "4. Simpan Perubahan Nilai\n"
                        "5. Exit\n"
                        "Pilih menu yang tersedia: ")
        print("")

        if pilihan == "1":
            baca_data()

        elif pilihan == "2":
            cari_rerata_prak_mhs()

        elif pilihan == "3":
            update_nilai_prak()

        elif pilihan == "4":
            simpan_perubahan()

        elif pilihan == "5":
            print("[5. EXIT]\nTERIMA KASIH!")
            break
        else:
            print("Pilih 1, 2, 3, 4 atau 5 untuk keluar\n")


if __name__ == "__main__":
    mulai()