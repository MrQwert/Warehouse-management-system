import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

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
#            price=price
        )

        ProductCategory.objects.create(
            product=product,
            category=category
        )

        return product

    except ValidationError as e:
        print(f"Error al crear el producto: {e}")


if __name__ == '__main__':
    title = input("Introduzca el título del producto: ")
    product_class_name = input("Introduzca la clase de producto (ej. 'Libros', 'Electrónica'): ")
    category_name = input("Introduzca la categoría del producto (ej. 'Ficción', 'Smartphones'): ")
#    price = float(input("Introduzca el precio del producto: "))

    new_product = create_product(title, product_class_name, category_name )

    if new_product:
        print(f"Producto '{new_product.title}' creado con éxito.")
