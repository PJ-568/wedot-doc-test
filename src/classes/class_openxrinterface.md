github_url

:   hide

# OpenXRInterface {#class_OpenXRInterface}

**Inherits:** `XRInterface<class_XRInterface>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Our OpenXR interface.

::: {.rst-class}
classref-introduction-group
:::

## Description

The OpenXR interface allows Godot to interact with OpenXR runtimes and
make it possible to create XR experiences and games.

Due to the needs of OpenXR this interface works slightly different than
other plugin based XR interfaces. It needs to be initialized when Godot
starts. You need to enable OpenXR, settings for this can be found in
your games project settings under the XR heading. You do need to mark a
viewport for use with XR in order for Godot to know which render result
should be output to the headset.

::: {.rst-class}
classref-introduction-group
:::

## Tutorials

- `Setting up XR <../tutorials/xr/setting_up_xr>`{.interpreted-text
  role="doc"}

::: {.rst-class}
classref-reftable-group
:::

## Properties

||
||
||
||
||
||
||
||

::: {.rst-class}
classref-reftable-group
:::

## Methods

||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Signals

:::: {#class_OpenXRInterface_signal_instance_exiting}
::: {.rst-class}
classref-signal
:::
::::

**instance_exiting**()
`🔗<class_OpenXRInterface_signal_instance_exiting>`{.interpreted-text
role="ref"}

Informs our OpenXR instance is exiting.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInterface_signal_pose_recentered}
::: {.rst-class}
classref-signal
:::
::::

**pose_recentered**()
`🔗<class_OpenXRInterface_signal_pose_recentered>`{.interpreted-text
role="ref"}

Informs the user queued a recenter of the player position.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInterface_signal_refresh_rate_changed}
::: {.rst-class}
classref-signal
:::
::::

**refresh_rate_changed**(refresh_rate:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_OpenXRInterface_signal_refresh_rate_changed>`{.interpreted-text
role="ref"}

Informs the user the HMD refresh rate has changed.

\*\*Note:\*\* Only emitted if XR runtime supports the refresh rate
extension.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInterface_signal_session_begun}
::: {.rst-class}
classref-signal
:::
::::

**session_begun**()
`🔗<class_OpenXRInterface_signal_session_begun>`{.interpreted-text
role="ref"}

Informs our OpenXR session has been started.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInterface_signal_session_focussed}
::: {.rst-class}
classref-signal
:::
::::

**session_focussed**()
`🔗<class_OpenXRInterface_signal_session_focussed>`{.interpreted-text
role="ref"}

Informs our OpenXR session now has focus.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInterface_signal_session_loss_pending}
::: {.rst-class}
classref-signal
:::
::::

**session_loss_pending**()
`🔗<class_OpenXRInterface_signal_session_loss_pending>`{.interpreted-text
role="ref"}

Informs our OpenXR session is in the process of being lost.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInterface_signal_session_stopping}
::: {.rst-class}
classref-signal
:::
::::

**session_stopping**()
`🔗<class_OpenXRInterface_signal_session_stopping>`{.interpreted-text
role="ref"}

Informs our OpenXR session is stopping.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInterface_signal_session_visible}
::: {.rst-class}
classref-signal
:::
::::

**session_visible**()
`🔗<class_OpenXRInterface_signal_session_visible>`{.interpreted-text
role="ref"}

Informs our OpenXR session is now visible (output is being sent to the
HMD).

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Enumerations

