import struct

# global header
alldata = open("wireshark.bin", "rb").read()
magic_number = alldata[:4]
data = alldata[24:]
                     
byte_order = None
if magic_number == b"\xa1\xb2\xc3\xd4":
    byte_order = '>'
elif magic_number == b"\xd4\xc3\xb2\xa1":
    byte_order = '<'
else:
    raise TypeError()

#packet header
packet_header_len = 16
position = 0
while position < len(data):
    ts_sec, ts_usec, incl_len, orig_len = struct.unpack("{0}4l".format(byte_order), data[position:position + packet_header_len])
    print("Packet timestamp seconds: {0}, microseconds: {1}".format(ts_sec, ts_usec))
    position = position + packet_header_len + incl_len
