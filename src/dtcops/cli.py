from __future__ import annotations

from pathlib import Path
from typing import Any

import typer
from rich.console import Console
from rich.table import Table

from dtcops.inventory import calculate_inventory
from dtcops.profit import calculate_profit
from dtcops.roi import calculate_roi
from dtcops.scorecard import calculate_scorecard
from dtcops.validators import CSVValidationError, read_csv

app = typer.Typer(help="CSV-based ecommerce operations toolkit.")
console = Console()


def _format_value(value: Any) -> str:
    if isinstance(value, float):
        if value == float("inf"):
            return "No sales"
        return f"{value:,.2f}"
    return str(value)


def _print_summary_table(title: str, data: dict[str, Any]) -> None:
    table = Table(title=title)
    table.add_column("Metric", style="bold")
    table.add_column("Value", justify="right")

    for key, value in data.items():
        label = key.replace("_", " ").title()
        table.add_row(label, _format_value(value))

    console.print(table)


def _print_rows_table(title: str, rows: list[dict[str, Any]]) -> None:
    table = Table(title=title)
    if not rows:
        console.print("No rows found.")
        return

    for column in rows[0].keys():
        table.add_column(column.replace("_", " ").title())

    for row in rows:
        table.add_row(*[_format_value(value) for value in row.values()])

    console.print(table)


def _load_csv_or_exit(path: Path):
    try:
        return read_csv(path)
    except CSVValidationError as exc:
        console.print(f"[red]Error:[/red] {exc}")
        raise typer.Exit(code=1) from exc


@app.command()
def roi(csv_path: Path) -> None:
    """Calculate ad ROI and break-even ACOS from a sales CSV."""
    dataframe = _load_csv_or_exit(csv_path)
    try:
        result = calculate_roi(dataframe)
    except CSVValidationError as exc:
        console.print(f"[red]Error:[/red] {exc}")
        raise typer.Exit(code=1) from exc
    _print_summary_table("ROI Summary", result)


@app.command()
def profit(csv_path: Path) -> None:
    """Calculate profit and margin from a sales CSV."""
    dataframe = _load_csv_or_exit(csv_path)
    try:
        result = calculate_profit(dataframe)
    except CSVValidationError as exc:
        console.print(f"[red]Error:[/red] {exc}")
        raise typer.Exit(code=1) from exc
    _print_summary_table("Profit Summary", result)


@app.command()
def inventory(csv_path: Path) -> None:
    """Flag inventory health from an inventory CSV."""
    dataframe = _load_csv_or_exit(csv_path)
    try:
        result = calculate_inventory(dataframe)
    except CSVValidationError as exc:
        console.print(f"[red]Error:[/red] {exc}")
        raise typer.Exit(code=1) from exc
    _print_rows_table("Inventory Summary", result)


@app.command()
def score(csv_path: Path) -> None:
    """Score product research opportunities from a CSV."""
    dataframe = _load_csv_or_exit(csv_path)
    try:
        result = calculate_scorecard(dataframe)
    except CSVValidationError as exc:
        console.print(f"[red]Error:[/red] {exc}")
        raise typer.Exit(code=1) from exc
    _print_rows_table("Product Research Scorecard", result)


if __name__ == "__main__":
    app()
