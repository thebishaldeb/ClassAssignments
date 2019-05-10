StringPieces = ["AY8PMPAR", "NGAT", "ME", "OME.", "ETINGAT2", "7MA", "Y8PMPA",
                "RKHO", "ME", "MEE", "TIN", "GAT27M", "KHOME.", "MEETI", "27MAY8", "PMP", "ARKH"]


def compareStrings(i, j):
    count = 0
    for k in range(len(StringPieces[i])):
        if StringPieces[j][count] == StringPieces[i][k]:
            if k+1 < len(StringPieces[i]) and StringPieces[j][count] == StringPieces[i][k+1] and StringPieces[j][count+1] != StringPieces[i][k+1]:
                k += 1
                count = 0
                continue
            count += 1
            if count == len(StringPieces[j]):
                print(StringPieces[i], StringPieces[j])
                StringPieces[j] = StringPieces[i]
                print("Hey --->", StringPieces[i], StringPieces[j])
                return
        else:
            count = 0

    if count > 1:
        x = StringPieces[i] + StringPieces[j][count:]

        print(StringPieces[i], StringPieces[j])
        StringPieces[i] = StringPieces[j] = x

        print("Hey --->", x)
        return

for i in range(len(StringPieces)):
    for j in range(len(StringPieces)):
        compareStrings(i, j)

message = StringPieces.pop()

print(message)
