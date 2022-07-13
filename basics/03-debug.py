def calIMC( weight, height ):
    IMC = weight / ( height * height )
    if ( IMC > 0 and IMC < 20 ):
        return "Your IMC is: " + str( IMC ) + ", You are thin"
    elif ( IMC >= 20 and IMC < 26 ):
        return "Your IMC is: " + str( IMC ) + ",You are normal"
    elif ( IMC >= 26 and IMC < 30 ):
        return "Your IMC is: " + str( IMC ) + ", You are fat"
    elif ( IMC >= 30 ):
        return "Your IMC is: " + str( IMC ) + ", You are very very very fat......"
    else:
        return "Invalid IMC"
        
weight = float( input( "Write your weight in KG: " ) )
height = float( input( "Write your height in CM: " ) )
print( calIMC( weight, height ) )