from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def printstat(station: dict) -> None:
    print("Valid station created:")
    print(f"ID: {staion.station_id}")
    print(f"Name: {staion.name}")
    print(f"Crew: {staion.crew_size} people")
    print(f"Power: {staion.power_level}%")
    print(f"Oxygen: {staion.oxygen_level}%")
    if staion.is_operational:
        print("Status: Operational")
    else:
        print("Status: Non-Operational")


if __name__ == "__main__":
    try:
        print("Space Station Data Validation")
        print("========================================")
        print("Valid station created:")
        staion = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=12/12/2006,
            is_operational=True,
        )
        printstat(staion)
        print("========================================")
        print("Expected validation error:")
        staion = SpaceStation(
            station_id="I",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=12/12/2012,
            is_operational=True,
        )
        printstat(staion)
        print("\n========================================")
        print("Expected validation error:")
    except Exception as e:
        print(e.errors()[0]["msg"])
