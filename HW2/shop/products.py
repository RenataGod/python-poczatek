# Zdefiniowanie dostępnych produktów

products = {
    "egg": {
        "quantity": 100,
        "price" : 1.00,
    },
    "bread": {
        "quantity": 100,
        "price" : 2.50,
    },
    "cheese" : {
        "quantity": 100,
        "price": 10.00,
    }
}

def update_product_quantity(product_name, ordered_quantity):
    products[product_name]["quantity"] -= ordered_quantity