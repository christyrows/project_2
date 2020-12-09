-- Table: public.poverty

-- DROP TABLE public.poverty;

CREATE TABLE public.poverty
(
    state character varying(25) COLLATE pg_catalog."default" NOT NULL,
    pov_rate double precision,
    CONSTRAINT poverty_pkey PRIMARY KEY (state)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.poverty
    OWNER to postgres;