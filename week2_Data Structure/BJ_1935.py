N = int(input())
expression = input()
num_list = []

for i in range(N):
    num_list.append(int(input()))

stack = []
for term in expression:
    if 'A' <= term <= 'Z':
        stack.append(num_list[ord(term) - ord('A')])
    else:
        num2 = stack.pop()
        num1 = stack.pop()
        if term == '+':
            stack.append(num1 + num2)
        elif term == '-':
            stack.append(num1 - num2)
        elif term == '*':
            stack.append(num1 * num2)
        elif term == '/':
            stack.append(num1 / num2)

res = stack.pop()
print(f"{res:.2f}")
