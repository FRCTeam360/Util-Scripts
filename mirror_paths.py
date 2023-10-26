# This script should mirror a list of path jsons and create a new path file 
# The mirrored path should also be on the other side of the field

# This is an example of a path json:
# {
#   "waypoints": [
#     {
#       "anchorPoint": {
#         "x": 1.470753655793026,
#         "y": 0.8
#       },
#       "prevControl": null,
#       "nextControl": {
#         "x": 2.470753655793027,
#         "y": 0.8
#       },
#       "holonomicAngle": 180.0,
#       "isReversal": false,
#       "velOverride": null,
#       "isLocked": false,
#       "isStopPoint": false,
#       "stopEvent": {
#         "names": [],
#         "executionBehavior": "parallel",
#         "waitBehavior": "none",
#         "waitTime": 0
#       }
#     },
#     {
#       "anchorPoint": {
#         "x": 3.86,
#         "y": 0.8
#       },
#       "prevControl": {
#         "x": 3.3749103335934914,
#         "y": 0.7922949173305678
#       },
#       "nextControl": {
#         "x": 4.345089666406508,
#         "y": 0.8077050826694323
#       },
#       "holonomicAngle": 180.0,
#       "isReversal": false,
#       "velOverride": 0.1,
#       "isLocked": false,
#       "isStopPoint": false,
#       "stopEvent": {
#         "names": [],
#         "executionBehavior": "parallel",
#         "waitBehavior": "none",
#         "waitTime": 0
#       }
#     },
#     {
#       "anchorPoint": {
#         "x": 6.7,
#         "y": 1.17
#       },
#       "prevControl": {
#         "x": 6.623146703436264,
#         "y": 1.1685019412895963
#       },
#       "nextControl": {
#         "x": 6.776853296563736,
#         "y": 1.1714980587104036
#       },
#       "holonomicAngle": 180.0,
#       "isReversal": false,
#       "velOverride": null,
#       "isLocked": false,
#       "isStopPoint": true,
#       "stopEvent": {
#         "names": [],
#         "executionBehavior": "parallel",
#         "waitBehavior": "none",
#         "waitTime": 0
#       }
#     },
#     {
#       "anchorPoint": {
#         "x": 6.169129603216471,
#         "y": 2.089707769159128
#       },
#       "prevControl": {
#         "x": 6.572991449890104,
#         "y": 1.4456029139347664
#       },
#       "nextControl": {
#         "x": 5.765267756542839,
#         "y": 2.73381262438349
#       },
#       "holonomicAngle": 160.0,
#       "isReversal": false,
#       "velOverride": null,
#       "isLocked": false,
#       "isStopPoint": false,
#       "stopEvent": {
#         "names": [],
#         "executionBehavior": "parallel",
#         "waitBehavior": "none",
#         "waitTime": 0
#       }
#     },
#     {
#       "anchorPoint": {
#         "x": 5.075808647857897,
#         "y": 2.69
#       },
#       "prevControl": {
#         "x": 5.4073079574730585,
#         "y": 2.6598636991258937
#       },
#       "nextControl": {
#         "x": 4.745343498745834,
#         "y": 2.7200422862829154
#       },
#       "holonomicAngle": 160.0,
#       "isReversal": false,
#       "velOverride": 0.05,
#       "isLocked": false,
#       "isStopPoint": false,
#       "stopEvent": {
#         "names": [],
#         "executionBehavior": "parallel",
#         "waitBehavior": "none",
#         "waitTime": 0
#       }
#     },
#     {
#       "anchorPoint": {
#         "x": 3.5,
#         "y": 2.694923680445652
#       },
#       "prevControl": {
#         "x": 4.858881008360308,
#         "y": 2.694923680445652
#       },
#       "nextControl": null,
#       "holonomicAngle": 160.0,
#       "isReversal": false,
#       "velOverride": null,
#       "isLocked": false,
#       "isStopPoint": false,
#       "stopEvent": {
#         "names": [],
#         "executionBehavior": "parallel",
#         "waitBehavior": "none",
#         "waitTime": 0
#       }
#     }
#   ],
#   "markers": []
# }

# The fields' dimensions are 802cm x 1654cm
# The field's origin is at the bottom left corner
# The field's x-axis is the long side of the field
# The field's y-axis is the short side of the field


import json
import math
import os
import sys

# Begin by taking the comma separated list of path jsons as a command line argument
if len(sys.argv) != 2:
    print("Usage: python mirror_paths.py <comma separated list of path jsons>")
    sys.exit(1)

# Get the list of path jsons
path_jsons = sys.argv[1].split(",")
print("Path jsons: " + str(path_jsons))

# For each path json, load it and mirror it
for path_json in path_jsons:
    # Load the path json
    with open(path_json, "r") as f:
        path = json.load(f)

    # Mirror the path
    for waypoint in path["waypoints"]:
        # Mirror the anchor point
        waypoint["anchorPoint"]["x"] = 16.54 - waypoint["anchorPoint"]["x"]

        # Mirror the prev control point
        if waypoint["prevControl"] is not None:
            waypoint["prevControl"]["x"] = 16.54 - waypoint["prevControl"]["x"]

        # Mirror the next control point
        if waypoint["nextControl"] is not None:
            waypoint["nextControl"]["x"] = 16.54 - waypoint["nextControl"]["x"]

        # Mirror the holonomic angle
        waypoint["holonomicAngle"] = 360.0 - waypoint["holonomicAngle"]

    # Save the mirrored path
    mirrored_path_json = os.path.splitext(path_json)[0] + "_mirrored.path"
    with open(mirrored_path_json, "w") as f:
        json.dump(path, f, indent=2)