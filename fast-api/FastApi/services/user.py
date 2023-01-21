from pydantic import BaseModel

class User(BaseModel):
    uid: int
    name: str
    surname: str
    url: str
    age: int

users = [
    User( uid = 1, name = 'Bryan Ariel', surname = 'Sanchez Anariba', url = 'https://bryan.dev', age = 25 ),
    User( uid = 2, name = 'Usuario Dos', surname = 'Sanchez Anariba', url = 'https://usuariodos.dev', age = 20 ),
    User( uid = 3, name = 'Usuario Tres', surname = 'Sanchez Anariba', url = 'https://usuariotres.dev', age = 30 )
]

def searchUser( uid: int ):
    try:
        userData = filter( lambda user: user.uid == uid, users )
        return list( userData )[0]
    except:
        return { 'error': 'User Not Found' }


def getUser( uid: int ):
    return filter( lambda user: user.uid == uid, users )

def getAllUsers():
    return { 'statusCode': 200, 'data': users }

def saveUser( userData: User ):
    users.append( userData )
    return { 'statusCode': 201, 'data': userData }