from flask import Flask
from flask import render_template, request, redirect
from flaskext.mysql import MySQL

app = Flask( __name__ )
mysqlConnection = MySQL()
app.config[ 'MYSQL_DATABASE_HOST' ] = 'localhost'
app.config[ 'MYSQL_DATABASE_USER' ] = 'root'
app.config[ 'MYSQL_DATABASE_PASSWORD' ] = ''
app.config[ 'MYSQL_DATABASE_DB' ] = 'bookdev'
mysqlConnection.init_app( app )

# Rutas Publicas Usuario
@app.route( '/' )
def inicio():
    return render_template( 'site/index.html' )

@app.route( '/books' )
def books():
    return render_template( 'site/books.html' )

@app.route( '/about' )
def about():
    return render_template( 'site/about.html' )

# RUTAS PARA ADMIN
@app.route( '/admin/' )
def admin_route():
        return render_template( 'admin/index.html' )

@app.route( '/admin/login' )
def admin_login_route():
    return render_template( 'admin/login.html' )

@app.route( '/admin/books' )
def admin_books_route():
    sql = 'SELECT * FROM Book'
    connection = mysqlConnection.connect()
    #print( connection )
    cursor = connection.cursor()
    cursor.execute( sql )
    books = cursor.fetchall()
    connection.commit()
    #print( books )
    return render_template( 'admin/books.html', data = books )

@app.route( '/admin/books/save', methods=[ 'POST' ] )
def admin_save_book_route():
    bookName = request.form[ 'bookName' ]
    bookUrl = request.form[ 'bookUrl' ]
    bookImage = request.files[ 'bookImage' ]
    sql = "INSERT INTO Book ( bookName, bookUrl, bookImage ) VALUES ( %s, %s, %s )"
    values = ( bookName, bookUrl, bookImage )
    connection = mysqlConnection.connect()
    cursor = connection.cursor()
    cursor.execute( sql, values )
    connection.commit()
    # print( bookName )
    # print( bookUrl )
    # print( bookImage )
    return redirect( '/admin/books' )

@app.route( '/admin/books/delete', methods=[ 'POST' ] )
def admin_delete_book_route():
    connection = mysqlConnection.connect()
    sql = "DELETE FROM Book Where id = %s"
    values = ( request.form[ 'bookId' ] )
    cursor = connection.cursor()
    cursor.execute( sql, values )
    connection.commit()
    return redirect( '/admin/books' )


# Levantar server
if __name__ == '__main__':
    app.run( debug = True ) #EJECUTAMOS LA APLICACION CON DEBUG PARA VER ERRORES

# 2: 07
