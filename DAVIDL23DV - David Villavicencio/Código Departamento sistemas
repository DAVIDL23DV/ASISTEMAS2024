import random

# Definición de preguntas y recomendaciones
cuestionario = {
    "Gestión de Acceso": [
        "¿Existe una política documentada de gestión de acceso que defina los niveles de acceso para diferentes roles dentro de la organización?",
        "¿Se revisan y actualizan regularmente las cuentas de usuario y sus privilegios de acceso?",
        "¿Se utilizan mecanismos de autenticación robustos, como contraseñas seguras, autenticación de dos factores o biometría?",
        "¿Existe un proceso formal para la creación, modificación y eliminación de cuentas de usuario?",
        "¿Se monitorean y registran los accesos a los sistemas de información de forma continua?"
    ],
    "Seguridad Física y Ambiental": [
        "¿Están protegidas las instalaciones críticas de TI contra accesos no autorizados mediante controles físicos adecuados?",
        "¿Existen medidas de protección contra desastres naturales, como sistemas de detección de incendios, sistemas de extinción y protección contra inundaciones?",
        "¿Se realiza un mantenimiento regular y pruebas de los sistemas de seguridad física y ambiental?",
        "¿Se llevan a cabo controles de acceso físico mediante sistemas de identificación y vigilancia?",
        "¿Están documentados y en vigor los procedimientos para la seguridad física de las instalaciones?"
    ],
    "Gestión de Comunicaciones y Operaciones": [
        "¿Existen procedimientos documentados para la gestión de las operaciones diarias de TI?",
        "¿Se gestionan y registran las configuraciones de red y sistemas de manera controlada?",
        "¿Se implementan controles para asegurar la protección y la integridad de los datos durante su transmisión y almacenamiento?",
        "¿Se realizan copias de seguridad regulares de los datos críticos y se prueban para asegurar su recuperabilidad?",
        "¿Existen procedimientos para la gestión de cambios en los sistemas de TI que incluyen evaluación de riesgos y aprobación formal?"
    ],
    "Control de Acceso a la Información": [
        "¿Están claramente definidas y documentadas las políticas de control de acceso a la información?",
        "¿Se utilizan mecanismos de cifrado para proteger la información sensible en tránsito y en reposo?",
        "¿Se implementan controles para restringir el acceso a la información en función del principio de mínimo privilegio?",
        "¿Existen procedimientos para la clasificación y etiquetado de la información según su nivel de sensibilidad?",
        "¿Se revisan y actualizan regularmente los permisos de acceso a la información?"
    ],
    "Gestión de Incidentes de Seguridad de la Información": [
        "¿Existe un procedimiento documentado para la identificación, notificación y gestión de incidentes de seguridad de la información?",
        "¿Se dispone de un equipo de respuesta a incidentes capacitado y preparado para manejar diferentes tipos de incidentes?",
        "¿Se registran y analizan todos los incidentes de seguridad de la información para identificar tendencias y áreas de mejora?",
        "¿Se realizan pruebas y simulacros de respuesta a incidentes de seguridad de manera regular?",
        "¿Existen mecanismos para la comunicación y notificación de incidentes de seguridad a las partes interesadas pertinentes?"
    ]
}

