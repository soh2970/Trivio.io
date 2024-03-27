from src.Player import Player
from src.UIs.LoadGameScreen import LoadGameScreen
import pygame


player = Player("t",100, 0, 1)
test = LoadGameScreen(player)
test.run()