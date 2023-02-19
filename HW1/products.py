# Zdefiniowanie dostępnych produktów

products = {
    "egg": {
        "amount" : 10,
        "price" : 1.00,
    },
    "bread": {
        "amount" : 10,
        "price" : 2.50,
    },
    "cheese" : {
        "amount" = 10,
        "price" = 10.00,
    }
}

def update_product_quantity(product_name, ordered_quantity):
    products[product_name]["qunatity"] -= ordered_quantity