github_url

:   hide

# OpenXRAPIExtension {#class_OpenXRAPIExtension}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Makes the OpenXR API available for GDExtension.

::: {.rst-class}
classref-introduction-group
:::

## Description

**OpenXRAPIExtension** makes OpenXR available for GDExtension. It
provides the OpenXR API to GDExtension through the
`get_instance_proc_addr<class_OpenXRAPIExtension_method_get_instance_proc_addr>`{.interpreted-text
role="ref"} method, and the OpenXR instance through
`get_instance<class_OpenXRAPIExtension_method_get_instance>`{.interpreted-text
role="ref"}.

It also provides methods for querying the status of OpenXR
initialization, and helper methods for ease of use of the API with
GDExtension.

::: {.rst-class}
classref-introduction-group
:::

## Tutorials

- [XrResult
  documentation](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrResult.html)
- [XrInstance
  documentation](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrInstance.html)
- [XrSpace
  documentation](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrSpace.html)
- [XrSession
  documentation](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrSession.html)
- [XrSystemId
  documentation](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrSystemId.html)
- [xrBeginSession
  documentation](https://registry.khronos.org/OpenXR/specs/1.0/man/html/xrBeginSession.html)
- [XrPosef
  documentation](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrPosef.html)

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

## Enumerations

:::: {#enum_OpenXRAPIExtension_OpenXRAlphaBlendModeSupport}
::: {.rst-class}
classref-enumeration
:::
::::

enum **OpenXRAlphaBlendModeSupport**:
`🔗<enum_OpenXRAPIExtension_OpenXRAlphaBlendModeSupport>`{.interpreted-text
role="ref"}

:::: {#class_OpenXRAPIExtension_constant_OPENXR_ALPHA_BLEND_MODE_SUPPORT_NONE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`OpenXRAlphaBlendModeSupport<enum_OpenXRAPIExtension_OpenXRAlphaBlendModeSupport>`{.interpreted-text
role="ref"} **OPENXR_ALPHA_BLEND_MODE_SUPPORT_NONE** = `0`

Means that
`XRInterface.XR_ENV_BLEND_MODE_ALPHA_BLEND<class_XRInterface_constant_XR_ENV_BLEND_MODE_ALPHA_BLEND>`{.interpreted-text
role="ref"} isn\'t supported at all.

:::: {#class_OpenXRAPIExtension_constant_OPENXR_ALPHA_BLEND_MODE_SUPPORT_REAL}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`OpenXRAlphaBlendModeSupport<enum_OpenXRAPIExtension_OpenXRAlphaBlendModeSupport>`{.interpreted-text
role="ref"} **OPENXR_ALPHA_BLEND_MODE_SUPPORT_REAL** = `1`

Means that
`XRInterface.XR_ENV_BLEND_MODE_ALPHA_BLEND<class_XRInterface_constant_XR_ENV_BLEND_MODE_ALPHA_BLEND>`{.interpreted-text
role="ref"} is really supported.

:::: {#class_OpenXRAPIExtension_constant_OPENXR_ALPHA_BLEND_MODE_SUPPORT_EMULATING}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`OpenXRAlphaBlendModeSupport<enum_OpenXRAPIExtension_OpenXRAlphaBlendModeSupport>`{.interpreted-text
role="ref"} **OPENXR_ALPHA_BLEND_MODE_SUPPORT_EMULATING** = `2`

Means that
`XRInterface.XR_ENV_BLEND_MODE_ALPHA_BLEND<class_XRInterface_constant_XR_ENV_BLEND_MODE_ALPHA_BLEND>`{.interpreted-text
role="ref"} is emulated.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_OpenXRAPIExtension_method_begin_debug_label_region}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**begin_debug_label_region**(label_name:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_OpenXRAPIExtension_method_begin_debug_label_region>`{.interpreted-text
role="ref"}

Begins a new debug label region, this label will be reported in debug
messages for any calls following this until
`end_debug_label_region<class_OpenXRAPIExtension_method_end_debug_label_region>`{.interpreted-text
role="ref"} is called. Debug labels can be stacked.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRAPIExtension_method_can_render}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **can_render**()
`🔗<class_OpenXRAPIExtension_method_can_render>`{.interpreted-text
role="ref"}

Returns `true` if OpenXR is initialized for rendering with an XR
viewport.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRAPIExtension_method_end_debug_label_region}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**end_debug_label_region**()
`🔗<class_OpenXRAPIExtension_method_end_debug_label_region>`{.interpreted-text
role="ref"}

Marks the end of a debug label region. Removes the latest debug label
region added by calling
`begin_debug_label_region<class_OpenXRAPIExtension_method_begin_debug_label_region>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRAPIExtension_method_get_error_string}
::: {.rst-class}
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_error_string**(result: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_OpenXRAPIExtension_method_get_error_string>`{.interpreted-text
role="ref"}

Returns an error string for the given
[XrResult](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrResult.html).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRAPIExtension_method_get_hand_tracker}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_hand_tracker**(hand_index: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_OpenXRAPIExtension_method_get_hand_tracker>`{.interpreted-text
role="ref"}

Returns the corresponding `XRHandTrackerEXT` handle for the given hand
index value.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRAPIExtension_method_get_instance}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_instance**()
`🔗<class_OpenXRAPIExtension_method_get_instance>`{.interpreted-text
role="ref"}

Returns the
[XrInstance](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrInstance.html)
created during the initialization of the OpenXR API.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRAPIExtension_method_get_instance_proc_addr}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_instance_proc_addr**(name:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_OpenXRAPIExtension_method_get_instance_proc_addr>`{.interpreted-text
role="ref"}

Returns the function pointer of the OpenXR function with the specified
name, cast to an integer. If the function with the given name does not
exist, the method returns `0`.

\*\*Note:\*\* `openxr/util.h` contains utility macros for acquiring
OpenXR functions, e.g. `GDEXTENSION_INIT_XR_FUNC_V(xrCreateAction)`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRAPIExtension_method_get_next_frame_time}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_next_frame_time**()
`🔗<class_OpenXRAPIExtension_method_get_next_frame_time>`{.interpreted-text
role="ref"}

Returns the predicted display timing for the next frame.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRAPIExtension_method_get_play_space}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_play_space**()
`🔗<class_OpenXRAPIExtension_method_get_play_space>`{.interpreted-text
role="ref"}

Returns the play space, which is an
[XrSpace](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrSpace.html)
cast to an integer.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRAPIExtension_method_get_predicted_display_time}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_predicted_display_time**()
`🔗<class_OpenXRAPIExtension_method_get_predicted_display_time>`{.interpreted-text
role="ref"}

Returns the predicted display timing for the current frame.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRAPIExtension_method_get_session}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_session**()
`🔗<class_OpenXRAPIExtension_method_get_session>`{.interpreted-text
role="ref"}

Returns the OpenXR session, which is an
[XrSession](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrSession.html)
cast to an integer.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRAPIExtension_method_get_swapchain_format_name}
::: {.rst-class}
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_swapchain_format_name**(swapchain_format:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_OpenXRAPIExtension_method_get_swapchain_format_name>`{.interpreted-text
role="ref"}

Returns the name of the specified swapchain format.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRAPIExtension_method_get_system_id}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_system_id**()
`🔗<class_OpenXRAPIExtension_method_get_system_id>`{.interpreted-text
role="ref"}

