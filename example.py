from datacapture import DataCapture

capture = DataCapture()
capture.add(2)
capture.add(7)
capture.add(2)
capture.add(2)
stats = capture.build_stats()

less_result = stats.less(4)
between_result = stats.between(3, 6)
greater_result = stats.greater(4)
print(f"numbers stored less than 4: {less_result}")
print(f"numbers stored between 3 and 6: {between_result}")
print(f"numbers stored greater than 4: {greater_result}")
