buffer_size = 5
with open("test.md", 'w', buffering=buffer_size) as r:
    r.write("Taslim ")
    print(r.writable())
    r.flush()
    r.write("Arif")
