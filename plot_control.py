import json
import matplotlib.pyplot as plt
import pandas as pd

controlList = []

print("File Reading Starts")
with open('control.json') as file:
    for jsonObj in file:
        controlDict = json.loads(jsonObj)
        controlDict['timestamp'] = int(controlDict['timestamp'].strip("[]"))
        controlList.append(controlDict)
print("File Reading Ends")

df = pd.DataFrame(controlList)

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(16, 8))

df.plot(x='timestamp', y='speed', ax=axes[0][0], ylabel='km/h')
df.plot(x='timestamp', y='steer', ax=axes[0][1], ylabel='rad')
df.plot(x='timestamp', y='throttle', ax=axes[1][0])
df.plot(x='timestamp', y='brake', ax=axes[1][1])

plt.savefig('control_plot.png')

print("Plot has been saved to control_plot.png")

# test1 = controlList[0]
# test2 = controlList[1]

# print(type(test1['timestamp']))

# print(f"Timestamp: {test1['timestamp']}, Speed: {test1['speed']}, Steer: {test1['steer']}, Throttle: {test1['throttle']}, Break: {test1['brake']}\n")

# print(f"Timestamp: {test2['timestamp']}, Speed: {test2['speed']}, Steer: {test2['steer']}, Throttle: {test2['throttle']}, Break: {test2['brake']}\n")