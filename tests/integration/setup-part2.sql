-- grant all access to test user within app schema
GRANT ALL PRIVILEGES ON ALL tables IN SCHEMA dpo TO integration_test_user;
GRANT ALL PRIVILEGES ON ALL sequences IN SCHEMA dpo TO integration_test_user;