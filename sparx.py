import click
from factory.modules import File

class Config(object):
    def __init__(self):
        self.verbose = False
 

pass_config = click.make_pass_decorator(Config, ensure=True)

@click.group()
@click.option('--verbose', is_flag=True)
@pass_config
def cli(config, verbose):
    """  Welcome to Sparx IO """
    config.verbose = verbose
   

@cli.command()
@click.argument('name')
def new(name):
    """ Create new application """
    click.echo("=======================================")
    click.echo("Crafting a new application ..... %s" % name)
    click.echo("=======================================")
    File.download("https://gitlab.com/cleverinsight-community/sparx/-/archive/master/sparx-master.tar.gz")


@cli.command()
@click.argument('type')
@click.option('--name')
def add(type, name):
    """ Add new service """
    click.echo("---------------------------------------")
    click.echo("Added new service called %s ..." % name)
    click.echo("---------------------------------------")


@cli.command()
@click.argument('type')
@click.option('--name')
def deploy(type, name):
    """ Create new deployment scaffolding """
    click.echo("---------------------------------------")
    click.echo("Added new deployment called %s ..." % name)
    click.echo("---------------------------------------")

    

