-- Table: public.state_health_rankings

-- DROP TABLE public.state_health_rankings;

CREATE TABLE public.state_health_rankings
(
    state text COLLATE pg_catalog."default" NOT NULL,
    "Rank" text COLLATE pg_catalog."default",
    "Value" text COLLATE pg_catalog."default"
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.state_health_rankings
    OWNER to postgres;

ALTER TABLE public.state_health_rankings
    ALTER COLUMN state SET STORAGE PLAIN;