grade = {}

number_of_people = int(input("Masukkan jumlah orang yang akan diinpt : "))

for i in range (number_of_people) :
  nama_mahasiswa = input("Masukkan nama mahasiswa : ")
  nilai_mahasiswa = int(input("Masukkan nilai mahasiswa : "))
  grade[nama_mahasiswa] = nilai_mahasiswa

print(grade)