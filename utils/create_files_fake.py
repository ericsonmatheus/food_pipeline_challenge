import random

import pandas as pd
from faker import Faker


class CreateFilesFake:
    def __init__(self):
        self.fake = Faker("pt_BR")

    def create_customers(self, quantity_customers: int) -> pd.DataFrame:
        """
        Generate a customer dataset with random names and signup dates.

        Args:
            quantity_customers (int): Number of customers to generate.

        Returns:
            pd.DataFrame: A DataFrame containing the generated customer data
        """
        customers = pd.DataFrame(
            {
                "id": range(1, quantity_customers + 1),
                "name": [self.fake.name() for _ in range(quantity_customers)],
                "signup_date": [
                    self.fake.date_between(start_date="-3y", end_date="today")
                    for _ in range(quantity_customers)
                ],
            }
        )
        return customers

    def create_products(self, quantity_products: int) -> pd.DataFrame:
        """
        Generate a product dataset with random names, categories, and prices.

        Args:
            quantity_products (int): Number of products to generate.
            categories (list): List of product categories.

        Returns:
            pd.DataFrame: A DataFrame containing the generated product data

        Obs:
            The maximum possible value for quantity_products is 21,
            as there are 21 unique category-product combinations.

        """
        product_categories = {
            "Bebidas": [
                "Suco de Laranja",
                "Coca-Cola",
                "Água Mineral",
                "Cerveja",
                "Vinho Tinto",
            ],
            "Laticínios": [
                "Queijo Mussarela",
                "Leite Integral",
                "Iogurte Natural",
                "Manteiga",
            ],
            "Carnes": ["Filé de Frango", "Carne Moída", "Picanha", "Linguiça"],
            "Padaria": ["Pão Francês", "Baguete", "Croissant", "Rosquinha"],
            "Hortifruti": ["Maçã", "Banana", "Alface", "Tomate", "Cenoura"],
            "Doces": ["Chocolate", "Bala de Goma", "Brigadeiro", "Pudim", "Sorvete"],
        }
        combinations = [
            (category, product)
            for category, products in product_categories.items()
            for product in products
        ]
        quantity_products = min(quantity_products, len(combinations))
        selecteds = random.sample(combinations, k=quantity_products)

        categories_opt, products_opt = zip(*selecteds)

        products = pd.DataFrame(
            {
                "id": range(1, quantity_products + 1),
                "name": products_opt,
                "category": categories_opt,
                "price": [
                    round(random.uniform(10, 100), 2) for _ in range(quantity_products)
                ],
            }
        )
        return products

    def create_sales(
        self, quantity_sales: int, quantity_customers: int, quantity_products: int
    ) -> pd.DataFrame:
        """
        Generate a sales dataset with randomly assigned customers,
        products, and sale dates.

        Args:
            quantity_sales (int): Number of sales records to generate.
            quantity_customers (int): Number of unique customers.
            quantity_products (int): Number of unique products.

        Returns:
            pd.DataFrame: A DataFrame containing the generated sales data
        """
        sales = pd.DataFrame(
            {
                "id": range(1, quantity_sales + 1),
                "customer_id": [
                    random.randint(1, quantity_customers) for _ in range(quantity_sales)
                ],
                "product_id": [
                    random.randint(1, quantity_products) for _ in range(quantity_sales)
                ],
                "sale_date": [
                    self.fake.date_between(start_date="-2y", end_date="today")
                    for _ in range(quantity_sales)
                ],
                "quantity": [random.randint(1, 10) for _ in range(quantity_sales)],
            }
        )
        return sales
