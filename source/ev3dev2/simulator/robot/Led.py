import arcade

from ev3dev2.simulator.robot import Robot
from ev3dev2.simulator.robot.BodyPart import BodyPart
from ev3dev2.simulator.util.Util import apply_scaling


class Led(BodyPart):
    """
    Class representing a Wheel of the simulated robot.
    """


    def __init__(self,
                 img_cfg,
                 robot: Robot,
                 delta_x: int,
                 delta_y: int):
        super(Led, self).__init__(None, robot, delta_x, delta_y)

        amber_texture = arcade.load_texture(img_cfg['led_amber'], scale=apply_scaling(0.33))
        black_texture = arcade.load_texture(img_cfg['led_black'], scale=apply_scaling(0.33))
        green_texture = arcade.load_texture(img_cfg['led_green'], scale=apply_scaling(0.33))
        red_texture = arcade.load_texture(img_cfg['led_red'], scale=apply_scaling(0.33))
        orange_texture = arcade.load_texture(img_cfg['led_orange'], scale=apply_scaling(0.33))
        yellow_texture = arcade.load_texture(img_cfg['led_yellow'], scale=apply_scaling(0.33))

        self.textures.append(amber_texture)
        self.textures.append(black_texture)
        self.textures.append(green_texture)
        self.textures.append(red_texture)
        self.textures.append(orange_texture)
        self.textures.append(yellow_texture)

        self.old_texture_index = 2
        self.set_texture(2)


    def set_color(self, color_index):
        if self.old_texture_index != color_index:
            self.old_texture_index = color_index
            self.set_texture(color_index)
