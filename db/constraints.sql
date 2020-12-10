--usuario constraints
ALTER TABLE usuario
ADD CONSTRAINT usuario_pk_nombre
PRIMARY KEY (nombre);


--servidor constraints
ALTER TABLE servidor
ADD CONSTRAINT serv_pk_nombre
PRIMARY KEY (nombre);

ALTER TABLE servidor
ADD CONSTRAINT serv_fk_unombre
FOREIGN KEY (usuario_nombre)
REFERENCES usuario(nombre);


--sala constraints
ALTER TABLE sala
ADD CONSTRAINT sala_pk_codigo_jugadores
PRIMARY KEY (codigo);

ALTER TABLE sala
ADD CONSTRAINT sala_fk_snombre
FOREIGN KEY (servidor_nombre)
REFERENCES servidor(nombre);

-- ALTER TABLE sala
-- ADD CONSTRAINT todos_son_jugadores
-- FOREIGN KEY (jugadores)
-- REFERENCES usuario(nombre);


--partida constraints
ALTER TABLE partida
ADD CONSTRAINT part_pk_codigo
PRIMARY KEY (codigo);

ALTER TABLE partida
ADD CONSTRAINT part_fk_snombre
FOREIGN KEY (servidor_nombre)
REFERENCES servidor(nombre);

ALTER TABLE partida
ADD CONSTRAINT part_fk_scodigo
FOREIGN KEY (sala_codigo)
REFERENCES sala(codigo);

/*
ALTER TABLE partida
ADD CONSTRAINT PEscenario
CHECK (EscenarioNombre IN ( SELECT nombre
                            FROM item
                            WHERE tipo="Escenario")
);
*/

--juega constraints
ALTER TABLE juega
ADD CONSTRAINT juega_pk_usuario_partida
PRIMARY KEY (usuario_nombre, partida_codigo);

ALTER TABLE juega
ADD CONSTRAINT juega_fk_usuario
FOREIGN KEY (usuario_nombre)
REFERENCES usuario(nombre);

ALTER TABLE juega
ADD CONSTRAINT juega_fk_partida
FOREIGN KEY (partida_codigo)
REFERENCES partida(codigo);


--item constraints
ALTER TABLE item
ADD CONSTRAINT item_pk_nombre
PRIMARY KEY (nombre);


--posee constraints
ALTER TABLE posee
ADD CONSTRAINT posee_pk_usuario_item
PRIMARY KEY (usuario_nombre, item_nombre);

ALTER TABLE posee
ADD CONSTRAINT posee_fk_usuario
FOREIGN KEY (usuario_nombre)
REFERENCES usuario(nombre);

ALTER TABLE posee
ADD CONSTRAINT posee_fk_item
FOREIGN KEY (item_nombre)
REFERENCES item(nombre);

/*
ALTER TABLE posee
ADD CONSTRAINT limite
CHECK ((SELECT count()
        FROM item I
        WHERE ItemNombre=I.nombre));
*/