# filename = input("Enter filename:")
filename = "printing.py"
in_file = open(filename, "r")
for line in in_file:
    if line.rstrip().startswith("#"):
        print("!!!!")
        print(line.strip())
in_file.close()
