import binascii

PRINT_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~`!@#$%^&*()-_=+.,/<>?;:'\"{[}]|\\"
def GetPrintable(data):
    return ''.join([a_byte if a_byte in PRINT_CHARS else "." for a_byte in data])
    
def SpacePad(data,size):
    return data + " " * (size - len(data))
    
def HexDump(data):
    bytes_per_line = 16
    bytes_per_half = 8
    hex_space = (bytes_per_half*3) - 1
    hex_data = ["%2.2X" % (ord(a_byte)) for a_byte in data]
    hex_lines = [
        "%8.8Xh: " % (cnt) +
        SpacePad(' '.join(hex_data[cnt:cnt+bytes_per_half]), hex_space) + 
        "    " + 
        SpacePad(' '.join(hex_data[cnt+bytes_per_half:cnt+bytes_per_line]), hex_space)  +
        "    " +
        GetPrintable(binascii.unhexlify(''.join(hex_data[cnt:cnt+bytes_per_line])))
         
        for cnt in xrange(0,len(hex_data),bytes_per_line)
    ]
    return '\n'.join(hex_lines)