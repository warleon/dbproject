CREATE SCHEMA db_project10_3; -- mil datos
CREATE SCHEMA db_project10_4; -- 10 mil datos
CREATE SCHEMA db_project10_5; -- 100 mil datos
CREATE SCHEMA db_project10_6; -- 1 millon de datos

-- Assumes dbproject folder in $HOME
SET SCHEMA 'db_project10_3';
\i dbproject/db/tables.sql
\i dbproject/db/constraints.sql

SET SCHEMA 'db_project10_4';
\i dbproject/db/tables.sql
\i dbproject/db/constraints.sql

SET SCHEMA 'db_project10_5';
\i dbproject/db/tables.sql
\i dbproject/db/constraints.sql

SET SCHEMA 'db_project10_6';
\i dbproject/db/tables.sql
\i dbproject/db/constraints.sql