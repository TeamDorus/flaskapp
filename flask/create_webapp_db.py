import pprint
from app import db
from app.config.models import TraccarEvent

db.create_all()

db.session.add(TraccarEvent(type='deviceOnline', status='Uit'))
db.session.add(TraccarEvent(type='deviceOffline', status='Uit'))
db.session.add(TraccarEvent(type='deviceUnknown', status='Uit'))
db.session.add(TraccarEvent(type='deviceMoving', status='Uit'))
db.session.add(TraccarEvent(type='deviceStopped', status='Uit'))
db.session.add(TraccarEvent(type='geofenceEnter', status='Uit'))
db.session.add(TraccarEvent(type='geofenceExit', status='Uit'))
db.session.commit()

print("\nFresh database content:")
print("-----------------------")
pprint.pprint(TraccarEvent.query.all())
print("\n")

