import os
import shutil
import argparse
import logging


logging.basicConfig(format="[%(levelname)s] %(message)s", level=logging.INFO)

parser = argparse.ArgumentParser()
parser.add_argument('--file', '-f', dest='notebook_path', required=True)

current_dir = os.path.abspath(os.path.dirname(__file__))
posts_dir = os.path.join(current_dir, '_posts')
images_dir = os.path.join(current_dir, 'images')
notebooks_dir = os.path.join(posts_dir, 'notebooks')


if __name__ == '__main__':
    logging.info("Start move notebook files in right folders")
    args = parser.parse_args()
    logging.info("Path to notebook: {}".format(args.notebook_path))

    if not os.path.exists(notebooks_dir):
        os.mkdir(notebooks_dir)

    command = r'jupyter nbconvert --config notebooks/configs/jekyll_config.py "{}"'.format(args.notebook_path)
    logging.info(command)
    os.system(command)

    for filename in os.listdir(notebooks_dir):
        if filename.endswith('.md'):
            shutil.move(os.path.join(notebooks_dir, filename), os.path.join(notebooks_dir, '..', filename.replace("'", "")))
            logging.info("{} moved".format(filename))
            break
    else:
        raise ValueError("Didn't find markdown file inside the {} folder.".format(notebooks_dir))

    filename, _ = filename.split('.', maxsplit=1)
    notebook_images = os.path.join(notebooks_dir, filename + '_files', 'notebooks')

    if os.path.exists(notebook_images):
        notebook_images_in_folder = os.listdir(notebook_images)
        for image_name in notebook_images_in_folder:
            full_image_path = os.path.join(notebook_images, image_name)
            shutil.move(full_image_path, os.path.join(images_dir, image_name))

        logging.info("Moved {} images".format(len(notebook_images_in_folder)))

    shutil.rmtree(notebooks_dir)
    logging.info("Remove {} directory".format(notebooks_dir))

    logging.info("Script finished. Exit")
