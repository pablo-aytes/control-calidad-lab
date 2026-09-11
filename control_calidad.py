# Lista de muestras de ejemplo con su id, reactivo y pureza (%)
muestras = [
    {"id": 1, "reactivo": "Etanol", "pureza": 97.5},
    {"id": 2, "reactivo": "Acido Clorhidrico", "pureza": 92.0},
    {"id": 3, "reactivo": "Metanol", "pureza": 95.0},
    {"id": 4, "reactivo": "Acetona", "pureza": 88.3},
    {"id": 5, "reactivo": "Cloroformo", "pureza": 99.1},
    {"id": 6, "reactivo": "Sulfato de Sodio", "pureza": "N/D"},
]


def evaluar_muestra(muestra):
    # Convertimos la pureza a numero antes de evaluarla, para detectar datos invalidos
    try:
        pureza = float(muestra["pureza"])
    except (TypeError, ValueError):
        return "ERROR"

    # La pureza debe estar dentro de un rango valido de 0 a 100
    if pureza < 0 or pureza > 100:
        return "ERROR"

    # Una muestra se aprueba si su pureza es mayor o igual a 95%
    if pureza >= 95:
        return "APROBADA"
    return "RECHAZADA"


def generar_reporte(muestras):
    # Encabezado del reporte en formato de tabla
    print(f"{'ID':<5}{'Reactivo':<20}{'Pureza (%)':<12}{'Resultado':<10}")
    print("-" * 47)

    aprobadas = 0
    rechazadas = 0
    errores = 0

    for muestra in muestras:
        resultado = evaluar_muestra(muestra)
        print(f"{muestra['id']:<5}{muestra['reactivo']:<20}{str(muestra['pureza']):<12}{resultado:<10}")

        if resultado == "APROBADA":
            aprobadas += 1
        elif resultado == "RECHAZADA":
            rechazadas += 1
        else:
            errores += 1

    # Resumen final del control de calidad
    print("-" * 47)
    print(f"Total de muestras: {len(muestras)}")
    print(f"Aprobadas: {aprobadas}")
    print(f"Rechazadas: {rechazadas}")
    print(f"Con error: {errores}")


if __name__ == "__main__":
    generar_reporte(muestras)
