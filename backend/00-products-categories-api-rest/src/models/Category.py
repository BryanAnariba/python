
class Category:

    def __init__(self, categoryId: int, categoryName: str) -> None:
        self.__categoryId = categoryId
        self.__categoryName= categoryName

    @property
    def categoryId( self ) -> int:
        return self.__categoryId
    
    @property
    def categoryName( self ) -> str:
        return self.__categoryName
    
    @categoryId.setter
    def categoryId( self, categoryId: int ) -> None:
        self.__categoryId = categoryId

    @categoryName.setter
    def categoryName( self, categoryName: str ) -> None:
        self.__categoryName = categoryName

    def toJson(self):
        return  { 'categoryId': self.__categoryId, 'categoryName': self.__categoryName }