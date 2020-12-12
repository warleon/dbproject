--query 1
select Se.locacion, Se.nombre, count(distinct Ju.usuario_nombre) as ju_act
from sala Sa, partida Pa, juega Ju, servidor Se
where
	Sa.codigo=Pa.sala_codigo and
	Ju.partida_codigo=Pa.codigo and
	Se.nombre=Sa.servidor_nombre and
	Se.activo=true and
	extract(week from Pa.fecha)=extract(week from now())
group by Se.locacion, Se.nombre
order by locacion, ju_act desc
;
--query 2
create temporary table LPH as
	SELECT Se.locacion, Ju.usuario_nombre as nombre, sum(Pa.duracion) as tjugado
	FROM juega Ju, Partida Pa, servidor Se
	WHERE
		Ju.partida_codigo = Pa.codigo and
		Se.nombre = Pa.servidor_nombre
	group by Se.locacion, Ju.usuario_nombre
	;

select i1.locacion, i1.nombre, i1.tjugado
from LPH i1
where (
	select count(*)
	from LPH i2
	where i1.locacion=i2.locacion and i1.tjugado<i2.tjugado
)<100
;

--query 3
SELECT
FROM
WHERE
;

--query 4
SELECT
FROM
WHERE
;

--query 5
SELECT
FROM
WHERE
;