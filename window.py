lst = list(map(int,input("Enter the number ").split()))
k = int(input("Enter the number"))

window = sum(lst[:k])  
maxsum = window

for i in range(k, len(lst)):
    window += lst[i]
    window -= lst[i-k]   # ✅ fixed here
    maxsum = max(maxsum, window)

print(maxsum)