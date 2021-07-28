from random import randint


requests = []
for i in range(ord('A'), ord('Z')+1):
    requests.append([chr(i),randint(2,10)])

print(requests)