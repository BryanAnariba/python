from django.db import models

'''
    Required Tables
        - Without Relationship
            Gender
            Category
        - With Relationship
            Client with Gender
            Product with Category
            Sale with Client

        - Intermediate Table
            SaleByProduct
'''

class Gender( models.Model ):
    gender_name = models.CharField( max_length=80, null=False, verbose_name='Gender Name' )

    def __str__(self) -> str:
        return f'{ self.gender_name }'
    
    class Meta():
        verbose_name = 'Gender'
        verbose_name_plural = 'Genders'
        db_table = 'Gender'
        ordering = [ 'id' ]

class Category( models.Model ):
    category_name = models.CharField( max_length=80, null=False, verbose_name='Category Name' )
    category_desc = models.CharField( max_length=150, null=False, verbose_name='Category Name' )

    def __str__(self) -> str:
        return f'{ self.category_name } { self.category_desc }'
    
    class Meta():
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'Category'
        ordering = [ 'id' ]

class Client( models.Model ):
    client_gender = models.ForeignKey( Gender, on_delete=models.PROTECT, null=False )
    client_first_name = models.CharField( max_length=80, null=False, verbose_name='Client Name' )
    client_last_name = models.CharField( max_length=80, null=False, verbose_name='Client Last Name' )
    client_document_identity = models.CharField( max_length=15, null=False, verbose_name='Document of Identity' )
    client_birth_date = models.DateField( null=False )
    client_address = models.TextField( null=True )
    client_status = models.BooleanField( default=True, null=False )

    def __str__(self) -> str:
        return f'{ self.client_first_name } { self.client_last_name }'
    
    class Meta():
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        db_table = 'Client'
        ordering = [ 'id' ]

class Product( models.Model ):
    product_category = models.ForeignKey( Category, on_delete=models.PROTECT, null=False )
    product_name = models.CharField( max_length=80, null=False, verbose_name='Product Name' )
    product_image = models.ImageField( upload_to='image/%Y/%m/%d' )
    producto_pvp = models.TextField()

    def __str__(self) -> str:
        return f'{ self.product_name }'
    
    class Meta():
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table = 'Product'
        ordering = [ 'id' ]

class Sale( models.Model ):
    sale_client = models.ForeignKey( Client, on_delete=models.PROTECT, null=False )
    sale_sub_total = models.DecimalField( default=0.00, decimal_places=2, max_digits=15 )
    sale_tax = models.DecimalField( default=0.00, decimal_places=2, max_digits=15 )
    sale_total = models.DecimalField( default=0.00, decimal_places=2, max_digits=15 )
    sale_created_add = models.DateTimeField()
    sale_product = models.ManyToManyField( Product, through='SaleByProduct', blank=True )

    def __str__(self) -> str:
        return  f'Client Id: { self.sale_client } - Sale Date: { self.sale_created_add }'
    
    class Meta():
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'
        db_table = 'Sale'
        ordering = [ 'id' ]

class SaleByProduct( models.Model ):
    sale = models.ForeignKey( Sale, on_delete=models.PROTECT, null=False )
    product = models.ForeignKey( Product, on_delete=models.PROTECT, null=False )
    sale_by_product_price = models.DecimalField( default=0.00, max_digits=15, decimal_places=2 )
    sale_by_product_quantity = models.PositiveIntegerField( default=0 )
    sale_by_product_subtotal = models.DecimalField( default=0.00, max_digits=15, decimal_places=2 )

    def __str__(self) -> str:
        return f'Sale: { self.sale } - Product: { self.product } - Subtotal: { self.sale_by_product_subtotal }'
    
    class Meta():
        verbose_name = 'SaleByProduct'
        verbose_name_plural = 'SalesByProducts'
        db_table = 'SaleByProduct'
        ordering = [ 'id' ]