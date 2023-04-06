ss=0
for _ in range(int(input())):
    s=input()
    ss+=4 if s=="Tetrahedron" else 6 if s=="Cube" else 8 if s=="Octahedron" else 12 if s=="Dodecahedron" else 20
print(ss)