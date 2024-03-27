import os
import typer
from rich.console import Console
from rich.table import Table
from model import MyPackage
from database import insert_package, get_all_packages

console = Console()
app = typer.Typer()

your_packages = []

@app.command(help="List of packages to be installed")
def showpackages():
    all_packages = get_all_packages()
    table = Table(show_header=True, header_style="bold green")
    table.add_column("#", style="bold yellow", width=6)
    table.add_column("packages", min_width=20, style="bold yellow", justify="center")
    table.add_column("status", min_width=12, justify="center", style="bold yellow", )
    # table.add_column("Done", min_width=12, justify="right")
    for index, package in enumerate(all_packages):
        table.add_row(str(index), package.package, "to be installed")
    console.print(table)


@app.command(help="Your project name")
def get_project_name(project_name: str = typer.Option(..., prompt="Please enter project name")):
    """
    cd into the folder where you want to have your project created,
    make sure project folder does not already exist,
    Provide name for your project
    """
    env_path = "env"

    try:
        isExist = os.path.exists(env_path)
        if isExist:
            os.makedirs(project_name)
            console.print(f"Hi, you are a new project with the name {project_name}")

        else:
            console.print("[bold red]Please create virtual environment")

    except FileExistsError:
        # directory already exists
        console.print(f"[bold red]Sorry 🥺, a folder with name '{project_name}' already exists")
        typer.echo("pip install django")


@app.command(help="Add to list of packages to be installed.")
def addpackage(package: str):
    package = MyPackage(package)
    insert_package(package)
    showpackages()

@app.command()
def asktoaddpackage(package: str):
    while True:
        console.print("add a new package,enter done when you have all your packages")
        addpackage()
        if package == "done":
            break


if __name__ == "__main__":
    app()
