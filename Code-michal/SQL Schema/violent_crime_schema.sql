-- Table: public.violent_crime

-- DROP TABLE public.violent_crime;

CREATE TABLE public.violent_crime
(
    abbr character varying(4) COLLATE pg_catalog."default",
    state character varying(25) COLLATE pg_catalog."default" NOT NULL,
    pop integer,
    vio_crime integer,
    vio_rate double precision,
    vio_rank integer,
    CONSTRAINT violent_crime_pkey PRIMARY KEY (state)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.violent_crime
    OWNER to postgres;