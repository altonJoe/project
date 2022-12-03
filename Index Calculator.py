import os

def clear():
    os.system("cls")

listnilai = [
    {'mat' : 0,
    'fis' : 0,
    'kim' : 0}
]

def mat():
    clear()
    jumlah = 0 
    uts = float(input("Nilai UTS\t\t: "))
    bkuis = int(input("Banyak kuis??  "))
    kuis = 0
    for i in range(bkuis):
        nil = float(input(f"Nilai Kuis {i+1}\t\t: "))
        kuis += nil
    lain = float(input("Nilai tugas lain\t: "))
    jumlah += ((uts*0.375)+(kuis/bkuis)*0.15+lain) 
    listnilai[0]['mat'] = (80-jumlah)/0.375
    print(f"Nilai UAS yang dibutuhkan untuk dapat A: {listnilai[0]['mat']:.2f}")
    while True: 
        balik = input("\n\nBalik (y/n)?? ")
        if balik == "y":
            home()
        elif balik == "n":
            quit()
def fis():
    clear()
    jumlah = 0 
    uts = float(input("Nilai UTS\t\t: "))
    bprak = int(input("Banyak Praktikum??  "))
    prak = 0
    for i in range(bprak):
        nila = float(input(f"Nilai Pratikum {i+1}\t\t: "))
        prak += nila
    rbl = float(input("Nilai RBL\t: "))
    lain = float(input("Nilai tugas lain\t: "))
    jumlah += ((uts*0.3)+prak*0.2 + rbl*0.1 + lain*0.1)
    listnilai[0]['fis'] = (75-jumlah)/0.3
    print(f"Nilai UAS yang dibutuhkan untuk dapat A: {listnilai[0]['fis']:.2f}")
    while True: 
        balik = input("\n\nBalik (y/n)?? ")
        if balik == "y":
            home()
        elif balik == "n":
            quit()
def kim():
    clear()
    jumlah = 0 
    uts = float(input("Nilai UTS\t\t: "))
    bkuis = int(input("Banyak kuis??  "))
    kuis = 0
    for i in range(bkuis):
        nil = float(input(f"Nilai Kuis {i+1}\t\t: "))
        kuis += nil
    bprak = int(input("Banyak Praktikum??  "))
    prak = 0
    for i in range(bprak):
        nila = float(input(f"Nilai Pratikum {i+1}\t\t: "))
        prak += nila
    jumlah += ((uts*0.35)+(kuis/bkuis)*0.1+prak*0.2)
    listnilai[0]['fis'] = (75-jumlah)/0.35 
    print(f"Nilai UAS yang dibutuhkan untuk dapat A: {listnilai[0]['kim']:.2f}")
    while True: 
        balik = input("\n\nBalik (y/n)?? ")
        if balik == "y":
            home()
        elif balik == "n":
            quit()
def cek():
    clear()
    print(f"List nilai yang dibutuhkan di UAS agar mendapatkan nilai A\nMatematika\t: {listnilai[0]['mat']:.2f}\nFisika\t\t: {listnilai[0]['fis']:.2f}\nKimia\t\t: {listnilai[0]['kim']:.2f}")
    while True: 
        balik = input("\n\nBalik (y/n)?? ")
        if balik == "y":
            home()
        elif balik == "n":
            quit()

def home():
    clear()
    while True: 
        pilihan = input("""Hallooo ＼(^▽^\＠)\ノ
Pilih Matkul: 
1. Matematika Dasar 
2. Fisika Dasar
3. Kimia Dasar
69. Cek 
-> """)
        if pilihan == "1": 
            mat()
        elif pilihan == "2":
            fis()
        elif pilihan == "3":
            kim()
        elif pilihan == "69":
            cek()
        
home()