Returns the id of the system, which is a
[XrSystemId](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrSystemId.html)
cast to an integer.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRAPIExtension_method_insert_debug_label}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**insert_debug_label**(label_name:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_OpenXRAPIExtension_method_insert_debug_label>`{.interpreted-text
role="ref"}

Inserts a debug label, this label is reported in any debug message
resulting from the OpenXR calls that follows, until any of
`begin_debug_label_region<class_OpenXRAPIExtension_method_begin_debug_label_region>`{.interpreted-text
role="ref"},
`end_debug_label_region<class_OpenXRAPIExtension_method_end_debug_label_region>`{.interpreted-text
role="ref"}, or
`insert_debug_label<class_OpenXRAPIExtension_method_insert_debug_label>`{.interpreted-text
role="ref"} is called.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRAPIExtension_method_is_environment_blend_mode_alpha_supported}
::: {.rst-class}
classref-method
:::
::::

`OpenXRAlphaBlendModeSupport<enum_OpenXRAPIExtension_OpenXRAlphaBlendModeSupport>`{.interpreted-text
role="ref"} **is_environment_blend_mode_alpha_supported**()
`🔗<class_OpenXRAPIExtension_method_is_environment_blend_mode_alpha_supported>`{.interpreted-text
role="ref"}

Returns
`OpenXRAlphaBlendModeSupport<enum_OpenXRAPIExtension_OpenXRAlphaBlendModeSupport>`{.interpreted-text
role="ref"} denoting if
`XRInterface.XR_ENV_BLEND_MODE_ALPHA_BLEND<class_XRInterface_constant_XR_ENV_BLEND_MODE_ALPHA_BLEND>`{.interpreted-text
role="ref"} is really supported, emulated or not supported at all.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRAPIExtension_method_is_initialized}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_initialized**()
`🔗<class_OpenXRAPIExtension_method_is_initialized>`{.interpreted-text
role="ref"}

Returns `true` if OpenXR is initialized.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRAPIExtension_method_is_running}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_running**()
`🔗<class_OpenXRAPIExtension_method_is_running>`{.interpreted-text
role="ref"}

Returns `true` if OpenXR is running
([xrBeginSession](https://registry.khronos.org/OpenXR/specs/1.0/man/html/xrBeginSession.html)
was successfully called and the swapchains were created).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRAPIExtension_method_openxr_is_enabled}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**openxr_is_enabled**(check_run_in_editor:
`bool<class_bool>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRAPIExtension_method_openxr_is_enabled>`{.interpreted-text
role="ref"}

Returns `true` if OpenXR is enabled.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRAPIExtension_method_register_composition_layer_provider}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**register_composition_layer_provider**(extension:
`OpenXRExtensionWrapperExtension<class_OpenXRExtensionWrapperExtension>`{.interpreted-text
role="ref"})
`🔗<class_OpenXRAPIExtension_method_register_composition_layer_provider>`{.interpreted-text
role="ref"}

Registers the given extension as a composition layer provider.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRAPIExtension_method_set_emulate_environment_blend_mode_alpha_blend}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_emulate_environment_blend_mode_alpha_blend**(enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_OpenXRAPIExtension_method_set_emulate_environment_blend_mode_alpha_blend>`{.interpreted-text
role="ref"}

If set to `true`, an OpenXR extension is loaded which is capable of
emulating the
`XRInterface.XR_ENV_BLEND_MODE_ALPHA_BLEND<class_XRInterface_constant_XR_ENV_BLEND_MODE_ALPHA_BLEND>`{.interpreted-text
role="ref"} blend mode.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRAPIExtension_method_set_object_name}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_object_name**(object_type: `int<class_int>`{.interpreted-text
role="ref"}, object_handle: `int<class_int>`{.interpreted-text
role="ref"}, object_name: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_OpenXRAPIExtension_method_set_object_name>`{.interpreted-text
role="ref"}

Set the object name of an OpenXR object, used for debug output.
`object_type` must be a valid OpenXR `XrObjectType` enum and
`object_handle` must be a valid OpenXR object handle.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRAPIExtension_method_transform_from_pose}
::: {.rst-class}
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**transform_from_pose**(pose: `const void*`)
`🔗<class_OpenXRAPIExtension_method_transform_from_pose>`{.interpreted-text
role="ref"}

Creates a `Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
from an
[XrPosef](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrPosef.html).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRAPIExtension_method_unregister_composition_layer_provider}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**unregister_composition_layer_provider**(extension:
`OpenXRExtensionWrapperExtension<class_OpenXRExtensionWrapperExtension>`{.interpreted-text
role="ref"})
`🔗<class_OpenXRAPIExtension_method_unregister_composition_layer_provider>`{.interpreted-text
role="ref"}

Unregisters the given extension as a composition layer provider.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRAPIExtension_method_xr_result}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **xr_result**(result:
`int<class_int>`{.interpreted-text role="ref"}, format:
`String<class_String>`{.interpreted-text role="ref"}, args:
`Array<class_Array>`{.interpreted-text role="ref"})
`🔗<class_OpenXRAPIExtension_method_xr_result>`{.interpreted-text
role="ref"}

Returns `true` if the provided
[XrResult](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrResult.html)
(cast to an integer) is successful. Otherwise returns `false` and prints
the
[XrResult](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrResult.html)
converted to a string, with the specified additional information.
