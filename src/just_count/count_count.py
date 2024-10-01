import just_count.square as square
import just_count.squareroot as squareroot

import click


@click.group()
def cmd_group():
    pass


@cmd_group.command()

@click.argument(
    "number",
    type=int,
    )

def sqr(number):
    print(f"The square of {number} is {square.square(number)}")


@cmd_group.command()

@click.argument(
    "number",
    type=int,
    )

def sqrt(number):
    print(f"The squareroot of {number} is {squareroot.squareroot(number)}")


if __name__ == '__main__':
    cmd_group()
    