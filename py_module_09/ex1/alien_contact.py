from pydantic import BaseModel, model_validator, Field
from datetime import datetime
from enum import Enum
from typing import Optional


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=300)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=None)

    @model_validator(mode='after')
    def validate(self):
        if self.contact_id[0:2] != "AC":
            raise ValueError("Contact ID must start with 'AC '(Alien Contact)")
        if (self.contact_type == ContactType.PHYSICAL
                and not self.is_verified):
            raise ValueError("Physical contact reports must be verified")
        if (self.contact_type == ContactType.TELEPATHIC
                and self.witness_count < 3):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError("Strong signals (> 7.0) "
                             "should include received messages")
        return self


if __name__ == "__main__":
    print("Alien Contact Log Validation")
    print("======================================")
    try:
        print("Valid contact report:")

        alien = AlienContact(contact_id="AC_2024_001",
                             timestamp=datetime.now(),
                             location="42 Lisbon, Lisbon, Portugal",
                             contact_type=ContactType.RADIO,
                             signal_strength=8.5,
                             duration_minutes=45,
                             witness_count=5,
                             message_received='Greetings from Zeta Reticuli'
                             )
        print(f"ID: {alien.contact_id}")
        print(f"TYPE: {alien.contact_type.value}")
        print(f"Location: {alien.location}")
        print(f"Signal: {alien.signal_strength} / 10")
        print(f"Duration: {alien.duration_minutes} minutes")
        print(f"Witness: {alien.witness_count}")
        print(f"Message: {alien.message_received}")

        print("\n======================================")
        print("Expected validation error:")

        alien = AlienContact(contact_id="AC_2024_001",
                             timestamp=datetime.now(),
                             location="42 Lisbon, Lisbon, Portugal",
                             contact_type=ContactType.TELEPATHIC,
                             signal_strength=8.5,
                             duration_minutes=45,
                             witness_count=1,
                             message_received=None,
                             is_verified=False
                             )

    except Exception as e:
        print(e.errors()[0]['msg'])
