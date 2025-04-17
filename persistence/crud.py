import uuid
from db import PersistentGraphState
from db import SessionLocal

def save_graph_state(srs_hash: str, generated_code: dict):
    db = SessionLocal()
    state = PersistentGraphState(
        id=str(uuid.uuid4()),
        srs_hash=srs_hash,
        components=generated_code
    )
    db.add(state)
    db.commit()
    db.close()

def load_graph_state_by_hash(srs_hash: str):
    db = SessionLocal()
    result = db.query(PersistentGraphState).filter(PersistentGraphState.srs_hash == srs_hash).first()
    db.close()
    return result
