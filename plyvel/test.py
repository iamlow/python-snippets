import plyvel

db = plyvel.DB('testdb', create_if_missing=True)

db.put(b'key', b'value')
db.put(b'another-key', b'another-value')
print(db.get(b'key'))
print(db.get(b'yet-another-key'))
print(db.get(b'yet-another-key', b'default-value'))
for key, value in db:
    print(key)
    print(value)
db.delete(b'key')
db.delete(b'another-key')
db.close()
