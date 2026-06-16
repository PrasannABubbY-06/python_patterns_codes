print(   )
print("//-------Right angle Triangle-------//")
print(   )
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print(   )
print("//-------Inverted Right angle Triangle-------//")
print(   )
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


print(   )
print("//-------Pyramid-------//")
print(   )


n = 7
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for k in range(2 * i + 1):
        print("*", end=" ")
    print()


print(   )
print("//-------Love-------//")
print(   )
for i in range(6):
    for j in range(7):
        if ((i == 0 and j % 3 != 0) or
            (i == 1 and j % 3 == 0) or
            (i - j == 2) or
            (i + j == 8)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(   )
print("//-------Circle's-------//")
print(   )


n = 15
outer_radius = 7
inner_radius = 3
center = n // 2
for i in range(n):
    for j in range(n):
        distance = ((i - center) ** 2 + (j - center) ** 2) ** 0.5

        if outer_radius - 0.5 <= distance <= outer_radius + 0.5:
            print("*", end=" ")
        elif inner_radius - 0.5 <= distance <= inner_radius + 0.5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(   )
print("//-------Diamond Pattern-------//")
print(   )

n = 5

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("* " * i)

for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    print("* " * i)

print(   )
print("//-------Hollow Pyramid-------//")
print(   )
n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1 or i == n:
            print("*", end="")
        else:
            print(" ", end="")

    print()

print(   )
print("//--------Number Triangle--------//")
print(   )
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print(   )
print("//-------Inverted Number Triangle-------//")
print(   )
n = 5
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print(   )
print("//-------square Pattern-------//")
print(   )
n = 5
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

print(   )
print("//-------X Pattern-------//")
print(   )
n = 5
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(   )
print("//-------P-------//")
print(   )

for i in range(6):
    for j in range(7):
        if( j==0 or (i==0 and j<4) or 
        (i==3 and j<4) or 
        (j==4 and 0<i<3)):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()



print(   )
print("//-------M-------//")
print(   )


for i in range(5):
    for j in range(5):
        if (j == 0)or(j == 4)or             \
            (i == j and i <= 2)or           \
            (i + j == 4 and i <= 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


print(   )
print("//--------S--------//")
print(   )

for i in range(5):
    for j in range(5):
        if (
            i == 0 or
            i == 2 or
            i == 4 or
            (j == 0 and i < 2) or
            (j == 4 and i > 2)
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(   )
print("//-------Hollow Square-------//")
print(   )
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(   )
print("//-------Hollow Square with Diagonals-------//")
print(   )
n = 7
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(   )
print("//-------Left Triangle (Mirrored)-------//")
print(   )
n = 5
for i in range(1, n + 1):
    print("  " * (n - i) + "* " * i)

print(   )
print("//-------Inverted Left Triangle-------//")
print(   )
n = 5
for i in range(n, 0, -1):
    print("  " * (n - i) + "* " * i)

print(   )
print("//-------Right Pascal Triangle-------//")
print(   )
n = 5
for i in range(1, n + 1):
    print("* " * i)
for i in range(n - 1, 0, -1):
    print("* " * i)

print(   )
print("//-------Sandglass Pattern-------//")
print(   )
n = 5
for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)
for i in range(2, n + 1):
    print(" " * (n - i) + "* " * i)

print(   )
print("//-------Hollow Diamond-------//")
print(   )
n = 5
for i in range(1, n + 1):
    for j in range(1, 2 * n):
        if j == n - i + 1 or j == n + i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(n - 1, 0, -1):
    for j in range(1, 2 * n):
        if j == n - i + 1 or j == n + i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print(   )
print("//-------Butterfly Pattern-------//")
print(   )
n = 5
for i in range(1, n + 1):
    print("* " * i + "    " * (n - i) + "* " * i)
for i in range(n, 0, -1):
    print("* " * i + "    " * (n - i) + "* " * i)

print(   )
print("//-------Rhombus Pattern-------//")
print(   )
n = 5
for i in range(n):
    print(" " * i + "* " * n)

print(   )
print("//-------Floyd's Triangle-------//")
print(   )
n = 5
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

print(   )
print("//-------Alphabet Triangle-------//")
print(   )
n = 5
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + i), end=" ")
    print()

print(   )
print("//-------Plus Pattern-------//")
print(   )
n = 5
for i in range(n):
    for j in range(n):
        if i == n // 2 or j == n // 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(   )
