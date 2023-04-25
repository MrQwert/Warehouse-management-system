import csv
from django.core.exceptions import ValidationError
from oscar.core.loading import get_model

Product = get_model('catalogue', 'Product')
ProductClass = get_model('catalogue', 'ProductClass')
ProductCategory = get_model('catalogue', 'ProductCategory')
Category = get_model('catalogue', 'Category')


def create_product(title, product_class_name, category_name):
    try:
        product_class, _ = ProductClass.objects.get_or_create(name=product_class_name)
        category, _ = Category.objects.get_or_create(name=category_name)

        product = Product.objects.create(
            title=title,
            product_class=product_class,
        )

        ProductCategory.objects.create(
            product=product,
            category=category
        )

        return product

    except ValidationError as e:
        print(f"Error al crear el producto: {e}")


def import_products_from_csv(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            title = row['Título del producto']
            product_class_name = row['Clase del producto']
            category_name = row['Categoría del producto']
            new_product = create_product(title, product_class_name, category_name)

            if new_product:
                print(f"Producto '{new_product.title}' creado con éxito.")

