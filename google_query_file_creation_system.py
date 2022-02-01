# Bianca
#File creation program with google query

print("\nGoogle Query File Creation System\n")
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
query = input("Enter your query: ")
line = ""
for j in search(query):
    line = line + (j) + " "
name = query + ".txt"
file = open(name, "w")
file.write(line)
file.close()
print("Your file is ready:", name)