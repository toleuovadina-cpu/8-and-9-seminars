print("9-семинар, 5-нұсқа")
print("1-есеп. Біркелкі екілік кодтау")
N = 121
k = 0
while 2 ** k < N:
    k += 1
print("Алфавиттегі символдар саны:", N)
print("Қажетті минималды бит саны:", k)
print("Тексеру:", 2 ** k, ">=", N)
print("\n2-есеп. Фано шарты бойынша декодтау")
codes = {
    "A": "0",
    "B": "10",
    "C": "110",
    "D": "111"
}
message = "10110111010"
fano = True
for a in codes:
    for b in codes:
        if a != b and codes[b].startswith(codes[a]):
            fano = False
print("Фано шарты:", "Орындалады" if fano else "Орындалмайды")
decoded = ""
parts = []
buffer = ""
for bit in message:
    buffer += bit
    for symbol, code in codes.items():
        if buffer == code:
            decoded += symbol
            parts.append(buffer)
            buffer = ""
            break
if buffer:
    print("Қате: хабар толық декодталмады")
else:
    print("Бастапқы хабар:", message)
    print("Кодтарға бөлінуі:", " | ".join(parts))
    print("Декодталған хабар:", decoded)


 # 9-семинар, 5-нұсқа

# =====================================
# 1-есеп. Біркелкі екілік кодтау
# =====================================

print("9-семинар, 5-нұсқа")
print("1-есеп. Біркелкі екілік кодтау")

N = 121
k = 0

while 2 ** k < N:
    k += 1

print("Алфавиттегі символдар саны:", N)
print("Қажетті минималды бит саны:", k)
print("Тексеру:", 2 ** k, ">=", N)



print("\n2-есеп. Фано шарты бойынша декодтау")
codes = {
    "A": "0",
    "B": "10",
    "C": "110",
    "D": "111"
}
message = "10110111010"
fano = True
for a in codes:
    for b in codes:
        if a != b and codes[b].startswith(codes[a]):
            fano = False
print("Фано шарты:", "Орындалады" if fano else "Орындалмайды")
decoded = ""
parts = []
buffer = ""
for bit in message:
    buffer += bit
    for symbol, code in codes.items():
        if buffer == code:
            decoded += symbol
            parts.append(buffer)
            buffer = ""
            break
if buffer:
    print("Қате: хабар толық декодталмады")
else:
    print("Бастапқы хабар:", message)
    print("Кодтарға бөлінуі:", " | ".join(parts))
    print("Декодталған хабар:", decoded)   