from solutions.CHK import checkout_solution


class TestCheckout():
    def test_empty(self):
        assert checkout_solution.checkout("") == 0

    def test_invalid(self):
        assert checkout_solution.checkout("---") == -1

    def test_deal(self):
        assert checkout_solution.checkout("AABA") == 160

    def test_deal_with_leftover_item(self):
        assert checkout_solution.checkout("AAAA") == 180

    def test_deal_multiple(self):
        assert checkout_solution.checkout("AAABB") == 175

    def test_no_deal(self):
        assert checkout_solution.checkout("ABCD") == 115

    def test_get_best_deal_gets_best(self):
        assert checkout_solution.get_best_deal("A", 10) == 5

    def test_get_best_deal_gets_second_best(self):
        assert checkout_solution.get_best_deal("A", 4) == 3

    # 2nd part
    def test_get_two_b_before(self):
        assert checkout_solution.checkout("EEB") == 80

    def test_get_two_b_after(self):
        assert checkout_solution.checkout("BEE") == 80

    def test_two_e(self):
        assert checkout_solution.checkout("EE") == 80

    def test_special_deal_twice(self):
        assert checkout_solution.checkout("BEBEEE") == 160

    # 3rd part
    def test_two_f_one_f_free(self):
        assert checkout_solution.checkout("FFF") == 20

    def test_two_f_one_f_free_when_five_in_total(self):
        assert checkout_solution.checkout("FFFFF") == 40

    def test_nine_f_three_f_free(self):
        assert checkout_solution.checkout("FFFFFFFFF") == 60

    # 4th part
    def test_three_u_one_u_free(self):
        assert checkout_solution.checkout("UUUU") == 120

    def test_three_r_one_q_free(self):
        assert checkout_solution.checkout("RRQR") == 150

    def test_three_n_one_m_free(self):
        assert checkout_solution.checkout("NMNN") == 120

    # 5th part
    def test_bundle_deal(self):
        assert checkout_solution.checkout("SSS") == 45

    def test_bundle_deal_twice(self):
        assert checkout_solution.checkout("SSSSYX") == 90

    def test_bundle_deal_applies_correctly_when_duplicate_items(self):
        assert checkout_solution.checkout("SSS") == 45

    def test_bundle_applies_best_deal(self):
        assert checkout_solution.checkout("SSZZZ") == 95