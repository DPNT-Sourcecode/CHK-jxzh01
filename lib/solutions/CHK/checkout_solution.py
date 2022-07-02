prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 70,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 20,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 17,
    "Y": 20,
    "Z": 21
}

offers = {
    "A": {
        3: 130,
        5: 200
    },
    "B": {
        2: 45
    },
    "H": {
        5: 45,
        10: 80
    },
    "K": {
        2: 120
    },
    "P": {
        5: 200
    },
    "Q": {
        3: 80
    },
    "V": {
        2: 90,
        3: 130
    }
}

# should be sorted by the value of the offer if offers not mutually exclusive
buy_x_get_n_times_y_free_offers = {
    "E": {
        2: "B"
    },
    "F": {
        3: "F"  # 2 + 1
    },
    "N": {
        3: "M"
    },
    "R": {
        3: "Q"
    },
    "U": {
        4: "U"  # 3 + 1
    }
}

buy_any_x_for_price_y_offers = {
    "ZTSYX": (3, 45)
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    global prices

    skus = skus.strip()
    prods = list(skus)
    cart = {}
    # validate input and accumulate cart
    for prod in prods:
        if not prod.isalpha():
            return -1
        if prod not in prices:
            return -1

        if prod in cart.keys():
            cart[prod] += 1
        else:
            cart[prod] = 1

    # calculate price
    cart_sum = 0

    # check priority offers
    apply_priority_offers(cart)

    # check bundle offers
    cart_sum += apply_bundle_offers(cart)

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
    # return max applicable offer quantity
    return max((q for q, p in offers[product].items() if quantity >= min(offers[product].keys()) and q <= quantity),
               default=1)


def apply_priority_offers(cart):
    for item, special_offers in buy_x_get_n_times_y_free_offers.items():
        if item not in cart:
            continue

        for quantity, freebie in special_offers.items():
            if cart[item] >= quantity and freebie in cart:
                cart[freebie] = max(cart[freebie] - cart[item] // quantity, 0)

def apply_bundle_offers(cart):
    total_price = 0
    for bundle, bundle_data in buy_any_x_for_price_y_offers.items():
        item_counts = {p: 0 for p in bundle}
        required_item_count = bundle_data[0]

        for item in bundle:
            # if bundle is complete, update cart and total price
            if required_item_count == 0:
                total_price += bundle_data[1]
                for i, c in item_counts.items():
                    if c > 0:
                        cart[i] -= c
                break

            if item not in cart:
                continue

            # deduce the maximum amount of items available
            items_applicable = max(cart[item], required_item_count)
            item_counts[item] += items_applicable
            required_item_count -= items_applicable

    return total_price

