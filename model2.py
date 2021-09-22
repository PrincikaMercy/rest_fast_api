from pydantic import BaseModel, Field


class Config:
    orm_mode = True


class ApplyJob(BaseModel):
    candidate_id: str
    candidate_first_name: str
    candidate_last_name: str
    gender: str
    interested_position: str
    mobile_number: str
    skill_set: str
    email_id: str
    experience: str
    apply_position: str


class JobApply(BaseModel):
    candidate_first_name: str = Field(..., example="enter your first name")
    candidate_last_name: str = Field(..., example="enter your last name")
    gender: str = Field(..., example="enter your gender")
    interested_position: str = Field(..., example="enter your interested position")
    mobile_number: str = Field(..., example="enter your mobile number")
    skill_set: str = Field(..., example="enter your skill set")
    email_id: str = Field(..., example="enter your email_id")
    experience: str = Field(..., example="enter your experience")
    apply_position: str = Field(..., example="which position to apply")


class JobUpdate(BaseModel):
    candidate_id: str = Field(..., example="enter your candidate id")
    candidate_first_name: str = Field(..., example="enter your first name")
    candidate_last_name: str = Field(..., example="enter your last name")
    gender: str = Field(..., example="enter your gender")
    interested_position: str = Field(..., example="enter your interested position")
    mobile_number: str = Field(..., example="enter your mobile number")
    skill_set: str = Field(..., example="enter your skill set")
    email_id: str = Field(..., example="enter your email_id")
    experience: str = Field(..., example="enter your experience")
    apply_position: str = Field(..., example="which position to apply")


class JobDelete(BaseModel):
    candidate_id: str = Field(..., example="enter your candidate id")
