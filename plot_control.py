import json
import matplotlib.pyplot as plt
import pandas as pd
import argparse
import os
from pathlib import Path

def main():
    controlList = []
    result_path = ""
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file_path", required=True, help="path of the control json file")
    args = ap.parse_args()

    if args.file_path:
        if os.path.exists(args.file_path):
            # Read the file
            with open(args.file_path) as file:
                print("file reading starts")
                # Create the dictionary for each json object and add to a list
                for jsonObj in file:
                    controlDict = json.loads(jsonObj)
                    controlDict['timestamp'] = int(controlDict['timestamp'].strip("[]"))
                    controlList.append(controlDict)
            print("file reading ends")
        else:
            print("file path does not exist")

        df = pd.DataFrame(controlList)

        # Config the layout of subplots
        fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(16, 8))

        # Config each subplot
        df.plot(x='timestamp', y='speed', ax=axes[0][0], ylabel='km/h')
        df.plot(x='timestamp', y='steer', ax=axes[0][1], ylabel='rad')
        df.plot(x='timestamp', y='throttle', ax=axes[1][0])
        df.plot(x='timestamp', y='brake', ax=axes[1][1])

        # Save the plot back to the path of the control json file
        result_path = os.path.split(args.file_path)[0]

        plt.savefig(Path(result_path)/'control_plot.png')

        print("plot has been saved to {}\control_plot.png".format(result_path))
    else:
        print("please provide valid path to the control json file")

if __name__ == '__main__':

    try:
        main()

    except KeyboardInterrupt:
        print('\nPlotting cancelled by user. Bye!')
    except RuntimeError as e:
        print(e)