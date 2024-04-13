class PO:
    '''
    Implementácia právnickej osoby s povinnými vlastnosťami pre registráciu do OR.
    '''
    def __init__(self, name, location, type_of_business, ico, owner_struc, basic_info, representatives):
        '''
        name = Názov PO
        location = Sídlo PO
        type_of_business = Typ podnikania PO
        ico = IČO PO
        owner_struc = Vlastnícke štruktúry (V prípade A.S.)
        basic_info = Základné informácie o vzniku PO
        representatives = Údaje o zástupcoch PO
        '''
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

    def validate_ico(self, registerPO):
        if not isinstance(self.ico, int):
            raise TypeError
        elif len([x for x in self.ico.split()]) != 8:
            raise ValueError
        elif self.ico in registerPO:
            raise Exception
        return True

    def validate_name(self):
        ...

    def validate_location(self):
        ...

    def validate_type_of_business(self):
        ...

    def validate_owner_struc(self):
        ...

    def validate_basic_info(self):
        ...

    def validate_representatives(self):
        ...
