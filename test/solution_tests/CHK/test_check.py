from solutions.CHK import checkout_solution


class TestCheckout():
    def test_empty(self):
        assert checkout_solution.checkout("") == 0

    def test_invalid(self):
        assert checkout_solution.checkout("M") == -1

    def test_deal(self):
        assert checkout_solution.checkout("AABA") == 160

    def test_deal_with_leftover_item(self):
        assert checkout_solution.checkout("AAAA") == 180

    def test_deal_multiple(self):
        assert checkout_solution.checkout("AAABB") == 175

    def test_no_deal(self):
        assert checkout_solution.checkout("ABCD") == 115

    def test_get_best_deal_best(self):
        assert checkout_solution.get_best_deal("A", 10) == 5

    def test_get_best_deal_second_best(self):
        assert checkout_solution.get_best_deal("A", 4) == 3

# 2nd part
    def test_get_two_b_before(self):
        assert checkout_solution.checkout("EEB") == 80

    def test_get_two_b_after(self):
        assert checkout_solution.checkout("BEE") == 80




