def test_positive(app):
    for _ in range(3):
        app.main.select_item()
        app.item.add_item_to_cart()

    app.main.open_cart()

    for _ in range(app.cart.get_items_quantity()):
        app.cart.remove_first_item()
