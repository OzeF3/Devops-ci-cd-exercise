import pytest

@pytest.fixture(autouse=True)
def reset_in_memory_data():
    # Reset USERS store (if exists)
    try:
        from app.routes import user_routes
        if hasattr(user_routes, "USERS"):
            user_routes.USERS.clear()
            user_routes.USERS.update({
                1: {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'},
                2: {'id': 2, 'name': 'Jane Smith', 'email': 'jane@example.com'}
            })
        if hasattr(user_routes, "NEXT_USER_ID"):
            user_routes.NEXT_USER_ID = 3
    except Exception:
        pass

    # Reset PRODUCTS store (if exists)
    try:
        from app.routes import product_routes

        if hasattr(product_routes, "products"):
            product_routes.products.clear()
            product_routes.products.extend([
                {'id': 1, 'name': 'Laptop', 'price': 999.99, 'stock': 10},
                {'id': 2, 'name': 'Mouse', 'price': 29.99, 'stock': 50},
                {'id': 3, 'name': 'Keyboard', 'price': 79.99, 'stock': 25},
            ])
    except Exception:
        pass

    yield