:::: {#enum_OpenXRInterface_Hand}
::: {.rst-class}
classref-enumeration
:::
::::

enum **Hand**: `🔗<enum_OpenXRInterface_Hand>`{.interpreted-text
role="ref"}

:::: {#class_OpenXRInterface_constant_HAND_LEFT}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Hand<enum_OpenXRInterface_Hand>`{.interpreted-text role="ref"}
**HAND_LEFT** = `0`

Left hand.

:::: {#class_OpenXRInterface_constant_HAND_RIGHT}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Hand<enum_OpenXRInterface_Hand>`{.interpreted-text role="ref"}
**HAND_RIGHT** = `1`

Right hand.

:::: {#class_OpenXRInterface_constant_HAND_MAX}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Hand<enum_OpenXRInterface_Hand>`{.interpreted-text role="ref"}
**HAND_MAX** = `2`

Maximum value for the hand enum.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_OpenXRInterface_HandMotionRange}
::: {.rst-class}
classref-enumeration
:::
::::

enum **HandMotionRange**:
`🔗<enum_OpenXRInterface_HandMotionRange>`{.interpreted-text role="ref"}

:::: {#class_OpenXRInterface_constant_HAND_MOTION_RANGE_UNOBSTRUCTED}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandMotionRange<enum_OpenXRInterface_HandMotionRange>`{.interpreted-text
role="ref"} **HAND_MOTION_RANGE_UNOBSTRUCTED** = `0`

Full hand range, if user closes their hands, we make a full fist.

:::: {#class_OpenXRInterface_constant_HAND_MOTION_RANGE_CONFORM_TO_CONTROLLER}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandMotionRange<enum_OpenXRInterface_HandMotionRange>`{.interpreted-text
role="ref"} **HAND_MOTION_RANGE_CONFORM_TO_CONTROLLER** = `1`

Conform to controller, if user closes their hands, the tracked data
conforms to the shape of the controller.

:::: {#class_OpenXRInterface_constant_HAND_MOTION_RANGE_MAX}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandMotionRange<enum_OpenXRInterface_HandMotionRange>`{.interpreted-text
role="ref"} **HAND_MOTION_RANGE_MAX** = `2`

Maximum value for the motion range enum.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_OpenXRInterface_HandTrackedSource}
::: {.rst-class}
classref-enumeration
:::
::::

enum **HandTrackedSource**:
`🔗<enum_OpenXRInterface_HandTrackedSource>`{.interpreted-text
role="ref"}

:::: {#class_OpenXRInterface_constant_HAND_TRACKED_SOURCE_UNKNOWN}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandTrackedSource<enum_OpenXRInterface_HandTrackedSource>`{.interpreted-text
role="ref"} **HAND_TRACKED_SOURCE_UNKNOWN** = `0`

The source of hand tracking data is unknown (the extension is likely
unsupported).

:::: {#class_OpenXRInterface_constant_HAND_TRACKED_SOURCE_UNOBSTRUCTED}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandTrackedSource<enum_OpenXRInterface_HandTrackedSource>`{.interpreted-text
role="ref"} **HAND_TRACKED_SOURCE_UNOBSTRUCTED** = `1`

The source of hand tracking is unobstructed, this means that an accurate
method of hand tracking is used, e.g. optical hand tracking, data
gloves, etc.

:::: {#class_OpenXRInterface_constant_HAND_TRACKED_SOURCE_CONTROLLER}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandTrackedSource<enum_OpenXRInterface_HandTrackedSource>`{.interpreted-text
role="ref"} **HAND_TRACKED_SOURCE_CONTROLLER** = `2`

The source of hand tracking is a controller, bone positions are inferred
from controller inputs.

:::: {#class_OpenXRInterface_constant_HAND_TRACKED_SOURCE_MAX}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandTrackedSource<enum_OpenXRInterface_HandTrackedSource>`{.interpreted-text
role="ref"} **HAND_TRACKED_SOURCE_MAX** = `3`

Maximum value for the hand tracked source enum.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_OpenXRInterface_HandJoints}
::: {.rst-class}
classref-enumeration
:::
::::

enum **HandJoints**:
`🔗<enum_OpenXRInterface_HandJoints>`{.interpreted-text role="ref"}

:::: {#class_OpenXRInterface_constant_HAND_JOINT_PALM}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"} **HAND_JOINT_PALM** = `0`

Palm joint.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_WRIST}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"} **HAND_JOINT_WRIST** = `1`

Wrist joint.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_THUMB_METACARPAL}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"} **HAND_JOINT_THUMB_METACARPAL** = `2`

Thumb metacarpal joint.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_THUMB_PROXIMAL}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"} **HAND_JOINT_THUMB_PROXIMAL** = `3`

Thumb proximal joint.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_THUMB_DISTAL}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"} **HAND_JOINT_THUMB_DISTAL** = `4`

Thumb distal joint.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_THUMB_TIP}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"} **HAND_JOINT_THUMB_TIP** = `5`

