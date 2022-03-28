
partyCountDown = int(input("How long 'til the party?: "))

if partyCountDown < 0:
    print("PARTY NOW!!!")
for i in range(partyCountDown, 0, -1):
    print(i)
    if i == 1:
        print("PARTY TIME!!!")

