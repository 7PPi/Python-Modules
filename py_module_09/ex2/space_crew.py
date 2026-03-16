"""Module documentation."""
from typing import Any
from pydantic import BaseModel, model_validator, Field
from enum import Enum
from datetime import datetime
from typing import List


class Rank(Enum):
    """Rank class."""
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """CrewMember class."""
    member_id: str = Field(min_length=1, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    """SpaceMission class."""
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=2, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=1000000.0)

    @model_validator(mode='after')
    def validate(self) -> Any:
        """validate function."""
        if self.mission_id[0] != 'M':
            raise ValueError(" Mission ID must start with 'M'")
        leader = False
        experienced = 0
        active = True
        for member in self.crew:
            if member.rank == Rank.CAPTAIN or member.rank == Rank.COMMANDER:
                leader = True
            if member.years_experience > 5:
                experienced += 1
            if not member.is_active:
                active = False
        long_m = True if experienced >= len(self.crew) / 2 else False
        if not leader:
            raise ValueError("Must have at least one Commander or Captain")
        if self.duration_days > 365 and not long_m:
            raise ValueError("Long missions (> 365 days) need "
                             "50% experienced crew (5+ years)")
        if not active:
            raise ValueError("All crew members must be active")
        return self


def main() -> None:
    """main function."""
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")

    members = [
        CrewMember(member_id="42Connor", name="Sarah Connor",
                   rank=Rank.COMMANDER, age=45,
                   specialization='Mission Command', years_experience=14),
        CrewMember(member_id="42Smith", name="John Smith",
                   rank=Rank.LIEUTENANT, age=35,
                   specialization='Navigation', years_experience=10),
        CrewMember(member_id="42Johnson", name="Alice Johnson",
                   rank=Rank.OFFICER, age=25,
                   specialization=' Engineering', years_experience=14),
    ]

    mission = SpaceMission(mission_id="M2024_MARS",
                           mission_name="Mars Colony Establishment",
                           destination="Mars", launch_date=datetime.today(),
                           duration_days=900, crew=members,
                           budget_millions=2500.0)

    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: {mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(f"- {member.name} ({member.rank.value})"
              f" - {member.specialization}")

    print("\n=========================================")
    print("Expected validation error:")
    members = [
        CrewMember(member_id="42Connor", name="Sarah Connor",
                   rank=Rank.LIEUTENANT, age=45,
                   specialization='Mission Command', years_experience=14),
        CrewMember(member_id="42Smith", name="John Smith",
                   rank=Rank.LIEUTENANT, age=35,
                   specialization='Navigation', years_experience=10),
        CrewMember(member_id="42Johnson", name="Alice Johnson",
                   rank=Rank.OFFICER, age=25,
                   specialization=' Engineering', years_experience=14),
    ]

    mission = SpaceMission(mission_id="M2024_MARS",
                           mission_name="Mars Colony Establishment",
                           destination="Mars", launch_date=datetime.today(),
                           duration_days=900, crew=members,
                           budget_millions=2500.0)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e.errors()[0]["msg"])
