import sys
import argparse

def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--links_file", dest="links_file", help="Links file", required=True)
    parser.add_argument("-o", "--nodes_file", dest="nodes_file", help="Nodes file", required=True)
    args = parser.parse_args(arguments)
    print(f"Links file: {format(args.links_file)}")
    print(f"Nodes file: {format(args.nodes_file)}")
            
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))