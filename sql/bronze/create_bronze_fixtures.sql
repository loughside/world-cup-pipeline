
CREATE TABLE bronze.fixtures (
  fixture_id INT NOT NULL,
  json_response NVARCHAR(MAX) NOT NULL,
  ingested_at DATETIME2 DEFAULT GETUTCDATE(),
  api_endpoint NVARCHAR(50) NOT NULL
  CONSTRAINT pk_fixtures PRIMARY KEY (fixture_id)
)