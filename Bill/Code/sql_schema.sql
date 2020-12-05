CREATE TABLE poverty_by_state (
	state_name VARCHAR(50),
	poverty_pct DEC,
	PRIMARY KEY (state_name)
)

CREATE TABLE education_by_state (
	state_name VARCHAR(50),
	education_pct DEC,
	PRIMARY KEY (state_name)
)

SELECT *
FROM poverty_by_state;

SELECT *
FROM education_by_state;