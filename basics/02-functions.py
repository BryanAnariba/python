def viewFinalPrice( product, price, discount ):
    finalPrice = ( price - ( ( discount * price) / 100 ))
    return "The Final Price of " + product + ' is: $.' + str( finalPrice )

def calIMC( weight, height ):
    IMC = weight / ( height * height )
    if ( IMC > 0 and IMC < 20 ):
        return "Your IMC is: " + str( IMC ) + ", You are thin"
    elif ( IMC >= 20 and IMC < 26 ):
        return "Your IMC is: " + str( IMC ) + ",You are normal"
    elif ( IMC >= 26 and IMC < 30 ):
        return "Your IMC is: " + str( IMC ) + ",Your are fat"
    elif ( IMC >= 30 ):
        return "Your IMC is: " + str( IMC ) + ",Your are very very very fat......"
    else:
        return "Invalid IMC"

print( viewFinalPrice( 'Pant', 40, 20 ) )
print( viewFinalPrice( 'Skirt', 30, 15 ) )

# IMC CALCULATOR
# Formule => IMC = weight / ( height * height )
# <= 19 => YOU ARE THIN
# 20 <= imc <= 25 normal
# 26 <= imc <= 30 fat
# >= 30 super fat

weight = float( input( "Write your weight in KG: " ) )
height = float( input( "Write your height in CM: " ) )
print( calIMC( weight, height ) )

# 1: 21


