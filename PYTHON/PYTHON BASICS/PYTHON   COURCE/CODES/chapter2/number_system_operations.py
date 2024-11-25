#program to convert binary,octal,hexadecimal codes into decimal
n1=0B101000101
n2=0o2345376
n3=0xA15B8
n=int(n1)
print("Binary 101000101 =",n)
n=int(n2)
print("octal 2345376 =",n)
n=int(n3)
print("Hexadecimal A15B8 =",n)
# we can also convert integers in any number system
a=45
print("Conversion of a into binary, octal and hexadecimal")
print(bin(a))
print(oct(a))
print(hex(a))