# Extracción de recomendaciones de la guía (Ejemplos basados en ISO 27001)
recomendaciones_detalladas = {
    "Gestión de Acceso": [
        "Revisar y actualizar la política de gestión de acceso para asegurar que todos los niveles de acceso estén claramente definidos y documentados, alineados con las mejores prácticas de la industria.",
        "Implementar un proceso riguroso para la revisión regular de cuentas de usuario y privilegios de acceso, asegurando que solo el personal autorizado tenga acceso a los sistemas necesarios.",
        "Adoptar mecanismos de autenticación multifactor, como contraseñas seguras combinadas con autenticación biométrica o tokens de seguridad, para fortalecer la protección contra accesos no autorizados.",
        "Establecer procedimientos claros y formales para la creación, modificación y eliminación de cuentas de usuario, incluyendo la aprobación por parte de supervisores y la verificación de identidades.",
        "Implementar un sistema de monitoreo continuo y registro de accesos a los sistemas de información, utilizando herramientas avanzadas de análisis para detectar y responder a actividades sospechosas."
    ],
    "Seguridad Física y Ambiental": [
        "Implementar controles físicos robustos, como puertas de seguridad, cámaras de vigilancia y personal de seguridad, para proteger las instalaciones críticas de TI contra accesos no autorizados.",
        "Desarrollar y mantener un plan integral de protección contra desastres naturales, incluyendo sistemas avanzados de detección y extinción de incendios, así como medidas de protección contra inundaciones.",
        "Realizar mantenimiento regular y pruebas exhaustivas de todos los sistemas de seguridad física y ambiental, asegurando su correcto funcionamiento y eficacia en la protección de la infraestructura de TI.",
        "Utilizar sistemas avanzados de identificación y vigilancia para controlar el acceso físico a las instalaciones, garantizando que solo el personal autorizado pueda ingresar a áreas críticas.",
        "Documentar y mantener actualizados los procedimientos de seguridad física, asegurando que todos los empleados y contratistas estén informados y capacitados en las políticas de seguridad."
    ],
    "Gestión de Comunicaciones y Operaciones": [
        "Desarrollar y documentar procedimientos detallados para la gestión de las operaciones diarias de TI, asegurando que todos los procesos sean consistentes y alineados con las mejores prácticas.",
        "Implementar un sistema de gestión de configuraciones que controle y registre todas las configuraciones de red y sistemas, facilitando la identificación y resolución de problemas.",
        "Adoptar controles de seguridad para proteger la integridad y confidencialidad de los datos durante su transmisión y almacenamiento, utilizando tecnologías como cifrado y VPNs.",
        "Realizar copias de seguridad regulares de todos los datos críticos, almacenándolas en ubicaciones seguras y realizando pruebas periódicas para asegurar su recuperabilidad en caso de fallos.",
        "Establecer procedimientos formales para la gestión de cambios en los sistemas de TI, incluyendo evaluaciones de riesgos detalladas y aprobaciones formales por parte de la dirección."
    ],
    "Control de Acceso a la Información": [
        "Definir y documentar claramente las políticas de control de acceso a la información, asegurando que todos los empleados comprendan y sigan las directrices establecidas.",
        "Implementar mecanismos de cifrado robustos para proteger la información sensible tanto en tránsito como en reposo, utilizando estándares avanzados de criptografía.",
        "Adoptar controles estrictos para restringir el acceso a la información basándose en el principio de mínimo privilegio, asegurando que los usuarios solo tengan acceso a los datos necesarios para su trabajo.",
        "Establecer procedimientos para la clasificación y etiquetado de la información según su nivel de sensibilidad, facilitando la gestión y protección adecuada de los datos.",
        "Revisar y actualizar regularmente los permisos de acceso a la información, asegurando que solo el personal autorizado tenga acceso a los datos sensibles."
    ],
    "Gestión de Incidentes de Seguridad de la Información": [
        "Desarrollar y documentar un procedimiento exhaustivo para la identificación, notificación y gestión de incidentes de seguridad de la información, asegurando una respuesta rápida y eficaz.",
        "Formar y capacitar a un equipo de respuesta a incidentes, preparado para manejar una variedad de incidentes de seguridad y minimizar su impacto en la organización.",
        "Registrar y analizar todos los incidentes de seguridad de la información, utilizando los datos para identificar tendencias, áreas de mejora y prevenir futuros incidentes.",
        "Realizar pruebas y simulacros regulares de respuesta a incidentes de seguridad, evaluando la efectividad de los procedimientos y realizando ajustes según sea necesario.",
        "Establecer mecanismos claros para la comunicación y notificación de incidentes de seguridad a todas las partes interesadas pertinentes, asegurando una transparencia y coordinación eficaces."
    ]
}

