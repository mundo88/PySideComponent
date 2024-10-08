import io
import os
import contextlib
from PIL import Image
with contextlib.redirect_stdout(None):  # Suppress import message
    import pygame
from xml.etree import ElementTree
from PySideComponent.tailwind_colors import TAILWIND_COLORS

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__)) 


def convert(
    icon_path:str,
    icon_type:str ,
    size: int = 24,
    color :str = TAILWIND_COLORS.ZINC_900,
    stroke_width: float = 2.0
) -> Image:
    """Load a specified Tabler icon into a Pillow Image
    with the option to provide a custom size, color, and stroke width

    :param icon: specified Tabler icon from the OutlineIcon or FilledIcon enum
    :param size: optional size of the icon
    :param color: optional color of the icon
    :param stroke_width: optional stroke-width of the icon
    :return: specified Tabler icon as Pillow Image
    """
    # Open and read svg file for specified icon
    if icon_type == "outline":
        color_attribute = 'stroke'
        svg_path = CURRENT_PATH + '/svg/outline/' + icon_path
    else:
        color_attribute = 'fill'
        svg_path = CURRENT_PATH + '/svg/filled/' + icon_path
        
    svg_string = open(svg_path, 'rt').read()

    # Parse xml data from svg string
    ElementTree.register_namespace('', 'http://www.w3.org/2000/svg')
    root = ElementTree.fromstring(svg_string)

    # Set attributes (width, height, transform, stroke / fill, and stroke-width)
    svg_default_size = int(root.get('width'))
    root.set('width', str(size))
    root.set('height', str(size))
    root.set('transform', 'scale(' + str(size / svg_default_size) + ')')
    root.set(color_attribute, color)
    if root.get('stroke-width') is not None:
        root.set('stroke-width', str(stroke_width))

    # Convert adjusted svg string to svg image and then bytes
    adjusted_svg_string = ElementTree.tostring(root, encoding='unicode')
    svg_image = pygame.image.load(io.BytesIO(adjusted_svg_string.encode()))
    image_bytes = pygame.image.tobytes(svg_image, 'RGBA')

    # Return Image created from bytes
    return Image.frombytes('RGBA', (size, size), image_bytes)