Thumb tip joint.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_INDEX_METACARPAL}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"} **HAND_JOINT_INDEX_METACARPAL** = `6`

Index metacarpal joint.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_INDEX_PROXIMAL}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"} **HAND_JOINT_INDEX_PROXIMAL** = `7`

Index proximal joint.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_INDEX_INTERMEDIATE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"} **HAND_JOINT_INDEX_INTERMEDIATE** = `8`

Index intermediate joint.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_INDEX_DISTAL}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"} **HAND_JOINT_INDEX_DISTAL** = `9`

Index distal joint.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_INDEX_TIP}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"} **HAND_JOINT_INDEX_TIP** = `10`

Index tip joint.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_MIDDLE_METACARPAL}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"} **HAND_JOINT_MIDDLE_METACARPAL** = `11`

Middle metacarpal joint.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_MIDDLE_PROXIMAL}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"} **HAND_JOINT_MIDDLE_PROXIMAL** = `12`

Middle proximal joint.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_MIDDLE_INTERMEDIATE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"} **HAND_JOINT_MIDDLE_INTERMEDIATE** = `13`

Middle intermediate joint.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_MIDDLE_DISTAL}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"} **HAND_JOINT_MIDDLE_DISTAL** = `14`

Middle distal joint.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_MIDDLE_TIP}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"} **HAND_JOINT_MIDDLE_TIP** = `15`

Middle tip joint.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_RING_METACARPAL}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"} **HAND_JOINT_RING_METACARPAL** = `16`

Ring metacarpal joint.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_RING_PROXIMAL}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"} **HAND_JOINT_RING_PROXIMAL** = `17`

Ring proximal joint.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_RING_INTERMEDIATE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"} **HAND_JOINT_RING_INTERMEDIATE** = `18`

Ring intermediate joint.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_RING_DISTAL}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"} **HAND_JOINT_RING_DISTAL** = `19`

Ring distal joint.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_RING_TIP}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"} **HAND_JOINT_RING_TIP** = `20`

Ring tip joint.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_LITTLE_METACARPAL}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"} **HAND_JOINT_LITTLE_METACARPAL** = `21`

Little metacarpal joint.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_LITTLE_PROXIMAL}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"} **HAND_JOINT_LITTLE_PROXIMAL** = `22`

Little proximal joint.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_LITTLE_INTERMEDIATE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"} **HAND_JOINT_LITTLE_INTERMEDIATE** = `23`

Little intermediate joint.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_LITTLE_DISTAL}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"} **HAND_JOINT_LITTLE_DISTAL** = `24`

Little distal joint.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_LITTLE_TIP}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"} **HAND_JOINT_LITTLE_TIP** = `25`

Little tip joint.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_MAX}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"} **HAND_JOINT_MAX** = `26`

Maximum value for the hand joint enum.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_OpenXRInterface_HandJointFlags}
::: {.rst-class}
classref-enumeration
:::
::::

flags **HandJointFlags**:
`🔗<enum_OpenXRInterface_HandJointFlags>`{.interpreted-text role="ref"}

:::: {#class_OpenXRInterface_constant_HAND_JOINT_NONE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJointFlags<enum_OpenXRInterface_HandJointFlags>`{.interpreted-text
role="ref"} **HAND_JOINT_NONE** = `0`

No flags are set.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_ORIENTATION_VALID}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJointFlags<enum_OpenXRInterface_HandJointFlags>`{.interpreted-text
role="ref"} **HAND_JOINT_ORIENTATION_VALID** = `1`

If set, the orientation data is valid, otherwise, the orientation data
is unreliable and should not be used.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_ORIENTATION_TRACKED}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJointFlags<enum_OpenXRInterface_HandJointFlags>`{.interpreted-text
role="ref"} **HAND_JOINT_ORIENTATION_TRACKED** = `2`

If set, the orientation data comes from tracking data, otherwise, the
orientation data contains predicted data.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_POSITION_VALID}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJointFlags<enum_OpenXRInterface_HandJointFlags>`{.interpreted-text
role="ref"} **HAND_JOINT_POSITION_VALID** = `4`

If set, the positional data is valid, otherwise, the positional data is
unreliable and should not be used.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_POSITION_TRACKED}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJointFlags<enum_OpenXRInterface_HandJointFlags>`{.interpreted-text
role="ref"} **HAND_JOINT_POSITION_TRACKED** = `8`

