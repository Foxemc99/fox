with open("names2.txt","r") as reader , open("names3.txt",'w') as writer:
    reader_line=reader.read()
    writer.write(reader_line)