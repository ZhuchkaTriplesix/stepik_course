def print_products(*products):
    filtered = [product for product in products if product and isinstance(product, str)]
    if filtered:
        for indx, product in enumerate(filtered, 1):
            print(f"{indx}) {product}")
    else:
        print("Нет продуктов")
