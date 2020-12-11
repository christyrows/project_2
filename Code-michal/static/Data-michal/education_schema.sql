-- Table: public.education

-- DROP TABLE public.education;

CREATE TABLE public.education
(
    state character varying(25) COLLATE pg_catalog."default" NOT NULL,
    college_per double precision,
    college_rank integer,
    CONSTRAINT education_pkey PRIMARY KEY (state)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.education
    OWNER to postgres;