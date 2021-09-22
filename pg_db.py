import databases, sqlalchemy

## Postgres Database
from sqlalchemy import ForeignKey

DATABASE_URL = "postgresql://postgres:password@127.0.0.1:5432/postgres"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

jobs = sqlalchemy.Table(
    "jobs_portal",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String(255), primary_key=True),
    sqlalchemy.Column("job_id", sqlalchemy.String(255), unique=True),
    sqlalchemy.Column("jobs", sqlalchemy.String(255)),
    sqlalchemy.Column("candidate_id", sqlalchemy.String(255), unique=True),
    sqlalchemy.Column("candidate_username", sqlalchemy.String(255)),
    sqlalchemy.Column("job_application", sqlalchemy.String(255)),
    sqlalchemy.Column("create_at", sqlalchemy.String(255)),
)

application = sqlalchemy.Table(
    "applied_job",
    metadata,
    sqlalchemy.Column("candidate_id", sqlalchemy.String(255), ForeignKey('jobs_portal.candidate_id')),
    sqlalchemy.Column("candidate_first_name", sqlalchemy.String(255)),
    sqlalchemy.Column("candidate_last_name", sqlalchemy.String(255)),
    sqlalchemy.Column("gender", sqlalchemy.String(255)),
    sqlalchemy.Column("interested_position", sqlalchemy.String(255)),
    sqlalchemy.Column("mobile_number", sqlalchemy.String(255)),
    sqlalchemy.Column("skill_set", sqlalchemy.String(255)),
    sqlalchemy.Column("email_id", sqlalchemy.String(255)),
    sqlalchemy.Column("experience", sqlalchemy.String(255)),
    sqlalchemy.Column("apply_position", sqlalchemy.String(255)),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL
)
metadata.create_all(engine)
