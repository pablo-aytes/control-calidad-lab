---
name: balance-materia
description: Resuelve balances de materia con reacción química siguiendo una metodología fija en 5 pasos (corrientes, reacción y masas molares, balances por componente, resolución del sistema, comprobación) y presenta el resultado en una tabla resumen. Úsala cuando el usuario pida resolver, plantear o revisar un balance de materia, balance de masa, balance estequiométrico o problema de proceso con reacción química.
---

# Balance de materia con reacción química

Esta skill enseña a resolver problemas de balance de materia con reacción química
de forma sistemática y verificable. Sigue siempre los 5 pasos en este orden, sin
saltarte ninguno, y termina con una tabla resumen. No presentes el resultado final
sin haber completado el paso de comprobación.

## Paso 1 — Identificar corrientes de entrada y salida

- Dibuja o describe el sistema como un diagrama de bloques (entrada(s) → proceso → salida(s)).
- Lista cada corriente con un nombre o número (ej. corriente 1, 2, 3...).
- Para cada corriente, indica qué componentes contiene y qué datos se conocen
  (caudal, masa, moles, fracción/porcentaje, si es conocido o incógnita).
- Define claramente la base de cálculo (por ejemplo, 100 kg de alimentación, o
  1 hora de operación) si el enunciado no la da explícitamente.
- Señala qué corrientes o composiciones son las incógnitas a resolver.

## Paso 2 — Plantear la reacción y las masas molares

- Escribe la ecuación química ajustada (balanceada), con sus coeficientes
  estequiométricos correctos.
- Calcula la masa molar (g/mol o kg/kmol) de cada compuesto que participa,
  usando los pesos atómicos.
- Si hay un reactivo limitante, identifícalo explícitamente comparando las
  relaciones estequiométricas con las cantidades alimentadas.
- Si se da un rendimiento, conversión o pureza, indícalo aquí y explica cómo
  se aplicará en los balances.

## Paso 3 — Plantear los balances de masa por componente

- Escribe un balance para cada especie química (y, si aplica, un balance
  global de masa total como verificación adicional):

  `Entrada + Generación − Consumo − Salida = Acumulación`

  En estado estacionario, Acumulación = 0.

- Expresa la generación y el consumo en función del avance de la reacción
  (extensión de reacción, ξ) y los coeficientes estequiométricos, o en
  función del reactivo limitante y la conversión, según convenga.
- Deja cada balance como una ecuación algebraica explícita con las incógnitas
  claramente identificadas.

## Paso 4 — Resolver el sistema de ecuaciones

- Cuenta el número de incógnitas y el número de ecuaciones independientes
  disponibles (balances por componente, balance global, datos de conversión
  o rendimiento, relaciones de composición). Verifica que el sistema esté
  determinado (grados de libertad = 0) antes de resolver.
- Resuelve el sistema paso a paso, mostrando el desarrollo algebraico
  (sustitución, eliminación, o el método que resulte más claro).
- Obtén los valores numéricos de todas las incógnitas (masas o moles de
  cada componente en cada corriente).

## Paso 5 — Verificar el resultado con un balance de comprobación

- Realiza un balance de comprobación independiente del cálculo principal,
  normalmente el balance de masa total (entrada total = salida total) o un
  balance atómico (por ejemplo, de un elemento que no reacciona o que se
  conserva, como el nitrógeno en muchos procesos de combustión).
- Compara el resultado de la comprobación con los datos originales y
  confirma que coincide (dentro de un margen de redondeo razonable).
- Si la comprobación no cierra, revisa los pasos anteriores antes de
  presentar el resultado: no continúes con un balance que no cuadra.

## Presentación del resultado final

Presenta siempre el resultado final en una **tabla resumen** con, como mínimo,
estas columnas:

| Corriente | Componente | Masa (o moles) | Fracción másica (o molar) | Caudal (si aplica) |
|---|---|---|---|---|

- Incluye una fila o total por cada corriente (entrada y salida).
- Añade, debajo de la tabla, una línea breve confirmando que el balance de
  comprobación cierra (ej. "Balance de comprobación: entrada = salida = X kg ✓").
- Si el proyecto en el que se usa esta skill requiere comentarios de código en
  español (como en este repositorio), cualquier código o script que acompañe
  la resolución (por ejemplo en Python) debe comentarse en español.
