import argparse

from uniplot import plot
from . import parse
from . import analysis

LOC="uniprot_receptor.xml.gz"

def dump(args):
    """Returns all protein data"""
    for record in parse.uniprot_seqrecords(LOC):
        print(record)

def names(args):
    """Returns a formatted list of protein names"""
    for record in parse.uniprot_seqrecords(LOC):
        print(record.name)

def average(args):
    """Returns the average length of proteins"""
    print("Average Length is {}".format(
        analysis.average_len(parse.uniprot_seqrecords(LOC))))

def plot_average_by_taxa(args):
    """Returns graph showing average protein length by taxonomy"""
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(LOC))
    plot.plot_bar_show(av)

def plot_average_by_taxa_pie(args):
    """Returns pie chart showing average protein length by taxonomy"""
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(LOC))
    plot.plot_pie_show(av)

def cli():
    """Adds arguments for the console interface"""
    ## Create a new parser
    parser = argparse.ArgumentParser(prog="uniplot")
    subparsers = parser.add_subparsers(help="Sub Command Help")

    parser.add_argument("--file-location", help="Allows you to pick the file for the program to run")



    ## Add subparsers
    subparsers.add_parser("dump", help="To dump all protein data to the CI").set_defaults(func=dump)
    subparsers.add_parser("list", help="To display a formatted list of all proteins").set_defaults(func=names)
    subparsers.add_parser("average", help="To print the average length of the proteins").set_defaults(func=average)
    subparsers.add_parser("plot-average-by-taxa",
                          help="Displays a graph of the average length of proteins by taxonomy").set_defaults(
        func=plot_average_by_taxa)
    subparsers.add_parser("plot-average-by-taxa-pie",
                          help="Displays a pie chart of the average length of proteins by taxonomy").set_defaults(
        func=plot_average_by_taxa_pie)



    ## Parse the command line
    args = parser.parse_args()
    ## Assign the users input file location
    global LOC
    LOC=args.file_location

    ## Take the func argument, which points to our function and call it.
    args.func(args)

