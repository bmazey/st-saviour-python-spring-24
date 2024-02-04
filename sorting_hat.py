class SortingHat:
    """the sorting hat"""
    def __init__(self, gryffindor: int, hufflepuff: int, ravenclaw: int, slytherin: int):
        self.houses = {
            'gryffindor': gryffindor,
            'hufflepuff': hufflepuff,
            'ravenclaw': ravenclaw,
            'slytherin': slytherin
        }

    def add(self, house: str) -> None:
        """adds a point to the provided house"""
        if house == 'gryffindor':
            self.houses['gryffindor'] = self.houses.get('gryffindor') + 1
        if house == 'hufflepuff':
            self.houses['hufflepuff'] = self.houses.get('hufflepuff') + 1
        if house == 'ravenclaw':
            self.houses['ravenclaw'] = self.houses.get('ravenclaw') + 1
        if house == 'slytherin':
            self.houses['slytherin'] = self.houses.get('slytherin') + 1

    def sort(self) -> str:
        """returns the first house with the highest score"""
        score = 0
        result = ''
        for house, points in self.houses.items():
            if points > score:
                result = house

        return result

    def clear(self) -> None:
        """resets all house points"""
        self.houses = {
            'gryffindor': 0,
            'hufflepuff': 0,
            'ravenclaw': 0,
            'slytherin': 0
        }
