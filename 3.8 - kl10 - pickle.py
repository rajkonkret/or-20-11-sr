import pickle

lista = [1, 2, 3, 4, 5]
# Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
# contex menadzer
with open('lista.txt', 'w') as fh:
    fh.write(str(lista))  # zapisuje jako string

with open('lista.txt', 'r') as file:
    data = file.read()

print(data)
print(type(data))  # <class 'str'>
print(data[0])  # [


with open("lista.pickle", "wb") as file:
    pickle.dump(lista, file)

with open("lista.pickle", "rb") as f:
    p = pickle.load(f)

print(p)
print(type(p))  # <class 'list'>
print(p[0])  # 1
