# Usage:
#  --readaddr <address> --readlen <read_length> --device <serdev> --baud <baudrate> --nodex <#>
import ghidorah
import argparse

defaultDevice = '/dev/cu.usbserial-FT079LCR2'
defaultDevice = '/dev/cu.usbserial-USAKMYZM'
defaultDevice = '/dev/cu.usbserial-A2003EyG'

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--readaddr', type=str, default='0x600',
                    help='address to read')
parser.add_argument('--readlen', type=str, default='0x10',
                    help='length to read')
parser.add_argument('--baud', type=int, default=57600,
                    help='baud rate')
parser.add_argument('--device', type=str, default=defaultDevice,
                    help='serial port')
parser.add_argument('--nodex', type=str, default='0xFF',
                    help='nodex (0-254, or 255 for broadcast (default)')

args = parser.parse_args()
baud = args.baud
device = args.device
readaddr = int(args.readaddr, 0)
readlen = int(args.readlen, 0)
nodex = int(args.nodex, 0)

l = ghidorah.Ghidorah(device, baud)
b = l.read(nodex, readaddr, readlen)
print(b)
