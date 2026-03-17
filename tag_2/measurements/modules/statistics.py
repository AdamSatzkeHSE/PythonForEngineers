def get_mean(measurements: list[float]):
    result = sum(measurements) / len(measurements)
    return result

def get_max(measurements: list[float]) -> float:
    """Funktion zur Berechnung der Maxima.

    Args:
        measurements (list[float]): Spannungswerte

    Returns:
        float: Maximalwert der Spannung
    """
    max_value = 0
    for value in measurements:
        if value > max_value:
            max_value = value

    return max_value

def get_min(measurements: list[float]):
    min_value = 1000
    for value in measurements:
        if value < min_value:
            min_value = value

    return min_value

def get_median(measurements: list[float]):
    sorted_values = sorted(measurements)
    print(sorted_values)

    if len(sorted_values) % 2 == 0:
        pass
    else:
        pass

# Wenn mein Modul das Hauptmodul ist, dann führe folgende Befehle aus.
if __name__ == "__main__":
    get_median([3, 7, 90, 1])