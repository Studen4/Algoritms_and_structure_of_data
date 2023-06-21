"""Module basic headphones data."""


class Headphones:
    """Class to represent headphones and classify them."""
    manufacturer: str
    model: str
    interface: str
    headphone_type: str
    min_frequency: int
    max_frequency: int

    def __init__(self, manufacturer: str, model: str, interface: str,
                 headphone_type: str, min_frequency: int, max_frequency: int) -> None:
        self.manufacturer = manufacturer
        self.model = model
        self.interface = interface
        self.headphone_type = headphone_type
        self.min_frequency = min_frequency
        self.max_frequency = max_frequency

    def __repr__(self):
        return f"Headphones({self.manufacturer}, {self.model}, " \
               f"{self.interface}, {self.headphone_type}" \
                f"{self.min_frequency}, {self.max_frequency})"

    def get_message(self) -> str:
        """Visual part of class."""
        if self.interface == "Bluetooth":
            interface_message = "wireless"
        else:
            interface_message = self.interface

        if self.min_frequency <= 40:
            if self.max_frequency >= 40000:
                message = "Feel the sound of HiFi with " \
                          f"{interface_message} {self.headphone_type} " \
                          f"{self.manufacturer} {self.model}"
            elif 20000 <= self.max_frequency < 40000:
                message = "Enjoy quality sound with " \
                          f"{interface_message} {self.headphone_type}" \
                          f" {self.manufacturer} {self.model}"
            elif self.min_frequency <= 30:
                message = "Hear the real bass with " \
                          f"{interface_message} {self.headphone_type}" \
                          f" {self.manufacturer} {self.model}"
            else:
                message = "Be in the rhythm of life with " \
                          f"{interface_message} {self.headphone_type} " \
                          f"{self.manufacturer} {self.model}"
        else:
            message = "Be in the rhythm of life with " \
                      f"{interface_message} {self.headphone_type}" \
                      f" {self.manufacturer} {self.model}"

        return message

    def get_info(self) -> str:
        """Function to get info for headphones."""
        return f"Headphones ({self.manufacturer} {self.model}) -" \
               f" {self.interface}, {self.headphone_type}"
