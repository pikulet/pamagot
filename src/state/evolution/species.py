from enum import Enum

class Gender(Enum):
    Male = 0
    Female = 1

class SpeciesType(Enum):
    Universal = 0
    Mame = 1
    Meme = 2
    Kuchi = 3

class Phase(Enum):
    Baby = 0
    Toddler = 1
    Teen = 2
    Adult = 3
    Elder = 4
    Special = 5

class Species:

    def __init__(self, name, species_type, phase, gender):
        self.__name = name
        self.__species_type = species_type
        self.__phase = phase
        self.__gender = gender

    @property
    def name(self):
        return self.__name

    @property
    def species_type(self):
        return self.__species_type

    @property
    def phase(self):
        return self.__phase

    @property
    def gender(self):
        return self.__gender

# baby
TsubutchiM = Species("Tsubutchi", SpeciesType.Universal, Phase.Baby, Gender.Male)
TsubutchiF = Species("Tsubutchi", SpeciesType.Universal, Phase.Baby, Gender.Female)

# toddler
HarutchiM = Species("Harutchi", SpeciesType.Universal, Phase.Toddler, Gender.Male)
HarutchiF = Species("Harutchi", SpeciesType.Universal, Phase.Toddler, Gender.Female)
PuchitchiM = Species("Harutchi", SpeciesType.Universal, Phase.Toddler, Gender.Male)
PuchitchiF = Species("Harutchi", SpeciesType.Universal, Phase.Toddler, Gender.Female)
MizutamatchiM = Species("Mizutamatchi", SpeciesType.Universal, Phase.Toddler, Gender.Male)
MizutamatchiF = Species("Mizutamatchi", SpeciesType.Universal, Phase.Toddler, Gender.Female)
MohitamatchiM = Species("Mohitamatchi", SpeciesType.Universal, Phase.Toddler, Gender.Male)
MohitamatchiF = Species("Mohitamatchi", SpeciesType.Universal, Phase.Toddler, Gender.Female)

# teen
Obotchi = Species("Obotchi", SpeciesType.Universal, Phase.Teen, Gender.Male)
Ojotchi = Species("Ojotchi", SpeciesType.Universal, Phase.Teen, Gender.Female)
Hawainotchi = Species("Hawainotchi", SpeciesType.Universal, Phase.Teen, Gender.Male)
Hawaikotchi = Species("Hawaikotchi", SpeciesType.Universal, Phase.Teen, Gender.Female)

YoungMametchi = Species("YoungMametchi", SpeciesType.Mame, Phase.Teen, Gender.Male)
YoungMimitchi = Species("YoungMimitchi", SpeciesType.Mame, Phase.Teen, Gender.Female)
YoungAndrotchi = Species("YoungAndrotchi", SpeciesType.Mame, Phase.Teen, Gender.Male)
Ringotchi = Species("Ringotchi", SpeciesType.Mame, Phase.Teen, Gender.Female)

Gourmetchi = Species("Gourmetchi", SpeciesType.Meme, Phase.Teen, Gender.Male)
YoungMemetchi = Species("YoungMemetchi", SpeciesType.Meme, Phase.Teen, Gender.Female)
Hinotamatchi = Species("Hinotamatchi", SpeciesType.Meme, Phase.Teen, Gender.Male)
Ichigotchi = Species("Ichigotchi", SpeciesType.Meme, Phase.Teen, Gender.Female)

YoungKuchipatchi = Species("YoungKuchipatchi", SpeciesType.Kuchi, Phase.Teen, Gender.Male)
YoungDorotchi = Species("YoungDorotchi", SpeciesType.Kuchi, Phase.Teen, Gender.Female)
Oniontchi = Species("Oniontchi", SpeciesType.Kuchi, Phase.Teen, Gender.Male)
Nikatchi = Species("Nikatchi", SpeciesType.Kuchi, Phase.Teen, Gender.Female)

# adult
Pyonchitchi = Species("Pyonchitchi", SpeciesType.Universal, Phase.Adult, Gender.Male)
Pyonkotchi = Species("Pyonkotchi", SpeciesType.Universal, Phase.Adult, Gender.Female)
Debatchi = Species("Debatchi", SpeciesType.Universal, Phase.Adult, Gender.Male)
Hanatchi = Species("Hanatchi", SpeciesType.Universal, Phase.Adult, Gender.Female)
Gozarutchi = Species("Gozarutchi", SpeciesType.Universal, Phase.Adult, Gender.Male)
Masktchi = Species("Masktchi", SpeciesType.Universal, Phase.Adult, Gender.Female)

Mametchi = Species("Mametchi", SpeciesType.Mame, Phase.Adult, Gender.Male)
Mimitchi = Species("Mimitchi", SpeciesType.Mame, Phase.Adult, Gender.Female)
Androtchi = Species("Androtchi", SpeciesType.Mame, Phase.Adult, Gender.Male)
Maidtchi = Species("Maidtchi", SpeciesType.Mame, Phase.Adult, Gender.Female)
Zukyutchi = Species("Zukyutchi", SpeciesType.Mame, Phase.Adult, Gender.Male)
Marotchi = Species("Marotchi", SpeciesType.Mame, Phase.Adult, Gender.Female)

Tosakatchi = Species("Tosakatchi", SpeciesType.Meme, Phase.Adult, Gender.Male)
Ponytchi = Species("Ponytchi", SpeciesType.Meme, Phase.Adult, Gender.Female)
Togetchi = Species("Togetchi", SpeciesType.Meme, Phase.Adult, Gender.Male)
Memetchi = Species("Memetchi", SpeciesType.Meme, Phase.Adult, Gender.Female)
Shimashimatchi = Species("Shimashimatchi", SpeciesType.Meme, Phase.Adult, Gender.Male)
Violetchi = Species("Violetchi", SpeciesType.Meme, Phase.Adult, Gender.Female)

Minotchi = Species("Minotchi", SpeciesType.Kuchi, Phase.Adult, Gender.Male)
Pukatchi = Species("Pukatchi", SpeciesType.Kuchi, Phase.Adult, Gender.Female)
Tarakotchi = Species("Tarakotchi", SpeciesType.Kuchi, Phase.Adult, Gender.Male)
Sebiretchi = Species("Sebiretchi", SpeciesType.Kuchi, Phase.Adult, Gender.Female)
Kuchipatchi = Species("Kuchipatchi", SpeciesType.Kuchi, Phase.Adult, Gender.Male)
Yattatchi = Species("Yattatchi", SpeciesType.Kuchi, Phase.Adult, Gender.Female)

# elder
Ojitchi = Species("Ojitchi", SpeciesType.Universal, Phase.Elder, Gender.Male)
Otokitchi = Species("Otokitchi", SpeciesType.Universal, Phase.Elder, Gender.Female)

# special
Oyajitchi = Species("Oyajitchi", SpeciesType.Universal, Phase.Special, Gender.Male)
Tensaitchi = Species("Tensaitchi", SpeciesType.Mame, Phase.Special, Gender.Male)
Makiko = Species("Makiko", SpeciesType.Meme, Phase.Special, Gender.Female)
Nonbiritchi = Species("Nonbiritchi", SpeciesType.Kuchi, Phase.Special, Gender.Male)