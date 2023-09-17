import os
import shutil
import zipfile

def _resetDir(dirname: str):
    """
    Removes a directory if it exists and creates a new one.
    """
    if os.path.exists(dirname):
        shutil.rmtree(dirname)
    os.mkdir(dirname)

if __name__ == '__main__':
    os.system(r'pyinstaller .\src\render.py')
    _resetDir('dist\minimap_renderer_gui')
    shutil.copy('LICENSE', 'dist\minimap_renderer_gui\LICENSE.txt')
    shutil.move('dist/render.exe', 'dist/minimap_renderer_gui/gui.exe')

    # zip the exe, with max compression
    with zipfile.ZipFile('dist/minimap_renderer_gui.zip', 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zip_file:
        for root, dirs, files in os.walk('dist/minimap_renderer_gui'):
            for file in files:
                # remove dist/ folder
                zip_file.write(os.path.join(root, file), arcname=os.path.join(root[len('dist/'):], file))
    print('complete')
