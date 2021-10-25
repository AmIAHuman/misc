import zipfile
import itertools
import os
os.chdir("/tmp/")

def extractFile(zip_file, password):
    try:
        zip_file.extractall(pwd=bytes(password, 'utf-8'))
        return True
    except KeyboardInterrupt:
        exit(0)
    except Exception:
        pass

zipfilename = 'file.zip'
nums = '0123456789'
zip_file = zipfile.ZipFile(zipfilename)

for c in itertools.product(nums, repeat=3):
    password = ''.join(x for x in c)
    print("Trying: %s" % password)
    if extractFile(zip_file, password):
        print('*' * 20)
        print('Password found: %s' % password)
        print('Files extracted...')
        exit(0)
        break

print('Password not found.')
