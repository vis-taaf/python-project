import random

batas = int(input("Batas angka yang akan ditebak : "))
def tebakAngka(x):
    angka_acak = random.randint(1, x)
    tebak = 0
    guess = 0
    while tebak != angka_acak:
        tebak = int(input("Tebaklah angka yang berada di antara angka 1 hingga {} : ".format(x)))
        if tebak > batas:
            print("Maaf, angka yang anda inputkan lebih besar dari batas \n")
        elif tebak > angka_acak:
            print("Maaf, angka anda terlalu tinggi \n")
            guess += 1
        elif tebak < angka_acak:
            print("Maaf, angka anda terlalu rendah \n")
            guess += 1
    guess += 1
    print("Horee.. selamat anda berhasil menebak angka {}".format(angka_acak))
    print("Anda berhasil menebak sebanyak {} kali".format(guess))

tebakAngka(batas)