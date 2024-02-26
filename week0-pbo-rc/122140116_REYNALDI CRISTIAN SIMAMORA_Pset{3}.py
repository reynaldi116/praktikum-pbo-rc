qq = open("Me.txt", "r")

print("Isi dari file : ")
print(qq.read())

qq = open("Me.txt", "a")
print("\nIsi file setelah di append : ")

qq.write("\nHalo, nama saya reynaldi, hobi saya mencari hobi")
qq.close()

qq = open("Me.txt", "r")
print(qq.read())

qq.close()