recomendaciones_medias = {
    "Gestión de Acceso": [
        "Actualizar la política de gestión de acceso para incluir todos los niveles de acceso.",
        "Revisar regularmente las cuentas de usuario y privilegios de acceso.",
        "Implementar autenticación multifactor para mejorar la seguridad.",
        "Formalizar el proceso de gestión de cuentas de usuario.",
        "Monitorear y registrar los accesos de manera continua."
    ],
    "Seguridad Física y Ambiental": [
        "Mejorar los controles físicos en instalaciones críticas de TI.",
        "Establecer medidas contra desastres naturales como sistemas de detección de incendios.",
        "Realizar mantenimiento regular de sistemas de seguridad.",
        "Implementar sistemas de identificación y vigilancia para el acceso físico.",
        "Documentar procedimientos de seguridad física."
    ],
    "Gestión de Comunicaciones y Operaciones": [
        "Documentar procedimientos para la gestión de operaciones de TI.",
        "Registrar configuraciones de red y sistemas de manera controlada.",
        "Implementar controles para proteger datos en transmisión y almacenamiento.",
        "Realizar copias de seguridad regulares y probar su recuperabilidad.",
        "Establecer procedimientos formales de gestión de cambios en TI."
    ],
    "Control de Acceso a la Información": [
        "Definir y documentar políticas de control de acceso a la información.",
        "Utilizar cifrado para proteger información sensible.",
        "Aplicar el principio de mínimo privilegio para el acceso a la información.",
        "Clasificar y etiquetar la información según su sensibilidad.",
        "Actualizar regularmente los permisos de acceso a la información."
    ],
    "Gestión de Incidentes de Seguridad de la Información": [
        "Documentar procedimientos para la gestión de incidentes de seguridad.",
        "Formar un equipo de respuesta a incidentes.",
        "Registrar y analizar incidentes de seguridad.",
        "Realizar pruebas y simulacros de respuesta a incidentes.",
        "Establecer mecanismos de notificación de incidentes de seguridad."
    ]
}

# Función para valorar y proporcionar recomendaciones
def valorar_cuestionario():
    resultados = {}
    sumatoria = {}
    for categoria, preguntas in cuestionario.items():
        resultados[categoria] = {}
        sumatoria[categoria] = 0
        for i, pregunta in enumerate(preguntas):
            print(f"\n{pregunta}")
            valoracion = int(input("Valoración (1-5): "))
            resultados[categoria][pregunta] = valoracion
            sumatoria[categoria] += valoracion
            if valoracion == 1:
                print(f"Recomendación: {recomendaciones_detalladas[categoria][i]}")
            elif valoracion == 2:
                print(f"Recomendación: {recomendaciones_detalladas[categoria][i]}")
            elif valoracion == 3:
                print(f"Recomendación: {recomendaciones_detalladas[categoria][i]}")
            elif valoracion == 4:
                print(f"Recomendación: {recomendaciones_medias[categoria][i]}")
            else:
                print("No se requiere recomendación. Cumple y supera las expectativas.")

    return resultados, sumatoria

# Ejecutar valoración
resultados, sumatoria = valorar_cuestionario()

# Mostrar resultados finales
for categoria, valoraciones in resultados.items():
    print(f"\nCategoria: {categoria}")
    for pregunta, valoracion in valoraciones.items():
        print(f"{pregunta}: {valoracion}")

# Mostrar sumatoria de cada aspecto clave
print("\nSumatoria de cada aspecto clave:")
for categoria, total in sumatoria.items():
    print(f"{categoria}: {total}")

# Guardar resultados en un archivo
with open("resultados_valoracion.txt", "w") as file:
    for categoria, valoraciones in resultados.items():
        file.write(f"\nCategoria: {categoria}\n")
        for pregunta, valoracion in valoraciones.items():
            file.write(f"{pregunta}: {valoracion}\n")
    file.write("\nSumatoria de cada aspecto clave:\n")
    for categoria, total in sumatoria.items():
        file.write(f"{categoria}: {total}\n")
