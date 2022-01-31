file = open("names_id.txt")
for i, line in enumerate(file):
    line = line.rstrip("\\n")
    print(" %4d: %s" % (i, line))
file.close()