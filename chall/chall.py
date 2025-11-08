from Crypto.Util.number import bytes_to_long, getPrime
import sympy

m = bytes_to_long(b"**REDACTED**")

e = 65537
p = getPrime(512)
q = sympy.nextprime(p)
n = p * q
c = pow(m, e, n)

print(f"n = {n}")
print(f"e = {e}")
print(f"c = {c}")
