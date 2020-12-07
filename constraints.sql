--servidor constraints
ALTER TABLE servidor
ADD CONSTRAINT pk_snombre
PRIMARY KEY (Nombre);

ALTER TABLE servidor
ADD CONSTRAINT fk_unombre
FOREIGN KEY (UsuarioNombre)
REFERENCES usuario(Nombre);

--usuario constraints
ALTER TABLE usuario
ADD CONSTRAINT pk_unombre
PRIMARY KEY (Nombre);

--sala constraints
ALTER TABLE sala
ADD CONSTRAINT pk_scodigo
PRIMARY KEY (codigo);

ALTER TABLE sala
ADD CONSTRAINT sfk_snombre
FOREIGN KEY (ServidorNombre)
REFERENCES servidor(Nombre);

ALTER TABLE sala
ADD CONSTRAINT todosSonJugadores
CHECK (ALL (listaJugadores) in usuario.Nombre);

--partida constraints
ALTER TABLE partida
ADD CONSTRAINT pk_pcodigo
PRIMARY KEY (codigo);

ALTER TABLE partida
ADD CONSTRAINT pfk_snombre
FOREIGN KEY (ServidorNombre)
REFERENCES servidor(Nombre);

ALTER TABLE partida
ADD CONSTRAINT pfk_scodigo
FOREIGN KEY (SalaCodigo)
REFERENCES sala(codigo);

ALTER TABLE partida
ADD CONSTRAINT PEscenario
CHECK (EscenarioNombre IN ( SELECT nombre
                            FROM item
                            WHERE tipo="Escenario")
);

--juega constraints
ALTER TABLE juega
ADD CONSTRAINT pk_usuario-partida
PRIMARY KEY (UsuarioNombre, PartidaCodigo);

ALTER TABLE juega
ADD CONSTRAINT jfk_usuario
FOREIGN KEY (UsuarioNombre)
REFERENCES usuario(nombre);

ALTER TABLE juega
ADD CONSTRAINT jfk_partida
FOREIGN KEY (PartidaCodigo)
REFERENCES partida(codigo);

--item constraints
ALTER TABLE item
ADD CONSTRAINT ipk_nombre
PRIMARY KEY (Nombre);

--posee constraints
ALTER TABLE posee
ADD CONSTRAINT pk_usuario-item
PRIMARY KEY (UsuarioNombre, ItemNombre);

ALTER TABLE posee
ADD CONSTRAINT pfk_usuario
FOREIGN KEY (UsuarioNombre)
REFERENCES usuario(nombre);

ALTER TABLE posee
ADD CONSTRAINT pfk_item
FOREIGN KEY (ItemNombre)
REFERENCES item(Nombre);

/*
ALTER TABLE posee
ADD CONSTRAINT limite
CHECK ((SELECT count()
        FROM item I
        WHERE ItemNombre=I.nombre));
*/