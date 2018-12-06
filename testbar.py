import sys,os,time,argparse
import cmdprogress

def test_multi(args):

    bar = cmdprogress.MultiBar(*args.levels)
    for x in bar:
        time.sleep(args.pause)

def test_bar(args):
    bar = cmdprogress.IncrementalBar(max=args.max)
    for x in bar:
        time.sleep(args.pause)


def main():
    parser = argparse.ArgumentParser(description='cmdprogress bar tester',epilog='Please consult https://github.com/luciancooper/cmdprogress for further information')
    subparsers = parser.add_subparsers(title="Available bar types",metavar='bar')
    parser_multi = subparsers.add_parser('multi', help='test a multi bar',description="Test a multi level bar")
    parser_multi.add_argument('levels',nargs='*',type=int,help='Known Maximums')
    #parser_multi.add_argument('-l','--layers',type=int,help='Number of layers in the multibar')
    parser_multi.add_argument('-p','--pause',type=float,default=0.25,help='Pause duration at each test iteration')
    parser_multi.set_defaults(func=test_multi)

    parser_bar = subparsers.add_parser('bar', help='test a progress bar',description="Test a progress level bar")
    parser_bar.add_argument('-m','--max',type=int,default=100,help='Maxiumum of the progress bar')
    parser_bar.add_argument('-p','--pause',type=float,default=0.25,help='Pause duration at each test iteration')
    parser_bar.set_defaults(func=test_bar)
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
