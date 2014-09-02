import hashlib
import binascii
import plistlib 
import sys
import os
from multiprocessing import Pool
from M2Crypto.EVP import pbkdf2

if len(sys.argv) < 2:
    print "Please pass in the directory of the backup"
    sys.exit(1)

backup_path = sys.argv[1]

if not os.path.exists(backup_path):
    print "Not a real backup path"
    sys.exit(1)

# hash name of the file that contains the restrictions passcode
filename = binascii.hexlify(hashlib.sha1("HomeDomain-Library/Preferences/com.apple.restrictionspassword.plist").digest())

full_path = os.path.join(backup_path, filename)

if not os.path.exists(full_path):
    print "passocde file not found for some reason"
    sys.exit(1)

plist = plistlib.readPlist(full_path)

hashKey = plist["RestrictionsPasswordKey"].data
salt = plist["RestrictionsPasswordSalt"].data
print salt
print "Hash:", binascii.hexlify(hashKey)
print "Salt:", binascii.hexlify(salt)

def test_key(r):
    for test_number in range(r[0], r[1]):
        test_pin = "%04d" % test_number
        #print "testing", test_pin
        test_hash = pbkdf2(test_pin, salt, 1000, 20)

        print "pin", test_pin, "hash:", binascii.hexlify(test_hash), "key: ", binascii.hexlify(hashKey)
        

        if test_hash == hashKey:
            return test_pin

    return None

pool = Pool(processes=4)              # start 4 worker processes
print pool.map(test_key, [(0,2500),(2501, 5000),(5001, 7500),(7501, 10000)]) 