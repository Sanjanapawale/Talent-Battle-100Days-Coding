num = int(input("Enter the number of people present in a room: "))
handshake = 0
for i in range(1, num):
    handshake += i
print("Total handshakes: ", handshake)