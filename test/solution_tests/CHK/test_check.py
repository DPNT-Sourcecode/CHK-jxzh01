from solutions.CHK import checkout_solution


class TestCheckout():
    def test_deal(self):
        assert checkout_solution.checkout("A A B A") == 160

    def test_no_deal(self):
        assert checkout_solution.checkout("A B C D") == 115

