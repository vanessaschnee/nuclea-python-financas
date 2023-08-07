-- DROP TABLE IF EXISTS public.cliente;

CREATE TABLE IF NOT EXISTS public.cliente
(
    id integer NOT NULL DEFAULT nextval('cliente_id_seq'::regclass),
    nome character varying(100) COLLATE pg_catalog."default" NOT NULL,
    cpf character varying(14) COLLATE pg_catalog."default" NOT NULL,
    rg character varying(20) COLLATE pg_catalog."default" NOT NULL,
    data_nascimento date NOT NULL,
    cep character varying(10) COLLATE pg_catalog."default" NOT NULL,
    logradouro character varying(50) COLLATE pg_catalog."default" NOT NULL,
    bairro character varying(20) COLLATE pg_catalog."default" NOT NULL,
    cidade character varying(15) COLLATE pg_catalog."default" NOT NULL,
    estado character varying(2) COLLATE pg_catalog."default" NOT NULL,
    num_casa character varying(5) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT cliente_pkey PRIMARY KEY (id),
    CONSTRAINT cliente_cpf_key UNIQUE (cpf)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.cliente
    OWNER to postgres;