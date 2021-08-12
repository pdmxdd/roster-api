from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from roster_utils import add_to_roster, get_roster

FILEPATH = './roster.csv'

app = FastAPI()

origins = ["localhost:8000", "localhost:4200", "127.0.0.1:*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/roster')
def http_get_roster():
    return get_roster(FILEPATH)

@app.post('/roster', status_code=201)
def http_post_new_student(first_name, last_name):
    added = add_to_roster(FILEPATH, first_name, last_name)
    return added