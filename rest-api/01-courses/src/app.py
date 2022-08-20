from ast import Pass
from asyncio.windows_events import NULL
from flask import Flask, jsonify, request
from config import config
from flask_mysqldb import MySQL

app = Flask( __name__ )
conn = MySQL( app )

@app.route( '/' )
def index():
    return jsonify([ { 'status': 200, 'data': 'Server Started on port 5000' }] ) 

@app.route( '/courses', methods=[ 'GET' ] )
def getCourses():
    try:
        cursor = conn.connection.cursor()
        sql = "SELECT * FROM Course"
        cursor.execute( sql )
        data = cursor.fetchall()
        courses = []
        for row in data:
            course = { 'Code': row[0], 'Name': row[1], 'Credits': row[2] }
            courses.append( course )
        return jsonify([{ 'status': 200, 'data': courses }])
    except Exception as ex:
        return jsonify([{ 'status': 400, 'data': f"Error: { ex }" }]), 400

@app.route( '/courses/<courseId>', methods = [ 'GET' ] )
def getCourse( courseId ):
    try:
        cursor = conn.connection.cursor()
        sql = "SELECT * FROM Course WHERE Code = '{0}'".format(courseId)
        #sql = "SELECT * FROM Course WHERE Code = '%s'"
        #cursor.execute( sql, ( courseId ) )
        cursor.execute( sql )
        data = cursor.fetchone()
        if data:
            course = { 'Code': data[0], 'Name': data[1], 'Credits': data[2] }
            return jsonify([ { 'status': 200, 'data': course } ]), 200
        else:
            return jsonify([ { 'status': 200, 'data': 'Course Not Found' } ])
    except Exception as ex:
        return jsonify([{ 'status': 400, 'data': f"Error: { ex }" }]), 400


@app.route( '/courses', methods=[ 'POST' ] )
def createNewCourse():
    try:
        Code = request.json[ 'Code' ]
        Name = request.json[ 'Name' ]
        Credits = request.json[ 'Credits' ]
        cursor = conn.connection.cursor()
        sql = "SELECT * FROM Course WHERE Code = '{0}'".format( Code )
        cursor.execute( sql )
        data = cursor.fetchone()
    
        if data:
            return jsonify([ { 'status': 200, 'data': 'Course Already Exists' } ]), 200
        else:
            cursor = conn.connection.cursor()
            sql = "INSERT INTO course ( Code, Name, Credits ) VALUES ( %s, %s, %s )"
            values = ( Code, Name, Credits )
            cursor.execute( sql, values )
            conn.connection.commit()
            return jsonify([ { 'status': 201, 'data': "Course {0} Created Successfully".format( Name ) } ]), 201

    except Exception as ex:
        return jsonify([{ 'status': 400, 'data': f"Error: { ex }" }]), 400

@app.route( '/courses/<courseId>', methods = [ 'PUT' ] )
def updateCourse( courseId ):
    try:
        #Code = request.json[ 'Code' ]
        Name = request.json[ 'Name' ]
        Credits = request.json[ 'Credits' ]
        cursor = conn.connection.cursor()
        sql = 'UPDATE Course SET Name = %s, Credits= %s WHERE Code = %s'
        values = ( Name, Credits, courseId )
        cursor.execute( sql, values )
        conn.connection.commit()
        return jsonify({ 'status': 200, 'data': "Course {0} Updated Successfully".format( Name ) }), 200
    except Exception as ex:
        return jsonify([{ 'status': 400, 'data': "Error: { ex }" }]), 400
@app.route( '/courses/<courseId>', methods = [ 'DELETE' ] )
def deleteCourse( courseId ):
    try:
        cursor = conn.connection.cursor()
        sql = "SELECT * FROM Course WHERE Code = '{0}'".format( courseId )
        cursor.execute( sql )
        data = cursor.fetchone()
    
        if data == None:
            return jsonify([ { 'status': 200, 'data': 'Course Does Not Exists' } ]), 200
        else:
            sql = "DELETE FROM Course WHERE Code = '{0}'".format( courseId )
            #values = ( courseId )
            cursor.execute( sql )
            conn.connection.commit()
            return jsonify([{ 'status': 204, 'data': 'Deleted Successfully' }]), 200
    except Exception as ex:
        return jsonify([{ 'status': 400, 'data': f"Error: { ex }" }]), 400

def pageNotFound( error ):
    return jsonify([ { 'status': 404, 'data': 'Request Not Found' }] ), 404

if ( __name__ == '__main__' ):
    app.config.from_object( config[ 'development' ] )
    app.register_error_handler( 404, pageNotFound )
    app.run()