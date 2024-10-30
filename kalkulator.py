def Pembagian():
        a = input("Masukan Angka Yang Mau Di Bagi : ")
        b = input("Masukan Angka Yang Mau Di Bagi : ")
        a = int(a)
        b = int(b)
        Hasilnya = a/b
        print("\033[91m=======================================\033[0m")
        print("\033[92mHasilnya ==>>\033[0m", Hasilnya)

def Pengurangan():
        a = input("Masukan Angka Yang Mau Di Kurangi : ")
        b = input("Masukan Angka Yang Mau Di Kurangi : ")
        a = int(a)
        b = int(b)
        Hasilnya = a-b
        print("\033[91m=======================================\033[0m")
        print("\033[92mHasilnya ==>>\033[0m", Hasilnya)

def Perkalian():
        a = input("Masukan Angka Yang Mau Di Kali : ")
        b = input("Masukan Angka Yang Mau Di Kali : ")
        a = int(a)
        b = int(b)
        Hasilnya = a*b
        print("\033[91m=======================================\033[0m")
        print("\033[92mHasilnya ==>>\033[0m", Hasilnya)

def Penambahan():
        a = input("Masukan Angka Yang Mau Di Tambah : ")
        b = input("Masukan Angka Yang Mau Di Tambah : ")
        a = int(a)
        b = int(b)
        Hasilnya = a+b
        print("\033[91m=======================================\033[0m")
        print("\033[92mHasilnya ==>>\033[0m", Hasilnya)

def Menu():
        while True:
                print("\033[91m=======================================\033[0m")
                print("Pilih Operasi Yang Mau Kamu Pergunakan")     
                print("1. Pembagian")          
                print("2. Pengurangan")
                print("3. Perkalian")
                print("4. Penambahan")
                print("5. exit")
                print("\033[91m=======================================\033[0m")
                Pilihan = input ("Masukan Pilihan 1-5 : ")
                if Pilihan == '1':
                    Pembagian()
                elif Pilihan == '2':
                    Pengurangan() 
                elif Pilihan == '3':
                    Perkalian()
                elif Pilihan == '4':
                    Penambahan()               
                elif Pilihan == '5':
                    print("\033[91m-------------------------------------------\033[0m")                    
                    print("\033[92mneshlw : \033[0m")
                    print("Terimaksih Telah Mengguanakan Program ini")  
                    print("\033[91m-------------------------------------------\033[0m")                            
                    break
                else:
                    print("Tidak Valid")  
Menu()