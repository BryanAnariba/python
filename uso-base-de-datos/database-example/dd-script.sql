CREATE TABLE Persona (
	idPersona INT NOT NULL PRIMARY KEY,
	nombrePersona VARCHAR(80) NOT NULL,
	apellidoPersona VARCHAR(80) NOT NULL,
	emailPersona VARCHAR(100) NOT NULL
);

CREATE OR ALTER FUNCTION getLastIdFromPersona()
	RETURNS INT
	AS
	BEGIN
		DECLARE @idPersona INT
		SET @idPersona = (SELECT MAX(idPersona) + 1 as idSiguiente FROM Persona)
		RETURN @idPersona;
	END;