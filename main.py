cash = int(input("Enter cash amount"))

note1 = cash // 100
note2 = (cash%100) // 50
note3 = ((cash%100))%50 // 20

print("you will get notes of 100 rupees:",note1)
print("you will get notes of 50 rupees:",note2)
print("you will get notes of 20 rupees:",note3)