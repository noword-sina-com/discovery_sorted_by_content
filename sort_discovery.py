#! /usr/bin/env python
#coding=utf-8
import re
import codecs
from hanziconv import HanziConv

def sort_func(s):
    m = re.search(ur"ed2k://\|file\|(.*)", s.strip())
    if m:
        s = m.group(1)
        m = re.search(ur"^(\[.+?\])(.+?)：", s)
        if m:
            s = m.group(2) + m.group(1)
        else:
            m = re.search(ur"^\[.+?\](.*)", s)
            if m:
                s = m.group(1)
    return s

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument("input", action="store", nargs = 1)
    parser.add_argument("output", action="store", nargs = 1)
    parser.add_argument("--encoding", action="store", default="utf_8_sig", nargs=1)
    parser.add_argument("--traditional", action="store_true", default=False)
    args = parser.parse_args()

    buf = codecs.open(args.input[0], "rb", args.encoding).read()

    if args.traditional:
        buf = HanziConv.toTraditional(buf)
    else:
        buf = HanziConv.toSimplified(buf)

    lines = buf.split("\n")
    lines.sort(key = sort_func)
    codecs.open(args.output[0], "wb", args.encoding).writelines(lines)
