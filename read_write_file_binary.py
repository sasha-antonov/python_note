from struct import *

file = open("stm32l162.bin", "rb")
read_file = file.read()
size_file = len(read_file)
file.close()

number_byte = 0
binfile = open('bin.dat', 'wb')

while(number_byte < size_file):
    file_byte = read_file[number_byte]
    number_byte = number_byte + 1
    file_bin = pack('B', file_byte)
    binfile.write(file_bin)

binfile.write(b'\xff')
print('end')

binfile.close()