If set, the positional data comes from tracking data, otherwise, the
positional data contains predicted data.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_LINEAR_VELOCITY_VALID}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJointFlags<enum_OpenXRInterface_HandJointFlags>`{.interpreted-text
role="ref"} **HAND_JOINT_LINEAR_VELOCITY_VALID** = `16`

If set, our linear velocity data is valid, otherwise, the linear
velocity data is unreliable and should not be used.

:::: {#class_OpenXRInterface_constant_HAND_JOINT_ANGULAR_VELOCITY_VALID}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandJointFlags<enum_OpenXRInterface_HandJointFlags>`{.interpreted-text
role="ref"} **HAND_JOINT_ANGULAR_VELOCITY_VALID** = `32`

If set, our angular velocity data is valid, otherwise, the angular
velocity data is unreliable and should not be used.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_OpenXRInterface_property_display_refresh_rate}
::: {.rst-class}
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**display_refresh_rate** = `0.0`
`🔗<class_OpenXRInterface_property_display_refresh_rate>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_display_refresh_rate**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_display_refresh_rate**()

The display refresh rate for the current HMD. Only functional if this
feature is supported by the OpenXR runtime and after the interface has
been initialized.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInterface_property_foveation_dynamic}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **foveation_dynamic** =
`false`
`🔗<class_OpenXRInterface_property_foveation_dynamic>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_foveation_dynamic**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_foveation_dynamic**()

Enable dynamic foveation adjustment, the interface must be initialized
before this is accessible. If enabled foveation will automatically
adjusted between low and
`foveation_level<class_OpenXRInterface_property_foveation_level>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Only works on compatibility renderer.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInterface_property_foveation_level}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **foveation_level** = `0`
`🔗<class_OpenXRInterface_property_foveation_level>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_foveation_level**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_foveation_level**()

Set foveation level from 0 (off) to 3 (high), the interface must be
initialized before this is accessible.

\*\*Note:\*\* Only works on compatibility renderer.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInterface_property_render_target_size_multiplier}
::: {.rst-class}
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**render_target_size_multiplier** = `1.0`
`🔗<class_OpenXRInterface_property_render_target_size_multiplier>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_render_target_size_multiplier**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_render_target_size_multiplier**()

The render size multiplier for the current HMD. Must be set before the
interface has been initialized.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInterface_property_vrs_min_radius}
::: {.rst-class}
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **vrs_min_radius** =
`20.0`
`🔗<class_OpenXRInterface_property_vrs_min_radius>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_vrs_min_radius**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_vrs_min_radius**()

The minimum radius around the focal point where full quality is
guaranteed if VRS is used as a percentage of screen size.

\*\*Note:\*\* Mobile and Forward+ renderers only. Requires
`Viewport.vrs_mode<class_Viewport_property_vrs_mode>`{.interpreted-text
role="ref"} to be set to
`Viewport.VRS_XR<class_Viewport_constant_VRS_XR>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInterface_property_vrs_strength}
::: {.rst-class}
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **vrs_strength** =
`1.0`
`🔗<class_OpenXRInterface_property_vrs_strength>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_vrs_strength**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_vrs_strength**()

The strength used to calculate the VRS density map. The greater this
value, the more noticeable VRS is. This improves performance at the cost
of quality.

\*\*Note:\*\* Mobile and Forward+ renderers only. Requires
`Viewport.vrs_mode<class_Viewport_property_vrs_mode>`{.interpreted-text
role="ref"} to be set to
`Viewport.VRS_XR<class_Viewport_constant_VRS_XR>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_OpenXRInterface_method_get_action_sets}
::: {.rst-class}
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **get_action_sets**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRInterface_method_get_action_sets>`{.interpreted-text
role="ref"}

