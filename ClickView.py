# Importing LeagueReader for typing intellisense
import sys

from resources import LeagueReader
import math
import os
from scripts.helpers import Draw


# Setup function | only runs once on script load
def setup() -> dict:
    global lastclick
    scriptSettings: dict = {
        "DisplayEnemyClicks": {
            "displayName": "DisplayEnemyClicks",
            "isEnabled": True
        },
        "DisplaySelfClicks": {
            "displayName": "DisplaySelfClicks",
            "isEnabled": True
        },
    }

    return scriptSettings


# OnTick function | Runs every tick
def on_tick(lReader: LeagueReader, pymeow, scriptSettings) -> None:

    if scriptSettings["DisplayEnemyClicks"]["isEnabled"]:
        for champ in lReader.get_players():
            if champ.teamId != lReader.localPlayer.teamId:
                draw_champion(champ, pymeow)
    if scriptSettings["DisplaySelfClicks"]["isEnabled"]:
        draw_champion(lReader.localPlayer, pymeow)


def draw_champion(champion, pymeow):
    startpos = champion.AiManager.startPathScreen
    endpos = champion.AiManager.endPathScreen
    ms = champion.moveSpeed
    if champion.AiManager.isDashing or ms>500:
        color = [1, 0, 0]
    elif 200 < ms <= 500:
        c1 = (ms-200)/300
        color = [c1, 1-c1, 0]
    else:
        color = [0,1,0]

    pymeow.line(startpos["x"], startpos["y"], endpos["x"], endpos["y"], 3, color)
