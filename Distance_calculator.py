# -------------------------------------
# Import libraries
# -------------------------------------
import time

# -------------------------------------
# Constants
# -------------------------------------
KILOMETERS_PER_MILE = 1.60934

# -------------------------------------
# Global variables
# -------------------------------------
speedMilesPerHour = 0.0
seconds = 0
speedMetresPerSecond = 0.0
totalDistance = 0.0

# -------------------------------------
# Subprograms
# -------------------------------------
def convertToMPS(pMilesPerHour):
  speedKmPerHour = pMilesPerHour * KILOMETERS_PER_MILE
  speedMPerSecond = (speedKmPerHour * 1000) / (60 * 60)
  
  # ====> Return the speed in metres per second
  return (              )

# -------------------------------------
# Main program
# -------------------------------------
speedMilesPerHour = float(input("Enter car speed in miles per hour (e.g. 60)"))
seconds = int(input("How many seconds: (e.g. 10)"))

# ====> Call the user defined subprogram
speedMetresPerSecond =              (speedMilesPerHour)

totalDistance = 0
print("=" * 37)
print("| Time (s) | Distance travelled (m) |")
print("=" * 37)

for i in range(seconds + 1):
  print("|{:^10}|{:^24.2f}|".format(totalDistance, i))
  totalDistance += speedMetresPerSecond
  
print("=" * 37)
