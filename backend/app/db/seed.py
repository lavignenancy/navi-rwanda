from app.db.session import SessionLocal
from app.models.service import Service


def seed_services() -> None:
    db = SessionLocal()

    try:
        existing_services = db.query(Service).count()

        if existing_services > 0:
            print("Services already exist.")
            return

        services = [
            Service(
                id="business-registration",
                name="Business Registration",
            ),
            Service(
                id="birth-certificate",
                name="Birth Certificate",
            ),
            Service(
                id="national-id",
                name="National ID Services",
            ),
        ]

        db.add_all(services)
        db.commit()

        print("Services seeded successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_services()