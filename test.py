import click


class Config(object):


    def __init__(self):
        self.verbose = False

pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--verbose', is_flag=True)
@click.option('--home-directory', type=click.Path())

@pass_config
def cli(config, verbose, home_directory):
    config.verbose = verbose

    if home_directory is None:
        home_directory = '.'
    config.home_directory =  home_directory

@cli.command()
@click.option('--string', default="Sparx Community", help="Greeting are my responsibility!!")
@click.option('--repeat', default=1, type=int, help="How many times you want to repeat")
@click.argument('out', type=click.File('w'), default='-', required=False)

@pass_config
def say(config, string, repeat, out):
    """ 
        Welcome to Sparx!!
    """

    if config.verbose:
        click.echo("We are in verbose mode")
        click.echo(b'\xe2\x98\x83', nl=False)

    click.echo("Home directory is %s" % config.home_directory)
    for x in xrange(repeat):
        click.echo('Welcome to %s!' % string, file=out)
        click.echo(click.style('Hello World!', fg='green'))
        click.echo(click.style('Some more text', bg='blue', fg='white'))
        click.echo(click.style('ATTENTION', blink=True, bold=True))



@cli.command()
def new():
    """ 
        Start `new` application skeleton
    """


@cli.command()
def create(config, string, repeat, out):
    """ 
    Create `Sparx` project
    """
    pass