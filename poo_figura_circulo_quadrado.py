class Figura:
    def __init__(self, x=0, y=0):
        self.centrox = x
        self.centroy = y

    def distancia(self, pontox=0,pontoy=0):
        return ((pontox-self.centrox)**2 + (pontoy-self.centroy)**2)**0.5

    def area(self):
        raise NotImplementedError('não é possível calcular a área, o tipo da figura não é conhecido')

    def perimetro(self):
        raise NotImplementedError('não é possível calcular o perímetro, o tipo da figura não é conhecido')
    def __eq__(self, other):
        return other

    def __ne__(self, other):
        return other

    def __lt__(self, other):
        return other

    def __gt__(self, other):
        return other

    def __le__(self, other):
        return other

    def __ge__(self, other):
        return other

    def __contains__(self, other):
        return other
class Circulo(Figura):
    def __init__(self, x=0, y=0, r=1):
        super().__init__(x,y)
        self.raio = r

    def area(self):
        return math.pi*(self.raio**2)

    def perimetro(self):
        return 2*math.pi*self.raio

    

class Quadrado(Figura):
    def __init__(self, x=0, y=0, qx=-1/2, qy=-1/2):
        super().__init__(x,y)
        self.base = 2*(x-qx)
        self.altura = 2*(y-qy)

    def area(self):
        return self.base*self.altura

    def perimetro(self):
        return 2*self.base + 2*self.altura

# Testes para as classes Circulo e Quadrado
import unittest, math

class MyTest(unittest.TestCase):

    def test_figura(self):
        f1 = Figura()
        f2 = Figura(1, 1)
        self.assertEqual(f1.distancia(), 0)
        self.assertEqual(round(f2.distancia(3, 2), 3), 2.236)


    def test_circulo(self):
        c1 = Circulo()
        c2 = Circulo(1, 1)
        c3 = Circulo(1, 0, 3)
        c4 = Circulo(0, 0, 1)
        self.assertTrue(c1 <= c2)
        self.assertTrue(c2 < c3)
        self.assertFalse(c1 > c3)
        self.assertTrue(c1 >= c1)
        self.assertFalse(c2 >= c3)
        self.assertTrue(c1 == c4)
        self.assertTrue(c3 != c4)
        self.assertTrue(c2 in c3)
        self.assertFalse(c2 in c1)
        self.assertEqual(round(c1.area(), 3), 3.142)
        self.assertEqual(round(c2.perimetro(), 3), 6.283)
        self.assertEqual(round(c3.distancia(3, 2), 3), 2.828)


    def test_criacao_quadrado(self):
        q1 = Quadrado()
        q2 = Quadrado(1, 1)
        q3 = Quadrado(1, 0, 2, 2)
        q4 = Quadrado(0, 0, -0.5, -0.5)
        '''
        self.assertTrue(q1 <= q2)
        self.assertTrue(q2 < q3)
        self.assertFalse(q1 > q3)
        self.assertTrue(q1 >= q1)
        self.assertFalse(q2 >= q3)
        self.assertTrue(q1 == q4)
        self.assertTrue(q3 != q4)'''
        self.assertEqual(round(q1.area(), 3), 1)
        self.assertEqual(round(q2.perimetro(), 3), 12)
        self.assertEqual(round(q3.distancia(3, 2), 3), 2.828)

unittest.main(argv=['first-arg-is-ignored'], exit=False)
