# OpenXR body tracking {#doc_openxr_body_tracking}

Support for full body tracking in OpenXR is only just becoming available
for a select few platforms. As support solidifies information will be
added to this page.

## HTC Tracker support

An option that has been available for some time is doing full body
tracking using HTC trackers. These are currently supported through
SteamVR and on HTC Elite XR headsets. They are exposed through the
action map system.

These trackers are identified by their roles which are assigned to them
when configured. Simply add
`XRController3D <class_xrcontroller3d>`{.interpreted-text role="ref"}
nodes as children to the
`XROrigin3D <class_xrorigin3d>`{.interpreted-text role="ref"} node and
assign one of the following trackers:

|                                              |
|----------------------------------------------|
| /user/vive_tracker_htcx/role/handheld_object |
| /user/vive_tracker_htcx/role/left_foot       |
| /user/vive_tracker_htcx/role/right_foot      |
| /user/vive_tracker_htcx/role/left_shoulder   |
| /user/vive_tracker_htcx/role/right_shoulder  |
| /user/vive_tracker_htcx/role/left_elbow      |
| /user/vive_tracker_htcx/role/right_elbow     |
| /user/vive_tracker_htcx/role/left_knee       |
| /user/vive_tracker_htcx/role/right_knee      |
| /user/vive_tracker_htcx/role/waist           |
| /user/vive_tracker_htcx/role/chest           |
| /user/vive_tracker_htcx/role/camera          |
| /user/vive_tracker_htcx/role/keyboard        |

HTC trackers

You can now use these as targets for IK modifiers on a full body avatar.
