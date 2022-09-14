# Importing LeagueReader for typing intellisense
from resources import LeagueReader
import math
import os
from scripts.helpers import Draw


# Setup function | only runs once on script load
def setup() -> dict:
    scriptSettings: dict = {
        "Minions": {
            "displayName": "Lasthitable Minions",
            "isEnabled": True
        },
    }

    return scriptSettings


# OnTick function | Runs every tick
def on_tick(lReader: LeagueReader, pymeow, scriptSettings) -> None:
    font = pymeow.font_init(20, "ComicSans")

    team = lReader.localPlayer.teamId
    ad = lReader.localPlayer.ad

    minions: list = [minion for minion in lReader.minions if minion.teamId != team]
    if scriptSettings['Minions']['isEnabled']:
        find_minions(lReader, pymeow, minions, ad)


def find_minions(lReader: LeagueReader, pymeow, minionlist, ad):
    for minion in minionlist:
        if minion.onScreen and minion.health < ad and "Minion" in minion.name:
            pos = minion.screenPos
            x,y = pos["x"], pos["y"]
            Draw.circle(
                pymeow=pymeow,
                x=x,
                y=y+20,
                radius=15,
                color="green",
                filled=True
            )




