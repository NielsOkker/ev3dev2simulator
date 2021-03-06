import arcade

from ev3dev2simulator.obstacle.BorderObstacle import BorderObstacle
from ev3dev2simulator.util.Util import to_color_code


class Border(BorderObstacle):
    """
    The outer line surrounding the playing field.
    """

    def __init__(self, board_width, board_height, color: arcade.Color, depth, edge_spacing):
        super(Border, self).__init__(board_width, board_height, to_color_code(color), depth, edge_spacing)

        # visualisation
        self.color = color
        self.shapes = None

    def get_shapes(self):
        return self.shapes

    @classmethod
    def from_config(cls, board_width, board_height, config):

        color = eval(config['color'])
        depth = int(config['depth'])
        spacing = int(config['outer_spacing'])

        return cls(board_width, board_height, color, depth, spacing)

    def create_shape(self, scale) -> [arcade.Shape]:

        self._calc_points(scale)
        """
        Create a list of shapes representing the four lines that make up this border.
        :return: a list of Arcade shapes.
        """
        colors = [self.color for _ in range(4)]
        self.shapes = []
        for side in [self.top_points, self.right_points, self.bottom_points, self.left_points]:
            self.shapes.append(arcade.create_rectangles_filled_with_colors(side, colors))
        return self.shapes
