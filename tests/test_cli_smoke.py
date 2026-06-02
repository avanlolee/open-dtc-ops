import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def run_cli_command(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "dtcops.cli", *args],
        cwd=PROJECT_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )


def test_roi_command_runs_against_sales_sample():
    result = run_cli_command("roi", "examples/sales_sample.csv")

    assert result.returncode == 0
    assert "ROI Summary" in result.stdout
    assert "Profitable" in result.stdout


def test_profit_command_runs_against_sales_sample():
    result = run_cli_command("profit", "examples/sales_sample.csv")

    assert result.returncode == 0
    assert "Profit Summary" in result.stdout
    assert "Net Profit" in result.stdout


def test_inventory_command_runs_against_inventory_sample():
    result = run_cli_command("inventory", "examples/inventory_sample.csv")

    assert result.returncode == 0
    assert "Inventory Summary" in result.stdout
    assert "Reorder Now" in result.stdout


def test_score_command_runs_against_product_research_sample():
    result = run_cli_command("score", "examples/product_research_sample.csv")

    assert result.returncode == 0
    assert "Product Research Scorecard" in result.stdout
    assert "Good" in result.stdout

