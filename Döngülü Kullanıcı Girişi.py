print(""" 

************************
Döngülü Kullanıcı Girişi
************************


""")


g_kul = ("bkbalta2023")
g_sif = ("1995Balta")
g_hak = 3

while True:

    kullanıcı_adı = input("Kullanıcı Adı: ")
    sifre = input("Şifre: ")

    if (kullanıcı_adı == g_kul and sifre != g_sif):
        print("Şifre Yanlış!")
        g_hak -= 1
        print("Kalan Giriş Hakkınız:" , g_hak)
    elif (kullanıcı_adı != g_kul and sifre == g_sif):
        print("Kullanıcı Adı Yanlış!")
        g_hak -= 1
        print("Kalan Giriş Hakkınız:" , g_hak)
    elif (kullanıcı_adı != g_kul and sifre != g_sif):
        print("Kullanıcı Adı ve Şifre Yanlış!")
        g_hak -= 1
        print("Kalan Giriş Hakkınız:", g_hak)
    else:
        print("Sisteme Başarıyla Giriş Yaptınız")
        break
    if (g_hak == 0):
        print("Giriş Hakkınız Doldu")
        break