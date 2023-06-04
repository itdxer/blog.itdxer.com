import os
import sys

from six.moves.urllib.parse import quote


filename = None
for arg in sys.argv:
    if arg.endswith('.ipynb'):
        filename, _ = arg.split('.ipynb', maxsplit=1)
        break


current_dir = os.path.abspath(os.path.dirname(__file__))

# modify this function to point your images to a custom path
# by default this saves all images to a directory 'images' in
# the root of the blog directory
def path2support(path):
    """Turn a file path into a URL"""
    return '{{ BASE_PATH }}/images/' + os.path.basename(path)


c = get_config()
c.NbConvertApp.export_format = 'markdown'
c.MarkdownExporter.template_path = [current_dir]
c.MarkdownExporter.template_file = os.path.join(current_dir, 'jekyll.tpl')
c.MarkdownExporter.filters = {'path2support': path2support}

if filename is not None:
    c.NbConvertApp.output_base = filename.lower().replace(' ', '-')
    c.FilesWriter.build_directory = os.path.join(
        current_dir, '..', '..', '_posts'
    )
