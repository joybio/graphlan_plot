#!/bin/python
__date__ = "2023-7-13"
__author__ = "Junbo Yang"
__email__ = "yang_junbo_hi@126.com"
__license__ = "MIT"

import itertools

"""
The MIT License (MIT)

Copyright (c) 2022 Junbo Yang <yang_junbo_hi@126.com> <1806389316@pku.edu.cn>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import argparse
import re
import time
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Manager


def parseArg():
    parser = argparse.ArgumentParser(description="This script is designed to convert the output (in tsv format) "
                                                 "of Humann3 into the Stamp format (spf).")
    parser.add_argument("-i", "--input", type=str, required=True,
                        help="Input file: Output of humann3 which should be a tsv file, e.g. taxonomy.tsv.", metavar="<file>")

    parser.add_argument("-o", "--out", type=str, required=True,
                        help='Output file', metavar="<file>")
    parser.add_argument("--version", action="version", version=get_version(),
                        help='Display version')
    return parser.parse_args()


def get_version():
    return "0.0.1"

def covertion(Input, Output):
    species_abun = {}
    with open(Output, "w") as out:
        tax = ["Kingdom","Phylum","Class","Order","Family","Genus","Species", "Strain"]
        out.write('\t'.join(tax) + "\t")
        pattern = re.compile('t__')
        with open(Input, "r") as Input_file:
            for i in Input_file:
                if i.startswith("#"):
                    pass
                else:
                    i = i.strip().split("\t")
                    if re.search("unclassified",i[0]):
                        pass
                    elif i[0].startswith("k__"):
                        if pattern.search(i[0]):
                            abundunce = i[1:]
                            taxonomy = re.sub(r'.__','',i[0])
                            taxonomy= taxonomy.split("|")
                            key = '|'.join(taxonomy)
                            if key in species_abun.keys():
                                species_abun[key] = [round(float(species_abun[key][idx]) + float(abundunce[idx]),4)
                                                                for idx in range(len(abundunce))]
                            else:
                                species_abun[key] = [round(float(abundunce[idx]),4) for idx in range(len(abundunce))]
                        else:
                            pass
                    elif i[0].startswith("clade_name"):
                        ID = i[1:]
                        out.write('\t'.join(ID) + "\n")
                    else:
                        ID = i[1:]
                        out.write('\t'.join(ID) + "\n")
            for key in species_abun.keys():
                out.write('\t'.join(key.split("|")) + "\t" + '\t'.join(map(str,species_abun[key])) + "\n")


def main():
    args = parseArg()
    covertion(args.input,args.out)

if __name__ == "__main__":
    e1 = time.time()
    main()
    e2 = time.time()
    print("INFO {} Total times: {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),
                                           round(float(e2 - e1), 2)))