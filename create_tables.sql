create table namelist (
    id serial primary key,
    label varchar(100) not null,
    when_entered timestamp without time zone NOT NULL DEFAULT now()
 );

create table names(
   id serial primary key,
   name varchar(100) not null,
   details jsonb 
   when_entered timestamp without time zone NOT NULL DEFAULT now()
);