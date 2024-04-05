import dice
from fastapi import FastAPI
from typing import List

app = FastAPI(title="Roll API", version="1.0.0")

@app.get("/dice", response_model=List[int], tags=["Roll"])
async def roll_dice(amount: int, sides: int) -> List[int]:
    """Roll dice."""
    rolls = roll(amount, sides)
    return rolls

def roll(amount: int, sides: int) -> List[int]:
    return dice.roll(f'{amount}d{sides}')
