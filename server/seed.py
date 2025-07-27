#!/usr/bin/env python3
from app       import app
from models    import db, Earthquake

with app.app_context():
    Earthquake.query.delete()
    sample = [
      (9.5, "Chile",    1960),
      (9.2, "Alaska",   1964),
      (8.6, "Alaska",   1946),
      (8.5, "Banda Sea",1934),
      (8.4, "Chile",    1922),
    ]
    for mag, loc, yr in sample:
        db.session.add(Earthquake(magnitude=mag, location=loc, year=yr))
    db.session.commit()
    print("Seeded 5 earthquakes.")