print("//-------Letter A-------//")
print(   )
for i in range(7):
    for j in range(5):
        if ((j == 0 or j == 4) and i != 0) or ((i == 0 or i == 3) and (0 < j < 4)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(   )
print("//-------Letter B-------//")
print(   )
for i in range(7):
    for j in range(5):
        if (j == 0) or (i == 0 or i == 3 or i == 6) and (j < 4) or (j == 4 and (i != 0 and i != 3 and i != 6)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(   )
print("//-------Letter C-------//")
print(   )
for i in range(7):
    for j in range(5):
        if (j == 0 and (i != 0 and i != 6)) or ((i == 0 or i == 6) and (j > 0)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(   )
print("//-------Letter D-------//")
print(   )
for i in range(7):
    for j in range(5):
        if (j == 0) or ((i == 0 or i == 6) and (j < 4)) or (j == 4 and (i != 0 and i != 6)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(   )
print("//-------Letter E-------//")
print(   )
for i in range(7):
    for j in range(5):
        if (j == 0) or (i == 0 or i == 3 or i == 6):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(   )
print("//-------Letter F-------//")
print(   )
for i in range(7):
    for j in range(5):
        if (j == 0) or (i == 0 or i == 3):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(   )
print("//-------Letter G-------//")
print(   )
for i in range(7):
    for j in range(5):
        if (j == 0 and (i != 0 and i != 6)) or ((i == 0 or i == 6) and (j > 0)) or (j == 4 and (i >= 3 and i != 6)) or (i == 3 and j >= 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(   )
print("//-------Letter H-------//")
print(   )
for i in range(7):
    for j in range(5):
        if (j == 0 or j == 4) or (i == 3):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(   )
print("//-------Letter I-------//")
print(   )
for i in range(7):
    for j in range(5):
        if (i == 0 or i == 6) or (j == 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(   )
print("//-------Letter J-------//")
print(   )
for i in range(7):
    for j in range(5):
        if (i == 0) or (j == 2 and i < 6) or (i == 6 and j < 2) or (i == 5 and j == 0):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(   )
print("//-------Letter K-------//")
print(   )
for i in range(7):
    for j in range(5):
        if (j == 0) or (i + j == 4) or (i - j == 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(   )
print("//-------Letter L-------//")
print(   )
for i in range(7):
    for j in range(5):
        if (j == 0) or (i == 6):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(   )
print("//-------Letter N-------//")
print(   )
for i in range(5):
    for j in range(5):
        if (j == 0 or j == 4 or i == j):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(   )
print("//-------Letter O-------//")
print(   )
for i in range(7):
    for j in range(5):
        if ((j == 0 or j == 4) and (i != 0 and i != 6)) or ((i == 0 or i == 6) and (j > 0 and j < 4)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(   )
print("//-------Letter Q-------//")
print(   )
for i in range(7):
    for j in range(6):
        if ((j == 0 or j == 4) and (i > 0 and i < 5)) or ((i == 0 or i == 5) and (j > 0 and j < 4)) or (i == j and i > 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(   )
print("//-------Letter R-------//")
print(   )
for i in range(7):
    for j in range(5):
        if (j == 0) or (i == 0 or i == 3) and (j < 4) or (j == 4 and i > 0 and i < 3) or (i - j == 2 and i > 3):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(   )
print("//-------Letter T-------//")
print(   )
for i in range(7):
    for j in range(5):
        if (i == 0) or (j == 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(   )
print("//-------Letter U-------//")
print(   )
for i in range(7):
    for j in range(5):
        if ((j == 0 or j == 4) and i < 6) or (i == 6 and (0 < j < 4)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(   )
print("//-------Letter V-------//")
print(   )
for i in range(4):
    for j in range(7):
        if (i == j or i + j == 6):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(   )
print("//-------Letter W-------//")
print(   )
for i in range(5):
    for j in range(5):
        if (j == 0 or j == 4) or (i >= 2 and (i + j == 4 or i == j)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(   )
print("//-------Letter Y-------//")
print(   )
for i in range(5):
    for j in range(5):
        if (i == j and i < 2) or (i + j == 4 and i < 2) or (j == 2 and i >= 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(   )
print("//-------Letter Z-------//")
print(   )
for i in range(5):
    for j in range(5):
        if (i == 0 or i == 4 or i + j == 4):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(   )
print("//-------K Shape-------//")
print(   )
n = 5
for i in range(n, 0, -1):
    print("* " * i)
for i in range(2, n + 1):
    print("* " * i)

print(   )
print("//-------Zig-Zag Pattern-------//")
print(   )
for i in range(1, 4):
    for j in range(1, 21):
        if ((i + j) % 4 == 0) or (i == 2 and j % 4 == 0):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(   )
print("//-------Arrowhead (Right)-------//")
print(   )
n = 5
for i in range(n):
    print("  " * i + "*")
for i in range(n-2, -1, -1):
    print("  " * i + "*")
