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
    os.system(r'pyinstaller --onefile .\src\render.py')
    _resetDir('dist\minimap_renderer_gui')
    # shutil.copy('wowsunpack.exe', 'dist\WoWsUnpack\wowsunpack.exe')
    # copy LICENSE and README.md as well
    # shutil.copy('LICENSE', 'dist\WoWsUnpack\LICENSE.txt')
    # shutil.copy('README.md', 'dist\WoWsUnpack\README.txt')
    # shutil.copy('使用说明.md', 'dist\WoWsUnpack\使用说明.txt')
    # shutil.move('dist/run.exe', 'dist/WoWsUnpack/unpack.exe')

    # create zip file from WoWsUnpack folder with compression
    with zipfile.ZipFile('dist/minimap_renderer_gui.zip', 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk('dist/minimap_renderer_gui'):
            for file in files:
                # remove dist/ folder
                zip_file.write(os.path.join(root, file), arcname=os.path.join(root[len('dist/'):], file))
    print('complete')
