from operator import itemgetter

data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantelle', 9]]

max_length = max((len(pair[0]) for pair in data))
for name, score in sorted(data, reverse=True, key=itemgetter(1, 0)):
    print(f"{name:{max_length}} = {score:3}")


def main():
    names = ["A", "Bob", "This one too"]
    string_to_length = make_string_to_length(names)
    print(string_to_length)

def make_string_to_length(strings):
    string_to_length = {}
    for s in strings:
        string_to_length[s] = len(s)
    return string_to_length

main()
