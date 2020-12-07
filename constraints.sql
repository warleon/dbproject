--usuario constraints
ALTER TABLE usuario
ADD CONSTRAINT usuario_pk_nombre
PRIMARY KEY (Nombre);


--servidor constraints
ALTER TABLE servidor
ADD CONSTRAINT serv_pk_nombre
PRIMARY KEY (Nombre);

ALTER TABLE servidor
ADD CONSTRAINT serv_fk_unombre
FOREIGN KEY (UsuarioNombre)
REFERENCES usuario(Nombre);


--sala constraints
ALTER TABLE sala
ADD CONSTRAINT sala_pk_codigo
PRIMARY KEY (codigo);

ALTER TABLE sala
ADD CONSTRAINT sala_fk_snombre
FOREIGN KEY (ServidorNombre)
REFERENCES servidor(Nombre);

// TODO fix
/* ALTER TABLE sala
ADD CONSTRAINT todosSonJugadores
CHECK (ALL (listaJugadores) in usuario.Nombre); */


--partida constraints
ALTER TABLE partida
ADD CONSTRAINT part_pk_codigo
PRIMARY KEY (codigo);

ALTER TABLE partida
ADD CONSTRAINT part_fk_snombre
FOREIGN KEY (ServidorNombre)
REFERENCES servidor(Nombre);

ALTER TABLE partida
ADD CONSTRAINT part_fk_scodigo
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
ADD CONSTRAINT juega_pk_usuario_partida
PRIMARY KEY (UsuarioNombre, PartidaCodigo);

ALTER TABLE juega
ADD CONSTRAINT juega_fk_usuario
FOREIGN KEY (UsuarioNombre)
REFERENCES usuario(nombre);

ALTER TABLE juega
ADD CONSTRAINT juega_fk_partida
FOREIGN KEY (PartidaCodigo)
REFERENCES partida(codigo);


--item constraints
ALTER TABLE item
ADD CONSTRAINT item_pk_nombre
PRIMARY KEY (Nombre);


--posee constraints
ALTER TABLE posee
ADD CONSTRAINT posee_pk_usuario_item
PRIMARY KEY (UsuarioNombre, ItemNombre);

ALTER TABLE posee
ADD CONSTRAINT posee_fk_usuario
FOREIGN KEY (UsuarioNombre)
REFERENCES usuario(nombre);

ALTER TABLE posee
ADD CONSTRAINT posee_fk_item
FOREIGN KEY (ItemNombre)
REFERENCES item(Nombre);

/*
ALTER TABLE posee
ADD CONSTRAINT limite
CHECK ((SELECT count()
        FROM item I
        WHERE ItemNombre=I.nombre));
*/