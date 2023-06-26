#!/usr/bin/env python
from wikinlplib import get_phrase
from wikinlplib import summarize_wiki

# import fire
import click

# pylint: disable=no-value-for-parameter


@click.command()
@click.option(
    "-f",
    "--func",
    required=True,
    type=click.Choice(["phrase", "summary"], case_sensitive=False),
    help="Available functions, e.g. phrase, summary",
)
@click.option("-n", "--name", required=True, help="Text for seraching")
def cli(func, name):
    """
    cli application for wikipedia text
    e.g., wikimlp --func=phrase --name=Germany
    """

    if func == "phrase" or func == "PHRASE":
        click.echo(get_phrase(name))
    else:
        click.echo(summarize_wiki(name))


if __name__ == "__main__":
    cli()
