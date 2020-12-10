-- Table: public.combined_data

-- DROP TABLE public.combined_data;

CREATE TABLE public.combined_data
(
    state character varying(25) COLLATE pg_catalog."default" NOT NULL,
    healthrank integer,
    value double precision,
    lat double precision,
    lon double precision,
    povrate double precision,
    povrank integer,
    violentcrimerate double precision,
    violentcrimerank integer,
    popindesert numeric,
    fooddesertrank integer,
    collegerate double precision,
    collegerank integer,
    CONSTRAINT combined_data_pkey PRIMARY KEY (state)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.combined_data
    OWNER to postgres;