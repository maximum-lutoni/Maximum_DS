import argparse

parser = argparse.ArgumentParser(description="Стандартное описание")
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='целое число сумматора')
parser.add_argument('--sum','-s', dest='accumulate',action='store_const',
                    const = sum, default=max, 
                    help = "Находим сумму чисел")

args = parser.parse_args()
print(args.accumulate(args.integers))