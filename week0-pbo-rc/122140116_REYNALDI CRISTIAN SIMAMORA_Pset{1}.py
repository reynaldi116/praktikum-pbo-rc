number_of_iteration = int(input("Masukkan jumlah iterasi : "))

for i in range(number_of_iteration):
  print(" " * (number_of_iteration - i - 1) + "*" * (2 * i + 1))
