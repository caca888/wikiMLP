#!/usr/bin/env python
# pylint: disable=E0401
from src.wikinlplib import get_phrase
from src.wikinlplib import summarize_wiki
from src.wikinlplib import get_sentiment
from src.wikinlplib import conclude_text

# import fire
import click

# pylint: disable=no-value-for-parameter


@click.command()
@click.option(
    "-f",
    "--func",
    required=True,
    type=click.Choice(["phrase", "summary", "sentiment", "conclude"], case_sensitive=False),
    help="Available functions, e.g. phrase, summary, sentiment, conclude",
)
@click.option("-n", "--name", required=True, help="Text for seraching")
def cli(func, name):
    """
    cli application for wikipedia text
    e.g., wikimlp --func=phrase --name=Germany 
    or    wikimlp --func=summary --name=Germany 
    or    wikimlp --func=sentiment --name=Germany
    """

    if func == "phrase" or func == "PHRASE":
        click.echo(get_phrase(name))
    elif func == "summary" or func == "SUMMARY":
        click.echo(summarize_wiki(name))
    elif func == "conclude" or func == "CONCLUDE":
        click.echo(conclude_text(name))
    else:
        get_sentiment(name)


if __name__ == "__main__":
    cli()
