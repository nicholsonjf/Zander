CREATE TABLE applications(
    application_id BIGSERIAL UNIQUE NOT NULL,
    application_name VARCHAR UNIQUE NOT NULL,
    batch_name VARCHAR,
    CONSTRAINT pk_application_id PRIMARY KEY (application_id)
    );

CREATE TABLE hrdb_lookups(
    application_id INTEGER UNIQUE NOT NULL,
    hrdb_lookup_date TIMESTAMP WITHOUT TIME ZONE,
    CONSTRAINT fk_application_id FOREIGN KEY (application_id)
        REFERENCES applications (application_id)
    );
    
