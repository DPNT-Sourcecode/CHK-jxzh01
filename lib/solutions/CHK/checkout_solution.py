
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
    skus = skus.strip()
    prods = list(skus)

    cart = {}
    sum = 0
    for prod in prods:
        if not prod.isalpha():
            continue
            
        if prod not in prices:
            return -1

        # accumulate cart
        if prod in cart.keys():
            cart[prod] += 1
        else:
            cart[prod] = 1







