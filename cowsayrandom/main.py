import typer


app = typer.Typer()


@app.callback()
def callback():
    """
    Awesome Portal Gun
    """
    
@app.command()
def hello_world():
    typer.echo("Hello world")


@app.command()
def shoot():
    """
    Shoot the portal gun
    """
    typer.echo("Shooting portal gun")


@app.command()
def load():
    """
    Load the portal gun
    """
    typer.echo("Loading portal gun")
