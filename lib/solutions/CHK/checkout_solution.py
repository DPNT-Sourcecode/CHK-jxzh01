
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
    prods = skus.split(",")

    res = 0
    for prod in prods:
        if prod not in prices:
            return -1

        #check if applicable for offer
        if prod.lower() 



