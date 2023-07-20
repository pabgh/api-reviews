import json

def ler_reviews(reviews_id: int = None):
    with open('data/reviews.json', 'r') as file:
        reviews = json.load(file)
    if reviews_id is not None:
        filtered_reviews = [r for r in reviews if r["id"] == reviews_id]
        return filtered_reviews
    else:
        return reviews

def add_new_review(reviews):
    with open('data/reviews.json', 'w') as file:
        json.dump(reviews, file, indent=2)