import pygame as py
import sys

class Assets:
    img_path = sys.path[0] + "/imgs"

    street_information = {
        "Mediterranean Avenue": [60, 50, (2, 10, 30, 90, 160, 250), "\\Streets\\Mediterranean Avenue.PNG", "top", "brown"],
        "Baltic Avenue": [60, 50, (4, 20, 60, 180, 320, 450), "\\Streets\\Baltic Avenue.PNG", "top", "brown"]
    }

    railroad_information = {
        "Reading Railroad": [200, (25, 50, 100, 200), "\\Streets\\Reading Railroad.PNG"]
    }

    board_img = img_path + "/Test.jpg"
    house_img = img_path + "/House.png"
    hotel_img = img_path + "/Hotel.png"

    dices_imgs: list = []
    dices_imgs_small: list = []
    dices_paths = [img_path + "/Dices/dice1.jpg",
              img_path + "/Dices/dice2.jpg",
              img_path + "/Dices/dice3.jpg",
              img_path + "/Dices/dice4.jpg",
              img_path + "/Dices/dice5.jpg",
              img_path + "/Dices/dice6.jpg"]

    @staticmethod
    def load():
        for key, value in Assets.street_information.items():
            value[3] = py.image.load(Assets.img_path + value[3])

        for key, value in Assets.railroad_information.items():
            value[2] = py.image.load(Assets.img_path + value[2])

        for i in Assets.dices_paths:
            Assets.dices_imgs.append(py.image.load(i))

        for i in Assets.dices_paths:
            Assets.dices_imgs_small.append(py.transform.scale(py.image.load(i), (100, 100)))

        Assets.board_img = py.image.load(Assets.board_img)
        Assets.house_img = py.image.load(Assets.house_img)
        Assets.hotel_img = py.image.load(Assets.hotel_img)
