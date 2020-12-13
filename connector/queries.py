Q1 = "select Se.locacion, Se.nombre, count(distinct Ju.usuario_nombre) as ju_act \
from sala Sa, partida Pa, juega Ju, servidor Se \
where \
	Sa.codigo=Pa.sala_codigo and \
	Ju.partida_codigo=Pa.codigo and \
	Se.nombre=Sa.servidor_nombre and \
	Se.activo=true and \
	extract(week from Pa.fecha)=extract(week from now()) \
group by Se.locacion, Se.nombre \
order by locacion, ju_act desc"

Q2 = "create temporary table LPH as \
	SELECT Se.locacion, Ju.usuario_nombre as nombre, sum(Pa.duracion) as tjugado \
	FROM juega Ju, Partida Pa, servidor Se \
	WHERE \
		Ju.partida_codigo = Pa.codigo and \
		Se.nombre = Pa.servidor_nombre \
	group by Se.locacion, Ju.usuario_nombre \
	; \
select i1.locacion, i1.nombre, i1.tjugado \
from LPH i1 \
where ( \
	select count(*) \
	from LPH i2 \
	where i1.locacion=i2.locacion and i1.tjugado<i2.tjugado \
)<100 \
;"

Q3 = "select distinct posee.item_nombre, count(LPH.nombre) vecesusado, sum(LPH.tjugado) tiempoacc \
from LPH, posee \
where \
	LPH.nombre=posee.usuario_nombre \
group by posee.item_nombre \
order by tiempoacc desc \
;"

Q4 = "SELECT S.nombre as servidor, avg(P.duracion) as duracion_media \
FROM partida P, servidor S \
WHERE P.servidor_nombre = S.nombre \
group by S.nombre \
order by duracion_media desc \
;"

Q5 = "select distinct posee.item_nombre, count(LPH.nombre) vecesusado, sum(LPH.tjugado) tiempoacc \
from LPH, posee, item \
where \
	LPH.nombre=posee.usuario_nombre and \
	item.nombre=posee.item_nombre and \
	item.tipo = 'Escenario'::itemtype \
group by posee.item_nombre \
;"

Q6 = "SELECT usuario_nombre, sum(bajas) as bajas_totales, sum(muertes) as muertes_totales \
FROM juega \
group by usuario_nombre \
order by bajas_totales \
;"

queries = [Q1, Q2, Q3, Q4, Q5, Q6]