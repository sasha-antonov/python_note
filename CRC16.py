data = [0x01, 0x01]
temp = 0xffff


for data_n in data:
    temp ^= data_n
    print(temp.to_bytes(2, 'big'))
    for n in range(8):
        flag = temp & 1
        print(flag.to_bytes(2, 'big'))
        temp >>= 1
        print(temp.to_bytes(2, 'big'))
        if (flag==1):
            temp ^= 0xA001
            print(temp.to_bytes(2, 'big'))

print(temp.to_bytes(2, 'big'))
print(temp)

