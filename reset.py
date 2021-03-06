# Usage:
#   --device <serdev> --baud <baudrate> --nodex <#>
import ghidorah
import argparse

defaultDevice = '/dev/cu.usbserial-FT079LCR2'
defaultDevice = '/dev/cu.usbserial-USAKMYZM'
defaultDevice = '/dev/cu.usbserial-A2003EyG'

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--baud', type=int, default=57600,
                    help='baud rate')
parser.add_argument('--device', type=str, default=defaultDevice,
                    help='serial port')
parser.add_argument('--nodex', type=str, default='0xFF',
                    help='nodex (0-254, or 255 for broadcast (default)')
parser.add_argument('--verbose', type=int, default=0,
                    help='verbosity')

args = parser.parse_args()
baud = args.baud
device = args.device
nodex = int(args.nodex, 0)
verbose = args.verbose

l = ghidorah.Ghidorah(device, baud)
# clr $7F; jmp $A027
l.write(nodex, 0x600, 0x6, [0x7F, 0x00, 0x71, 0x7E, 0xA0, 0x27])
l.exec(nodex, 0x600)

