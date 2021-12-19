import click
import json

@click.command()
@click.argument('filename', type=click.Path(exists=True))
@click.argument('mints', type=click.Path(exists=True))
@click.option('--data', default='=', help='example --data=owner_wallet')

def parse(filename, mints, data):
    """Simple program that greets NAME for a total of COUNT times."""
    print(f"parsing: ", mints)
    f = open(mints)

    f2 = open(filename,)
    json_data = json.load(f2)

    lines = f.readlines()
    for l in lines:
        mint = l.strip()
        for item in json_data:
            if item['mint_account'] == mint:
                print(mint, ",", item[data], "\n")

if __name__ == '__main__':
    parse()