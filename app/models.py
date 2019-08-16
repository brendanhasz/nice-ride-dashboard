from app import db



class Station(db.Model):
    """A Nice Ride station

    Attributes
    ----------
    station_id : Integer
        Unique station identifier
    name : String
        Name of the station
    docks : Integer
        Number of docks at the station (max number of bikes)
    latitude : Float
        Latitude of the station's location
    longitude : Float
        Longitude of the station's location
    """

    station_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True, unique=False)
    docks = db.Column(db.Integer, index=True, unique=False)
    latitude = db.Column(db.Float(), index=True, unique=False)
    longitude = db.Column(db.Float(), index=True, unique=False)

    def __repr__(self):
        return '<Station %r>' % self.name



class AvailabilityHistory(db.Model):
    """A historical bike availability observation

    Attributes
    ----------
    station_id : Integer
        Station identifier
    datetime : DateTime
        Date and time of this observation
    num_bikes : Integer
        Number of bikes at the station
    """

    station_id = db.Column(db.Integer, index=True, unique=False)
    datetime = db.Column(db.DateTime, index=True, unique=False)
    num_bikes = db.Column(db.Integer, index=True, unique=False)

    def __repr__(self):
        return ('<AvailabilityHistory for %r at %r>' %
                (self.station_id, self.datetime))



class AvailabilityPrediction(db.Model):
    """A bike availability prediction

    Attributes
    ----------
    station_id : Integer
        Station identifier
    datetime : DateTime
        Date and time of this observation
    prediction_datetime : DateTime
        Date and time of this observation
    num_bikes : Integer
        Predicted number of bikes at the station
    prediction_type : String
        Type of prediction ('5prc', '50prc', '95prc', etc)
    """

    station_id = db.Column(db.Integer, index=True, unique=False)
    datetime = db.Column(db.DateTime, index=True, unique=False)
    prediction_datetime = db.Column(db.DateTime, index=True, unique=False)
    num_bikes = db.Column(db.Integer, index=True, unique=False)
    prediction_type = db.Column(db.String(16), index=True, unique=False)

    def __repr__(self):
        return ('<AvailabilityPrediction %r for %r at %r from %r>' %
                (self.prediction_type, self.station_id, 
                 self.datetime, self.prediction_datetime)
