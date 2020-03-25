Nama = ('Nama : Nilam Syukur')
NIM = ('NIM : H061181016')

print(Nama)
print(NIM)

def f(x):
    return 4*x**2 - 18

def df(x):
    return 8*x

def newtonRaphson(f, df, x, tol):
    a = f(x)
    iterasi = 0
    while abs(a) > tol and iterasi < 100:
        try:
            x = x - float(a)/df(x)
        except ZeroDivisionError:
            print("Error! - turunan bernilai 0 untuk  x = ", x)

        a = f(x)
        iterasi += 1
        
    if abs(a) > tol:
        iterasi = -1
    return x, iterasi

root,numlter = newtonRaphson(f, df, x=100, tol=1.0e-0)

if numlter > 0:
    print("Jumlah iterasi : %d" % (1 + 2*numlter))
    print("Akar: %f" % (root))

else:
    print("Solusi tidak ditemukan!")