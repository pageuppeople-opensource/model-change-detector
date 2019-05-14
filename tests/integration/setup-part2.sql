-- create user
CREATE USER integration_test_user WITH ENCRYPTED PASSWORD 'integration_test_password';

-- setup user
GRANT CONNECT ON DATABASE integration_test_db TO integration_test_user;
GRANT CREATE ON DATABASE integration_test_db TO integration_test_user;
