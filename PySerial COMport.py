import serial

ser = serial.Serial('COM1', 9600, dsrdtr = 0, timeout = 1)
# timeout - если соединение не установится, то через 1 сек. произойдет разъединение
# dsr/dtr (готовность источника/приемника) выполнена аппаратно

ser.write(b'\xFF')
input_data = ser.read()
ser.close
