import datetime, uuid
import random
import string
from starlette.responses import RedirectResponse
import model2 as mdapply
import model as mdcand
from pg_db import database, jobs, application
from fastapi import FastAPI
from typing import List

app = FastAPI(
    docs_url="/api/v2/docs",
    redoc_url="/api/v2/redocs",
    title="Job Portal",
    description="This portal for job seekers",
    version="2.0",
    openapi_url="/api/v2/openapi.json",

)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
async def homepage():
    url = "http://127.0.0.1:8000/api/v2/docs"
    return RedirectResponse(url=url)


@app.get("/jobs", response_model=List[mdcand.JobList], tags=["Jobs"])
async def find_all_canditate():
    query = jobs.select()
    return await database.fetch_all(query)


@app.post("/jobs", response_model=mdcand.JobList, tags=["Jobs"])
async def register_canditate(job: mdcand.JobEntry):
    ID = str(uuid.uuid1())
    JobID = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(4, 9)))
    CandID = str(random.randint(100, 1000))
    JDate = str(datetime.datetime.now())
    query = jobs.insert().values(
        id=ID,
        job_id=JobID,
        jobs=job.jobs,
        candidate_id=CandID,
        candidate_username=job.candidate_username,
        job_application=job.job_application,
        create_at=JDate
    )

    await database.execute(query)
    return {
        "id": ID,
        **job.dict(),
        "create_at": JDate,
        "job_id": JobID,
        "candidate_id": CandID
    }


@app.get("/jobs/{job_id}", response_model=mdcand.JobList, tags=["Jobs"])
async def find_job_by_id(job_id: str):
    query = jobs.select().where(jobs.c.job_id == job_id)
    return await database.fetch_one(query)


@app.put("/jobs", response_model=mdcand.JobList, tags=["Jobs"])
async def update_candidate(job: mdcand.JobUpdate):
    gDate = str(datetime.datetime.now())
    query = jobs.update(). \
        where(jobs.c.job_id == job.job_id). \
        values(
        jobs=job.jobs,
        candidate_username=job.candidate_username,
        job_application=job.job_application,
        create_at=gDate,
    )
    await database.execute(query)

    return await find_job_by_id(job.job_id)


@app.delete("/jobs/{job_id}", tags=["Jobs"])
async def delete_user(job: mdcand.JobDelete, candidate_id: str, job_id: str):
    if candidate_id:
        query = jobs.delete().where(jobs.c.candidate_id == job.candidate_id)
        await database.execute(query)
    elif job_id:
        query = jobs.delete().where(jobs.c.job_id == job.job_id)
        await database.execute(query)

    return {
        "status": True,
        "message": "This candidate has been deleted successfully."
    }


@app.post("/apply_jobs", response_model=mdapply.ApplyJob, tags=["ApplyJobs"])
async def apply_job(job: mdapply.JobApply, candidate_id: str):
    job_candidate_query = jobs.select().where(jobs.c.candidate_id == candidate_id)
    c_query = database.fetch_one(job_candidate_query)
    if c_query:
        query = application.insert().values(
            candidate_id=candidate_id,
            candidate_first_name=job.candidate_first_name,
            candidate_last_name=job.candidate_last_name,
            gender=job.gender,
            interested_position=job.interested_position,
            mobile_number=job.mobile_number,
            skill_set=job.skill_set,
            email_id=job.email_id,
            experience=job.experience,
            apply_position=job.apply_position,
        )

        await database.execute(query)

        apply_candidate_query = application.select().where(application.c.candidate_id == candidate_id)
        return await database.fetch_one(apply_candidate_query)


@app.get("/apply_jobs/{candidate_id}", response_model=mdapply.ApplyJob, tags=["ApplyJobs"])
async def find_canditate_by_id(candidate_id: str):
    apply_candidate_query = application.select().where(application.c.candidate_id == candidate_id)
    return await database.fetch_one(apply_candidate_query)


@app.put("/apply_jobs/{candidate_id}", response_model=mdapply.ApplyJob, tags=["ApplyJobs"])
async def update_candidate(job: mdapply.JobUpdate):
    query = application.update(). \
        where(application.c.candidate_id == job.candidate_id). \
        values(
        candidate_first_name=job.candidate_first_name,
        candidate_last_name=job.candidate_last_name,
        gender=job.gender,
        interested_position=job.interested_position,
        mobile_number=job.mobile_number,
        skill_set=job.skill_set,
        email_id=job.email_id,
        experience=job.experience,
        apply_position=job.apply_position,
    )
    await database.execute(query)

    apply_candidate_query = application.select().where(application.c.candidate_id == job.candidate_id)
    return await database.fetch_one(apply_candidate_query)


@app.delete("/apply_jobs/{candidate_id}", tags=["ApplyJobs"])
async def delete_user(job: mdapply.JobDelete):
    query = application.delete().where(application.c.candidate_id == job.candidate_id)
    await database.execute(query)

    return {
        "status": True,
        "message": "This applied job has been deleted successfully."
    }
