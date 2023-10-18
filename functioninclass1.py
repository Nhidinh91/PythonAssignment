def draw_pruce(size):
    for n in range(1,size+1):
        for x in range(size-n):
            print(" ",end="")
        for y in range(n*2-1):
            print("*",end="")
        print()
    return
size = int(input("Please input the size of the tree: "))
draw_pruce(size)