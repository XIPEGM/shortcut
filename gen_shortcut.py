# gen_distance.shortcut.py
import plistlib
import uuid

def loc(lat, lon):
    return {"WFLocationValue": {"Latitude": lat, "Longitude": lon}}

A = loc(24.453025, 118.032766)   # 点1 京口岩
B = loc(24.479800, 118.089400)   # 点2 厦门岛内某处

actions = [
    {
        "WFWorkflowActionIdentifier": "is.workflow.actions.getdistance",
        "WFWorkflowActionParameters": {
            "UUID": str(uuid.uuid4()).upper(),
            "WFGetDirectionsCustomLocation": A,
            "WFGetDistanceDestination": B,
            "WFGetDirectionsActionMode": "Direct",
            "WFDistanceUnit": "Kilometers",
            "Accuracy": "Best",
            "CustomOutputName": "距离"
        }
    },
    {
        "WFWorkflowActionIdentifier": "is.workflow.actions.showresult",
        "WFWorkflowActionParameters": {
            "UUID": str(uuid.uuid4()).upper(),
            "Text": "两点直线距离（公里）"
            # 想带出上一步结果，正式做法是用 token 引用上个 UUID，
            # 这里为极简先只显示文字；要带值见下方“token 写法”
        }
    }
]

shortcut = {
    "WFWorkflowClientVersion": "2612.0.4",
    "WFWorkflowMinimumClientVersion": 900,
    "WFWorkflowMinimumClientVersionString": "900",
    "WFWorkflowIcon": {
        "WFWorkflowIconStartColor": 4282601983,
        "WFWorkflowIconGlyphNumber": 61440
    },
    "WFWorkflowTypes": [],
    "WFWorkflowInputContentItemClasses": [],
    "WFWorkflowOutputContentItemClasses": [],
    "WFWorkflowImportQuestions": [],
    "WFWorkflowHasOutputFallback": False,
    "WFWorkflowActions": actions
}

with open("distance.shortcut", "wb") as f:
    plistlib.dump(shortcut, f)

print("已生成 distance.shortcut")
