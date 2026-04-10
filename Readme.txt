| ID    | Nombre del Requisito             | Descripción                                                                                                                       | Tipo         | Prioridad |
| ----- | -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------- |
| RF01  | Registrar tarea                  | El sistema debe permitir registrar una nueva tarea ingresando título, descripción y estado.                                       | Funcional    | Alta      |
| RF02  | Consultar tareas                 | El sistema debe permitir visualizar todas las tareas almacenadas en la base de datos.                                             | Funcional    | Alta      |
| RF03  | Editar tarea                     | El sistema debe permitir modificar la información de una tarea existente.                                                         | Funcional    | Media     |
| RF04  | Eliminar tarea                   | El sistema debe permitir eliminar tareas registradas en la base de datos.                                                         | Funcional    | Media     |
| RF05  | Persistencia de datos            | El sistema debe almacenar la información en una base de datos relacional para evitar pérdida de datos al reiniciar el contenedor. | Funcional    | Alta      |
| RNF01 | Programación Orientada a Objetos | La aplicación debe desarrollarse utilizando clases, métodos y principios de programación orientada a objetos.                     | No Funcional | Alta      |
| RNF02 | Dockerización                    | La aplicación debe ejecutarse dentro de un contenedor Docker.                                                                     | No Funcional | Alta      |
| RNF03 | Uso de volúmenes                 | La aplicación debe utilizar volúmenes de Docker para garantizar persistencia de datos.                                            | No Funcional | Alta      |
| RNF04 | Base de datos relacional         | La aplicación debe conectarse a una base de datos relacional (ejemplo: SQLite, MySQL o PostgreSQL).                               | No Funcional | Alta      |
| RNF05 | Interfaz web simple              | La aplicación debe contar con una interfaz web básica para ingresar y visualizar información.                                     | No Funcional | Media     |
| RNF06 | Publicación en Docker Hub        | El contenedor debe ser publicado en Docker Hub para su despliegue.                                                                | No Funcional | Media     |
| RNF07 | Compatibilidad Linux             | La aplicación debe ejecutarse correctamente en un entorno Linux.                                                                  | No Funcional | Media     |

# Task Manager Lite

Simple CRUD application using:

- Flask
- MySQL
- Docker

## Run project

docker-compose up --build

Access:

http://localhost:5000