Returns a list of action sets registered with Godot (loaded from the
action map at runtime).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInterface_method_get_available_display_refresh_rates}
::: {.rst-class}
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**get_available_display_refresh_rates**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRInterface_method_get_available_display_refresh_rates>`{.interpreted-text
role="ref"}

Returns display refresh rates supported by the current HMD. Only
returned if this feature is supported by the OpenXR runtime and after
the interface has been initialized.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInterface_method_get_hand_joint_angular_velocity}
::: {.rst-class}
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_hand_joint_angular_velocity**(hand:
`Hand<enum_OpenXRInterface_Hand>`{.interpreted-text role="ref"}, joint:
`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRInterface_method_get_hand_joint_angular_velocity>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`XRHandTracker.get_hand_joint_angular_velocity<class_XRHandTracker_method_get_hand_joint_angular_velocity>`{.interpreted-text
role="ref"} obtained from
`XRServer.get_tracker<class_XRServer_method_get_tracker>`{.interpreted-text
role="ref"} instead.

If handtracking is enabled, returns the angular velocity of a joint
(`joint`) of a hand (`hand`) as provided by OpenXR. This is relative to
`XROrigin3D<class_XROrigin3D>`{.interpreted-text role="ref"}!

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInterface_method_get_hand_joint_flags}
::: {.rst-class}
classref-method
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`HandJointFlags<enum_OpenXRInterface_HandJointFlags>`{.interpreted-text
role="ref"}\] **get_hand_joint_flags**(hand:
`Hand<enum_OpenXRInterface_Hand>`{.interpreted-text role="ref"}, joint:
`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRInterface_method_get_hand_joint_flags>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`XRHandTracker.get_hand_joint_flags<class_XRHandTracker_method_get_hand_joint_flags>`{.interpreted-text
role="ref"} obtained from
`XRServer.get_tracker<class_XRServer_method_get_tracker>`{.interpreted-text
role="ref"} instead.

If handtracking is enabled, returns flags that inform us of the validity
of the tracking data.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInterface_method_get_hand_joint_linear_velocity}
::: {.rst-class}
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_hand_joint_linear_velocity**(hand:
`Hand<enum_OpenXRInterface_Hand>`{.interpreted-text role="ref"}, joint:
`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRInterface_method_get_hand_joint_linear_velocity>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`XRHandTracker.get_hand_joint_linear_velocity<class_XRHandTracker_method_get_hand_joint_linear_velocity>`{.interpreted-text
role="ref"} obtained from
`XRServer.get_tracker<class_XRServer_method_get_tracker>`{.interpreted-text
role="ref"} instead.

If handtracking is enabled, returns the linear velocity of a joint
(`joint`) of a hand (`hand`) as provided by OpenXR. This is relative to
`XROrigin3D<class_XROrigin3D>`{.interpreted-text role="ref"} without
worldscale applied!

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInterface_method_get_hand_joint_position}
::: {.rst-class}
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_hand_joint_position**(hand:
`Hand<enum_OpenXRInterface_Hand>`{.interpreted-text role="ref"}, joint:
`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRInterface_method_get_hand_joint_position>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`XRHandTracker.get_hand_joint_transform<class_XRHandTracker_method_get_hand_joint_transform>`{.interpreted-text
role="ref"} obtained from
`XRServer.get_tracker<class_XRServer_method_get_tracker>`{.interpreted-text
role="ref"} instead.

If handtracking is enabled, returns the position of a joint (`joint`) of
a hand (`hand`) as provided by OpenXR. This is relative to
`XROrigin3D<class_XROrigin3D>`{.interpreted-text role="ref"} without
worldscale applied!

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInterface_method_get_hand_joint_radius}
::: {.rst-class}
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_hand_joint_radius**(hand:
`Hand<enum_OpenXRInterface_Hand>`{.interpreted-text role="ref"}, joint:
`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRInterface_method_get_hand_joint_radius>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`XRHandTracker.get_hand_joint_radius<class_XRHandTracker_method_get_hand_joint_radius>`{.interpreted-text
role="ref"} obtained from
`XRServer.get_tracker<class_XRServer_method_get_tracker>`{.interpreted-text
role="ref"} instead.

If handtracking is enabled, returns the radius of a joint (`joint`) of a
hand (`hand`) as provided by OpenXR. This is without worldscale applied!

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInterface_method_get_hand_joint_rotation}
::: {.rst-class}
classref-method
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
**get_hand_joint_rotation**(hand:
`Hand<enum_OpenXRInterface_Hand>`{.interpreted-text role="ref"}, joint:
`HandJoints<enum_OpenXRInterface_HandJoints>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRInterface_method_get_hand_joint_rotation>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`XRHandTracker.get_hand_joint_transform<class_XRHandTracker_method_get_hand_joint_transform>`{.interpreted-text
role="ref"} obtained from
`XRServer.get_tracker<class_XRServer_method_get_tracker>`{.interpreted-text
role="ref"} instead.

If handtracking is enabled, returns the rotation of a joint (`joint`) of
a hand (`hand`) as provided by OpenXR.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInterface_method_get_hand_tracking_source}
::: {.rst-class}
classref-method
:::
::::

`HandTrackedSource<enum_OpenXRInterface_HandTrackedSource>`{.interpreted-text
role="ref"} **get_hand_tracking_source**(hand:
`Hand<enum_OpenXRInterface_Hand>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRInterface_method_get_hand_tracking_source>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`XRHandTracker.hand_tracking_source<class_XRHandTracker_property_hand_tracking_source>`{.interpreted-text
role="ref"} obtained from
`XRServer.get_tracker<class_XRServer_method_get_tracker>`{.interpreted-text
role="ref"} instead.

If handtracking is enabled and hand tracking source is supported, gets
the source of the hand tracking data for `hand`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInterface_method_get_motion_range}
::: {.rst-class}
classref-method
:::
::::

