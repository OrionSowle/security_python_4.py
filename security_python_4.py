device_id_list = ["1926087", "1926088", "1926088", "190260001", "1926088", "1926090"]
asiocaiated_with_id = ["osolwe:1926087", "bjoe:1926088", "uuser:1926088","uuser:190260001", "zjoe:1926088", "jbob:1926090"]

device_id_list_length = len("1926088")
asiocaiated_with_id_length = len("jbob")

if device_id_list_length == 7:
    print("your device id length is 7")
else:
    print("your device id length is not 7")

if asiocaiated_with_id_length == 4:
    print("your device id is 4\n")
else:
    print("your device id is not 4\n")

for i in asiocaiated_with_id:
    print("\n", i)

print("\n")

print("this could your suspect on bad behavior\n")
print(asiocaiated_with_id[3])




