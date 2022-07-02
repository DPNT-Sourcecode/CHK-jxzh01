from solutions.CHK import checkout_solution


class TestCheckout():
    def test_empty(self):
        assert checkout_solution.checkout("") == 0

    def test_invalid(self):
        assert checkout_solution.checkout("M") == -1

    def test_with_seperator(self):
        assert checkout_solution.checkout("A,B,  D") == 95

    def test_deal(self):
        assert checkout_solution.checkout("A A B A") == 160

    def test_deal_with_leftover_item(self):
        assert checkout_solution.checkout("A A A A") == 180

    def test_deal_multiple(self):
        assert checkout_solution.checkout("A A A B B") == 175

    def test_no_deal(self):
        assert checkout_solution.checkout("A B C D") == 115


