def compute_first(grammar):
    first = {}

    def compute_first_rec(non_terminal):
        if non_terminal in first:
            return first[non_terminal]
        first_set = set()
        for production in grammar[non_terminal]:
            if len(production) == 0 or production[0] == "#":
                first_set.add("#")  # Add epsilon to FIRST set
            elif production[0] not in grammar:
                first_set.add(production[0])
            else:
                first_set |= compute_first_rec(production[0])
        first[non_terminal] = first_set
        return first_set

    for non_terminal in grammar:
        compute_first_rec(non_terminal)

    return first

# Example grammar
grammar = {"S": ["TF"], "F": ["+TF", "#"], "T": ["(S)", "#"]}

start_symbol = "S"

first = compute_first(grammar)

print("FIRST set:")
for non_terminal in first:
    print(non_terminal, ":", first[non_terminal])
