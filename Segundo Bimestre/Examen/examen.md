## Introducción

Para el proyecto, Sara y yo hemos creado "Retroplay", una tienda de videojuegos clásicos. Elegimos este tema porque a los dos nos gustan mucho los juegos retro y nos parecía una idea más interesante que la típica tienda online.

Trabajar juntos ha sido cómodo porque estamos cerca y tenemos buena comunicación. Siendo sincero, en este proyecto yo he participado un poco menos que ella; calcularía que el reparto de trabajo ha sido un 70% Sara y un 30% yo.

Sobre las herramientas, hemos usado PHP porque es el lenguaje que estamos aprendiendo en clase y creemos que es el más apto para este proyecto. También usamos HTML, CSS y JS para la para darle estructura y estilo a la web, y MySQL para gestionar los usuarios y los productos.

## Detalles del proyecto

1. Base de datos
- Primero hicimos la base de datos con mysql por consola. Creamos 4 tablas importantes: la tabla de usuarios, la de productos y la de reservas. Lo mas complicado fue la tabla `lineareservas`, que sirve para unir las reservas con los productos, ya que una sola reserva puede tener varios juegos diferentes y necesitabamos guardar eso bien.

2. Login y registro de usuarios
- Creamos un formulario de registro y de login, con el estilo retro y con un asteroide de fondo para que se vea mas interesante. 
- En el codigo php, usamos la funcion `password_hash` para encriptar la contraseña y que sea segura. Tambien usamos sentencias preparadas para evitar que nos hackeen la base de datos. Si el usuario se equivoca al entrar, le sale una alerta de error.

3. Inicio
- Esta es la pagina principal de la tienda luego de iniciar sesion. Aqui usamos un bucle en php para mostrar todos los productos que hay en la base de datos.
- Los dividimos en dos secciones: videojuegos y consolas. Ademas, pusimos un codigo para que si un juego no tiene imagen, salga una imagen por defecto (la del Nintendogs) para que la pagina no se vea fea o con errores.
- En la parte de arriba tenemos el menu para ir al carrito, al perfil o a mis reservas.

4. Carrito de compras
- Esta parte tiene su truco. Usamos Javascript y una cosa llamada `localStorage`. Esto sirve para guardar los productos en el navegador del usuario. Asi, si cambias de pagina, los productos siguen en el carrito y no se borran.
- Cuando le das a pagar, enviamos esa lista al php para que procese la compra.

5. Reservas
- Aqui se muestran todas las reservas que has hecho. Lo importante aqui es que al crear la reserva usamos "transacciones". Esto significa que el sistema intenta guardar la reserva y los productos a la vez, y si algo falla, no se guarda nada. Asi evitamos tener reservas a medias.
- Aun nos falta agregar el boton para cancelar una reserva.

6. Perfil
- Aqui se muestra el perfil del usuario, con su, correo, telefono y contraseña. Los datos los sacamos de la base de datos buscando por el ID del usuario conectado.
- Tambien hay un apartado donde puedes cambiar la contraseña

## Finalización
En conclusión, creo que el proyecto nos ha quedado bastante bien. Hemos conseguido hacer una tienda completa, donde puedes registrarte, ver productos, añadirlos al carrito y hacer la reserva de verdad guardándose en la base de datos.

Personalmente, me ha servido para entender mejor cómo se conectan todas las partes (el PHP, la base de datos y el HTML). Sé que nos faltan algunos detalles por pulir, como poder cancelar las reservas o terminar bien la parte de editar el perfil, pero la funcionalidad principal marcha bien y estamos contentos con el resultado.