#make a new databse with 3 pngs file
#items and the values
import dbm

db1  = dbm.open("captions", "c")

db1["apple"] = "deliciousness"
db1["banana"] = "squishy"
db1["orange"] = "gross"

for item in db1:
    print(item, db1[item])

# b'apple' b'deliciousness'
# b'banana' b'squishy'
# b'orange' b'gross'
