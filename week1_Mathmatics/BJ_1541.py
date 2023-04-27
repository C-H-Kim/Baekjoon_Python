import sys

exp_list = sys.stdin.readline().split('-')
add_term = []

for exp in exp_list:
    term_list = exp.split('+')
    subtotal = 0

    for term in term_list:
        subtotal += int(term)

    add_term.append(subtotal)

res = add_term[0]
for i in range(1, len(add_term)):
    res -= add_term[i]

print(res)
