CREATE TYPE contractType AS ENUM ('tipo1','tipo2','tipo3');--pendiente
CREATE TYPE itemType AS ENUM ('Escenario', 'Audio', '3Dmodel');--pendiente

CREATE TABLE servidor(
	nombre			varchar(35), -- Porque no id?
	usuario_nombre	varchar(30),
	ip				varchar(15),
	activo			boolean,
	idioma			varchar(10),
	locacion		varchar(15)
);

CREATE TABLE usuario(
	nombre			varchar(30),
	is_jugador 		boolean,
	is_comerciante	boolean,
	is_server_Owner 	boolean
);

CREATE TABLE sala(
	servidor_nombre	varchar(35),
	codigo			int,
	--UsuarioNombre	varchar(30),
   	en_juego			boolean
	--Jugadores		varchar(30)
);

CREATE TABLE partida(
	codigo			int,
	servidor_nombre	varchar(30), -- para que si sala solo pertenece a un servidor
	sala_codigo		int,
	-- Jugadores		varchar(30), innecesario por la tabla juega
	fecha			date,
	duracion		time,
	escenario_nombre	varchar(16)
	-- acciones		varchar(255)--direccion en disco de las acciones hechas en esa partida
);

CREATE TABLE juega(
	usuario_nombre	varchar(30),
	partida_codigo	int
);

CREATE TABLE item(
	nombre			varchar(60),
	limite_usos		int,
	descripcion		varchar(255),
	contrato		contractType,
	tipo			itemType,
	precio			int
);

CREATE TABLE posee(
	usuario_nombre	varchar(30),
	item_nombre		varchar(60)
);
