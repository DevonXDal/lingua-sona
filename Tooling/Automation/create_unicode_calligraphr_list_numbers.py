start = 0xE1FB
count = 16 # Note that Lingua Sona was built to handle Base 2 (Binary), Base 10 (Decimal), and Base 16 (Hexadecimal) from its initial design

print("".join(chr(start + i) for i in range(count)))
