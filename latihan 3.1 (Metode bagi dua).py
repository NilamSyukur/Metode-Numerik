Nama = ('Nama : Nilam Syukur')
NIM = ('NIM : H061181016')

print(Nama)
print(NIM)

import math

def f(x):
    return math.exp(x)-5*x**4*x**2

a=int(input('masukkan nilai batas bawah='))
b=int(input('masukkan nilai batas atas='))
e=float(input('masukkan nilai toleransi='))
N=int(input('masukkan jumlah iterasi='))

a=2
b=3
e=0.00001
N=100

if f(a)*f(b)>0:
    print('nilai yang dimasukkan tidak mengurung akar')

iterasi=0

print('***********************')
print('c         f(c)')
print('***********************')

while True:
    iterasi +=1
    c= (a+b)/2

    if f(a)*f(c) <0:
        b=c

    else:
        a=c
    print('{:7.5f} /t {:+15.10f}'. format (c,f(c))) #7karakter dan 5 angka blkng koma

    if abs (f(c)) < e or iterasi >= N:
        break
    
print('*******************')