prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15
}

offers = {
    "A": {
        3: 130
    },
    "B": {
        2: 45
    }
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # clean up input
    skus = skus.strip()
    prods = list(skus)

    # accumulate cart
    cart = {}
    for prod in prods:
        # validate
        if not prod.isalpha():
            continue
        if prod not in prices:
            return -1

        if prod in cart.keys():
            cart[prod] += 1
        else:
            cart[prod] = 1

    # calculate price
    cart_sum = 0
    for product, quantity in cart.items():
        # check if offer applicable
        if product in offers:
            while cart[product] != 0:
                # check if offer applicable and update cart
                quantity = get_best_deal(product, cart[product])
                if quantity == 1:
                    cart_sum += prices[product]
                else:
                    cart_sum += offers[product][quantity]
                cart[product] -= quantity
        else:
            cart_sum += prices[product] * cart[product]
            cart[product] = 0

    return cart_sum


def get_best_deal(product, quantity):
    # return max applicable offer
    return max((q for q, p in offers[product].items() if quantity >= min(offers[product].keys())),
               default=1)




