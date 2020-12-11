-- Table: public.food_deserts

-- DROP TABLE public.food_deserts;

CREATE TABLE public.food_deserts
(
    state character varying(25) COLLATE pg_catalog."default" NOT NULL,
    abbr character varying(2) COLLATE pg_catalog."default",
    deserts integer,
    pop integer,
    pop_in_deserts integer,
    desert_rate double precision,
    desert_rank integer,
    pov_rate double precision,
    pov_rank integer,
    CONSTRAINT food_deserts_pkey PRIMARY KEY (state)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.food_deserts
    OWNER to postgres;