from datetime import datetime

from constants import DATE_FORMATS

ERROR_TIMESTAMP = 'No valid date format found'
ERROR_VARCHAR = 'Too much value - {text} > {maximum_text}'
ERROR_COMMA_BEFORE = (
    'In the number before the dot - {number} > {maximum_number}'
)
ERROR_COMMA_AFTER = 'In the number after the dot - {number} > {maximum_number}'


class Parent:
    def __init__(self, null=False):
        self.null = null

    def checking_empty_field(self, variable, type_variable=str):
        """Валидация на разрешения пустых полей"""
        if self.null and not variable:
            return 'null'
        return type_variable(variable)


class Timestamp(Parent):
    """Поле времни"""

    def action(self, data):
        for date_formate in DATE_FORMATS:
            try:
                datetime.strptime(data, date_formate)
                return self.checking_empty_field(data)
            except ValueError:
                pass
        raise ValueError(ERROR_TIMESTAMP)


class Varchar(Parent):
    """Поле строки с ограничением"""

    def __init__(self, max_length, null=False):
        super().__init__(null)
        self.max_length = max_length

    def action(self, data):
        if len(data) > self.max_length:
            raise ValueError(ERROR_VARCHAR.format(
                text=len(data), maximum_text=self.max_length
            ))
        return self.checking_empty_field(data)


class Decimal(Parent):
    """Поле с плавающей запятой"""

    def __init__(self, comma_before, comma_after, null=False):
        super().__init__(null)
        self.comma_before = comma_before
        self.comma_after = comma_after

    def action(self, data):
        try:
            number_dot = self.checking_empty_field(data, float)
            if number_dot == 'null':
                return number_dot

            numbers = str(number_dot).split('.')
            if len(numbers[0]) > self.comma_before:
                raise ValueError(ERROR_COMMA_BEFORE.format(
                    number=len(numbers[0]), maximum_number=self.comma_before
                ))
            if len(numbers[1]) > self.comma_after:
                raise ValueError(
                    ERROR_COMMA_AFTER.format(
                        number=len(numbers[1]), maximum_number=self.comma_after
                    )
                )
        except IndexError:
            pass
        return number_dot


class Boolean(Parent):
    """Поле логического типа"""

    def action(self, data):
        return self.checking_empty_field(data, bool)


class Smallint(Parent):
    """Поле целочисленного числа"""

    def action(self, data):
        return self.checking_empty_field(data, int)


class Text(Parent):
    """Поле текст"""

    def action(self, data):
        return self.checking_empty_field(data)
