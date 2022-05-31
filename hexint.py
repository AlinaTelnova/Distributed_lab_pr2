def number_of_bytes(value):
     mas = list(value)
     n=len(mas)
     number_of_bytes=int(n/2)
     print('Number of bytes:',number_of_bytes)
def hex_to_little_endian(value):
    mas = list(value)
    n=len(mas)
    i=0
    little_endian=0
    while True:
        m=int(mas[n-1],base=16)
        if (m!=0):break
        if (m==0) and (int (mas[n-2],base=16)!=0) and ((n-1)%2==1):break
        little_endian+=m*pow(16,i)
        if (n==0):break
        n-=1
    while n>0:
        m=int(mas[n-1],base=16)
        little_endian+=m*pow(16,i)
        n-=1
        i+=1
    print('Little-endian:', little_endian)
def hex_to_big_endian(value):
    mas = list(value)
    n=len(mas)
    i=0
    big_endian=0
    while n>0:
        m=int(mas[n-1],base=16)
        big_endian+=m*pow(16,i)
        n-=1
        i+=1
    print('Big-endian:', big_endian)
def little_endian_to_hex(little_endian):
     import os, sys
     base = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
     little_endian = int(little_endian)
     bitList = []
     while True:
          if (little_endian == 0): break
          little_endian, res = divmod(little_endian,16)
          bitList.append(base[res])
     value=''.join([str(i) for i in bitList[::-1]])
     print('Value:', value)
def big_endian_to_hex(big_endian):
     import os, sys
     base = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
     big_endian = int(big_endian)
     bitList = []
     while True:
          if (big_endian == 0): break
          big_endian, res = divmod(big_endian,16)
          bitList.append(base[res])
     value=''.join([str(i) for i in bitList[::-1]])
     print('Value:', value)
