from fastapi import FastAPI

from models.models import FeedBack
# from models.users import User, SecondUser

app = FastAPI()

fake_users = {
    1: {'username': 'jon doe', 'email': 'jon@mail.com'},
    2: {'username': 'john deo', 'email': 'deo@mail.com'}
}


@app.get('/users/{user_id}')
def read_user(user_id: int):
    if user_id in fake_users:
        return fake_users[user_id]
    return {'error': 'User not found'}

@app.post('/feedback')
def feedback(feedback: FeedBack):
    feedback_list = []
    feedback_list.append(feedback)
    return {'message': f'Спасибо за отзыв, {feedback.name}'}
