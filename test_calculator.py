import calculator

class TestCalculator:
    def test_add(self):
        assert 10 == calculator.add(4, 6)
    def test_subtract(self):
        assert -2 == calculator.subtract(7, 9)
