"""Bus line"""

def countSwaps(passengers):
    # passengers is an int array represents stations at which i-th passenger will descend
    dLeft = []
    dRight = []
    for i in range(len(passengers)):
        dr = 0
        dl = 0
        for j in range(i, 0, -1):       # cuenta mayores a la izquierda de i
            if passengers[j]>passengers[i]:
                dl += 1
        for j in range(i, len(passengers)):     # cuenta mayores a la derecha de i
            if passengers[j]>passengers[i]:
                dr += 1

        dLeft.append(dl)     # we will append len(passengers) times
        dRight.append(dr)

    A = 0
    # resultado B es el mínimo de cada una de las entradas entre arreglos dLeft y dRight
    B = 0
    for i in range(len(passengers)):
        A += dLeft[i]
        B += min(dLeft[i], dRight[i])

    print(A, B)

# Too slow, for N^5 it would take N^10 operations in the worst case since O(n^2). This takes like 10s

def main():
    N = int(input())
    passengers = []
    for _ in range(N):
        passengers.append(int(input()))

    countSwaps(passengers)

main()


# JUEZ EN LÍNEA: https://juezguapa.com/blog/gpmx?fbclid=IwAR18tgX8BAcGd0fGNXllb2uOysEmwndppaHfngaY-3iyA6X5RAPPfYoyVhI