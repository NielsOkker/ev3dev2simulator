from ev3dev2simulator.config.config import get_simulation_settings
from ev3dev2simulator.robotpart.BodyPart import BodyPart


class Led(BodyPart):
    """
    Class representing a Wheel of the simulated robotpart.
    """
    def __init__(self, brick: int, robot, side, brick_x_offset, brick_y_offset):
        offset_x = - 20 if side == 'left' else 20
        config = {
            'brick': brick,
            'name': f'led_{side}',
            'x_offset': brick_x_offset,
            'y_offset': brick_y_offset,
        }

        dims = get_simulation_settings()['body_part_sizes']['led']
        super().__init__(config, robot, dims['width'], dims['height'], 'led', offset_x, - 32.5)
        self.old_texture_index = 1

    def setup_visuals(self, scale):
        img_cfg = get_simulation_settings()['image_paths']
        src_list = [img_cfg[f'led_{color}'] for color in ['amber', 'black', 'red', 'green', 'orange', 'yellow']]
        self.init_sprite_with_list(src_list, scale, 1)

    def set_color_texture(self, color):
        if self.old_texture_index != color:
            self.old_texture_index = color
            self.sprite.set_texture(color)
