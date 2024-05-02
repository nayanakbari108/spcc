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


def compute_follow(grammar, start_symbol):
    follow = {non_terminal: set() for non_terminal in grammar}

    # Adding $ (end of input) to follow of start symbol
    follow[start_symbol].add("$")

    # Helper function to compute follow recursively
    def compute_follow_rec(non_terminal):
        for nt in grammar:
            for production in grammar[nt]:
                if non_terminal in production:
                    idx = production.index(non_terminal)
                    if idx < len(production) - 1:
                        next_symbol = production[idx + 1]
                        if next_symbol not in grammar:
                            follow[non_terminal].add(next_symbol)
                        else:
                            first_of_next = compute_first(grammar)[next_symbol]
                            if "#" in first_of_next:
                                follow[non_terminal] |= first_of_next - {"#"}
                                follow[non_terminal] |= compute_follow_rec(next_symbol)
                            else:
                                follow[non_terminal] |= first_of_next
                    else:
                        if nt != non_terminal and nt != "":
                            follow[non_terminal] |= compute_follow_rec(nt)
        return follow[non_terminal]

    # Computing follow sets recursively
    for non_terminal in grammar:
        compute_follow_rec(non_terminal)

    return follow


# Example grammar
grammar = {"S": ["TF"], "F": ["+TF", "#"], "T": ["(S)", "id"]}

start_symbol = "S"

first = compute_first(grammar)
follow = compute_follow(grammar, start_symbol)

print("FIRST set:")
for non_terminal in first:
    print(non_terminal, ":", first[non_terminal])

print("\nFOLLOW set:")
for non_terminal in follow:
    print(non_terminal, ":", follow[non_terminal])