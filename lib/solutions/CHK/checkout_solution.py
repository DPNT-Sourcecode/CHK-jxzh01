

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15
    }

    offers = {
        "3A": 130,
        "2B": 45
    }

    skus = skus.strip()
    prods = skus.split(",")




