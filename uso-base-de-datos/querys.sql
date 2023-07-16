-- Busquedas por idPersona
SELECT * FROM PERSONA WHERE idPersona = 2;
SELECT * FROM PERSONA WHERE idPersona IN (1,2);

-- Creacion
INSERT INTO Persona ( idPersona, nombrePersona, apellidoPersona, emailPersona ) VALUES ( 3, 'Erick', 'Anariba', 'eanariba@gmail.com' );

-- Actualizacion
UPDATE Persona SET nombrePersona = 'Erickson', apellidoPersona = 'Jimenez' WHERE idPersona = 4;

-- Delete
DELETE FROM Persona WHERE idPersona = 5;