CREATE TYPE contractType AS ENUM ('tipo1','tipo2','tipo3');--pendiente
CREATE TYPE itemType AS ENUM ('Escenario', 'Audio', '3Dmodel');--pendiente


CREATE TABLE servidor(
	Nombre			varchar(35),
	UsuarioNombre	varchar(30),
	ip				varchar(15),
	activo			boolean,
	jugadores		int,
	flujo			int,
	idioma			varchar(10),
	locacion		varchar(15)
);

CREATE TABLE usuario(
	nombre			varchar(30),
	tipo			varchar(3)
	--j(jugador)c(comerciante)s(server-owner)
);

CREATE TABLE sala(
	ServidorNombre	varchar(35),
	codigo			int,
	UsuarioNombre	varchar(30),
   	enJuego			boolean,
	listaJugadores	varchar(30)[]
);

CREATE TABLE partida(
	codigo			int,
	ServidorNombre	varchar(30),
	SalaCodigo		int,
	--listaJugadores	varchar(30)[]--innecesario x la tabla juega
	fecha			date,
	duracion		float,
	EscenarioNombre	varchar(16),
	acciones		varchar(255)--direccion en disco de las acciones hechas en esa partida
);

CREATE TABLE juega(
	UsuarioNombre	varchar(30),
	PartidaCodigo	int
);

CREATE TABLE item(
	nombre			varchar(60),
	limiteUsos		int,
	descripcion		varchar(255),
	contrato		contractType,
	tipo			itemType,
	data			bytea
);

CREATE TABLE posee(
	UsuarioNombre	varchar(30),
	ItemNombre		varchar(60)
);
