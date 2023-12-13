import typer
from typing_extensions import Annotated
from pathlib import Path
from typing import Optional
from rich.prompt import Prompt

app = typer.Typer(rich_markup_mode="rich")


@app.command()
def main(
    file: Annotated[
        Optional[Path],
        typer.Option(
            exists=True,
            file_okay=True,
            dir_okay=False,
            writable=False,
            readable=True,
            resolve_path=True,
            prompt="Enter the path of your data file(csv)",
        ),
    ]
) -> None:
    text = file.read_text()
    print(f"Config file contents: {text}")


if __name__ == "__main__":
    app()
