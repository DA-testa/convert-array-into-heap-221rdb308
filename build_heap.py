# python3

def sort(i, n, data, swaps):
    min_index = i
    l = 2 * i + 1
    if l < n and data[l] < data[min_index]:
        min_index = l
    r = 2 * i + 2
    if r < n and data[r] < data[min_index]:
        min_index = r
        
    if i != min_index:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        sort(min_index, n, data, swaps)
    return min_index


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2, -1, -1):
        sort(i, n, data, swaps)
        

    assert len(swaps) <= 4 * len(data)
    return swaps


def main():
    
    print("Input Input type:")
    input_type = input()
    if "I" in input_type:
        print("Input data:")
        n = int(input())
        data = list(map(int, input().split()))
    else:
        filename = input("Enter filename:")
        folder = './tests/'
        with open(folder + filename, 'r') as test:
            n = int(test.readline())
            data = list(map(int, test.readline().split()))
    assert len(data) == n
    swaps = build_heap(data)


   
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
