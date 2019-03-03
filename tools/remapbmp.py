#!/usr/bin/env python

import argparse

MAP={
    '\x32':'\x31',
    '\x30':'\x12',
    '\x31':'\x32',
    '\x22':'\x13',
    '\x21':'\x02',
    '\x23':'\x03',
    '\x12':'\x11',
    '\x11':'\x20',
    '\x02':'\x01',
    '\x01':'\x02',
    '\x03':'\x21',
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser("remap bmp")
    parser.add_argument('infile')
    parser.add_argument('outfile')
    args = parser.parse_args()

    infile = args.infile
    outfile = args.outfile

    with open(infile, 'rb') as h_in:
        with open(outfile, 'wb') as h_out:
            header = h_in.read(54)
            h_out.write(header)
            
            inbyte = h_in.read(1)
            while inbyte:
                outbyte = MAP.get(inbyte, inbyte)
                h_out.write(outbyte)
                inbyte = h_in.read(1)

