#!/usr/bin/python2 
import binascii
import codecs


# (OP 00E0) '6602 640A 650F 221A F629 F429 F529 6010 6110 D015 00E0 0000 0000 6BFF 00EE' 
# (OP 1) '6001 6102 1200'#
# (OP 2)
# (OP 3) '6011 3011 1200 6196 3103 1200'
# (OP 4) '6012 4011 1200 6105 4105 1200'
# (OP 5) '6245 6445 5240 1200 624F 5240 1200'

# (OP 6) '6001 6102 6203 6304 6405 6506 6607 6708 6809 690A 6A0B 6B0C 6C0D 6D0E 6E0F 6F10'
# (OP 7) '7055 7155 1200'
# (OP 8)
# (OP 9) '6011 6112 9010 1200 6012 9010 1200 61FF'
# (OP A) 'A202 A302 AFFF'
# (OP B) '7002 B200'
# (OP C) 'C012 1200'
# (OP FX07)
# (OP FX0A)
# (OP FX18) '6015 F018'
# (OP FX1E) 'A020 6302 F31E'
# (OP FX29) '6602 640A 650F F629 F429 F529 6010 6110 D015 D015'
# (OP FX33) '619C A300 F133 6001 F01E F01E'
# (OP FX55) '600A 610B 620C 630D 640E A300 F455 6F01 FF1E FF1E FF1E FF1E'
# (OP FX65) '6A0A 6B0B 6C0C 6D0D 6E0E A300 FF55 6F01 FF1E FF1E FF1E FF1E FF65'

new_str = codecs.decode(hx.replace(" ", ""), 'hex')

output_file = open("TEST", "wb")
output_file.write(new_str)

output_file.close()
