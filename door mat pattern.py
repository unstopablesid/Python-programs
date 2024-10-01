print("Enter the size of your doormat in the length and width:")
N, M = map(int, input().split())

# Top half
for i in range(1, N, 2): 
    print((i * ".|.").center(M, "-"))

# Center line
print("WELCOME".center(M, "-"))

# Bottom half
for i in range(N-2, -1, -2): 
    print((i * ".|.").center(M, "-"))
