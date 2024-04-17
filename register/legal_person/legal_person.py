"""Module LegalPerson contains class LegalPerson, which represents a legal person
in the Slovak Republic. It contains all the necessary information."""


class LegalPerson:
    """Class LegalPerson represents a legal person in the Slovak Republic. It contains all the necessary information."""

    def __init__(self, name, location, type_of_business, ico, owner_struc, basic_info, representatives):
        """ Initialize.

        :param name: Name of the legal person.
        :param location: Location of the legal person.
        :param type_of_business: Type of business of the legal person.
        :param ico: Identification number of the legal person.
        :param owner_struc: Ownership structure of the legal person.
        :param basic_info: Basic information about the legal person.
        :param representatives: Information about the representatives of the legal person.
        """
        self.name = name
        self.location = location
        self.type_of_business = type_of_business
        self.ico = ico
        self.owner_struc = owner_struc
        self.basic_info = basic_info
        self.representatives = representatives

    def __str__(self):
        return f"PO(Meno: {self.name}, Sídlo: {self.location}, Typ podnikania: {self.type_of_business}," \
               f"IČO: {self.ico}, Vlastnícke štruktúry: {self.owner_struc}, Základné informácie: {self.basic_info}," \
               f"Údaje o zástupcoch: {self.representatives})"

    def validate_ico(self, register):
        """ Validate the identification number of the legal person.

        :param register: List of identification numbers of legal persons.
        :return: True if the identification number is valid, otherwise raise an exception.
        :raises TypeError: If the identification number is not an integer.
        :rtype: bool.
        """
        if not isinstance(self.ico, int):
            raise TypeError
        elif len([x for x in self.ico.split()]) != 8:
            raise ValueError
        elif self.ico in register:
            raise Exception
        return True

    def validate_name(self, register):
        """ Validate the name of the legal person.

        :param register: List of names of legal persons.
        :return: True if the name is valid, otherwise raise an exception.
        :rtype: bool.
        """

    def validate_location(self, register):
        """Validate the location of the legal person.

        :param register: List of locations of legal persons.
        :return: True if the location is valid, otherwise raise an exception.
        :rtype: bool.
        """

    def validate_type_of_business(self, register):
        """Validate the type of business of the legal person.

        :param register: List of types of business of legal persons.
        :return: True if the type of business is valid, otherwise raise an exception.
        :rtype: bool.
        """

    def validate_owner_struc(self, register):
        """Validate the ownership structure of the legal person.

        :param register: List of ownership structures of legal persons.
        :return: True if the ownership structure is valid, otherwise raise an exception.
        :rtype: bool.
        """

    def validate_basic_info(self, register):
        """Validate the basic information about the legal person.

        :param register: List of basic information about legal persons.
        :return: True if the basic information is valid, otherwise raise an exception.
        :rtype: bool.
        """

    def validate_representatives(self, register):
        """Validate the information about the representatives of the legal person.

        :param register: List of information about representatives of legal persons.
        :return: True if the information about the representatives is valid, otherwise raise an exception.
        :rtype: bool.
        """
