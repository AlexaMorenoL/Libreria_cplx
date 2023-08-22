import unittest
import CplxNum.py as lc

class Testcplxfunc(unittest.TestCase):

    def test_sumacplx(self):
        #(3 + 5i) + (-2.6 + 6.8i) = 0.4 + 11.8i
        c1 = (3, 5)
        c2 = (-2.6, 6.8)
        suma = lc.sumacplx(c1, c2)
        self.assertAlmostEqual(suma[0], 0.4)
        self.assertAlmostEqual(suma[1], 11.8)
        #(3 + 8i) + (-4 + 10.7i) = -1 + 18.7i
        c1 = (3, 8)
        c2 = (-4, 10.7)
        suma = lc.sumacplx(c1, c2)
        self.assertAlmostEqual(suma[0], -1)
        self.assertAlmostEqual(suma[1],18.7)

    def test_restacplx(self):
        #(4 + 7i) - (2 + 3i) = 2 + 4i
        c1 = (4, 7)
        c2 = (2, 3)
        resta = lc.restacplx(c1, c2)
        self.assertAlmostEqual(resta[0], 2)
        self.assertAlmostEqual(resta[1], 4)
        #(-3 + 2i) - (-3 + 2i) = 0, 0
        c1 = (-3, 2)
        c2 = (-3, 2)
        resta = lc.restacplx(c1, c2)
        self.assertAlmostEqual(resta[0], 0)
        self.assertAlmostEqual(resta[1],0)

    def test_multcplx(self):
        #(2 + 3i) * (4 + 5i) = -7 + 22i
        c1 = (2, 3)
        c2 = (4, 5)
        multiplicacion = lc.multcplx(c1, c2)
        self.assertAlmostEqual(multiplicacion[0], -7)
        self.assertAlmostEqual(multiplicacion[1], 22)
        #(-3 + 2i) * (1 - 4i) = -11 - 2i
        c1 = (-3, 2)
        c2 = (1, 3)
        multiplicacion = lc.multplx(c1, c2)
        self.assertAlmostEqual(multiplicacion[0], -11)
        self.assertAlmostEqual(multiplicacion[1], 2)

    def test_divisioncplx(self):
        #(1-1i) / (2 - 3i) = 0.38 + 0.07i
        c1 = (2, 3)
        c2 = (4, 5)
        division = lc.div_cplx(c1, c2)
        self.assertAlmostEqual(division[0], -7)
        self.assertAlmostEqual(division[1], 22)
        #(3 + 2i) / (4 - 5i) = 0.04 + 0.56i
        c1 = (3, 2)
        c2 = (4, 5)
        division = lc.div_cplxplx(c1, c2)
        self.assertAlmostEqual(division[0], 0.04)
        self.assertAlmostEqual(division[1], 0.56)

    def test_modulocplx(self):
        #|3 + 4i| = 5
        c = (3, 4)
        modulo = lc.modulocplx(c)
        self.assertAlmostEqual(modulo, 5)
        #|-5 - 12i| = 13
        c = (-5, 12)
        modulo = lc.modulocplxplx(c)
        self.assertAlmostEqual(modulo, 13)


if __name__ == '__main__':
    unittest.main()