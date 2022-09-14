import shutil
import os

need_dir = "/Users/black/Documents/design"

os.chdir(need_dir)
need_dir_archive = "/Users/black/Documents/design/projects"
# shutil.make_archive('another', 'zip', need_dir_archive)
shutil.unpack_archive('v_gz.tar.gz', "o_my")
