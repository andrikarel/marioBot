__author__ = 'justinarmstrong'

from . import setup,tools
from .states import main_menu,load_screen,level2
from . import constants as c
from . import game_connector 
from .components import Agent

def main():
    """Add states to control here."""
    state_dict = {c.MAIN_MENU: main_menu.Menu(),
                  c.LOAD_SCREEN: load_screen.LoadScreen(),
                  c.TIME_OUT: load_screen.TimeOut(),
                  c.GAME_OVER: load_screen.GameOver(),
                  c.LEVEL1: level2.Level2()}
    
    gc = game_connector.GameConnector(state_dict[c.LEVEL1])

    run_it = tools.Control(setup.ORIGINAL_CAPTION,gc)
    run_it.setup_states(state_dict, c.MAIN_MENU)
   
    run_it.main()






