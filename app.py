import pandas as pd
import streamlit as st

from utils.create_files_fake import CreateFilesFake

fake = CreateFilesFake()

customers = fake.create_customers(50)
products = fake.create_products(100)
sales = fake.create_sales(1000, len(customers), len(products))

customers
products
sales
