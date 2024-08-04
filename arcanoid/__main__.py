import unicurses as curses
from arcanoid.screen import main

curses.wrapper(main)