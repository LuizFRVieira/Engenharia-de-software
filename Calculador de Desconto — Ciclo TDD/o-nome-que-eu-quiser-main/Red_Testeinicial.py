import unittest


class TestDiscountCalculator(unittest.TestCase):

    def test_no_discount(self):
        # Não funciona porque a classe DiscountCalculator não foi criada/importada.
        calc = DiscountCalculator('none')
        self.assertEqual(calc.apply(100.0), 100.0)

    def test_percentage_discount(self):
        # Vai dar NameError: DiscountCalculator não existe no código.
        calc = DiscountCalculator('percentage', 10)
        self.assertEqual(calc.apply(100.0), 90.0)

    def test_coupon_discount(self):
        # Falha pelo mesmo motivo: falta definir a classe DiscountCalculator.
        calc = DiscountCalculator('coupon', 20)
        self.assertEqual(calc.apply(100.0), 80.0)

    def test_coupon_discount_never_negative(self):
        # O teste nem chega a rodar direito, pois a classe não foi definida.
        calc = DiscountCalculator('coupon', 150)
        self.assertEqual(calc.apply(100.0), 0.0)


# Executa os testes, mas eles falham porque DiscountCalculator não existe.
unittest.main(argv=[''], verbosity=2, exit=False)