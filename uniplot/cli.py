import argparse

from uniplot import plot
from . import parse
from . import analysis

LOC="uniprot_receptor.xml.gz"

def dump(args):
    for record in parse.uniprot_seqrecords(LOC):
        print(record)

def names(args):
    for record in parse.uniprot_seqrecords(LOC):
        print(record.name)

def average(args):
    print("Average Length is {}".format(
        analysis.average_len(parse.uniprot_seqrecords(LOC))))


def cli():
    ## Create a new parser
    parser = argparse.ArgumentParser(prog="uniplot")

    subparsers = parser.add_subparsers(help="Sub Command Help")

    ## Add subparsers
    subparsers.add_parser("dump", help="To dump a list of all proteins").set_defaults(func=dump)
    subparsers.add_parser("list", help="To display a formatted list of all proteins").set_defaults(func=names)
    subparsers.add_parser("average", help="To print the average length of the proteins").set_defaults(func=average)


    ## Parse the command line
    args = parser.parse_args()

    ## Take the func argument, which points to our function and call it.
    args.func(args)

