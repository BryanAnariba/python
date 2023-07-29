class Category:

    def __init__(self, categoryId: int, categoryName: str) -> None:
        self._categoryId = categoryId
        self._categoryName = categoryName

    @property
    def categoryId( self ) -> int:
        return self._categoryId

    @property
    def categoryName( self ) -> str:
        return self._categoryName

    @categoryId.setter
    def categoryId( self, categoryId ) -> None:
        self._categoryId = categoryId

    @categoryName.setter
    def categoryName( self, categoryName ) -> None:
        self._categoryName = categoryName

    def toJson (self):
        return {
            'categoryId': self._categoryId,
            'categoryName': self._categoryName
        }
