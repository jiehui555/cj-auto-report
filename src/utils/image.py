from typing import List
from PIL import Image


def merge_images(img_paths: List[str], output_name: str, background: tuple = (255, 255, 255)) -> str:
    """
    Merge multiple images vertically (stack them on top of each other)

    Args:
        img_paths: List of image file paths to merge
        output_name: Name for the output file (without extension)
        background: Background color as RGB tuple, defaults to white

    Returns:
        Path to the merged image file
    """
    # Open all images
    images = [Image.open(img_path) for img_path in img_paths]

    # Get dimensions
    widths = [img.size[0] for img in images]
    heights = [img.size[1] for img in images]

    # Calculate final dimensions
    max_width = max(widths)
    total_height = sum(heights)

    # Create new blank image
    new_img = Image.new('RGB', (max_width, total_height), background)

    # Paste images one by one with centering
    y_offset = 0
    for img in images:
        x_offset = (max_width - img.width) // 2
        new_img.paste(img, (x_offset, y_offset))
        y_offset += img.height

    # Save
    save_path = f"{output_name}.png"
    new_img.save(save_path, quality=95)

    return save_path