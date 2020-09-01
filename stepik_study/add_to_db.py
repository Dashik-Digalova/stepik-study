from stepik_study.data import *
from stepik_study.views import *
from stepik_study.models import *
import json

db = SQLAlchemy()


def addtodb():
    with app.app_context():

        for t in teachers:
            goals = json.dumps(t["goals"])
            free = json.dumps(t["free"])
            db.session.add(Teacher(
                name=t["name"],
                about=t["about"],
                rating=t["rating"],
                picture=t["picture"],
                price=t["price"],
                goals=goals,
                free=free
                        ))
    db.session.commit()


if __name__ == "__main__":
    addtodb()