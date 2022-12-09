S = input()
count = [0] * 26

for s in S:
    if ord('a') <= ord(s) <= ord('z'):
        count[ord(s) - ord('a')] += 1
    elif ord('A') <= ord(s) <= ord('Z'):
        count[ord(s) - ord('A')] += 1
    else:
        pass

maximum = -1
for idx, freq in enumerate(count):
    if maximum < freq:
        maximum = freq
        ch = chr(idx + ord('A'))
    elif maximum == freq:
        ch = '?'
    else:
        pass

print(ch)
