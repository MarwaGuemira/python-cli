import click

def convert_to_roman(number):
    roman_numerals = {
        1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C",
        90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V",
        4: "IV", 1: "I"
    }

    result = ""
    for value in roman_numerals.keys():
        while number >= value:
            result += roman_numerals[value]
            number -= value
    return result


def convert_to_number(roman):
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }
    result = 0
    rest = 0
    for symbol in reversed(roman):
        value = roman_numerals[symbol]
        if value < rest:
            result -= value
        else:
            result += value
        rest = value
    return result


@click.command()
@click.option('--to-roman', is_flag=True)
@click.option('--to-number', is_flag=True)
@click.argument('input')
def convert(to_roman, to_number, input):
    if to_roman:
        result = convert_to_roman(int(input))
    elif to_number:
        result = convert_to_number(input)
    else:
        click.echo("Please specify --to-roman or --to-number")
        return

    click.echo(result)


if __name__ == '__main__':
    convert()
