# Ejercicios_17-24

En esta actividad trabajaremos los siguientes siete ejercicios de la primera actividad del semestre, importante aclarar que utilizare la misma configuración del menú de la anterior actividad:

## Suma de los siguientes 100 números

"Escribir un programa en Python que lea un número entero desde teclado y realiza la suma de los 100 número siguientes, mostrando el resultado en pantalla."

Para hacer este ejercicio definimos a siguiente función:

![image](https://github.com/user-attachments/assets/99f943a5-10d0-49f4-a16a-d1c358c532a4)

En esta función tenemos as siguientes variables que exlicare brevemente:

##### Variable X:

Esta variable toma el valor del número entero que ingresemos por medio de la función input.

##### Variable conteo:

La utilizaremos para llevar el conteo de cuantas veces debe entrar al ciclo "while" es decir cuantas veces queremos que se repitan las operaciones que tenemos en el ciclo que en este caso son 100 veces.

##### Variable suma:

La definimos para llevar la suma de los cien números siguientes

#### Ejecución

Para comprar que este código funciona presento la ejecución:

![image](https://github.com/user-attachments/assets/6966919e-c56a-4a89-ba9b-bd6075af0aff)

## Convertir de euros a dolares

"Escribir un programa en Python que convierta de euros a dólares. Recibirá un número decimal correspondiente a la cantidad en euros y contestará con la cantidad correspondiente en dolares." 

Este ejercicio es muy sencillos pues o único que debe hacer es definir una función que multiplique el valor igresado de euros y os mutiplique por el factor de conversión que fluctúa en el valor de 1.1301, esto que dije se vera mejor mediante el siguiente código:

![image](https://github.com/user-attachments/assets/4ab91ea4-9ffa-4916-ac82-4ef97c92c176)

#### Ejecución

![image](https://github.com/user-attachments/assets/d59db357-6a89-4346-9bdd-0123edc743a8)

## Área rectángulo

"Escribir un programa en Python que calcule el área de un rectángulo del cual se le proporcionará por el teclado su altura y anchura (números decimales)."

Este ejercicio lo habíamos trabajado anteriormente impícitamente en el área de los sólidos, por lo tanto solo traje a este código la función solamente con la parte que calcula lo que necesitamos.

![image](https://github.com/user-attachments/assets/d4f9c9ca-2db2-48df-ba50-b13a0d3235dd)

#### Ejecución

![image](https://github.com/user-attachments/assets/0eb84750-6deb-4a58-b87e-e812d634294f)

## Menor y mayor entre dos números

"Escribir un programa en Python que lea dos números del teclado y diga cual es el mayor y cual el menor."

Para este ejercicio comparamos mediante el operador lógico "if" en donde sí a<b imprimirá en pantalla que a es el mayor y b el menor, por otro lado sí b<a pondrá lo contrario y como último sí a=b imprimirá que los valores son iguales.

![image](https://github.com/user-attachments/assets/8f9f38a7-74ac-464c-9a85-afea933fa97b)

#### Ejecución

![image](https://github.com/user-attachments/assets/138f4882-8a9b-4bf5-beaf-b412a1783be6)
![image](https://github.com/user-attachments/assets/0d20bee6-3aed-4c3a-a27c-557d70ec29b7)
![image](https://github.com/user-attachments/assets/e756486d-2df7-4bbe-aef6-b711ee75754f)

## Números impares menores que x

"Escribir un programa en Python que lea un número entero por el teclado e imprima todos los número impares menores que él."

En este ejercicio aplicaremos un "while" similar al utilizado en el ejercicio 1, dentro de este ciclo utilizaremos "if" para comparar los valores del rango y que solo imprima los impares mediante el modulo de 2, utilizaremos las siguientes vaiables:

##### Variable n:

Esta variable toma el valor del número entero que ingresemos por medio de la función input.

##### Variable rango:

La utilizaremos para plantear un rango desde el opuesto de n para que desde allí empiece a comparar el modiulo de dos en los números del rango en el operador lógico e imprima solo los impares.

![image](https://github.com/user-attachments/assets/718bcc91-96e1-44dd-acbf-099f19f35206)

#### Ejecución

![image](https://github.com/user-attachments/assets/0c1ef00d-d4e4-4388-9025-b15b4789c1a9)

## Algoritmo de Euclides

"Implemente el algoritmo de Euclides para encontrar el gcd de dos número leídos desde teclado."

Aunque parezca un ejercicio díficil se vuelve muy secillo al importar la biblioteca math que nos permeti ejectutar este algoritmo solo llamando math.gcd.

![image](https://github.com/user-attachments/assets/5299272d-3755-4a3f-b7b9-51d73280e16f)

#### Ejecución

![image](https://github.com/user-attachments/assets/3c28b945-34fb-4092-980a-9e3cf74746d8)

## Cuadratica

"Escriba un programa que lea los coeficientes a, b y c de una ecuación de segundo, y estudie si tiene o no solución. En caso positivo, las soluciones se calcularán e imprimirán en pantalla."

Afrontaremos la primer parte mediante el determinante b**2 - 4*a*c , donde el resultado de este determiante nos permitirá saber si tiene dos soluciones, una solución o no tiene soluciones reales, esto lo separaremos mediante el operador lógico "if" como se muestra en el código:

![image](https://github.com/user-attachments/assets/3bcfc6c4-184b-4897-854a-1871b53170ad)

#### Ejecución

![image](https://github.com/user-attachments/assets/501e1b55-ef60-4f8d-916e-151f17088268)
![image](https://github.com/user-attachments/assets/485da5b9-5fcf-4d70-a9bb-3975556c733f)
![image](https://github.com/user-attachments/assets/fa93918e-d087-4b35-a893-382b59bb843f)






