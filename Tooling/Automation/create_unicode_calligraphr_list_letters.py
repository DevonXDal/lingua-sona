start = 0xE100
count = 251

print("".join(chr(start + i) for i in range(count)))
