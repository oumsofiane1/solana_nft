import click
import json

@click.command()
@click.argument('filename', type=click.Path(exists=True))
@click.argument('mints', type=click.Path(exists=True))
@click.option('--data', default='=', help='example --data=mintWalletAddress')

def parse(filename, mints, data):
    """Simple program that greets NAME for a total of COUNT times."""
    print(f"parsing: ", mints)
    f = open(mints)
    s = set()

    lines = f.readlines()
    for l in lines:
        s.add(l.strip())

    print(f"parsing: ", filename)
    f = open(filename,)
    json_data = json.load(f)

    for item in json_data:
        if s.__contains__(item['mint_account']):
            print(item[data])


if __name__ == '__main__':
    parse()