`HandMotionRange<enum_OpenXRInterface_HandMotionRange>`{.interpreted-text
role="ref"} **get_motion_range**(hand:
`Hand<enum_OpenXRInterface_Hand>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRInterface_method_get_motion_range>`{.interpreted-text
role="ref"}

If handtracking is enabled and motion range is supported, gets the
currently configured motion range for `hand`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInterface_method_is_action_set_active}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_action_set_active**(name: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRInterface_method_is_action_set_active>`{.interpreted-text
role="ref"}

Returns `true` if the given action set is active.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInterface_method_is_eye_gaze_interaction_supported}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_eye_gaze_interaction_supported**()
`🔗<class_OpenXRInterface_method_is_eye_gaze_interaction_supported>`{.interpreted-text
role="ref"}

Returns the capabilities of the eye gaze interaction extension.

\*\*Note:\*\* This only returns a valid value after OpenXR has been
initialized.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInterface_method_is_foveation_supported}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_foveation_supported**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRInterface_method_is_foveation_supported>`{.interpreted-text
role="ref"}

Returns `true` if OpenXR\'s foveation extension is supported, the
interface must be initialized before this returns a valid value.

\*\*Note:\*\* This feature is only available on the compatibility
renderer and currently only available on some stand alone headsets. For
Vulkan set
`Viewport.vrs_mode<class_Viewport_property_vrs_mode>`{.interpreted-text
role="ref"} to `VRS_XR` on desktop.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInterface_method_is_hand_interaction_supported}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_hand_interaction_supported**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRInterface_method_is_hand_interaction_supported>`{.interpreted-text
role="ref"}

Returns `true` if OpenXR\'s hand interaction profile is supported and
enabled.

\*\*Note:\*\* This only returns a valid value after OpenXR has been
initialized.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInterface_method_is_hand_tracking_supported}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_hand_tracking_supported**()
`🔗<class_OpenXRInterface_method_is_hand_tracking_supported>`{.interpreted-text
role="ref"}

Returns `true` if OpenXR\'s hand tracking is supported and enabled.

\*\*Note:\*\* This only returns a valid value after OpenXR has been
initialized.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInterface_method_set_action_set_active}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_action_set_active**(name: `String<class_String>`{.interpreted-text
role="ref"}, active: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_OpenXRInterface_method_set_action_set_active>`{.interpreted-text
role="ref"}

Sets the given action set as active or inactive.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInterface_method_set_motion_range}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_motion_range**(hand:
`Hand<enum_OpenXRInterface_Hand>`{.interpreted-text role="ref"},
motion_range:
`HandMotionRange<enum_OpenXRInterface_HandMotionRange>`{.interpreted-text
role="ref"})
`🔗<class_OpenXRInterface_method_set_motion_range>`{.interpreted-text
role="ref"}

If handtracking is enabled and motion range is supported, sets the
currently configured motion range for `hand` to `motion_range`.
