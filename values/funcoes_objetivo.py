import numpy as np

class FuncoesObjetivo():

    @staticmethod
    def f_obj1(x):
        x1, x2 = x
        return (x1**4) + (x2**4) - 3

    @staticmethod
    def f_obj2(x):
        x1, x2 = x
        return 20 + ((x1**2) - (10 * np.cos(2 * np.pi * x1)))+((x2 ** 2) - (10 * np.cos(2 * np.pi * x2)))

    @staticmethod
    def f_obj3(x):
        x1, x2 = x
        return (4 - 2*1*x1**2+x1**4/3) * (x1**2) +( x1 * x2) + (4 * (x2**2) - 4)*(x2**2)

    @staticmethod
    def S1(x):
        x1, x2 = x
        return 1 + ((x1 + x2 + 1)**2) * (19 - 14*x1 + 3*x1**2 - 14*x2 + 6*x1*x2 + 3*x2**2)
    
    @staticmethod
    def S2(x):
        x1, x2 = x
        return 30 + ((2*x1 - 3*x2)**2) * (18 - 32*x1 + 12*x1**2 +48*x2 - 36*x1*x2 + 27*x2**2)
    
    @staticmethod
    def f_obj4(x):
        return FuncoesObjetivo.S1(x) * FuncoesObjetivo.S2(x)