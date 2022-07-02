from solutions.CHK import checkout_solution


class TestCheckout():
    def test_get_best_deal_0(self):
        assert checkout_solution.checkout("A A B A") == 160

    def test_get_best_deal_1(self):
        assert checkout_solution.checkout("A B C D") == 115
