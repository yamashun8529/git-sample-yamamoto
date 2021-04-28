import os
import pathlib
import glob
import shutil

print(os.path.exists('test.txt'))
print(os.path.isfile('test.txt'))
print(os.path.isdir('Practice Python'))

#os.rename('test.txt', 'rename.txt')
#os.symlink('rename.txt', 'symlink.txt') # copy and link

#os.mkdir('test_dir')
#os.rmdir('test_dir')

#pathlib.Path('empty.txt').touch()
#os.remove('empty.txt')

#os.mkdir('test_dir')
#os.mkdir('test_dir/test_dir2')
#print(os.listdir('test_dir'))
#pathlib.Path('test_dir/test_dir2/empty.txt').touch()
#shutil.copy('test_dir/test_dir2/empty.txt',
#            'test_dir/test_dir2/empty2.txt')
#print(glob.glob('test_dir/test_dir2/*'))
#shutil.rmtree('test_dir')#全消去気を付ける

print(os.getcwd())