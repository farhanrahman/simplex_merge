#!/usr/bin/env python

import optparse
from PyPDF2 import PdfFileWriter, PdfFileReader

parser = optparse.OptionParser("merge.py")
parser.add_option("--even_file", default=None,
                 dest="even_file",
                 help="First pdf having even pages only")
parser.add_option("--odd_file", default=None,
                 dest="odd_file",
                 help="Pdf file having the odd pages only")
parser.add_option("-o", "--output_file", default=None,
                 dest="output_file",
                 help="Name of output file for the merge")
(opt, args) = parser.parse_args()

if not (opt.even_file and opt.odd_file and opt.output_file):
    parser.print_help()
    exit(1)

output_pdf_object = PdfFileWriter()

even = PdfFileReader(open(opt.even_file,"rb"))
odd = PdfFileReader(open(opt.odd_file,"rb"))

assert(even.numPages == odd.numPages)

num_pages = even.numPages

for i in range(0, num_pages):
    output_pdf_object.addPage(even.getPage(i))
    output_pdf_object.addPage(odd.getPage(num_pages-i-1))

output_pdf_object.write(open(opt.output_file,"wb"))
