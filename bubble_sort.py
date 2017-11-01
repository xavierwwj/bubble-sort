inp = [3,8,23,6,3,5,6]
def bubble_sort(inp):
    n = len(inp)
    while n > 1:
        for i in range(n-1):
            if inp[i] > inp[i+1]:
                inp[i+1], inp[i] = inp[i], inp[i+1]
        n -= 1
    return inp
output = bubble_sort(inp)
print(output)
