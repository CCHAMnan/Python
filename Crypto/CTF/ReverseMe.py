data = bytearray.fromhex('43544B806B357A73696436715F61683531633832317D')
for i in range(2, 11):
    data[i] -= 5
data[11] += 3
print(data.decode('unicode_escape'))