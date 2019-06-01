import os
import shutil
import yaml
import click
from factory.modules import download

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
    download("https://github.com/CleverInsight/sparx-core/archive/v1.0.0.tar.gz", name)


@cli.command()
@click.argument('type')
@click.option('--name')
def add(type, name):
    """ Add new service """
    click.echo("Added new service called %s ..." % name)
   

@cli.command()
@click.argument('name')
def rm(name):
    """ Remove application created """
    if os.path.exists(name):
        shutil.rmtree(name)
        click.echo(name + " removed..")
    else:
        click.echo("No such app exists...")
    


@cli.command()
@click.argument('type')
@click.option('--name')
def deploy(type, name):
    """ Create new deployment scaffolding """
    click.echo("Added new deployment called %s ..." % name)