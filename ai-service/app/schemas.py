from enum import Enum

from pydantic import BaseModel, Field


class Category(str, Enum):
    BILLING = "BILLING"
    TECHNICAL = "TECHNICAL"
    ACCOUNT = "ACCOUNT"
    SHIPPING = "SHIPPING"
    GENERAL = "GENERAL"


class Priority(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    URGENT = "URGENT"


class Sentiment(str, Enum):
    POSITIVE = "POSITIVE"
    NEUTRAL = "NEUTRAL"
    NEGATIVE = "NEGATIVE"


class ClassifyRequest(BaseModel):
    subject: str = Field(min_length=1, max_length=200)
    body: str = Field(min_length=1, max_length=5000)


class ClassifyResponse(BaseModel):
    category: Category
    priority: Priority
    sentiment: Sentiment
    confidence: float = Field(ge=0, le=1)