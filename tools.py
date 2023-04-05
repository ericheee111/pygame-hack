import pygame

def transform_image_constant(img, width = None, height = None):
    if width is not None and height is not None:
        return pygame.transform.scale(img, (width, height))
    elif width is not None:
        ratio = img.get_width() / width
        return pygame.transform.scale(img, (width, img.get_height() / ratio))
    elif height is not None:
        ratio = img.get_height() / height
        return pygame.transform.scale(img, (img.get_width() / ratio, height))
    else:
        raise Exception("Transform Image Constant ERROR")

def obj_is_mask(obj1, obj2):
    offset = (obj1.rect.x - obj2.rect.x, obj1.rect.y - obj2.rect.y)
    return obj2.mask.overlap(obj1.mask, offset)