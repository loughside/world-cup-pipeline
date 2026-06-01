
CREATE TABLE bronze.standings (
  id INT IDENTITY(1,1),
  json_response NVARCHAR(MAX) NOT NULL,
  ingested_at DATETIME2 DEFAULT GETUTCDATE(),
  api_endpoint NVARCHAR(50) NOT NULL
  CONSTRAINT pk_standings PRIMARY KEY (id)
)