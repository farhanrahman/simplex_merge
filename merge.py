#!/usr/bin/env python

import optparse
import re
from PyPDF2 import PdfFileWriter, PdfFileReader

parser = optparse.OptionParser("merge.py")
parser.add_option("--file_list", default=None,
                 dest="file_list",
                 help="File containing list of documents to merge")
parser.add_option("-o", "--output_file", default=None,
                 dest="output_file",
                 help="Name of output file for the merge")

(opt, args) = parser.parse_args()

if not (opt.file_list and opt.output_file):
    parser.print_help()
    exit(1)

output_pdf_object = PdfFileWriter()

lines = open(opt.file_list).readlines()

for line in lines:
    f = PdfFileReader(open(line.replace("\n", ""),"rb"))
    num_pages = f.numPages

    for i in range(0, num_pages):
        output_pdf_object.addPage(f.getPage(i))

output_pdf_object.write(open(opt.output_file,"wb"))
