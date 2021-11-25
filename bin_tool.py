import intelhex
import click
import sys
import traceback

bin_tool_version = '0.0.1'

@click.group()
def cli():
    pass

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)
    sys.exit(0)


@click.command()
def version():
    """output version"""
    click.echo(f'version: {bin_tool_version}')

@click.command()
@click.option('--bin', type=str, prompt='intput your bin file', help='input bin file path')
@click.option('--hex', type=str,  prompt='intput save hex file path', help='input hex file path')
def bin_to_hex(bin:str, hex:str):
    try:
        intelhex.bin2hex(bin, hex, 0)
    except Exception as e:
        print('err:' + traceback.format_exc())
        sys.exit(1)

cli.add_command(hello)
cli.add_command(version)
cli.add_command(bin_to_hex)


if __name__ == '__main__':
    cli()
    sys.exit(0)