from alerts import blink_alert
from printer import default_printer

def alert_if_critical(vitals, printer=default_printer, blinker=blink_alert):
    all_ok = True
    for vital in vitals:
        val, min_val, max_val = vital["value"], vital["min"], vital["max"]
        if val < min_val or val > max_val:
            printer(
                f"{vital['name']} out of range! "
                f"Value: {val} (Expected: {min_val} to {max_val})"
            )
            blinker()
            all_ok = False
    return all_ok

def vitals_ok(vitals, printer=default_printer, blinker=blink_alert):
    return alert_if_critical(vitals, printer, blinker)
