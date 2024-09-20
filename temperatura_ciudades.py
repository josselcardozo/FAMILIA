 #Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 59},
            {"day": "Martes", "temp": 69},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 49},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 88},
            {"day": "Domingo", "temp": 90}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 36},
            {"day": "Martes", "temp": 70},
            {"day": "Miércoles", "temp": 73},
            {"day": "Jueves", "temp": 81},
            {"day": "Viernes", "temp": 77},
            {"day": "Sábado", "temp": 69},
            {"day": "Domingo", "temp": 53}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 72},
            {"day": "Martes", "temp": 89},
            {"day": "Miércoles", "temp": 85},
            {"day": "Jueves", "temp": 52},
            {"day": "Viernes", "temp": 88},
            {"day": "Sábado", "temp": 81},
            {"day": "Domingo", "temp": 65}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 77},
            {"day": "Martes", "temp": 88},
            {"day": "Miércoles", "temp": 90},
            {"day": "Jueves", "temp": 89},
            {"day": "Viernes", "temp": 74},
            {"day": "Sábado", "temp": 67},
            {"day": "Domingo", "temp": 91}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 42},
            {"day": "Martes", "temp": 54},
            {"day": "Miércoles", "temp": 78},
            {"day": "Jueves", "temp": 79},
            {"day": "Viernes", "temp": 77},
            {"day": "Sábado", "temp": 55},
            {"day": "Domingo", "temp": 89}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 93},
            {"day": "Martes", "temp": 96},
            {"day": "Miércoles", "temp": 60},
            {"day": "Jueves", "temp": 42},
            {"day": "Viernes", "temp": 65},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 81}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 61},
            {"day": "Martes", "temp": 65},
            {"day": "Miércoles", "temp": 78},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 76},
            {"day": "Sábado", "temp": 75},
            {"day": "Domingo", "temp": 84}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 66},
            {"day": "Martes", "temp": 61},
            {"day": "Miércoles", "temp": 69},
            {"day": "Jueves", "temp": 73},
            {"day": "Viernes", "temp": 76},
            {"day": "Sábado", "temp": 87},
            {"day": "Domingo", "temp": 80}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 80},
            {"day": "Martes", "temp": 82},
            {"day": "Miércoles", "temp": 84},
            {"day": "Jueves", "temp": 91},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 85},
            {"day": "Domingo", "temp": 82}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 79},
            {"day": "Martes", "temp": 71},
            {"day": "Miércoles", "temp": 73},
            {"day": "Jueves", "temp": 90},
            {"day": "Viernes", "temp": 77},
            {"day": "Sábado", "temp": 94},
            {"day": "Domingo", "temp": 81}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 81},
            {"day": "Martes", "temp": 93},
            {"day": "Miércoles", "temp": 95},
            {"day": "Jueves", "temp": 94},
            {"day": "Viernes", "temp": 89},
            {"day": "Sábado", "temp": 88},
            {"day": "Domingo", "temp": 85}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 98},
            {"day": "Martes", "temp": 80},
            {"day": "Miércoles", "temp": 92},
            {"day": "Jueves", "temp": 87},
            {"day": "Viernes", "temp": 82},
            {"day": "Sábado", "temp": 93},
            {"day": "Domingo", "temp": 80}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for i, ciudad in enumerate(temperaturas):
    for j, semana in enumerate(ciudad):
        suma = 0
        for dia in semana:
            suma += dia['temp']
        promedio = suma / len(semana)  # Promedio de la semana (7 días)
        print(f"Promedio de temperaturas para Ciudad {i+1}, Semana {j+1}: {promedio:.2f}")
