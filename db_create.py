from application import db
from application.models import Station
from application.models import AvailabilityHistory
from application.models import AvailabilityPrediction

db.create_all()

print("Databases created.")
