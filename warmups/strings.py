
# lines = [
#     "dinner",
#     "dinner",
#     "dinner",
#     "dinner",
# ]
# filename = "dinner.txt"
#
# out_file = open(filename, "w")
# for line in lines:
#     out_file.write(line + "\n")
# out_file.close()
#
# print(f"Wrote {len(lines)} lines to {filename}")

strings = ["Bob" "this is another" "one"]
for strings in strings:
    filename = (f"{strings}.txt")
    print()
    with open(filename, "w") as out_file:
        print(strings, file=out_file)


