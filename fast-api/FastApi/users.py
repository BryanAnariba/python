from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from services.user import getAllUsers, getUser, saveUser, User,searchUser

app = FastAPI()

@app.post( '/api/users', status_code=status.HTTP_201_CREATED )
async def createUser( userData: User ):
    user = searchUser( userData.uid )
    if type( user ) == User:
        raise HTTPException( status_code=status.HTTP_400_BAD_REQUEST, detail=( 'User ' + userData.name + ' already exists' ) )
    else:
        return  { 'statusCode': status.HTTP_200_OK, 'data': saveUser( userData ) }

@app.get( '/api/users', status_code=status.HTTP_200_OK )
async def getUsers():
    return getAllUsers()

@app.get( '/api/users/{uid}' )
async def getUserById( uid: int ):
    try:
        user = getUser( uid )
        response = list( user )[0]
        return  { 'statusCode': status.HTTP_200_OK, 'data': response }
    except:
        response = [{ 'error': 'User not found'}]
        raise HTTPException( status_code = status.HTTP_400_BAD_REQUEST, detail='User Not Found' )

