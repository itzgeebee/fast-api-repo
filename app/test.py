from . import schemas, models
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from .database import get_db

router = APIRouter()


# Get all tests
@router.get('/')
def get_tests(db: Session = Depends(get_db)):
    tests = db.query(models.Test).all()

    return {
        "status": "success",
        "tests": tests
    }


@router.post('/')
def create_test(payload: schemas.TestBaseSchema, db: Session = Depends(get_db)):
    new_test = models.Test(**payload.dict())
    db.add(new_test)
    db.commit()
    db.refresh(new_test)
    return {"status": "success", "test": new_test}


@router.get('/{testId}')
def get_test(testId: str, db: Session = Depends(get_db)):
    test = db.query(models.Test).filter(models.Test.id == testId).first()
    if not test:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No test with this id: {id} found")

    return {"status": "success", "test": test}