import pdb
import random
from models.product_type import ProductType
from models.brand import Brand
from models.product import Product
from models.stock import Stock
import repositories.product_type_repository as product_type_repository
import repositories.brand_repository as brand_repository
import repositories.product_repository as product_repository
import repositories.stock_repository as stock_repository


def clear_all_tables():

    product_repository.delete_all()
    product_type_repository.delete_all()
    brand_repository.delete_all()
    stock_repository.delete_all()


def setup_product_types():

    product_type_name_1 = "Smartphone"
    global product_type_1
    product_type_1 = ProductType(product_type_name_1)
    product_type_name_2 = "Feature Phone"
    global product_type_2
    product_type_2 = ProductType(product_type_name_2)
    product_type_name_3 = "Charger"
    global product_type_3
    product_type_3 = ProductType(product_type_name_3)
    product_type_name_4 = "Screen protector"
    global product_type_4
    product_type_4 = ProductType(product_type_name_4)

    product_type_repository.save(product_type_1)
    product_type_repository.save(product_type_2)
    product_type_repository.save(product_type_3)
    product_type_repository.save(product_type_4)


def setup_brands():

    brand1_name = "Dappel"
    brand1_description = "like Mappel but with a D"
    brand1_warranty_details = "Daylight robbery"
    global brand1
    brand1 = Brand(brand1_name, brand1_description, brand1_warranty_details)
    global brand2
    brand2 = Brand("ShangTsung", "Soul-eater", "Combustable")
    brand_repository.save(brand1)
    brand_repository.save(brand2)


def setup_products():

    product_1_name = "ED209"
    product_1_description = "Not great on stairs"
    product_1_distributor_price = 200
    product_1_sale_price = 600
    product_1_warranty_length = 120
    global product_1
    product_1 = Product(
        product_1_name,
        product_type_1,
        brand1,
        product_1_description,
        product_1_distributor_price,
        product_1_sale_price,
        product_1_warranty_length,
    )
    product_2_name = "dezapper"
    product_2_description = "It will zapp you into the past"
    product_2_distributor_price = 300
    product_2_sale_price = 700
    product_2_warranty_length = 140
    global product_2
    product_2 = Product(
        product_2_name,
        product_type_1,
        brand1,
        product_2_description,
        product_2_distributor_price,
        product_2_sale_price,
        product_2_warranty_length,
    )

    global product_3
    product_3 = Product(
        product_2_name, product_type_3, brand2, product_2_description, 130, 500, 300
    )

    global product_4
    product_4 = Product(
        product_2_name, product_type_4, brand2, product_2_description, 140, 360, 150
    )

    product_repository.save(product_1)
    product_repository.save(product_2)
    product_repository.save(product_3)
    product_repository.save(product_4)


def create_stock_from_products():
    all_products = product_repository.select_all()
    choices = range(0,30)
    
    for product in all_products:
        item_to_stock = Stock(product)
        random_number = random.choice(choices)
        item_to_stock.modify_count(random_number)

        stock_repository.save(item_to_stock)


clear_all_tables()
setup_product_types()
setup_brands()
setup_products()
create_stock_from_products()


pdb.set_trace()
