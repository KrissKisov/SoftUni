
CREATE TABLE clients(
	id SERIAL PRIMARY KEY
	,name VARCHAR(10)
)
;

CREATE TABLE employees(
	id SERIAL PRIMARY KEY
	,first_name VARCHAR(30)
	,last_name VARCHAR(30)
	,project_id INT
)
;

CREATE TABLE projects(
	id SERIAL PRIMARY KEY 
	,client_id INT 
	,project_lead_id INT
)
;

ALTER TABLE
	employees
ADD CONSTRAINT
	fk_project_id_id
		FOREIGN KEY(project_id)
			REFERENCES projects(id)
;

ALTER TABLE
	projects
ADD CONSTRAINT
	fk_client_id_id
		FOREIGN KEY(client_id)
			REFERENCES clients(id)

,ADD CONSTRAINT
	fk_project_lead_id_id
		FOREIGN KEY(project_lead_id)
			REFERENCES employees(id)
;
