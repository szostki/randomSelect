from __future__ import division
import random
from pyfiglet import Figlet
from asciimatics.effects import Cog, Print, Cycle
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
import sys


autoTeam = [
    'Pawel',
    'Dawid',
    'Monika',
    'Darek', 
    'Michal', 
    'Marcin', 
    ]

secure_random = random.SystemRandom()    

def demo(screen):
    # Typical terminals are 80x24 on UNIX and 80x25 on Windows
    f = Figlet(font='slant')
    
    
    effects = [
        Cog(screen, 20, 10, 10),
        Cog(screen, 60, 25, 15, direction=-1),
        Print(screen, FigletText(f.renderText(secure_random.choice(autoTeam)), font="term"), x=45, y=22, start_frame=60)
    ]

    effects.append( Print(screen, FigletText(f.renderText('Super team na dzis:'), font='term'), x=90, y=int(0)))
    currentMemberIndex = 1
    for member in autoTeam:
        effects.append( Print(screen, FigletText(f.renderText(member), font='term'), x=120, y=int(7 * currentMemberIndex)+2))
        currentMemberIndex += 1

    screen.play([Scene(effects, -1)], stop_on_resize=True)

while True:
    try:
        Screen.wrapper(demo)
        sys.exit(0)
    except ResizeScreenError:
        pass