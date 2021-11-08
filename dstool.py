import click
import json

@click.command()
@click.argument('filename', type=click.Path(exists=True))
@click.option('--tag', help='tag of the form; tagName=value')
@click.option('--data', default='mintWalletAddress', help='example --data=mintWalletAddress')

def parse(filename, tag, data):
    """Simple program that greets NAME for a total of COUNT times."""
    print(f"parsing: ", filename)

    filter = tag.split("=")

    f = open(filename,)
    json_data = json.load(f)

    for item in json_data:
        for att in item['nftData']['attributes']:
            if att['trait_type'] == filter[0] and att['value'] == filter[1]:
                print(item[data])


if __name__ == '__main__':
    parse()