# simplex_merge
Simple way to merge two single sided scanned documents

I got an HP OfficeJet Pro 6960 thinking that it would be able to do duplex scanning. It does duplex printing and its great but I wanted to also have a double sided scan feature from the tray feeder. I only found that it doesn't do duplex scanning after trying it out at home.

Fortunately I figured out a way to merge and interleave two documents to achieve duplex scanning. This requires one to scan the same set of documents twice. Here is what you need to do:

1) Load up the document on the tray and scan it
2) Flip the document on the long binding side as if you are turning a page
3) Scan again

Effectively you will need to then interleave the two documents, the last document starting from the end. This is what the script exactly does! Very simple!

Following points show how to use it.

# Instructions

1. Install pypdf2: ```sudo pip install pypdf2```
2. Scan document once (assuming stored as "even.pdf")
3. Flip document like you would flip a page and scan again (assuming stored as "odd.pdf")
4. Invoke ```python merge.py  --even_file=even.pdf --odd_file=odd.pdf -o out.pdf```
