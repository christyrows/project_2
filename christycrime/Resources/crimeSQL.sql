CREATE TABLE crimeStats (
  year VARCHAR(5),
  stateAb VARCHAR(50),
  state VARCHAR(50),
  population VARCHAR(50),
  violentCrime VARCHAR(50),
  homicide VARCHAR(50),
  rapeLegacy VARCHAR(50),
  rapeRevised VARCHAR(50),
  robbery VARCHAR(50),
  aggAssault VARCHAR(50),
  propertyCrime VARCHAR(50),
  burglary VARCHAR(50),
  larceny VARCHAR(50),
  mvTheft VARCHAR(50),
  caveats VARCHAR
)

select * 
from crimestats;
ALTER TABLE crimestats DROP raperevised;