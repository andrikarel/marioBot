__author__ = 'justinarmstrong'

from . import setup,tools
from .states import main_menu,load_screen,level1
from . import constants as c
from . import game_connector 
from .components import ReflexAgent

def main():
    """Add states to control here."""
    state_dict = {c.MAIN_MENU: main_menu.Menu(),
                  c.LOAD_SCREEN: load_screen.LoadScreen(),
                  c.TIME_OUT: load_screen.TimeOut(),
                  c.GAME_OVER: load_screen.GameOver(),
                  c.LEVEL1: level1.No_enemies_level()}
    
    gc = game_connector.GameConnector(state_dict[c.LEVEL1])

    run_it = tools.Control(setup.ORIGINAL_CAPTION,gc)
    run_it.setup_states(state_dict, c.MAIN_MENU)
   
    run_it.main()






