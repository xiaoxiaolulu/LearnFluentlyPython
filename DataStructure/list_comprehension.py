symbols = '$¢£¥€¤'
codes = []

for symbol in symbols:
    codes.append(ord(symbol))

print(codes)


print([ord(symbol) for symbol in symbols])
