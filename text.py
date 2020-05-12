# text.py
# -*- coding: utf-8 -*-
#
# The python script in this file makes the various parts of a model planisphere.
#
# Copyright (C) 2014-2020 Dominic Ford <dcf21-www@dcford.org.uk>
#
# This code is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# You should have received a copy of the GNU General Public License along with
# this file; if not, write to the Free Software Foundation, Inc., 51 Franklin
# Street, Fifth Floor, Boston, MA  02110-1301, USA

# ----------------------------------------------------------------------------

# A list of text strings, which we can render in various languages

text = {
    "en":
        {
            "title": "PLANISPHERE",
            "instructions_1": "Turn the starwheel until you find the point around its edge where today's date is marked, and line this point up with the current time. The viewing window now shows all of the constellations that are visible in the sky.",
            "instructions_2": "Go outside and face {cardinal}. Holding the planisphere up to the sky, the stars marked at the bottom of the viewing window should match up with those that you see in the sky in front of you.",
            "instructions_3": """Turn to face east or west, and rotate the planisphere so that the word "East" or "West" is at the bottom of the window. Once again, the stars at the bottom of the viewing window should match up with those that you see in the sky in front of you.""",
            "instructions_4": (
                r"A planisphere is a simple hand-held device which shows a map of which stars are visible in the night sky at any particular time. By rotating the star wheel, it shows how stars move across the sky through the night, and how different constellations are visible at different times of year.",
                "",
                r"The constellations of the night sky revolve around the celestial poles once every 23 hour and 56 minutes. The idea of representing the night sky as a flat map, which is turned to emulate the night sky's rotation, dated back to the ancient Greek astronomer Hipparchus (circa 150 BC). The fact that this rotation takes four minutes less than the length of a day means that stars rise four minutes earlier each day, or half-an-hour earlier each week. Through the year, new constellations become visible in the pre-dawn sky, and disappear into evening twilight."),
            "more_info": "For more information, see https://in-the-sky.org/planisphere       \u00A9 Dominic Ford 2020.",
            "glue_here": "GLUE HERE",
            "cut_out_instructions": (
                "Cut out this shaded area with scissors.",
                "",
                "It will become a viewing window through which to look at the star wheel behind."
            ),
            "cardinal_points": {"n": "NORTH", "s": "SOUTH", "w": "WEST", "e": "EAST"},
            "months": [
                [31, "JANUARY"],
                [28, "FEBRUARY"],
                [31, "MARCH"],
                [30, "APRIL"],
                [31, "MAY"],
                [30, "JUNE"],
                [31, "JULY"],
                [31, "AUGUST"],
                [30, "SEPTEMBER"],
                [31, "OCTOBER"],
                [30, "NOVEMBER"],
                [31, "DECEMBER"]
            ],
            "constellation_translations": {
            }
        },
    "mn":
        {
            "title": "ПЛАНИСФЕР",
            "instructions_1": "Оддын дугуйг аажмаар эргүүлэн өнөөдрийн огноог одоогийн цагтай харгалдаа байрлуулбал яг одоо тэнгэрт ямар одод байгаа нь оддын цонхоор харагдана.",
            "instructions_2": "Планисферийн цонхны доод захаар харагдаж байгаа одод умард зүгийн тэнгэрт байгаа ододтой таарах ёстой.",
            "instructions_3": """Одоо планисферээ бага зэрэг эргүүлэн “Өрнө” эсвэл “Дорно” гэсэн бичгийг доод талд нь гарга. Тэгвэл өмнөхтэй адилаар планисферийн цонхны доод захаар харагдаж байгаа одод баруун эсвэл зүүн зүгийн тэнгэрт байгаа ододтой таарах ёстой.""",
            "instructions_4": (
                r"Планисфер нь өгөгдсөн агшинд шөнийн тэнгэрт ямар одод харагдахыг дүрсэлж үзүүлдэг хялбар багаж юм. Оддын дугуйг эргүүлэн шөнийн турш тэнгэр дээгүүр одод хэрхэн хөдөлдгийг, улирлаас хамааран жилийн турш шөнө харагдах одод хэрхэн өөрчлөгддөгийг алган дээрээ тавьсан мэт хараарай.",
                "",
                r"Одот тэнгэр туйлуудаа 23 цаг 56 минутад нэг бүтэн тойрдог. Шөнийн тэнгэрийг хавтгай зураг болгон дүрслээд, хоногийн эргэлтийнх нь оронд зургаа эргүүлэх санаа нь МЭӨ 150 оны үеийн эртний Грекийн агуу одон оронч Гиппархын нээлт юм. Оддын эргэлтийн үе 24 цаг хүрэхгүй, 4 минут дутуу байгаагаас болоод одод хоног бүр 4 минутаар, сар бүр 2 цагаар  эрт манддаг. Тэгэхээр жишээ нь яг шөнө дунд орой дээр гарах одод жилийн турш аажмаар солигдох ба жил бүр яг энэ дараалал нь давтагдана."),
            "more_info": "\u00A9 Доминик Форд 2020.",
            "glue_here": "НААЛТ",
            "cut_out_instructions": (
                "Саарлаар будагдсан хэсгийг хайчилж ав.",
                "",
                "Ар талд байгаа оддын дугуйг энэ цонхоор харах юм."

            ),
            "cardinal_points": {"n": "УМАРД", "s": "ӨМНӨ", "w": "ӨРНӨ", "e": "ДОРНО"},
            "months": [
                [31, "1 сар"],
                [28, "2 сар"],
                [31, "3 сар"],
                [30, "4 сар"],
                [31, "5 сар"],
                [30, "6 сар"],
                [31, "7 сар"],
                [31, "8 сар"],
                [30, "9 сар"],
                [31, "10 сар"],
                [30, "11 сар"],
                [31, "12 сар"],
            ],
            "constellation_translations": {
                "Andromeda": "Адаг чуулган",
                "Antlia": "Luftpumpe",
                "Apus": "Paradiesvogel",
                "Aquarius": "Хумх",
                "Aquila": "Adler",
                "Ara": "Altar",
                "Aries": "Хонь",
                "Auriga": "Fuhrmann",
                "Boötes": "Bärenhüter",
                "Caelum": "Grabstichel",
                "Camelopardalis": "Giraffe",
                "Cancer": "Мэлхий",
                "Canes_Venatici": "Jagdhunde",
                "Canis_Major": "Großer_Hund",
                "Canis_Minor": "Kleiner_Hund",
                "Capricornus": "Steinbock",
                "Carina": "Kiel_des_Schiffs",
                "Cassiopeia": "Хүн таван од",
                "Centaurus": "Zentaur",
                "Cepheus": "Kepheus",
                "Cetus": "Walfisch",
                "Chamaeleon": "Chamäleon",
                "Circinus": "Zirkel",
                "Columba": "Taube",
                "Coma_Berenices": "Haar_der_Berenike",
                "Corona_Australis": "Südliche_Krone",
                "Corona_Borealis": "Nördliche_Krone",
                "Corvus": "Rabe",
                "Crater": "Becher",
                "Crux": "Kreuz_des_Südens",
                "Cygnus": "Schwan",
                "Delphinus": "Delphin",
                "Dorado": "Schwertfisch",
                "Draco": "Drache",
                "Equuleus": "Füllen",
                "Eridanus": "Eridanus",
                "Fornax": "Chemischer_Ofen",
                "Gemini": "Ихэр",
                "Grus": "Kranich",
                "Hercules": "Herkules",
                "Horologium": "Pendeluhr",
                "Hydra": "Wasserschlange",
                "Hydrus": "Kleine_Wasserschlange",
                "Indus": "Indianer",
                "Lacerta": "Eidechse",
                "Leo": "Арслан",
                "Leo_Minor": "Kleiner_Löwe",
                "Lepus": "Hase",
                "Libra": "Waage",
                "Lupus": "Wolf",
                "Lynx": "Luchs",
                "Lyra": "Leier",
                "Mensa": "Tafelberg",
                "Microscopium": "Mikroskop",
                "Monoceros": "Einhorn",
                "Musca": "Fliege",
                "Norma": "Winkelmaß",
                "Octans": "Oktant",
                "Ophiuchus": "Schlangenträger",
                "Orion": "Марал",
                "Pavo": "Pfau",
                "Pegasus": "Pegasus",
                "Perseus": "Perseus",
                "Phoenix": "Phönix",
                "Pictor": "Maler",
                "Pisces": "Загас",
                "Piscis_Austrinus": "Südlicher_Fisch",
                "Puppis": "Achterdeck_des_Schiffs",
                "Pyxis": "Schiffskompass",
                "Reticulum": "Netz",
                "Sagitta": "Pfeil",
                "Sagittarius": "Нум",
                "Scorpius": "Skorpion",
                "Sculptor": "Bildhauer",
                "Scutum": "Schild",
                "Serpens": "Schlange",
                "Sextans": "Sextant",
                "Taurus": "Үхэр",
                "Telescopium": "Teleskop",
                "Triangulum": "Dreieck",
                "Triangulum_Australe": "Südliches_Dreieck",
                "Tucana": "Tukan",
                "Ursa_Major": "Долоон бурхан",
                "Ursa_Minor": "Алтан мөнгөн шарга",
                "Vela": "Segel_des_Schiffs",
                "Virgo": "Jungfrau",
                "Volans": "Fliegender_Fisch",
                "Vulpecula": "Fuchs",
            }
        }
}
