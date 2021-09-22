from pydantic import BaseModel, Field


class Config:
    orm_mode = True


class JobList(BaseModel):
    id: str
    job_id: str
    jobs: str
    candidate_id: str
    candidate_username: str
    job_application: str
    create_at: str


class JobEntry(BaseModel):
    jobs: str = Field(..., example="python developer")
    candidate_username: str = Field(..., example="princika")
    job_application: str = Field(..., example="python")


class JobUpdate(BaseModel):
    job_id: str = Field(..., example="Enter your candidate id to update")
    jobs: str = Field(..., example="python developer")
    candidate_username: str = Field(..., example="princika")
    job_application: str = Field(..., example="python")


class JobDelete(BaseModel):
    candidate_id: str = Field(..., example="enter your candidate id")
    job_id: str = Field(..., example="enter your job id")
