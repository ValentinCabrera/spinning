\c postgres
DROP database spinning;

Create database spinning;

\c spinning

create table marca (
    id serial,
    nombre varchar(50),
    constraint pk_id_marca primary key (id)
);

create table modelo (
    id serial,
    nombre varchar(50),
    garantia int,
    descripcion varchar(50),
    marca int,
    constraint pk_id_modelo primary key (id),
    constraint fk_marca_modelo foreign key (marca) references marca(id)

);
create table unidadMedida(
    id serial,
    nombre varchar(50),
    constraint pk_id_unidadMedida primary key (id)
);

create table garantia (
    id serial,
    cantidad int,
    unidadMedida int,
    constraint pk_id_garantia primary key (id),
    constraint fk_unidadMed_garantia foreign key (unidadMedida) references unidadMedida(id)
);

create table pais(
    id serial,
    nombre varchar(50),
    constraint pk_id_pais primary key (id)
);

create table provincia(
    id serial,
    nombre varchar(50),
    pais int,
    constraint pk_id_provincia primary key (id),
    constraint fk_pais_provincia foreign key (pais) references pais(id)
);

create table localidad(
    id serial,
    nombre varchar(50),
    codPostal int,
    provincia int,
    constraint pk_id_localidad primary key (id),
    constraint fk_provincia_localidad foreign key (provincia) references provincia(id)
);

create table barrio(
    id serial,
    nombre varchar(50),
    localidad int,
    constraint pk_id_barrio primary key (id),
    constraint fk_localidad_barrio foreign key (localidad) references localidad(id)
);

create table direccion (
    id serial,
    calle varchar (50),
    numAltura int,
    barrio int,
    constraint pk_id_direccion primary key (id),
    constraint fk_barrio_direccion foreign key (barrio) references barrio(id)
);

create table proveedor (
    id serial,
    razonSocial varchar(50),
    cuit NUMERIC(11),
    numTel numeric(10),
    mail varchar(50),
    direccion int,
    constraint pk_id_proveedor primary key (id),
    constraint fk_direccion_proveedor foreign key (direccion) references direccion(id)

);

create table bicicleta(
    id serial,
    marca int,
    fechaCompra date,
    fechaUltimoService date,
    fechaProximoService date,
    proveedor int,
    constraint pk_id_bicicleta primary key (id),
    constraint fk_marca_bicicleta foreign key (marca) references marca(id),
    constraint fk_proveedor_bicicleta foreign key (proveedor) references proveedor(id),
    constraint control_fechaProximoService check (fechaProximoService >= (fechaUltimoService + INTERVAL '1 year'))

);

create table tipoDoc(
    id serial,
    nombre varchar(50),
    constraint pk_id_tipoDoc primary key (id)
);

create table profesor(
    id serial,
    nombre varchar(50),
    apellido varchar(50),
    tipoDoc int,
    numDoc numeric(8),
    fechaNacimiento date,
    fechaIngreso date,
    descripcion varchar(50),
    direccion int,
    constraint pk_id_profesor primary key (id),
    constraint fk_tipoDoc_profesor foreign key (tipoDoc) references tipoDoc(id),
    constraint fk_direccion_profesor foreign key (direccion) references direccion(id)
);

create table horario(
    id serial,
    horaInicio time,
    horaFin time,
    constraint pk_id_horario primary key (id)
);

create table diaSemana(
    id serial,
    nombre varchar(50),
    constraint pk_id_diaSemana primary key (id)
);

create table turno(
    id serial,
    horario int,
    diaSemana int,
    capacidadMax int,
    profesor int,
    constraint pk_id_turno primary key (id),
    constraint fk_horario_turno foreign key (horario) references horario(id),
    constraint fk_diaSemana_turno foreign key (diaSemana) references diaSemana(id),
    constraint fk_profesor_turno foreign key (profesor) references profesor(id)
);

create table turno_bicicleta(
    id serial,
    idTurno int,
    idBicicleta int,
    constraint pk_id_turnno_bicicleta primary key (id),
    constraint fk_turno_turno_bicicleta foreign key (idTurno) references turno(id),
    constraint fk_bicicleta_turno_bicicleta foreign key (idBicicleta) references bicicleta(id)
);

create table plan(
    id serial,
    cantidadDias int,
    precio float,
    constraint pk_id_plan primary key (id),
    constraint control_precio_positivo check (precio > 0)
);

create table alumno(
    id serial,
    nombre varchar(50),
    apellido varchar(50),
    tipoDoc int,
    numDoc NUMERIC(8),
    fechaNacimiento date,
    fechaIngreso date,
    numTel NUMERIC(10),
    plan int,
    direccion int,
    constraint pk_id_alumno primary key (id),
    constraint fk_tipoDoc_alumno foreign key (tipoDoc) references tipoDoc(id),
    constraint fk_paln_alumno foreign key (plan) references plan(id),
    constraint fk_direccion_alumno foreign key (direccion) references direccion(id)
);

create table detalleTurno(
    id serial,
    idAlumno int,
    idTurno int,
    constraint pk_id_detalleTurno primary key (id),
    constraint fk_idAlumno_detalleTurno foreign key (idAlumno) references alumno(id),
    constraint fk_idTurno_detalleTurno foreign key (idTurno) references turno(id)
);