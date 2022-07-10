"""Validator module."""
import re


class Validator:
    """Validator."""

    def validate_name_surname(self, name_surname: str):
        """Validates name and surname."""
        return bool(re.search("^[A-Z][a-z]{1,29}\s[A-Z][a-z]{1,29}$", name_surname))

    def validate_age(self, age: str):
        """Validates age."""
        return bool(re.search("^((1[6-9])|([2-9][0-9]))$", age))

    def validate_country(self, country: str):
        """Validates country."""
        return bool(re.search("^[A-Z][a-zA-z]{1,9}$", country))

    def validate_region(self, region: str):
        """Validates region."""
        return bool(re.search("^[A-Z]\w{1,9}$", region))

    def validate_living_place(self, living_place: str):
        """Validates living place."""
        return bool(
            re.search(
                "^[A-Z][a-zA-z]{2,19}\s((st.)|(av.)|(prosp.)|(rd.))\s\d[0-9a-z]$",
                living_place,
            )
        )

    def validate_index(self, index: str):
        """Validates index."""
        return bool(re.search("^\d{5}$", index))

    def validate_phone(self, phone: str):
        """Validates phone."""
        return bool(
            re.search("^\+((\d{9,12})|(\d{2}\s\(\d{3}\)\s\d{3}(-\d+){2}))$", phone)
        )

    def validate_email(self, email: str):
        """Validates email."""
        for _ in ["@.", ".@", ".."]:
            if _ in email:
                return False
        return bool(
            re.search(
                "^[^\s\.]\S{0,63}@[a-z\.]{1,255}\.(((com)|(org)|(edu)|(gov)|(net)|(ua))\.?)+$",
                email,
            )
        )

    def validate_id(self, id: str):
        """Validates id."""
        if id.count("0") != 1:
            return False
        return bool(re.search("^\d{6}$", id))

    def validate(self, data: str):
        """Validate function."""
        for _ in ["; ", ", ", ",", ";"]:
            temp = data.split(_)
            if len(temp) == 9:
                data = temp
                break
        for ind, _ in enumerate(
            [
                self.validate_name_surname,
                self.validate_age,
                self.validate_country,
                self.validate_region,
                self.validate_living_place,
                self.validate_index,
                self.validate_phone,
                self.validate_email,
                self.validate_id,
            ]
        ):
            if _(data[ind]) == False:
                return False
        return True
