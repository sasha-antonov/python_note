from struct import *
import tkinter
import serial

def push_test(event):
    print('CRC')
    
    file = open("stm32l162.bin", "rb")
    read_file = file.read()
    size_file = len(read_file)
    print(size_file)
    file.close()

    syze_file_byte_1 = 0
    syze_file_byte_2 = 0
    syze_file_byte_3 = 0
    syze_file_byte_4 = 0
    
    print(size_file)
    size_file_byte_1 = size_file & 0x000000ff
    size_file_byte_2 = (size_file>>8) & 0x0000ff
    size_file_byte_3 = ((size_file>>16) & 0x00ff) 
    size_file_byte_4 = (size_file>>24)

    binfile = open('bin.bin', 'wb')
    binfile.write(pack('B', size_file_byte_4))
    binfile.write(pack('B', size_file_byte_3))
    binfile.write(pack('B', size_file_byte_2))
    binfile.write(pack('B', size_file_byte_1))
    
    data = read_file
    temp = 0xffff

    for data_n in data:
        temp ^= data_n
        for n in range(8):
            flag = temp & 1
            temp >>= 1
            if (flag==1):
                temp ^= 0xA001

    number_byte = 0
    while (number_byte < size_file):
        file_byte = read_file[number_byte]
        number_byte = number_byte + 1
        file_bin = pack('B', file_byte)
        binfile.write(file_bin)

    temp_1_byte = temp & 0x00FF
    temp_2_byte = temp>>8
    temp_1_byte = pack('B', temp_1_byte)
    temp_2_byte = pack('B', temp_2_byte)
    binfile.write(temp_1_byte)
    binfile.write(temp_2_byte)
    print('end')


def push_prog(event):
    print('push_prog')

def push_open(event):
    print('Load')
    file = open("bin.bin", "rb")
    read_file = file.read()
    size_file = len(read_file)
    file.close()

    ser.write(b'\x6C')
    data = ser.read()
    print(data)

    number_line = 0
    while(number_line < (4)): 
        x = read_file[number_line]
        number_line = number_line + 1
        print(x)
        print(number_line)
        ser.write(pack('B', x))

    data = ser.read()
    print(data)

    number_line = 4
    while(number_line < (size_file)): 
        x = read_file[number_line]
        number_line = number_line + 1
        print(x)
        print(number_line)
        ser.write(pack('B', x))

    print("end")

ser = serial.Serial('COM1', 115200, dsrdtr = 0)
file = open("stm32l162.bin", "rb")

win_1 = tkinter.Tk()
win_1.geometry('290x135')

label_1 = tkinter.Label(win_1, text='PROGRAMMER')
button_1 = tkinter.Button(win_1, text="CRC")
button_2 = tkinter.Button(win_1, text="Close")
button_3 = tkinter.Button(win_1, text='Load')

button_1.bind('<Button-1>', push_test)
button_2.bind('<Button-1>', push_prog)
button_3.bind('<Button-1>', push_open)

label_1.place(x=10, y=10)
button_1.place(x=180, y=50)
button_2.place(x=10, y=50)
button_3.place(x=85, y=70)
win_1.mainloop()













