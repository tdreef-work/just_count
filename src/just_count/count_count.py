import just_count.square as square
import just_count.squareroot as squareroot

import click


@click.command()

@click.argument(
    "number",
    type=int,
    )

def main(number):
    print(f"The square of {number} is {square.square(number)}")
    print(f"The squareroot of {number} is {squareroot.squareroot(number)}")


if __name__ == '__main__':
    main()