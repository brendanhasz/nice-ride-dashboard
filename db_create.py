from app import db
from app.models import Station
from app.models import AvailabilityHistory
from app.models import AvailabilityPrediction

db.create_all()

print("Databases created.")
