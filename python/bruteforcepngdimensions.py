import binascii
import struct

crc32key = 0x00000600 # Change this value
for i in range(0, 65535):
  height = struct.pack('>i', i)
  for x in range(0, 65535):
    width = struct.pack('>i', x)
    print("Height: " + height + " Width: " + width)
    data = '\x49\x48\x44\x52' + width + height + '\x08\x06\x00\x00\x00'

    crc32result = binascii.crc32(data) & 0xffffffff

    if crc32result == crc32key:
      print "Got Height: "
      print ''.join(map(lambda c: "%02X" % ord(c), height))
      print "Got Width: "
      print ''.join(map(lambda c: "%02X" % ord(c), width))
      exit(0)
