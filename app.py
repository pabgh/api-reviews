from fastapi import FastAPI
from models.review import Review
from controller.reviews import ler_reviews, add_new_review

app = FastAPI()

@app.get("/")
def root():
    """Funcao root do projeto de API"""
    return {"Fast":"API" }

@app.get("/{name}")
def say_hello(name: str):
    if not name:
        pass
    return {"Hello": name}

@app.get("/api/reviews/{reviews_id}")
def get_reviews(reviews_id: int = None):
    reviews = ler_reviews(reviews_id)
    return reviews[0]

@app.get("/api/reviews")
def get_reviews():
    return ler_reviews()

@app.post("/api/reviews")
def add_review(review: Review):
    reviews = ler_reviews()
    reviews.append(review.model_dump())
    add_new_review(reviews)
    return review

