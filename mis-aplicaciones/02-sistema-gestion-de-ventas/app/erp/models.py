from django.db import models
import datetime

'''
    Tablas
        Client
        Product
        Category
        DetSale
        Sale
'''

class Client( models.Model ):
    firstName = models.CharField( max_length=80, null=False, verbose_name='First Name' )
    lastName = models.CharField( max_length=80, null=False, verbose_name='Last Name' )
    dni = models.CharField( max_length=15, null=False, verbose_name='DNI' )
    gender = models.CharField( max_length=1, null=False )
    birthdayDate = models.DateField( null=False )
    address = models.TextField( null=True )
    status = models.BooleanField( null=False, default=True )

    def __str__(self) -> str:
        return f'{ self.firstName } { self.lastName }' 

    class Meta():
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        db_table='Client'
        ordering = ['id']

class Category( models.Model ):
    name = models.CharField( max_length=80, null=False )
    desc = models.TextField()

    def __str__(self) -> str:
        return f'{ self.categoryName }'
    
    class Meta():
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table='Category'
        ordering = ['id']

class Product( models.Model ):
    category = models.ForeignKey( 
        Category, 
        on_delete=models.PROTECT,
        null=False
    )
    name = models.CharField( max_length=80, null=False )
    
    def __str__(self) -> str:
        return f'{ self.categoryName }'
    
    class Meta():
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table='Product'
        ordering = ['id']

class Sale( models.Model ):
    client = models.ForeignKey( 
        Client, 
        on_delete=models.PROTECT,
        null=False
    )
    subTotal = models.DecimalField( default=0.00, max_digits=15, decimal_places=2 )
    tax = models.DecimalField( default=0.00, max_digits=15, decimal_places=2 )
    total = models.DecimalField( default=0.00, max_digits=15, decimal_places=2 )
    createdAt = models.DateTimeField( default=datetime.datetime.now  )
    status = models.BooleanField( null=False, default=True )
    detailProductSale = models.ManyToManyField(
        Product,
        through='DetailProductSale',
        blank=True
    )

    def __str__(self) -> str:
        return f'Client: { self.client } Sale Date: { self.saleDate }'
    
    class Meta():
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'
        db_table='Sale'
        ordering = ['id']

class DetailProductSale( models.Model ):
    sale = models.ForeignKey( 
        Sale,
        on_delete=models.PROTECT,
        null=True
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        null=True
    )
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField( default=0.00, max_digits=15, decimal_places=2 )
    subTotal = models.DecimalField( default=0.00, max_digits=15, decimal_places=2 )

    def __str__(self) -> str:
        return f'DetailProductSale: { self.sale } Sale Date: { self.product }'

    class Meta():
        verbose_name = 'DetailProductSale'
        verbose_name_plural = 'DetailProductsSales'
        db_table='DetailProductSale'
        ordering = ['id']
