CREATE TABLE `Academia`
(
 `idAcademia` int NOT NULL AUTO_INCREMENT ,
 `Academia`   varchar(100) NOT NULL ,
 `telefono`   varchar(45) NOT NULL ,
 `web`        varchar(255) NOT NULL ,

PRIMARY KEY (`idAcademia`)
);

CREATE TABLE `Alumno`
(
 `idAlumno`   int NOT NULL AUTO_INCREMENT ,
 `idAcademia` int NOT NULL ,
 `nombre`     varchar(80) NOT NULL ,
 `apellido`   varchar(80) NOT NULL ,
 `email`      varchar(255) NOT NULL ,
 `telefono`   varchar(45) NOT NULL ,

PRIMARY KEY (`idAlumno`),
KEY `FK_2` (`idAcademia`),
CONSTRAINT `FK_2` FOREIGN KEY `FK_2` (`idAcademia`) REFERENCES `Academia` (`idAcademia`)
);

CREATE TABLE `Profesor`
(
 `idProfesor` int NOT NULL AUTO_INCREMENT ,
 `idAcademia` int NOT NULL ,
 `nombre`     varchar(80) NOT NULL ,
 `apellido`   varchar(80) NOT NULL ,
 `email`      varchar(255) NOT NULL ,
 `telefono`   varchar(45) NOT NULL ,

PRIMARY KEY (`idProfesor`),
KEY `FK_2` (`idAcademia`),
CONSTRAINT `FK_1` FOREIGN KEY `FK_2` (`idAcademia`) REFERENCES `Academia` (`idAcademia`)
);


CREATE TABLE `Curso`
(
 `idCurso`          int NOT NULL AUTO_INCREMENT ,
 `idProfesor`       int NOT NULL ,
 `nombreCurso`      varchar(100) NOT NULL ,
 `descripcionCurso` varchar(255) NULL ,

PRIMARY KEY (`idCurso`),
KEY `FK_2` (`idProfesor`),
CONSTRAINT `FK_3` FOREIGN KEY `FK_2` (`idProfesor`) REFERENCES `Profesor` (`idProfesor`)
);

CREATE TABLE `AlumnoPorCurso`
(
 `idAlumnoPorCurso` int NOT NULL AUTO_INCREMENT ,
 `idAlumno`         int NOT NULL ,
 `idCurso`          int NOT NULL ,

PRIMARY KEY (`idAlumnoPorCurso`),
KEY `FK_1` (`idAlumno`),
CONSTRAINT `FK_4` FOREIGN KEY `FK_1` (`idAlumno`) REFERENCES `Alumno` (`idAlumno`),
KEY `FK_2` (`idCurso`),
CONSTRAINT `FK_5` FOREIGN KEY `FK_2` (`idCurso`) REFERENCES `Curso` (`idCurso`)
);

CREATE TABLE `Nota`
(
 `idNota`   int NOT NULL AUTO_INCREMENT ,
 `idAlumno` int NOT NULL ,
 `idCurso`  int NOT NULL ,
 `nota`     float NOT NULL ,

PRIMARY KEY (`idNota`),
KEY `FK_2` (`idAlumno`),
CONSTRAINT `FK_6` FOREIGN KEY `FK_2` (`idAlumno`) REFERENCES `Alumno` (`idAlumno`),
KEY `FK_3` (`idCurso`),
CONSTRAINT `FK_7` FOREIGN KEY `FK_3` (`idCurso`) REFERENCES `Curso` (`idCurso`)
);
