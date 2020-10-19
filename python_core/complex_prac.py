# Math library for Complex Numbers
import cmath

a = complex(1,2)
print('a:',a)

b = 1+2j
print('b:',b)
print(f'Real:{b.real}, type:{type(b.real)}, conjugate:{b.conjugate()}',)

print('sqrt:',cmath.sqrt(b))
print('Phase:',cmath.phase(b))
print('Abs:',abs(b))
print('Rectangular to polar:',cmath.rect(abs(b),cmath.phase(b)))

# check exp(j*pi) + 1 = 0
# isclose will help to check equality. DO SET ABS_TOL. 
print(cmath.isclose(cmath.exp(complex(0,cmath.pi))+1,0,abs_tol=0.000001))