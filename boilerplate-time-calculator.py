def add_time(start, duration):
    # Extrair a hora de início
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))

    # Extrair a duração
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Converter a hora de início em minutos
    total_start_minute = start_hour * 60 + start_minute

    # Calcular o novo horário adicionando a duração
    total_end_minutes = total_start_minute + duration_hour * 60 + duration_minute
    end_hour = (total_end_minutes // 60) % 24
    end_minute = total_end_minutes % 60

    # Determinar se é AM ou PM
    if end_hour < 12:
        new_period = "AM"
    else:
        new_period = "PM"

    # Converter para o formato de 12 horas
    if end_hour == 0:
        new_hour = 12
    elif end_hour > 12:
        new_hour = end_hour - 12
    else:
        new_hour = end_hour

    # Determinar o número de dias depois
    days_later = total_end_minutes // 1440

    new_time = f"{new_hour:02d}:{end_minute:02d} {new_period}"
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time


if __name__ == "__main__":
    print(add_time("11:06 PM", "2:02"))

    # Run unit tests automatically
    from boilerplate_time_calculator import test_add_time
    test_add_time()
