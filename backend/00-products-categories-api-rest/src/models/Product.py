from Category import Category

class Product( Category ):

    def __init__(self, categoryId: int, categoryName: str, productId: int, productName: str, productPrice: float, productStock: int) -> None:
        super().__init__(categoryId, categoryName)
        self.__productId = productId
        self.__productName = productName
        self.__productPrice = productPrice
        self.__productStock = productStock

    @property
    def productId( self ) -> int:
        return self.__productId
    
    @property
    def productName( self ) -> str:
        return self.__productName
    
    @property
    def productPrice( self ) -> float:
        return self.__productPrice
    
    @property
    def productStock( self ) -> int:
        return self.__productStock
    
    @productId.setter
    def productId( self, productId: int ) -> None:
        self.__productId = productId
    
    @productName.setter
    def productName( self, productName: str ) -> None:
        self.__productName = productName

    @productPrice.setter
    def productPrice( self, productPrice: float ) -> None:
        self.__productPrice = productPrice

    @productStock.setter
    def productStock( self, productStock: int ) -> None:
        self.__productStock = productStock

    def toJson( self ):
        return  { 
            'productId': self.productId,
            'productName': self.productName,
            'productPrice': self.productPrice,
            'productStock': self.productStock,
            'categoryId': self.categoryId, 
            'categoryName': self.categoryName
        }