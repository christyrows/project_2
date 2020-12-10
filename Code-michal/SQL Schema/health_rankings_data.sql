-- Table: public.health_rankings

-- DROP TABLE public.health_rankings;

CREATE TABLE public.health_rankings
(
    state character varying(25) COLLATE pg_catalog."default" NOT NULL,
    rank integer,
    value numeric,
    lat double precision,
    "long" double precision,
    pov_rank integer,
    vio_rank integer,
    food_rank integer,
    college_rank integer,
    CONSTRAINT health_rankings_pkey PRIMARY KEY (state)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.health_rankings
    OWNER to postgres;