-- setup server
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- create user
CREATE USER integration_test_user WITH ENCRYPTED PASSWORD 'integration_test_password';

-- setup user
GRANT CONNECT ON DATABASE postgres TO integration_test_user;
GRANT CREATE ON DATABASE postgres TO integration_test_user;

