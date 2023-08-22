import math

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def sumacplx(c1, c2):
    real= c1[0] + c2[0]
    imaginaria= c1[1] + c2[1]
    return (real, imaginaria)

def restacplx(c1, c2):
    real= c1[0] - c2[0]
    imaginaria= c1[1] - c2[1]
    return (real, imaginaria)

def multcplx(c1, c2):
    real = (c1[0] * c2[0])-(c1[1] * c2[1])
    imaginaria = (c1[1] * c2[0])+(c1[0] * c2[1])
    return (real, imaginaria)

def div_cplx(c1, c2):
    denom = c2[0]*2 + c2[1]*2
    c2_conjugate = (c2[0], -c2[1])
    num = multcplx(c1, c2_conjugate)
    real = num[0] / denom
    imaginaria = num[1] / denom
    return (real, imaginaria)

def modulocplx(c):
    modulo = math.sqrt(c[0]**2 + c[1]**2)
    return modulo

def conjucplx(c1, c2):
    conju = c1 - c2
    return conju

def cartesian_to_polarcplx(c):
    x = c[0]
    y = c[1]
    resultado = round(math.sqrt(x**2 + y**2), 2)
    theta = round(math.atan2(y, x))
    return (resultado, theta)

def fasecplx(c):
    fase = round(math.atan2(c[1], c[0]), 2)
    return fase

if __name__ == '__main__':
    print_hi('PyCharm')
    print("La suma de los números complejos es:", sumacplx((4,2),(3,5)))
    print("La resta de los números complejos es:", restacplx((4,2),(3,5)))
    print("La multiplicación de los números complejos es:", multcplx((2, 6),(3, 5)))
    print("La división de los números complejos es:", div_cplx((4,2),(5,3)))
    print("El módulo de los números complejos es:", modulocplx(3, -2.6))
    print("El conjugado de los números complejos es:", conjucplx(3, -2.6))
    print("La coordenada cartesiana convertida en coordenada polar es:", cartesian_to_polarcplx((math.sqrt(2), math.pi /4)))
    print("La fase del número complejo es:", fasecplx((3, 3)))