data = "1100"
code = [0] * 7
positions = [3, 5, 6, 7]
for i in range(4):
    code[positions[i] - 1] = int(data[i])
code[0] = code[2] ^ code[4] ^ code[6]
code[1] = code[2] ^ code[5] ^ code[6]
code[3] = code[4] ^ code[5] ^ code[6]
print("8-семинар, 5-нұсқа")
print("1-есеп. Хэмминг кодын құру")
print("Ақпараттық комбинация:", data)
print("a1 =", code[0])
print("a2 =", code[1])
print("a4 =", code[3])
print("Хэмминг коды:", "".join(map(str, code)))



print("\n2-есеп. Қатені анықтау және түзету")
code = list("0111100")
print("Бастапқы код:", "".join(code))
code[2] = "1" if code[2] == "0" else "0"
print("Қате код:", "".join(code))
bits = list(map(int, code))
e1 = bits[0] ^ bits[2] ^ bits[4] ^ bits[6]
e2 = bits[1] ^ bits[2] ^ bits[5] ^ bits[6]
e3 = bits[3] ^ bits[4] ^ bits[5] ^ bits[6]
syndrome = e1 + 2 * e2 + 4 * e3
print("E1 =", e1)
print("E2 =", e2)
print("E3 =", e3)
print("Синдром:", format(syndrome, "03b"))
print("Қате позиция:", syndrome)
if syndrome != 0:
    bits[syndrome - 1] ^= 1
print("Түзетілген код:", "".join(map(str, bits)))