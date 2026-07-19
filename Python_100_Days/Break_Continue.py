from Utilities import Logging_Report

for i in range(10):
    print("Multiplication Table of 5: ", 5 * i)
    Logging_Report.logger.info(f"Multiplication Table of 5: {5 * i}")
    if i == 5:
        Logging_Report.logger.info(f"Breaking the loop at i: {i}")
        break
    else:
        Logging_Report.logger.info(f"Continuing the loop at i: {i}")
        continue