from pymongo import MongoClient
from fastapi import FastAPI
import uvicorn


app = FastAPI()


def setup_db():
    client = MongoClient("localhost", 27017)
    database = client["fumble_api"]
    critical_collection = database["critical_collection"]
    return critical_collection


@app.get("/")
def read_root():
    critical_collection = setup_db()
    docs = [doc for doc in critical_collection.distinct("short")]
    return docs


@app.get("/{fumble}/{roll}")
def define_word(fumble, roll):
    critical_collection = setup_db()
    docs = critical_collection.find({"short": fumble})
    for doc in docs:
        new_roll = doc["roll"]
        if isinstance(new_roll, int):
            if int(roll) == new_roll:
                return {doc["type"], doc["label"], doc["desc"]}
        else:
            if int(roll) in new_roll:
                return {doc["type"], doc["label"], doc["desc"]}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
