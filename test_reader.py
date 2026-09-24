import reader

path = input("Path of PDF:\n")

list =  reader.pdf_reader(path)

print(list)