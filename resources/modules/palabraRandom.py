import random


def palabra_elegida():
    palabras = ['hola', 'amor', 'felicidad', 'casa', 'perro', 'gato', 'comida', 'agua', 'sol', 'luna', 'estrellas',
                'playa', 'bosque', 'aire', 'viento', 'tierra', 'fuego', 'trabajo', 'familia',
                'amigos', 'salud', 'dinero', 'viaje', 'coche', 'barco', 'tren', 'bicicleta', 'libro', 
                'arte', 'cine', 'teatro', 'fiesta', 'deporte', 'zapatos', 'moda', 'belleza', 'suero', 
                'tristeza', 'esperanza', 'risa', 'risas', 'palabra', 'silencio', 'naturaleza', 'amistad',
                'beso', 'abrazo', 'calle', 'ciudad', 'universo', 'misterio', 'aventura', 'viaje', 'magia',
                'reloj', 'tiempo', 'historia', 'cultura', 'despertar', 'amanecer', 'anochecer', 'pasado',
                'presente', 'futuro', 'calor', 'dulce', 'amargo', 'color', 'blanco', 'negro', 'rojo', 'azul',
                'verde', 'amarillo', 'feliz', 'triste', 'esperanza', 'paciencia', 'cuidado', 'respeto', 'gratitud',
                'libertad', 'justicia', 'paz', 'felino', 'canino', 'arbol', 'planta', 'mar', 'nube', 'cascada',
                'lluvia', 'nieve', 'primavera', 'verano', 'invierno', 'nacimiento', 'muerte', 'amoroso', 'valiente',
                'generoso', 'humilde', 'inteligente', 'amable', 'fuerte', 'creativo', 'sincero', 'curioso', 'honesto',
                'agradecido', 'estudiante', 'profesor', 'enfermero', 'abogado', 'artista', 'escritor',
                'actor', 'cantante', 'sonrisa', 'abrazo', 'cuento', 'ciencia', 'medicina', 'justicia', 'paz',
                'aventura', 'progreso', 'esperanza', 'felicidad', 'plenitud', 'soledad', 'aprendizaje',
                'resiliencia', 'liderazgo', 'paciencia', 'fracaso', 'serenidad', 'cambio', 'equilibrio', 'sonido',
                'silencio', 'sonar', 'imaginar', 'descubrir', 'explorar', 'desafiar', 'crecer', 'transformar',
                'celebrar', 'amar', 'vivir']

    return random.choice(palabras)
