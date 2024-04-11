# pruebaOOP
Descripción del Problema:
Estás encargado/a de desarrollar un programa para ayudar a los estudiantes a organizar sus actividades académicas. El
programa debe permitir a los usuarios agregar eventos importantes como exámenes, trabajos prácticos y reuniones
de estudio, y luego mostrar una lista de estos eventos en una agenda.
Requerimientos Funcionales:
1. Clases de Eventos:
• Define una clase base llamada Evento con los siguientes atributos y métodos:
• Atributos: fecha, descripcion
• Método __init__ para inicializar los atributos, tomando la fecha y la descripción como
argumentos.
• Método __str__ para representar el evento como una cadena de texto.

2. Clases Específicas de Eventos:
• Define clases hijas que hereden de la clase Evento, como Examen, TrabajoPractico, y
ReunionEstudio. Cada clase hija debe tener atributos y métodos específicos relacionados con el tipo
de evento.
3. Agenda:
• Define una clase Agenda que tenga una lista de eventos como atributo.
• Implementa métodos en la clase Agenda para agregar eventos, mostrar todos los eventos y eliminar
un evento por su descripción.

4. Interfaz de Usuario:
• Crea un programa principal donde importes las clases necesarias, crees una agenda, agregues varios
eventos de diferentes tipos, y luego muestres y elimines algunos eventos.

Requerimientos No Funcionales:
• El programa debe ser fácil de usar e intuitivo para los usuarios.
• Debe ser implementado en Python utilizando programación orientada a objetos.
Entrega:
• El código fuente del programa en archivos separados para cada clase.
• Documentación que explique la estructura del programa, cómo se utilizan las clases y cualquier decisión de
diseño importante.