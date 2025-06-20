def validate_correct_value(value, name_figure_attr):

    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise TypeError(f'{name_figure_attr} повинні(о) бути числом (int або float)')
    elif value <= 0:
        raise ValueError(f'{name_figure_attr} повинні(о) бути більше 0')

def validate_correct_triangle_sides(a,b,c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError(
            f"Неможливо створити трикутник зі сторонами a={a}, b={b}, c={c}: "
            "сума довжин будь-яких двох сторін повинна бути більшою за третю."
        )
