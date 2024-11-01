github_url

:   hide

# DisplayServer {#class_DisplayServer}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

A server interface for low-level window management.

::: {.rst-class}
classref-introduction-group
:::

## Description

**DisplayServer** handles everything related to window management. It is
separated from `OS<class_OS>`{.interpreted-text role="ref"} as a single
operating system may support multiple display servers.

\*\*Headless mode:\*\* Starting the engine with the `--headless`
`command line argument <../tutorials/editor/command_line_tutorial>`{.interpreted-text
role="doc"} disables all rendering and window management functions. Most
functions from **DisplayServer** will return dummy values in this case.

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

:::: {#enum_DisplayServer_Feature}
::: {.rst-class}
classref-enumeration
:::
::::

enum **Feature**: `🔗<enum_DisplayServer_Feature>`{.interpreted-text
role="ref"}

:::: {#class_DisplayServer_constant_FEATURE_GLOBAL_MENU}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Feature<enum_DisplayServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_GLOBAL_MENU** = `0`

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Display server supports global menu. This allows the application to
display its menu items in the operating system\'s top bar. **macOS**

:::: {#class_DisplayServer_constant_FEATURE_SUBWINDOWS}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Feature<enum_DisplayServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_SUBWINDOWS** = `1`

Display server supports multiple windows that can be moved outside of
the main window. **Windows, macOS, Linux (X11)**

:::: {#class_DisplayServer_constant_FEATURE_TOUCHSCREEN}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Feature<enum_DisplayServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_TOUCHSCREEN** = `2`

Display server supports touchscreen input. **Windows, Linux (X11),
Android, iOS, Web**

:::: {#class_DisplayServer_constant_FEATURE_MOUSE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Feature<enum_DisplayServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_MOUSE** = `3`

Display server supports mouse input. **Windows, macOS, Linux
(X11/Wayland), Android, Web**

:::: {#class_DisplayServer_constant_FEATURE_MOUSE_WARP}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Feature<enum_DisplayServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_MOUSE_WARP** = `4`

Display server supports warping mouse coordinates to keep the mouse
cursor constrained within an area, but looping when one of the edges is
reached. **Windows, macOS, Linux (X11/Wayland)**

:::: {#class_DisplayServer_constant_FEATURE_CLIPBOARD}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Feature<enum_DisplayServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_CLIPBOARD** = `5`

Display server supports setting and getting clipboard data. See also
`FEATURE_CLIPBOARD_PRIMARY<class_DisplayServer_constant_FEATURE_CLIPBOARD_PRIMARY>`{.interpreted-text
role="ref"}. **Windows, macOS, Linux (X11/Wayland), Android, iOS, Web**

:::: {#class_DisplayServer_constant_FEATURE_VIRTUAL_KEYBOARD}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Feature<enum_DisplayServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_VIRTUAL_KEYBOARD** = `6`

Display server supports popping up a virtual keyboard when requested to
input text without a physical keyboard. **Android, iOS, Web**

:::: {#class_DisplayServer_constant_FEATURE_CURSOR_SHAPE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Feature<enum_DisplayServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_CURSOR_SHAPE** = `7`

Display server supports setting the mouse cursor shape to be different
from the default. **Windows, macOS, Linux (X11/Wayland), Android, Web**

:::: {#class_DisplayServer_constant_FEATURE_CUSTOM_CURSOR_SHAPE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Feature<enum_DisplayServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_CUSTOM_CURSOR_SHAPE** = `8`

Display server supports setting the mouse cursor shape to a custom
image. **Windows, macOS, Linux (X11/Wayland), Web**

:::: {#class_DisplayServer_constant_FEATURE_NATIVE_DIALOG}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Feature<enum_DisplayServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_NATIVE_DIALOG** = `9`

Display server supports spawning text dialogs using the operating
system\'s native look-and-feel. See
`dialog_show<class_DisplayServer_method_dialog_show>`{.interpreted-text
role="ref"}. **Windows, macOS**

:::: {#class_DisplayServer_constant_FEATURE_IME}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Feature<enum_DisplayServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_IME** = `10`

Display server supports [Input Method
Editor](https://en.wikipedia.org/wiki/Input_method), which is commonly
used for inputting Chinese/Japanese/Korean text. This is handled by the
operating system, rather than by Godot. **Windows, macOS, Linux (X11)**

:::: {#class_DisplayServer_constant_FEATURE_WINDOW_TRANSPARENCY}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Feature<enum_DisplayServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_WINDOW_TRANSPARENCY** = `11`

Display server supports windows can use per-pixel transparency to make
windows behind them partially or fully visible. **Windows, macOS, Linux
(X11/Wayland)**

:::: {#class_DisplayServer_constant_FEATURE_HIDPI}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Feature<enum_DisplayServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_HIDPI** = `12`

Display server supports querying the operating system\'s display scale
factor. This allows for *reliable* automatic hiDPI display detection, as
opposed to guessing based on the screen resolution and reported display
DPI (which can be unreliable due to broken monitor EDID). **Windows,
Linux (Wayland), macOS**

:::: {#class_DisplayServer_constant_FEATURE_ICON}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Feature<enum_DisplayServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_ICON** = `13`

Display server supports changing the window icon (usually displayed in
the top-left corner). **Windows, macOS, Linux (X11)**

:::: {#class_DisplayServer_constant_FEATURE_NATIVE_ICON}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Feature<enum_DisplayServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_NATIVE_ICON** = `14`

Display server supports changing the window icon (usually displayed in
the top-left corner). **Windows, macOS**

:::: {#class_DisplayServer_constant_FEATURE_ORIENTATION}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Feature<enum_DisplayServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_ORIENTATION** = `15`

Display server supports changing the screen orientation. **Android,
iOS**

:::: {#class_DisplayServer_constant_FEATURE_SWAP_BUFFERS}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Feature<enum_DisplayServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_SWAP_BUFFERS** = `16`

Display server supports V-Sync status can be changed from the default
(which is forced to be enabled platforms not supporting this feature).
**Windows, macOS, Linux (X11/Wayland)**

:::: {#class_DisplayServer_constant_FEATURE_CLIPBOARD_PRIMARY}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Feature<enum_DisplayServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_CLIPBOARD_PRIMARY** = `18`

Display server supports Primary clipboard can be used. This is a
different clipboard from
`FEATURE_CLIPBOARD<class_DisplayServer_constant_FEATURE_CLIPBOARD>`{.interpreted-text
role="ref"}. **Linux (X11/Wayland)**

:::: {#class_DisplayServer_constant_FEATURE_TEXT_TO_SPEECH}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Feature<enum_DisplayServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_TEXT_TO_SPEECH** = `19`

Display server supports text-to-speech. See `tts_*` methods. **Windows,
macOS, Linux (X11/Wayland), Android, iOS, Web**

:::: {#class_DisplayServer_constant_FEATURE_EXTEND_TO_TITLE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Feature<enum_DisplayServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_EXTEND_TO_TITLE** = `20`

Display server supports expanding window content to the title. See
`WINDOW_FLAG_EXTEND_TO_TITLE<class_DisplayServer_constant_WINDOW_FLAG_EXTEND_TO_TITLE>`{.interpreted-text
role="ref"}. **macOS**

:::: {#class_DisplayServer_constant_FEATURE_SCREEN_CAPTURE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Feature<enum_DisplayServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_SCREEN_CAPTURE** = `21`

Display server supports reading screen pixels. See
`screen_get_pixel<class_DisplayServer_method_screen_get_pixel>`{.interpreted-text
role="ref"}.

:::: {#class_DisplayServer_constant_FEATURE_STATUS_INDICATOR}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Feature<enum_DisplayServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_STATUS_INDICATOR** = `22`

Display server supports application status indicators.

:::: {#class_DisplayServer_constant_FEATURE_NATIVE_HELP}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Feature<enum_DisplayServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_NATIVE_HELP** = `23`

Display server supports native help system search callbacks. See
`help_set_search_callbacks<class_DisplayServer_method_help_set_search_callbacks>`{.interpreted-text
role="ref"}.

:::: {#class_DisplayServer_constant_FEATURE_NATIVE_DIALOG_INPUT}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Feature<enum_DisplayServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_NATIVE_DIALOG_INPUT** = `24`

Display server supports spawning text input dialogs using the operating
system\'s native look-and-feel. See
`dialog_input_text<class_DisplayServer_method_dialog_input_text>`{.interpreted-text
role="ref"}. **Windows, macOS**

:::: {#class_DisplayServer_constant_FEATURE_NATIVE_DIALOG_FILE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Feature<enum_DisplayServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_NATIVE_DIALOG_FILE** = `25`

Display server supports spawning dialogs for selecting files or
directories using the operating system\'s native look-and-feel. See
`file_dialog_show<class_DisplayServer_method_file_dialog_show>`{.interpreted-text
role="ref"} and
`file_dialog_with_options_show<class_DisplayServer_method_file_dialog_with_options_show>`{.interpreted-text
role="ref"}. **Windows, macOS, Linux (X11/Wayland)**

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_DisplayServer_MouseMode}
::: {.rst-class}
classref-enumeration
:::
::::

enum **MouseMode**: `🔗<enum_DisplayServer_MouseMode>`{.interpreted-text
role="ref"}

:::: {#class_DisplayServer_constant_MOUSE_MODE_VISIBLE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`MouseMode<enum_DisplayServer_MouseMode>`{.interpreted-text role="ref"}
**MOUSE_MODE_VISIBLE** = `0`

Makes the mouse cursor visible if it is hidden.

:::: {#class_DisplayServer_constant_MOUSE_MODE_HIDDEN}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`MouseMode<enum_DisplayServer_MouseMode>`{.interpreted-text role="ref"}
**MOUSE_MODE_HIDDEN** = `1`

Makes the mouse cursor hidden if it is visible.

:::: {#class_DisplayServer_constant_MOUSE_MODE_CAPTURED}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`MouseMode<enum_DisplayServer_MouseMode>`{.interpreted-text role="ref"}
**MOUSE_MODE_CAPTURED** = `2`

Captures the mouse. The mouse will be hidden and its position locked at
the center of the window manager\'s window.

\*\*Note:\*\* If you want to process the mouse\'s movement in this mode,
you need to use
`InputEventMouseMotion.relative<class_InputEventMouseMotion_property_relative>`{.interpreted-text
role="ref"}.

:::: {#class_DisplayServer_constant_MOUSE_MODE_CONFINED}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`MouseMode<enum_DisplayServer_MouseMode>`{.interpreted-text role="ref"}
**MOUSE_MODE_CONFINED** = `3`

Confines the mouse cursor to the game window, and make it visible.

:::: {#class_DisplayServer_constant_MOUSE_MODE_CONFINED_HIDDEN}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`MouseMode<enum_DisplayServer_MouseMode>`{.interpreted-text role="ref"}
**MOUSE_MODE_CONFINED_HIDDEN** = `4`

Confines the mouse cursor to the game window, and make it hidden.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_DisplayServer_ScreenOrientation}
::: {.rst-class}
classref-enumeration
:::
::::

enum **ScreenOrientation**:
`🔗<enum_DisplayServer_ScreenOrientation>`{.interpreted-text role="ref"}

:::: {#class_DisplayServer_constant_SCREEN_LANDSCAPE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`ScreenOrientation<enum_DisplayServer_ScreenOrientation>`{.interpreted-text
role="ref"} **SCREEN_LANDSCAPE** = `0`

Default landscape orientation.

:::: {#class_DisplayServer_constant_SCREEN_PORTRAIT}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`ScreenOrientation<enum_DisplayServer_ScreenOrientation>`{.interpreted-text
role="ref"} **SCREEN_PORTRAIT** = `1`

Default portrait orientation.

:::: {#class_DisplayServer_constant_SCREEN_REVERSE_LANDSCAPE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`ScreenOrientation<enum_DisplayServer_ScreenOrientation>`{.interpreted-text
role="ref"} **SCREEN_REVERSE_LANDSCAPE** = `2`

Reverse landscape orientation (upside down).

:::: {#class_DisplayServer_constant_SCREEN_REVERSE_PORTRAIT}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`ScreenOrientation<enum_DisplayServer_ScreenOrientation>`{.interpreted-text
role="ref"} **SCREEN_REVERSE_PORTRAIT** = `3`

Reverse portrait orientation (upside down).

:::: {#class_DisplayServer_constant_SCREEN_SENSOR_LANDSCAPE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`ScreenOrientation<enum_DisplayServer_ScreenOrientation>`{.interpreted-text
role="ref"} **SCREEN_SENSOR_LANDSCAPE** = `4`

Automatic landscape orientation (default or reverse depending on
sensor).

:::: {#class_DisplayServer_constant_SCREEN_SENSOR_PORTRAIT}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`ScreenOrientation<enum_DisplayServer_ScreenOrientation>`{.interpreted-text
role="ref"} **SCREEN_SENSOR_PORTRAIT** = `5`

Automatic portrait orientation (default or reverse depending on sensor).

:::: {#class_DisplayServer_constant_SCREEN_SENSOR}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`ScreenOrientation<enum_DisplayServer_ScreenOrientation>`{.interpreted-text
role="ref"} **SCREEN_SENSOR** = `6`

Automatic landscape or portrait orientation (default or reverse
depending on sensor).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_DisplayServer_VirtualKeyboardType}
::: {.rst-class}
classref-enumeration
:::
::::

enum **VirtualKeyboardType**:
`🔗<enum_DisplayServer_VirtualKeyboardType>`{.interpreted-text
role="ref"}

:::: {#class_DisplayServer_constant_KEYBOARD_TYPE_DEFAULT}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`VirtualKeyboardType<enum_DisplayServer_VirtualKeyboardType>`{.interpreted-text
role="ref"} **KEYBOARD_TYPE_DEFAULT** = `0`

Default text virtual keyboard.

:::: {#class_DisplayServer_constant_KEYBOARD_TYPE_MULTILINE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`VirtualKeyboardType<enum_DisplayServer_VirtualKeyboardType>`{.interpreted-text
role="ref"} **KEYBOARD_TYPE_MULTILINE** = `1`

Multiline virtual keyboard.

:::: {#class_DisplayServer_constant_KEYBOARD_TYPE_NUMBER}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`VirtualKeyboardType<enum_DisplayServer_VirtualKeyboardType>`{.interpreted-text
role="ref"} **KEYBOARD_TYPE_NUMBER** = `2`

Virtual number keypad, useful for PIN entry.

:::: {#class_DisplayServer_constant_KEYBOARD_TYPE_NUMBER_DECIMAL}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`VirtualKeyboardType<enum_DisplayServer_VirtualKeyboardType>`{.interpreted-text
role="ref"} **KEYBOARD_TYPE_NUMBER_DECIMAL** = `3`

Virtual number keypad, useful for entering fractional numbers.

:::: {#class_DisplayServer_constant_KEYBOARD_TYPE_PHONE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`VirtualKeyboardType<enum_DisplayServer_VirtualKeyboardType>`{.interpreted-text
role="ref"} **KEYBOARD_TYPE_PHONE** = `4`

Virtual phone number keypad.

:::: {#class_DisplayServer_constant_KEYBOARD_TYPE_EMAIL_ADDRESS}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`VirtualKeyboardType<enum_DisplayServer_VirtualKeyboardType>`{.interpreted-text
role="ref"} **KEYBOARD_TYPE_EMAIL_ADDRESS** = `5`

Virtual keyboard with additional keys to assist with typing email
addresses.

:::: {#class_DisplayServer_constant_KEYBOARD_TYPE_PASSWORD}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`VirtualKeyboardType<enum_DisplayServer_VirtualKeyboardType>`{.interpreted-text
role="ref"} **KEYBOARD_TYPE_PASSWORD** = `6`

Virtual keyboard for entering a password. On most platforms, this should
disable autocomplete and autocapitalization.

\*\*Note:\*\* This is not supported on Web. Instead, this behaves
identically to
`KEYBOARD_TYPE_DEFAULT<class_DisplayServer_constant_KEYBOARD_TYPE_DEFAULT>`{.interpreted-text
role="ref"}.

:::: {#class_DisplayServer_constant_KEYBOARD_TYPE_URL}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`VirtualKeyboardType<enum_DisplayServer_VirtualKeyboardType>`{.interpreted-text
role="ref"} **KEYBOARD_TYPE_URL** = `7`

Virtual keyboard with additional keys to assist with typing URLs.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_DisplayServer_CursorShape}
::: {.rst-class}
classref-enumeration
:::
::::

enum **CursorShape**:
`🔗<enum_DisplayServer_CursorShape>`{.interpreted-text role="ref"}

:::: {#class_DisplayServer_constant_CURSOR_ARROW}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`CursorShape<enum_DisplayServer_CursorShape>`{.interpreted-text
role="ref"} **CURSOR_ARROW** = `0`

Arrow cursor shape. This is the default when not pointing anything that
overrides the mouse cursor, such as a
`LineEdit<class_LineEdit>`{.interpreted-text role="ref"} or
`TextEdit<class_TextEdit>`{.interpreted-text role="ref"}.

:::: {#class_DisplayServer_constant_CURSOR_IBEAM}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`CursorShape<enum_DisplayServer_CursorShape>`{.interpreted-text
role="ref"} **CURSOR_IBEAM** = `1`

I-beam cursor shape. This is used by default when hovering a control
that accepts text input, such as
`LineEdit<class_LineEdit>`{.interpreted-text role="ref"} or
`TextEdit<class_TextEdit>`{.interpreted-text role="ref"}.

:::: {#class_DisplayServer_constant_CURSOR_POINTING_HAND}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`CursorShape<enum_DisplayServer_CursorShape>`{.interpreted-text
role="ref"} **CURSOR_POINTING_HAND** = `2`

Pointing hand cursor shape. This is used by default when hovering a
`LinkButton<class_LinkButton>`{.interpreted-text role="ref"} or a URL
tag in a `RichTextLabel<class_RichTextLabel>`{.interpreted-text
role="ref"}.

:::: {#class_DisplayServer_constant_CURSOR_CROSS}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`CursorShape<enum_DisplayServer_CursorShape>`{.interpreted-text
role="ref"} **CURSOR_CROSS** = `3`

Crosshair cursor. This is intended to be displayed when the user needs
precise aim over an element, such as a rectangle selection tool or a
color picker.

:::: {#class_DisplayServer_constant_CURSOR_WAIT}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`CursorShape<enum_DisplayServer_CursorShape>`{.interpreted-text
role="ref"} **CURSOR_WAIT** = `4`

Wait cursor. On most cursor themes, this displays a spinning icon
*besides* the arrow. Intended to be used for non-blocking operations
(when the user can do something else at the moment). See also
`CURSOR_BUSY<class_DisplayServer_constant_CURSOR_BUSY>`{.interpreted-text
role="ref"}.

:::: {#class_DisplayServer_constant_CURSOR_BUSY}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`CursorShape<enum_DisplayServer_CursorShape>`{.interpreted-text
role="ref"} **CURSOR_BUSY** = `5`

Wait cursor. On most cursor themes, this *replaces* the arrow with a
spinning icon. Intended to be used for blocking operations (when the
user can\'t do anything else at the moment). See also
`CURSOR_WAIT<class_DisplayServer_constant_CURSOR_WAIT>`{.interpreted-text
role="ref"}.

:::: {#class_DisplayServer_constant_CURSOR_DRAG}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`CursorShape<enum_DisplayServer_CursorShape>`{.interpreted-text
role="ref"} **CURSOR_DRAG** = `6`

Dragging hand cursor. This is displayed during drag-and-drop operations.
See also
`CURSOR_CAN_DROP<class_DisplayServer_constant_CURSOR_CAN_DROP>`{.interpreted-text
role="ref"}.

:::: {#class_DisplayServer_constant_CURSOR_CAN_DROP}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`CursorShape<enum_DisplayServer_CursorShape>`{.interpreted-text
role="ref"} **CURSOR_CAN_DROP** = `7`

\"Can drop\" cursor. This is displayed during drag-and-drop operations
if hovering over a `Control<class_Control>`{.interpreted-text
role="ref"} that can accept the drag-and-drop event. On most cursor
themes, this displays a dragging hand with an arrow symbol besides it.
See also
`CURSOR_DRAG<class_DisplayServer_constant_CURSOR_DRAG>`{.interpreted-text
role="ref"}.

:::: {#class_DisplayServer_constant_CURSOR_FORBIDDEN}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`CursorShape<enum_DisplayServer_CursorShape>`{.interpreted-text
role="ref"} **CURSOR_FORBIDDEN** = `8`

Forbidden cursor. This is displayed during drag-and-drop operations if
the hovered `Control<class_Control>`{.interpreted-text role="ref"}
can\'t accept the drag-and-drop event.

:::: {#class_DisplayServer_constant_CURSOR_VSIZE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`CursorShape<enum_DisplayServer_CursorShape>`{.interpreted-text
role="ref"} **CURSOR_VSIZE** = `9`

Vertical resize cursor. Intended to be displayed when the hovered
`Control<class_Control>`{.interpreted-text role="ref"} can be vertically
resized using the mouse. See also
`CURSOR_VSPLIT<class_DisplayServer_constant_CURSOR_VSPLIT>`{.interpreted-text
role="ref"}.

:::: {#class_DisplayServer_constant_CURSOR_HSIZE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`CursorShape<enum_DisplayServer_CursorShape>`{.interpreted-text
role="ref"} **CURSOR_HSIZE** = `10`

Horizontal resize cursor. Intended to be displayed when the hovered
`Control<class_Control>`{.interpreted-text role="ref"} can be
horizontally resized using the mouse. See also
`CURSOR_HSPLIT<class_DisplayServer_constant_CURSOR_HSPLIT>`{.interpreted-text
role="ref"}.

:::: {#class_DisplayServer_constant_CURSOR_BDIAGSIZE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`CursorShape<enum_DisplayServer_CursorShape>`{.interpreted-text
role="ref"} **CURSOR_BDIAGSIZE** = `11`

Secondary diagonal resize cursor (top-right/bottom-left). Intended to be
displayed when the hovered `Control<class_Control>`{.interpreted-text
role="ref"} can be resized on both axes at once using the mouse.

:::: {#class_DisplayServer_constant_CURSOR_FDIAGSIZE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`CursorShape<enum_DisplayServer_CursorShape>`{.interpreted-text
role="ref"} **CURSOR_FDIAGSIZE** = `12`

Main diagonal resize cursor (top-left/bottom-right). Intended to be
displayed when the hovered `Control<class_Control>`{.interpreted-text
role="ref"} can be resized on both axes at once using the mouse.

:::: {#class_DisplayServer_constant_CURSOR_MOVE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`CursorShape<enum_DisplayServer_CursorShape>`{.interpreted-text
role="ref"} **CURSOR_MOVE** = `13`

Move cursor. Intended to be displayed when the hovered
`Control<class_Control>`{.interpreted-text role="ref"} can be moved
using the mouse.

:::: {#class_DisplayServer_constant_CURSOR_VSPLIT}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`CursorShape<enum_DisplayServer_CursorShape>`{.interpreted-text
role="ref"} **CURSOR_VSPLIT** = `14`

Vertical split cursor. This is displayed when hovering a
`Control<class_Control>`{.interpreted-text role="ref"} with splits that
can be vertically resized using the mouse, such as
`VSplitContainer<class_VSplitContainer>`{.interpreted-text role="ref"}.
On some cursor themes, this cursor may have the same appearance as
`CURSOR_VSIZE<class_DisplayServer_constant_CURSOR_VSIZE>`{.interpreted-text
role="ref"}.

:::: {#class_DisplayServer_constant_CURSOR_HSPLIT}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`CursorShape<enum_DisplayServer_CursorShape>`{.interpreted-text
role="ref"} **CURSOR_HSPLIT** = `15`

Horizontal split cursor. This is displayed when hovering a
`Control<class_Control>`{.interpreted-text role="ref"} with splits that
can be horizontally resized using the mouse, such as
`HSplitContainer<class_HSplitContainer>`{.interpreted-text role="ref"}.
On some cursor themes, this cursor may have the same appearance as
`CURSOR_HSIZE<class_DisplayServer_constant_CURSOR_HSIZE>`{.interpreted-text
role="ref"}.

:::: {#class_DisplayServer_constant_CURSOR_HELP}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`CursorShape<enum_DisplayServer_CursorShape>`{.interpreted-text
role="ref"} **CURSOR_HELP** = `16`

Help cursor. On most cursor themes, this displays a question mark icon
instead of the mouse cursor. Intended to be used when the user has
requested help on the next element that will be clicked.

:::: {#class_DisplayServer_constant_CURSOR_MAX}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`CursorShape<enum_DisplayServer_CursorShape>`{.interpreted-text
role="ref"} **CURSOR_MAX** = `17`

Represents the size of the
`CursorShape<enum_DisplayServer_CursorShape>`{.interpreted-text
role="ref"} enum.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_DisplayServer_FileDialogMode}
::: {.rst-class}
classref-enumeration
:::
::::

enum **FileDialogMode**:
`🔗<enum_DisplayServer_FileDialogMode>`{.interpreted-text role="ref"}

:::: {#class_DisplayServer_constant_FILE_DIALOG_MODE_OPEN_FILE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`FileDialogMode<enum_DisplayServer_FileDialogMode>`{.interpreted-text
role="ref"} **FILE_DIALOG_MODE_OPEN_FILE** = `0`

The native file dialog allows selecting one, and only one file.

:::: {#class_DisplayServer_constant_FILE_DIALOG_MODE_OPEN_FILES}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`FileDialogMode<enum_DisplayServer_FileDialogMode>`{.interpreted-text
role="ref"} **FILE_DIALOG_MODE_OPEN_FILES** = `1`

The native file dialog allows selecting multiple files.

:::: {#class_DisplayServer_constant_FILE_DIALOG_MODE_OPEN_DIR}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`FileDialogMode<enum_DisplayServer_FileDialogMode>`{.interpreted-text
role="ref"} **FILE_DIALOG_MODE_OPEN_DIR** = `2`

The native file dialog only allows selecting a directory, disallowing
the selection of any file.

:::: {#class_DisplayServer_constant_FILE_DIALOG_MODE_OPEN_ANY}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`FileDialogMode<enum_DisplayServer_FileDialogMode>`{.interpreted-text
role="ref"} **FILE_DIALOG_MODE_OPEN_ANY** = `3`

The native file dialog allows selecting one file or directory.

:::: {#class_DisplayServer_constant_FILE_DIALOG_MODE_SAVE_FILE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`FileDialogMode<enum_DisplayServer_FileDialogMode>`{.interpreted-text
role="ref"} **FILE_DIALOG_MODE_SAVE_FILE** = `4`

The native file dialog will warn when a file exists.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_DisplayServer_WindowMode}
::: {.rst-class}
classref-enumeration
:::
::::

enum **WindowMode**:
`🔗<enum_DisplayServer_WindowMode>`{.interpreted-text role="ref"}

:::: {#class_DisplayServer_constant_WINDOW_MODE_WINDOWED}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`WindowMode<enum_DisplayServer_WindowMode>`{.interpreted-text
role="ref"} **WINDOW_MODE_WINDOWED** = `0`

Windowed mode, i.e. `Window<class_Window>`{.interpreted-text role="ref"}
doesn\'t occupy the whole screen (unless set to the size of the screen).

:::: {#class_DisplayServer_constant_WINDOW_MODE_MINIMIZED}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`WindowMode<enum_DisplayServer_WindowMode>`{.interpreted-text
role="ref"} **WINDOW_MODE_MINIMIZED** = `1`

Minimized window mode, i.e. `Window<class_Window>`{.interpreted-text
role="ref"} is not visible and available on window manager\'s window
list. Normally happens when the minimize button is pressed.

:::: {#class_DisplayServer_constant_WINDOW_MODE_MAXIMIZED}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`WindowMode<enum_DisplayServer_WindowMode>`{.interpreted-text
role="ref"} **WINDOW_MODE_MAXIMIZED** = `2`

Maximized window mode, i.e. `Window<class_Window>`{.interpreted-text
role="ref"} will occupy whole screen area except task bar and still
display its borders. Normally happens when the maximize button is
pressed.

:::: {#class_DisplayServer_constant_WINDOW_MODE_FULLSCREEN}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`WindowMode<enum_DisplayServer_WindowMode>`{.interpreted-text
role="ref"} **WINDOW_MODE_FULLSCREEN** = `3`

Full screen mode with full multi-window support.

Full screen window covers the entire display area of a screen and has no
decorations. The display\'s video mode is not changed.

\*\*On Android:\*\* This enables immersive mode.

\*\*On Windows:\*\* Multi-window full-screen mode has a 1px border of
the
`ProjectSettings.rendering/environment/defaults/default_clear_color<class_ProjectSettings_property_rendering/environment/defaults/default_clear_color>`{.interpreted-text
role="ref"} color.

\*\*On macOS:\*\* A new desktop is used to display the running project.

\*\*Note:\*\* Regardless of the platform, enabling full screen will
change the window size to match the monitor\'s size. Therefore, make
sure your project supports
`multiple resolutions <../tutorials/rendering/multiple_resolutions>`{.interpreted-text
role="doc"} when enabling full screen mode.

:::: {#class_DisplayServer_constant_WINDOW_MODE_EXCLUSIVE_FULLSCREEN}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`WindowMode<enum_DisplayServer_WindowMode>`{.interpreted-text
role="ref"} **WINDOW_MODE_EXCLUSIVE_FULLSCREEN** = `4`

A single window full screen mode. This mode has less overhead, but only
one window can be open on a given screen at a time (opening a child
window or application switching will trigger a full screen transition).

Full screen window covers the entire display area of a screen and has no
border or decorations. The display\'s video mode is not changed.

\*\*On Android:\*\* This enables immersive mode.

\*\*On Windows:\*\* Depending on video driver, full screen transition
might cause screens to go black for a moment.

\*\*On macOS:\*\* A new desktop is used to display the running project.
Exclusive full screen mode prevents Dock and Menu from showing up when
the mouse pointer is hovering the edge of the screen.

\*\*On Linux (X11):\*\* Exclusive full screen mode bypasses compositor.

\*\*Note:\*\* Regardless of the platform, enabling full screen will
change the window size to match the monitor\'s size. Therefore, make
sure your project supports
`multiple resolutions <../tutorials/rendering/multiple_resolutions>`{.interpreted-text
role="doc"} when enabling full screen mode.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_DisplayServer_WindowFlags}
::: {.rst-class}
classref-enumeration
:::
::::

enum **WindowFlags**:
`🔗<enum_DisplayServer_WindowFlags>`{.interpreted-text role="ref"}

:::: {#class_DisplayServer_constant_WINDOW_FLAG_RESIZE_DISABLED}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`WindowFlags<enum_DisplayServer_WindowFlags>`{.interpreted-text
role="ref"} **WINDOW_FLAG_RESIZE_DISABLED** = `0`

The window can\'t be resized by dragging its resize grip. It\'s still
possible to resize the window using
`window_set_size<class_DisplayServer_method_window_set_size>`{.interpreted-text
role="ref"}. This flag is ignored for full screen windows.

:::: {#class_DisplayServer_constant_WINDOW_FLAG_BORDERLESS}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`WindowFlags<enum_DisplayServer_WindowFlags>`{.interpreted-text
role="ref"} **WINDOW_FLAG_BORDERLESS** = `1`

The window do not have native title bar and other decorations. This flag
is ignored for full-screen windows.

:::: {#class_DisplayServer_constant_WINDOW_FLAG_ALWAYS_ON_TOP}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`WindowFlags<enum_DisplayServer_WindowFlags>`{.interpreted-text
role="ref"} **WINDOW_FLAG_ALWAYS_ON_TOP** = `2`

The window is floating on top of all other windows. This flag is ignored
for full-screen windows.

:::: {#class_DisplayServer_constant_WINDOW_FLAG_TRANSPARENT}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`WindowFlags<enum_DisplayServer_WindowFlags>`{.interpreted-text
role="ref"} **WINDOW_FLAG_TRANSPARENT** = `3`

The window background can be transparent.

\*\*Note:\*\* This flag has no effect if
`is_window_transparency_available<class_DisplayServer_method_is_window_transparency_available>`{.interpreted-text
role="ref"} returns `false`.

\*\*Note:\*\* Transparency support is implemented on Linux
(X11/Wayland), macOS, and Windows, but availability might vary depending
on GPU driver, display manager, and compositor capabilities.

:::: {#class_DisplayServer_constant_WINDOW_FLAG_NO_FOCUS}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`WindowFlags<enum_DisplayServer_WindowFlags>`{.interpreted-text
role="ref"} **WINDOW_FLAG_NO_FOCUS** = `4`

The window can\'t be focused. No-focus window will ignore all input,
except mouse clicks.

:::: {#class_DisplayServer_constant_WINDOW_FLAG_POPUP}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`WindowFlags<enum_DisplayServer_WindowFlags>`{.interpreted-text
role="ref"} **WINDOW_FLAG_POPUP** = `5`

Window is part of menu or
`OptionButton<class_OptionButton>`{.interpreted-text role="ref"}
dropdown. This flag can\'t be changed when the window is visible. An
active popup window will exclusively receive all input, without stealing
focus from its parent. Popup windows are automatically closed when uses
click outside it, or when an application is switched. Popup window must
have transient parent set (see
`window_set_transient<class_DisplayServer_method_window_set_transient>`{.interpreted-text
role="ref"}).

:::: {#class_DisplayServer_constant_WINDOW_FLAG_EXTEND_TO_TITLE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`WindowFlags<enum_DisplayServer_WindowFlags>`{.interpreted-text
role="ref"} **WINDOW_FLAG_EXTEND_TO_TITLE** = `6`

Window content is expanded to the full size of the window. Unlike
borderless window, the frame is left intact and can be used to resize
the window, title bar is transparent, but have minimize/maximize/close
buttons.

Use
`window_set_window_buttons_offset<class_DisplayServer_method_window_set_window_buttons_offset>`{.interpreted-text
role="ref"} to adjust minimize/maximize/close buttons offset.

Use
`window_get_safe_title_margins<class_DisplayServer_method_window_get_safe_title_margins>`{.interpreted-text
role="ref"} to determine area under the title bar that is not covered by
decorations.

\*\*Note:\*\* This flag is implemented only on macOS.

:::: {#class_DisplayServer_constant_WINDOW_FLAG_MOUSE_PASSTHROUGH}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`WindowFlags<enum_DisplayServer_WindowFlags>`{.interpreted-text
role="ref"} **WINDOW_FLAG_MOUSE_PASSTHROUGH** = `7`

All mouse events are passed to the underlying window of the same
application.

:::: {#class_DisplayServer_constant_WINDOW_FLAG_SHARP_CORNERS}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`WindowFlags<enum_DisplayServer_WindowFlags>`{.interpreted-text
role="ref"} **WINDOW_FLAG_SHARP_CORNERS** = `8`

Window style is overridden, forcing sharp corners.

\*\*Note:\*\* This flag is implemented only on Windows (11).

:::: {#class_DisplayServer_constant_WINDOW_FLAG_MAX}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`WindowFlags<enum_DisplayServer_WindowFlags>`{.interpreted-text
role="ref"} **WINDOW_FLAG_MAX** = `9`

Max value of the
`WindowFlags<enum_DisplayServer_WindowFlags>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_DisplayServer_WindowEvent}
::: {.rst-class}
classref-enumeration
:::
::::

enum **WindowEvent**:
`🔗<enum_DisplayServer_WindowEvent>`{.interpreted-text role="ref"}

:::: {#class_DisplayServer_constant_WINDOW_EVENT_MOUSE_ENTER}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`WindowEvent<enum_DisplayServer_WindowEvent>`{.interpreted-text
role="ref"} **WINDOW_EVENT_MOUSE_ENTER** = `0`

Sent when the mouse pointer enters the window.

:::: {#class_DisplayServer_constant_WINDOW_EVENT_MOUSE_EXIT}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`WindowEvent<enum_DisplayServer_WindowEvent>`{.interpreted-text
role="ref"} **WINDOW_EVENT_MOUSE_EXIT** = `1`

Sent when the mouse pointer exits the window.

:::: {#class_DisplayServer_constant_WINDOW_EVENT_FOCUS_IN}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`WindowEvent<enum_DisplayServer_WindowEvent>`{.interpreted-text
role="ref"} **WINDOW_EVENT_FOCUS_IN** = `2`

Sent when the window grabs focus.

:::: {#class_DisplayServer_constant_WINDOW_EVENT_FOCUS_OUT}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`WindowEvent<enum_DisplayServer_WindowEvent>`{.interpreted-text
role="ref"} **WINDOW_EVENT_FOCUS_OUT** = `3`

Sent when the window loses focus.

:::: {#class_DisplayServer_constant_WINDOW_EVENT_CLOSE_REQUEST}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`WindowEvent<enum_DisplayServer_WindowEvent>`{.interpreted-text
role="ref"} **WINDOW_EVENT_CLOSE_REQUEST** = `4`

Sent when the user has attempted to close the window (e.g. close button
is pressed).

:::: {#class_DisplayServer_constant_WINDOW_EVENT_GO_BACK_REQUEST}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`WindowEvent<enum_DisplayServer_WindowEvent>`{.interpreted-text
role="ref"} **WINDOW_EVENT_GO_BACK_REQUEST** = `5`

Sent when the device \"Back\" button is pressed.

\*\*Note:\*\* This event is implemented only on Android.

:::: {#class_DisplayServer_constant_WINDOW_EVENT_DPI_CHANGE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`WindowEvent<enum_DisplayServer_WindowEvent>`{.interpreted-text
role="ref"} **WINDOW_EVENT_DPI_CHANGE** = `6`

Sent when the window is moved to the display with different DPI, or
display DPI is changed.

\*\*Note:\*\* This flag is implemented only on macOS.

:::: {#class_DisplayServer_constant_WINDOW_EVENT_TITLEBAR_CHANGE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`WindowEvent<enum_DisplayServer_WindowEvent>`{.interpreted-text
role="ref"} **WINDOW_EVENT_TITLEBAR_CHANGE** = `7`

Sent when the window title bar decoration is changed (e.g.
`WINDOW_FLAG_EXTEND_TO_TITLE<class_DisplayServer_constant_WINDOW_FLAG_EXTEND_TO_TITLE>`{.interpreted-text
role="ref"} is set or window entered/exited full screen mode).

\*\*Note:\*\* This flag is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_DisplayServer_VSyncMode}
::: {.rst-class}
classref-enumeration
:::
::::

enum **VSyncMode**: `🔗<enum_DisplayServer_VSyncMode>`{.interpreted-text
role="ref"}

:::: {#class_DisplayServer_constant_VSYNC_DISABLED}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`VSyncMode<enum_DisplayServer_VSyncMode>`{.interpreted-text role="ref"}
**VSYNC_DISABLED** = `0`

No vertical synchronization, which means the engine will display frames
as fast as possible (tearing may be visible). Framerate is unlimited
(regardless of
`Engine.max_fps<class_Engine_property_max_fps>`{.interpreted-text
role="ref"}).

:::: {#class_DisplayServer_constant_VSYNC_ENABLED}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`VSyncMode<enum_DisplayServer_VSyncMode>`{.interpreted-text role="ref"}
**VSYNC_ENABLED** = `1`

Default vertical synchronization mode, the image is displayed only on
vertical blanking intervals (no tearing is visible). Framerate is
limited by the monitor refresh rate (regardless of
`Engine.max_fps<class_Engine_property_max_fps>`{.interpreted-text
role="ref"}).

:::: {#class_DisplayServer_constant_VSYNC_ADAPTIVE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`VSyncMode<enum_DisplayServer_VSyncMode>`{.interpreted-text role="ref"}
**VSYNC_ADAPTIVE** = `2`

Behaves like
`VSYNC_DISABLED<class_DisplayServer_constant_VSYNC_DISABLED>`{.interpreted-text
role="ref"} when the framerate drops below the screen\'s refresh rate to
reduce stuttering (tearing may be visible). Otherwise, vertical
synchronization is enabled to avoid tearing. Framerate is limited by the
monitor refresh rate (regardless of
`Engine.max_fps<class_Engine_property_max_fps>`{.interpreted-text
role="ref"}). Behaves like
`VSYNC_ENABLED<class_DisplayServer_constant_VSYNC_ENABLED>`{.interpreted-text
role="ref"} when using the Compatibility rendering method.

:::: {#class_DisplayServer_constant_VSYNC_MAILBOX}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`VSyncMode<enum_DisplayServer_VSyncMode>`{.interpreted-text role="ref"}
**VSYNC_MAILBOX** = `3`

Displays the most recent image in the queue on vertical blanking
intervals, while rendering to the other images (no tearing is visible).
Framerate is unlimited (regardless of
`Engine.max_fps<class_Engine_property_max_fps>`{.interpreted-text
role="ref"}).

Although not guaranteed, the images can be rendered as fast as possible,
which may reduce input lag (also called \"Fast\" V-Sync mode).
`VSYNC_MAILBOX<class_DisplayServer_constant_VSYNC_MAILBOX>`{.interpreted-text
role="ref"} works best when at least twice as many frames as the display
refresh rate are rendered. Behaves like
`VSYNC_ENABLED<class_DisplayServer_constant_VSYNC_ENABLED>`{.interpreted-text
role="ref"} when using the Compatibility rendering method.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_DisplayServer_HandleType}
::: {.rst-class}
classref-enumeration
:::
::::

enum **HandleType**:
`🔗<enum_DisplayServer_HandleType>`{.interpreted-text role="ref"}

:::: {#class_DisplayServer_constant_DISPLAY_HANDLE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandleType<enum_DisplayServer_HandleType>`{.interpreted-text
role="ref"} **DISPLAY_HANDLE** = `0`

Display handle:

- Linux (X11): `X11::Display*` for the display.
- Linux (Wayland): `wl_display` for the display.
- Android: `EGLDisplay` for the display.

:::: {#class_DisplayServer_constant_WINDOW_HANDLE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandleType<enum_DisplayServer_HandleType>`{.interpreted-text
role="ref"} **WINDOW_HANDLE** = `1`

Window handle:

- Windows: `HWND` for the window.
- Linux (X11): `X11::Window*` for the window.
- Linux (Wayland): `wl_surface` for the window.
- macOS: `NSWindow*` for the window.
- iOS: `UIViewController*` for the view controller.
- Android: `jObject` for the activity.

:::: {#class_DisplayServer_constant_WINDOW_VIEW}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandleType<enum_DisplayServer_HandleType>`{.interpreted-text
role="ref"} **WINDOW_VIEW** = `2`

Window view:

- Windows: `HDC` for the window (only with the GL Compatibility
  renderer).
- macOS: `NSView*` for the window main view.
- iOS: `UIView*` for the window main view.

:::: {#class_DisplayServer_constant_OPENGL_CONTEXT}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandleType<enum_DisplayServer_HandleType>`{.interpreted-text
role="ref"} **OPENGL_CONTEXT** = `3`

OpenGL context (only with the GL Compatibility renderer):

- Windows: `HGLRC` for the window (native GL), or `EGLContext` for the
  window (ANGLE).
- Linux (X11): `GLXContext*` for the window.
- Linux (Wayland): `EGLContext` for the window.
- macOS: `NSOpenGLContext*` for the window (native GL), or `EGLContext`
  for the window (ANGLE).
- Android: `EGLContext` for the window.

:::: {#class_DisplayServer_constant_EGL_DISPLAY}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandleType<enum_DisplayServer_HandleType>`{.interpreted-text
role="ref"} **EGL_DISPLAY** = `4`

- Windows: `EGLDisplay` for the window (ANGLE).
- macOS: `EGLDisplay` for the window (ANGLE).
- Linux (Wayland): `EGLDisplay` for the window.

:::: {#class_DisplayServer_constant_EGL_CONFIG}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`HandleType<enum_DisplayServer_HandleType>`{.interpreted-text
role="ref"} **EGL_CONFIG** = `5`

- Windows: `EGLConfig` for the window (ANGLE).
- macOS: `EGLConfig` for the window (ANGLE).
- Linux (Wayland): `EGLConfig` for the window.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_DisplayServer_TTSUtteranceEvent}
::: {.rst-class}
classref-enumeration
:::
::::

enum **TTSUtteranceEvent**:
`🔗<enum_DisplayServer_TTSUtteranceEvent>`{.interpreted-text role="ref"}

:::: {#class_DisplayServer_constant_TTS_UTTERANCE_STARTED}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`TTSUtteranceEvent<enum_DisplayServer_TTSUtteranceEvent>`{.interpreted-text
role="ref"} **TTS_UTTERANCE_STARTED** = `0`

Utterance has begun to be spoken.

:::: {#class_DisplayServer_constant_TTS_UTTERANCE_ENDED}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`TTSUtteranceEvent<enum_DisplayServer_TTSUtteranceEvent>`{.interpreted-text
role="ref"} **TTS_UTTERANCE_ENDED** = `1`

Utterance was successfully finished.

:::: {#class_DisplayServer_constant_TTS_UTTERANCE_CANCELED}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`TTSUtteranceEvent<enum_DisplayServer_TTSUtteranceEvent>`{.interpreted-text
role="ref"} **TTS_UTTERANCE_CANCELED** = `2`

Utterance was canceled, or TTS service was unable to process it.

:::: {#class_DisplayServer_constant_TTS_UTTERANCE_BOUNDARY}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`TTSUtteranceEvent<enum_DisplayServer_TTSUtteranceEvent>`{.interpreted-text
role="ref"} **TTS_UTTERANCE_BOUNDARY** = `3`

Utterance reached a word or sentence boundary.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Constants

:::: {#class_DisplayServer_constant_SCREEN_WITH_MOUSE_FOCUS}
::: {.rst-class}
classref-constant
:::
::::

**SCREEN_WITH_MOUSE_FOCUS** = `-4`
`🔗<class_DisplayServer_constant_SCREEN_WITH_MOUSE_FOCUS>`{.interpreted-text
role="ref"}

Represents the screen containing the mouse pointer.

\*\*Note:\*\* On Linux (Wayland), this constant always represents the
screen at index `0`.

:::: {#class_DisplayServer_constant_SCREEN_WITH_KEYBOARD_FOCUS}
::: {.rst-class}
classref-constant
:::
::::

**SCREEN_WITH_KEYBOARD_FOCUS** = `-3`
`🔗<class_DisplayServer_constant_SCREEN_WITH_KEYBOARD_FOCUS>`{.interpreted-text
role="ref"}

Represents the screen containing the window with the keyboard focus.

\*\*Note:\*\* On Linux (Wayland), this constant always represents the
screen at index `0`.

:::: {#class_DisplayServer_constant_SCREEN_PRIMARY}
::: {.rst-class}
classref-constant
:::
::::

**SCREEN_PRIMARY** = `-2`
`🔗<class_DisplayServer_constant_SCREEN_PRIMARY>`{.interpreted-text
role="ref"}

Represents the primary screen.

\*\*Note:\*\* On Linux (Wayland), this constant always represents the
screen at index `0`.

:::: {#class_DisplayServer_constant_SCREEN_OF_MAIN_WINDOW}
::: {.rst-class}
classref-constant
:::
::::

**SCREEN_OF_MAIN_WINDOW** = `-1`
`🔗<class_DisplayServer_constant_SCREEN_OF_MAIN_WINDOW>`{.interpreted-text
role="ref"}

Represents the screen where the main window is located. This is usually
the default value in functions that allow specifying one of several
screens.

\*\*Note:\*\* On Linux (Wayland), this constant always represents the
screen at index `0`.

:::: {#class_DisplayServer_constant_MAIN_WINDOW_ID}
::: {.rst-class}
classref-constant
:::
::::

**MAIN_WINDOW_ID** = `0`
`🔗<class_DisplayServer_constant_MAIN_WINDOW_ID>`{.interpreted-text
role="ref"}

The ID of the main window spawned by the engine, which can be passed to
methods expecting a `window_id`.

:::: {#class_DisplayServer_constant_INVALID_WINDOW_ID}
::: {.rst-class}
classref-constant
:::
::::

**INVALID_WINDOW_ID** = `-1`
`🔗<class_DisplayServer_constant_INVALID_WINDOW_ID>`{.interpreted-text
role="ref"}

The ID that refers to a nonexistent window. This is returned by some
**DisplayServer** methods if no window matches the requested result.

:::: {#class_DisplayServer_constant_INVALID_INDICATOR_ID}
::: {.rst-class}
classref-constant
:::
::::

**INVALID_INDICATOR_ID** = `-1`
`🔗<class_DisplayServer_constant_INVALID_INDICATOR_ID>`{.interpreted-text
role="ref"}

The ID that refers to a nonexistent application status indicator.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_DisplayServer_method_clipboard_get}
::: {.rst-class}
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **clipboard_get**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_clipboard_get>`{.interpreted-text
role="ref"}

Returns the user\'s clipboard as a string if possible.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_clipboard_get_image}
::: {.rst-class}
classref-method
:::
::::

`Image<class_Image>`{.interpreted-text role="ref"}
**clipboard_get_image**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_clipboard_get_image>`{.interpreted-text
role="ref"}

Returns the user\'s clipboard as an image if possible.

\*\*Note:\*\* This method uses the copied pixel data, e.g. from a image
editing software or a web browser, not an image file copied from file
explorer.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_clipboard_get_primary}
::: {.rst-class}
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**clipboard_get_primary**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_clipboard_get_primary>`{.interpreted-text
role="ref"}

Returns the user\'s
[primary](https://unix.stackexchange.com/questions/139191/whats-the-difference-between-primary-selection-and-clipboard-buffer)
clipboard as a string if possible. This is the clipboard that is set
when the user selects text in any application, rather than when pressing
`Ctrl + C`{.interpreted-text role="kbd"}. The clipboard data can then be
pasted by clicking the middle mouse button in any application that
supports the primary clipboard mechanism.

\*\*Note:\*\* This method is only implemented on Linux (X11/Wayland).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_clipboard_has}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **clipboard_has**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_clipboard_has>`{.interpreted-text
role="ref"}

Returns `true` if there is a text content on the user\'s clipboard.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_clipboard_has_image}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**clipboard_has_image**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_clipboard_has_image>`{.interpreted-text
role="ref"}

Returns `true` if there is an image content on the user\'s clipboard.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_clipboard_set}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clipboard_set**(clipboard: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_DisplayServer_method_clipboard_set>`{.interpreted-text
role="ref"}

Sets the user\'s clipboard content to the given string.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_clipboard_set_primary}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clipboard_set_primary**(clipboard_primary:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_DisplayServer_method_clipboard_set_primary>`{.interpreted-text
role="ref"}

Sets the user\'s
[primary](https://unix.stackexchange.com/questions/139191/whats-the-difference-between-primary-selection-and-clipboard-buffer)
clipboard content to the given string. This is the clipboard that is set
when the user selects text in any application, rather than when pressing
`Ctrl + C`{.interpreted-text role="kbd"}. The clipboard data can then be
pasted by clicking the middle mouse button in any application that
supports the primary clipboard mechanism.

\*\*Note:\*\* This method is only implemented on Linux (X11/Wayland).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_create_status_indicator}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**create_status_indicator**(icon:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}, tooltip:
`String<class_String>`{.interpreted-text role="ref"}, callback:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_DisplayServer_method_create_status_indicator>`{.interpreted-text
role="ref"}

Creates a new application status indicator with the specified icon,
tooltip, and activation callback.

`callback` should take two arguments: the pressed mouse button (one of
the `MouseButton<enum_@GlobalScope_MouseButton>`{.interpreted-text
role="ref"} constants) and the click position in screen coordinates (a
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_cursor_get_shape}
::: {.rst-class}
classref-method
:::
::::

`CursorShape<enum_DisplayServer_CursorShape>`{.interpreted-text
role="ref"} **cursor_get_shape**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_cursor_get_shape>`{.interpreted-text
role="ref"}

Returns the default mouse cursor shape set by
`cursor_set_shape<class_DisplayServer_method_cursor_set_shape>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_cursor_set_custom_image}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**cursor_set_custom_image**(cursor:
`Resource<class_Resource>`{.interpreted-text role="ref"}, shape:
`CursorShape<enum_DisplayServer_CursorShape>`{.interpreted-text
role="ref"} = 0, hotspot: `Vector2<class_Vector2>`{.interpreted-text
role="ref"} = Vector2(0, 0))
`🔗<class_DisplayServer_method_cursor_set_custom_image>`{.interpreted-text
role="ref"}

Sets a custom mouse cursor image for the given `shape`. This means the
user\'s operating system and mouse cursor theme will no longer influence
the mouse cursor\'s appearance.

`cursor` can be either a `Texture2D<class_Texture2D>`{.interpreted-text
role="ref"} or an `Image<class_Image>`{.interpreted-text role="ref"},
and it should not be larger than 256×256 to display correctly.
Optionally, `hotspot` can be set to offset the image\'s position
relative to the click point. By default, `hotspot` is set to the
top-left corner of the image. See also
`cursor_set_shape<class_DisplayServer_method_cursor_set_shape>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_cursor_set_shape}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**cursor_set_shape**(shape:
`CursorShape<enum_DisplayServer_CursorShape>`{.interpreted-text
role="ref"})
`🔗<class_DisplayServer_method_cursor_set_shape>`{.interpreted-text
role="ref"}

Sets the default mouse cursor shape. The cursor\'s appearance will vary
depending on the user\'s operating system and mouse cursor theme. See
also
`cursor_get_shape<class_DisplayServer_method_cursor_get_shape>`{.interpreted-text
role="ref"} and
`cursor_set_custom_image<class_DisplayServer_method_cursor_set_custom_image>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_delete_status_indicator}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**delete_status_indicator**(id: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_DisplayServer_method_delete_status_indicator>`{.interpreted-text
role="ref"}

Removes the application status indicator.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_dialog_input_text}
::: {.rst-class}
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**dialog_input_text**(title: `String<class_String>`{.interpreted-text
role="ref"}, description: `String<class_String>`{.interpreted-text
role="ref"}, existing_text: `String<class_String>`{.interpreted-text
role="ref"}, callback: `Callable<class_Callable>`{.interpreted-text
role="ref"})
`🔗<class_DisplayServer_method_dialog_input_text>`{.interpreted-text
role="ref"}

Shows a text input dialog which uses the operating system\'s native
look-and-feel. `callback` should accept a single
`String<class_String>`{.interpreted-text role="ref"} parameter which
contains the text field\'s contents.

\*\*Note:\*\* This method is implemented if the display server has the
`FEATURE_NATIVE_DIALOG_INPUT<class_DisplayServer_constant_FEATURE_NATIVE_DIALOG_INPUT>`{.interpreted-text
role="ref"} feature. Supported platforms include macOS and Windows.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_dialog_show}
::: {.rst-class}
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**dialog_show**(title: `String<class_String>`{.interpreted-text
role="ref"}, description: `String<class_String>`{.interpreted-text
role="ref"}, buttons:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}, callback: `Callable<class_Callable>`{.interpreted-text
role="ref"})
`🔗<class_DisplayServer_method_dialog_show>`{.interpreted-text
role="ref"}

Shows a text dialog which uses the operating system\'s native
look-and-feel. `callback` should accept a single
`int<class_int>`{.interpreted-text role="ref"} parameter which
corresponds to the index of the pressed button.

\*\*Note:\*\* This method is implemented if the display server has the
`FEATURE_NATIVE_DIALOG<class_DisplayServer_constant_FEATURE_NATIVE_DIALOG>`{.interpreted-text
role="ref"} feature. Supported platforms include macOS and Windows.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_enable_for_stealing_focus}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**enable_for_stealing_focus**(process_id:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_DisplayServer_method_enable_for_stealing_focus>`{.interpreted-text
role="ref"}

Allows the `process_id` PID to steal focus from this window. In other
words, this disables the operating system\'s focus stealing protection
for the specified PID.

\*\*Note:\*\* This method is implemented only on Windows.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_file_dialog_show}
::: {.rst-class}
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**file_dialog_show**(title: `String<class_String>`{.interpreted-text
role="ref"}, current_directory: `String<class_String>`{.interpreted-text
role="ref"}, filename: `String<class_String>`{.interpreted-text
role="ref"}, show_hidden: `bool<class_bool>`{.interpreted-text
role="ref"}, mode:
`FileDialogMode<enum_DisplayServer_FileDialogMode>`{.interpreted-text
role="ref"}, filters:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}, callback: `Callable<class_Callable>`{.interpreted-text
role="ref"})
`🔗<class_DisplayServer_method_file_dialog_show>`{.interpreted-text
role="ref"}

Displays OS native dialog for selecting files or directories in the file
system.

Each filter string in the `filters` array should be formatted like this:
`*.txt,*.doc;Text Files`. The description text of the filter is optional
and can be omitted. See also
`FileDialog.filters<class_FileDialog_property_filters>`{.interpreted-text
role="ref"}.

Callbacks have the following arguments:
`status: bool, selected_paths: PackedStringArray, selected_filter_index: int`.

\*\*Note:\*\* This method is implemented if the display server has the
`FEATURE_NATIVE_DIALOG_FILE<class_DisplayServer_constant_FEATURE_NATIVE_DIALOG_FILE>`{.interpreted-text
role="ref"} feature. Supported platforms include Linux (X11/Wayland),
Windows, and macOS.

\*\*Note:\*\* `current_directory` might be ignored.

\*\*Note:\*\* On Linux, `show_hidden` is ignored.

\*\*Note:\*\* On macOS, native file dialogs have no title.

\*\*Note:\*\* On macOS, sandboxed apps will save security-scoped
bookmarks to retain access to the opened folders across multiple
sessions. Use
`OS.get_granted_permissions<class_OS_method_get_granted_permissions>`{.interpreted-text
role="ref"} to get a list of saved bookmarks.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_file_dialog_with_options_show}
::: {.rst-class}
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**file_dialog_with_options_show**(title:
`String<class_String>`{.interpreted-text role="ref"}, current_directory:
`String<class_String>`{.interpreted-text role="ref"}, root:
`String<class_String>`{.interpreted-text role="ref"}, filename:
`String<class_String>`{.interpreted-text role="ref"}, show_hidden:
`bool<class_bool>`{.interpreted-text role="ref"}, mode:
`FileDialogMode<enum_DisplayServer_FileDialogMode>`{.interpreted-text
role="ref"}, filters:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}, options: `Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\], callback: `Callable<class_Callable>`{.interpreted-text
role="ref"})
`🔗<class_DisplayServer_method_file_dialog_with_options_show>`{.interpreted-text
role="ref"}

Displays OS native dialog for selecting files or directories in the file
system with additional user selectable options.

Each filter string in the `filters` array should be formatted like this:
`*.txt,*.doc;Text Files`. The description text of the filter is optional
and can be omitted. See also
`FileDialog.filters<class_FileDialog_property_filters>`{.interpreted-text
role="ref"}.

`options` is array of `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}s with the following keys:

- `"name"` - option\'s name `String<class_String>`{.interpreted-text
  role="ref"}.
- `"values"` -
  `PackedStringArray<class_PackedStringArray>`{.interpreted-text
  role="ref"} of values. If empty, boolean option (check box) is used.
- `"default"` - default selected option index
  (`int<class_int>`{.interpreted-text role="ref"}) or default boolean
  value (`bool<class_bool>`{.interpreted-text role="ref"}).

Callbacks have the following arguments:
`status: bool, selected_paths: PackedStringArray, selected_filter_index: int, selected_option: Dictionary`.

\*\*Note:\*\* This method is implemented if the display server has the
`FEATURE_NATIVE_DIALOG_FILE<class_DisplayServer_constant_FEATURE_NATIVE_DIALOG_FILE>`{.interpreted-text
role="ref"} feature. Supported platforms include Linux (X11/Wayland),
Windows, and macOS.

\*\*Note:\*\* `current_directory` might be ignored.

\*\*Note:\*\* On Linux (X11), `show_hidden` is ignored.

\*\*Note:\*\* On macOS, native file dialogs have no title.

\*\*Note:\*\* On macOS, sandboxed apps will save security-scoped
bookmarks to retain access to the opened folders across multiple
sessions. Use
`OS.get_granted_permissions<class_OS_method_get_granted_permissions>`{.interpreted-text
role="ref"} to get a list of saved bookmarks.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_force_process_and_drop_events}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**force_process_and_drop_events**()
`🔗<class_DisplayServer_method_force_process_and_drop_events>`{.interpreted-text
role="ref"}

Forces window manager processing while ignoring all
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"}s. See also
`process_events<class_DisplayServer_method_process_events>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This method is implemented on Windows and macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_get_accent_color}
::: {.rst-class}
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**get_accent_color**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_get_accent_color>`{.interpreted-text
role="ref"}

Returns OS theme accent color. Returns `Color(0, 0, 0, 0)`, if accent
color is unknown.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_get_base_color}
::: {.rst-class}
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **get_base_color**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_get_base_color>`{.interpreted-text
role="ref"}

Returns the OS theme base color (default control background). Returns
`Color(0, 0, 0, 0)` if the base color is unknown.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_get_display_cutouts}
::: {.rst-class}
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Rect2<class_Rect2>`{.interpreted-text role="ref"}\]
**get_display_cutouts**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_get_display_cutouts>`{.interpreted-text
role="ref"}

Returns an `Array<class_Array>`{.interpreted-text role="ref"} of
`Rect2<class_Rect2>`{.interpreted-text role="ref"}, each of which is the
bounding rectangle for a display cutout or notch. These are
non-functional areas on edge-to-edge screens used by cameras and
sensors. Returns an empty array if the device does not have cutouts. See
also
`get_display_safe_area<class_DisplayServer_method_get_display_safe_area>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Currently only implemented on Android. Other platforms
will return an empty array even if they do have display cutouts or
notches.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_get_display_safe_area}
::: {.rst-class}
classref-method
:::
::::

`Rect2i<class_Rect2i>`{.interpreted-text role="ref"}
**get_display_safe_area**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_get_display_safe_area>`{.interpreted-text
role="ref"}

Returns the unobscured area of the display where interactive controls
should be rendered. See also
`get_display_cutouts<class_DisplayServer_method_get_display_cutouts>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_get_keyboard_focus_screen}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_keyboard_focus_screen**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_get_keyboard_focus_screen>`{.interpreted-text
role="ref"}

Returns the index of the screen containing the window with the keyboard
focus, or the primary screen if there\'s no focused window.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_get_name}
::: {.rst-class}
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_name**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_DisplayServer_method_get_name>`{.interpreted-text
role="ref"}

Returns the name of the **DisplayServer** currently in use. Most
operating systems only have a single **DisplayServer**, but Linux has
access to more than one **DisplayServer** (currently X11 and Wayland).

The names of built-in display servers are `Windows`, `macOS`, `X11`
(Linux), `Wayland` (Linux), `Android`, `iOS`, `web` (HTML5), and
`headless` (when started with the `--headless`
`command line argument <../tutorials/editor/command_line_tutorial>`{.interpreted-text
role="doc"}).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_get_primary_screen}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_primary_screen**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_get_primary_screen>`{.interpreted-text
role="ref"}

Returns index of the primary screen.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_get_screen_count}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_screen_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_get_screen_count>`{.interpreted-text
role="ref"}

Returns the number of displays available.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_get_screen_from_rect}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_screen_from_rect**(rect: `Rect2<class_Rect2>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_get_screen_from_rect>`{.interpreted-text
role="ref"}

Returns index of the screen which contains specified rectangle.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_get_swap_cancel_ok}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_swap_cancel_ok**()
`🔗<class_DisplayServer_method_get_swap_cancel_ok>`{.interpreted-text
role="ref"}

Returns `true` if positions of **OK** and **Cancel** buttons are swapped
in dialogs. This is enabled by default on Windows to follow interface
conventions, and be toggled by changing
`ProjectSettings.gui/common/swap_cancel_ok<class_ProjectSettings_property_gui/common/swap_cancel_ok>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This doesn\'t affect native dialogs such as the ones
spawned by
`dialog_show<class_DisplayServer_method_dialog_show>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_get_window_at_screen_position}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_window_at_screen_position**(position:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_get_window_at_screen_position>`{.interpreted-text
role="ref"}

Returns the ID of the window at the specified screen `position` (in
pixels). On multi-monitor setups, the screen position is relative to the
virtual desktop area. On multi-monitor setups with different screen
resolutions or orientations, the origin may be located outside any
display like this:

``` text
* (0, 0)        +-------+
                |       |
+-------------+ |       |
|             | |       |
|             | |       |
+-------------+ +-------+
```

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_get_window_list}
::: {.rst-class}
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**get_window_list**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_get_window_list>`{.interpreted-text
role="ref"}

Returns the list of Godot window IDs belonging to this process.

\*\*Note:\*\* Native dialogs are not included in this list.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_add_check_item}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**global_menu_add_check_item**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, label:
`String<class_String>`{.interpreted-text role="ref"}, callback:
`Callable<class_Callable>`{.interpreted-text role="ref"} = Callable(),
key_callback: `Callable<class_Callable>`{.interpreted-text role="ref"} =
Callable(), tag: `Variant<class_Variant>`{.interpreted-text role="ref"}
= null, accelerator: `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"} = 0, index: `int<class_int>`{.interpreted-text role="ref"} =
-1)
`🔗<class_DisplayServer_method_global_menu_add_check_item>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Adds a new checkable item with text `label` to the global menu with ID
`menu_root`.

Returns index of the inserted item, it\'s not guaranteed to be the same
as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut
that can be pressed to trigger the menu button even if it\'s not
currently open. The `accelerator` is generally a combination of
`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`{.interpreted-text
role="ref"}s and `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"}s using bitwise OR such as `KEY_MASK_CTRL | KEY_A`
(`Ctrl + A`{.interpreted-text role="kbd"}).

\*\*Note:\*\* The `callback` and `key_callback` Callables need to accept
exactly one Variant parameter, the parameter passed to the Callables
will be the value passed to `tag`.

\*\*Note:\*\* This method is implemented only on macOS.

\*\*Supported system menu IDs:\*\*

``` text
"_main" - Main menu (macOS).
"_dock" - Dock popup menu (macOS).
"_apple" - Apple menu (macOS, custom items added before "Services").
"_window" - Window menu (macOS, custom items added after "Bring All to Front").
"_help" - Help menu (macOS).
```

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_add_icon_check_item}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**global_menu_add_icon_check_item**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, icon:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}, label:
`String<class_String>`{.interpreted-text role="ref"}, callback:
`Callable<class_Callable>`{.interpreted-text role="ref"} = Callable(),
key_callback: `Callable<class_Callable>`{.interpreted-text role="ref"} =
Callable(), tag: `Variant<class_Variant>`{.interpreted-text role="ref"}
= null, accelerator: `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"} = 0, index: `int<class_int>`{.interpreted-text role="ref"} =
-1)
`🔗<class_DisplayServer_method_global_menu_add_icon_check_item>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Adds a new checkable item with text `label` and icon `icon` to the
global menu with ID `menu_root`.

Returns index of the inserted item, it\'s not guaranteed to be the same
as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut
that can be pressed to trigger the menu button even if it\'s not
currently open. The `accelerator` is generally a combination of
`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`{.interpreted-text
role="ref"}s and `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"}s using bitwise OR such as `KEY_MASK_CTRL | KEY_A`
(`Ctrl + A`{.interpreted-text role="kbd"}).

\*\*Note:\*\* The `callback` and `key_callback` Callables need to accept
exactly one Variant parameter, the parameter passed to the Callables
will be the value passed to `tag`.

\*\*Note:\*\* This method is implemented only on macOS.

\*\*Supported system menu IDs:\*\*

``` text
"_main" - Main menu (macOS).
"_dock" - Dock popup menu (macOS).
"_apple" - Apple menu (macOS, custom items added before "Services").
"_window" - Window menu (macOS, custom items added after "Bring All to Front").
"_help" - Help menu (macOS).
```

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_add_icon_item}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**global_menu_add_icon_item**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, icon:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}, label:
`String<class_String>`{.interpreted-text role="ref"}, callback:
`Callable<class_Callable>`{.interpreted-text role="ref"} = Callable(),
key_callback: `Callable<class_Callable>`{.interpreted-text role="ref"} =
Callable(), tag: `Variant<class_Variant>`{.interpreted-text role="ref"}
= null, accelerator: `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"} = 0, index: `int<class_int>`{.interpreted-text role="ref"} =
-1)
`🔗<class_DisplayServer_method_global_menu_add_icon_item>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Adds a new item with text `label` and icon `icon` to the global menu
with ID `menu_root`.

Returns index of the inserted item, it\'s not guaranteed to be the same
as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut
that can be pressed to trigger the menu button even if it\'s not
currently open. The `accelerator` is generally a combination of
`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`{.interpreted-text
role="ref"}s and `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"}s using bitwise OR such as `KEY_MASK_CTRL | KEY_A`
(`Ctrl + A`{.interpreted-text role="kbd"}).

\*\*Note:\*\* The `callback` and `key_callback` Callables need to accept
exactly one Variant parameter, the parameter passed to the Callables
will be the value passed to `tag`.

\*\*Note:\*\* This method is implemented only on macOS.

\*\*Supported system menu IDs:\*\*

``` text
"_main" - Main menu (macOS).
"_dock" - Dock popup menu (macOS).
"_apple" - Apple menu (macOS, custom items added before "Services").
"_window" - Window menu (macOS, custom items added after "Bring All to Front").
"_help" - Help menu (macOS).
```

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_add_icon_radio_check_item}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**global_menu_add_icon_radio_check_item**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, icon:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}, label:
`String<class_String>`{.interpreted-text role="ref"}, callback:
`Callable<class_Callable>`{.interpreted-text role="ref"} = Callable(),
key_callback: `Callable<class_Callable>`{.interpreted-text role="ref"} =
Callable(), tag: `Variant<class_Variant>`{.interpreted-text role="ref"}
= null, accelerator: `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"} = 0, index: `int<class_int>`{.interpreted-text role="ref"} =
-1)
`🔗<class_DisplayServer_method_global_menu_add_icon_radio_check_item>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Adds a new radio-checkable item with text `label` and icon `icon` to the
global menu with ID `menu_root`.

Returns index of the inserted item, it\'s not guaranteed to be the same
as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut
that can be pressed to trigger the menu button even if it\'s not
currently open. The `accelerator` is generally a combination of
`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`{.interpreted-text
role="ref"}s and `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"}s using bitwise OR such as `KEY_MASK_CTRL | KEY_A`
(`Ctrl + A`{.interpreted-text role="kbd"}).

\*\*Note:\*\* Radio-checkable items just display a checkmark, but don\'t
have any built-in checking behavior and must be checked/unchecked
manually. See
`global_menu_set_item_checked<class_DisplayServer_method_global_menu_set_item_checked>`{.interpreted-text
role="ref"} for more info on how to control it.

\*\*Note:\*\* The `callback` and `key_callback` Callables need to accept
exactly one Variant parameter, the parameter passed to the Callables
will be the value passed to `tag`.

\*\*Note:\*\* This method is implemented only on macOS.

\*\*Supported system menu IDs:\*\*

``` text
"_main" - Main menu (macOS).
"_dock" - Dock popup menu (macOS).
"_apple" - Apple menu (macOS, custom items added before "Services").
"_window" - Window menu (macOS, custom items added after "Bring All to Front").
"_help" - Help menu (macOS).
```

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_add_item}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**global_menu_add_item**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, label:
`String<class_String>`{.interpreted-text role="ref"}, callback:
`Callable<class_Callable>`{.interpreted-text role="ref"} = Callable(),
key_callback: `Callable<class_Callable>`{.interpreted-text role="ref"} =
Callable(), tag: `Variant<class_Variant>`{.interpreted-text role="ref"}
= null, accelerator: `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"} = 0, index: `int<class_int>`{.interpreted-text role="ref"} =
-1)
`🔗<class_DisplayServer_method_global_menu_add_item>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Adds a new item with text `label` to the global menu with ID
`menu_root`.

Returns index of the inserted item, it\'s not guaranteed to be the same
as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut
that can be pressed to trigger the menu button even if it\'s not
currently open. The `accelerator` is generally a combination of
`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`{.interpreted-text
role="ref"}s and `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"}s using bitwise OR such as `KEY_MASK_CTRL | KEY_A`
(`Ctrl + A`{.interpreted-text role="kbd"}).

\*\*Note:\*\* The `callback` and `key_callback` Callables need to accept
exactly one Variant parameter, the parameter passed to the Callables
will be the value passed to `tag`.

\*\*Note:\*\* This method is implemented only on macOS.

\*\*Supported system menu IDs:\*\*

``` text
"_main" - Main menu (macOS).
"_dock" - Dock popup menu (macOS).
"_apple" - Apple menu (macOS, custom items added before "Services").
"_window" - Window menu (macOS, custom items added after "Bring All to Front").
"_help" - Help menu (macOS).
```

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_add_multistate_item}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**global_menu_add_multistate_item**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, label:
`String<class_String>`{.interpreted-text role="ref"}, max_states:
`int<class_int>`{.interpreted-text role="ref"}, default_state:
`int<class_int>`{.interpreted-text role="ref"}, callback:
`Callable<class_Callable>`{.interpreted-text role="ref"} = Callable(),
key_callback: `Callable<class_Callable>`{.interpreted-text role="ref"} =
Callable(), tag: `Variant<class_Variant>`{.interpreted-text role="ref"}
= null, accelerator: `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"} = 0, index: `int<class_int>`{.interpreted-text role="ref"} =
-1)
`🔗<class_DisplayServer_method_global_menu_add_multistate_item>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Adds a new item with text `label` to the global menu with ID
`menu_root`.

Contrarily to normal binary items, multistate items can have more than
two states, as defined by `max_states`. Each press or activate of the
item will increase the state by one. The default value is defined by
`default_state`.

Returns index of the inserted item, it\'s not guaranteed to be the same
as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut
that can be pressed to trigger the menu button even if it\'s not
currently open. The `accelerator` is generally a combination of
`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`{.interpreted-text
role="ref"}s and `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"}s using bitwise OR such as `KEY_MASK_CTRL | KEY_A`
(`Ctrl + A`{.interpreted-text role="kbd"}).

\*\*Note:\*\* By default, there\'s no indication of the current item
state, it should be changed manually.

\*\*Note:\*\* The `callback` and `key_callback` Callables need to accept
exactly one Variant parameter, the parameter passed to the Callables
will be the value passed to `tag`.

\*\*Note:\*\* This method is implemented only on macOS.

\*\*Supported system menu IDs:\*\*

``` text
"_main" - Main menu (macOS).
"_dock" - Dock popup menu (macOS).
"_apple" - Apple menu (macOS, custom items added before "Services").
"_window" - Window menu (macOS, custom items added after "Bring All to Front").
"_help" - Help menu (macOS).
```

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_add_radio_check_item}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**global_menu_add_radio_check_item**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, label:
`String<class_String>`{.interpreted-text role="ref"}, callback:
`Callable<class_Callable>`{.interpreted-text role="ref"} = Callable(),
key_callback: `Callable<class_Callable>`{.interpreted-text role="ref"} =
Callable(), tag: `Variant<class_Variant>`{.interpreted-text role="ref"}
= null, accelerator: `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"} = 0, index: `int<class_int>`{.interpreted-text role="ref"} =
-1)
`🔗<class_DisplayServer_method_global_menu_add_radio_check_item>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Adds a new radio-checkable item with text `label` to the global menu
with ID `menu_root`.

Returns index of the inserted item, it\'s not guaranteed to be the same
as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut
that can be pressed to trigger the menu button even if it\'s not
currently open. The `accelerator` is generally a combination of
`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`{.interpreted-text
role="ref"}s and `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"}s using bitwise OR such as `KEY_MASK_CTRL | KEY_A`
(`Ctrl + A`{.interpreted-text role="kbd"}).

\*\*Note:\*\* Radio-checkable items just display a checkmark, but don\'t
have any built-in checking behavior and must be checked/unchecked
manually. See
`global_menu_set_item_checked<class_DisplayServer_method_global_menu_set_item_checked>`{.interpreted-text
role="ref"} for more info on how to control it.

\*\*Note:\*\* The `callback` and `key_callback` Callables need to accept
exactly one Variant parameter, the parameter passed to the Callables
will be the value passed to `tag`.

\*\*Note:\*\* This method is implemented only on macOS.

\*\*Supported system menu IDs:\*\*

``` text
"_main" - Main menu (macOS).
"_dock" - Dock popup menu (macOS).
"_apple" - Apple menu (macOS, custom items added before "Services").
"_window" - Window menu (macOS, custom items added after "Bring All to Front").
"_help" - Help menu (macOS).
```

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_add_separator}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**global_menu_add_separator**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_DisplayServer_method_global_menu_add_separator>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Adds a separator between items to the global menu with ID `menu_root`.
Separators also occupy an index.

Returns index of the inserted item, it\'s not guaranteed to be the same
as `index` value.

\*\*Note:\*\* This method is implemented only on macOS.

\*\*Supported system menu IDs:\*\*

``` text
"_main" - Main menu (macOS).
"_dock" - Dock popup menu (macOS).
"_apple" - Apple menu (macOS, custom items added before "Services").
"_window" - Window menu (macOS, custom items added after "Bring All to Front").
"_help" - Help menu (macOS).
```

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_add_submenu_item}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**global_menu_add_submenu_item**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, label:
`String<class_String>`{.interpreted-text role="ref"}, submenu:
`String<class_String>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_DisplayServer_method_global_menu_add_submenu_item>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Adds an item that will act as a submenu of the global menu `menu_root`.
The `submenu` argument is the ID of the global menu root that will be
shown when the item is clicked.

Returns index of the inserted item, it\'s not guaranteed to be the same
as `index` value.

\*\*Note:\*\* This method is implemented only on macOS.

\*\*Supported system menu IDs:\*\*

``` text
"_main" - Main menu (macOS).
"_dock" - Dock popup menu (macOS).
"_apple" - Apple menu (macOS, custom items added before "Services").
"_window" - Window menu (macOS, custom items added after "Bring All to Front").
"_help" - Help menu (macOS).
```

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_clear}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**global_menu_clear**(menu_root:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_DisplayServer_method_global_menu_clear>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Removes all items from the global menu with ID `menu_root`.

\*\*Note:\*\* This method is implemented only on macOS.

\*\*Supported system menu IDs:\*\*

``` text
"_main" - Main menu (macOS).
"_dock" - Dock popup menu (macOS).
"_apple" - Apple menu (macOS, custom items added before "Services").
"_window" - Window menu (macOS, custom items added after "Bring All to Front").
"_help" - Help menu (macOS).
```

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_get_item_accelerator}
::: {.rst-class}
classref-method
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**global_menu_get_item_accelerator**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_global_menu_get_item_accelerator>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Returns the accelerator of the item at index `idx`. Accelerators are
special combinations of keys that activate the item, no matter which
control is focused.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_get_item_callback}
::: {.rst-class}
classref-method
:::
::::

`Callable<class_Callable>`{.interpreted-text role="ref"}
**global_menu_get_item_callback**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_global_menu_get_item_callback>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Returns the callback of the item at index `idx`.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_get_item_count}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**global_menu_get_item_count**(menu_root:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_global_menu_get_item_count>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Returns number of items in the global menu with ID `menu_root`.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_get_item_icon}
::: {.rst-class}
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**global_menu_get_item_icon**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_global_menu_get_item_icon>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Returns the icon of the item at index `idx`.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_get_item_indentation_level}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**global_menu_get_item_indentation_level**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_global_menu_get_item_indentation_level>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Returns the horizontal offset of the item at the given `idx`.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_get_item_index_from_tag}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**global_menu_get_item_index_from_tag**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, tag:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_global_menu_get_item_index_from_tag>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Returns the index of the item with the specified `tag`. Indices are
automatically assigned to each item by the engine, and cannot be set
manually.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_get_item_index_from_text}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**global_menu_get_item_index_from_text**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, text:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_global_menu_get_item_index_from_text>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Returns the index of the item with the specified `text`. Indices are
automatically assigned to each item by the engine, and cannot be set
manually.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_get_item_key_callback}
::: {.rst-class}
classref-method
:::
::::

`Callable<class_Callable>`{.interpreted-text role="ref"}
**global_menu_get_item_key_callback**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_global_menu_get_item_key_callback>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Returns the callback of the item accelerator at index `idx`.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_get_item_max_states}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**global_menu_get_item_max_states**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_global_menu_get_item_max_states>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Returns number of states of a multistate item. See
`global_menu_add_multistate_item<class_DisplayServer_method_global_menu_add_multistate_item>`{.interpreted-text
role="ref"} for details.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_get_item_state}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**global_menu_get_item_state**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_global_menu_get_item_state>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Returns the state of a multistate item. See
`global_menu_add_multistate_item<class_DisplayServer_method_global_menu_add_multistate_item>`{.interpreted-text
role="ref"} for details.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_get_item_submenu}
::: {.rst-class}
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**global_menu_get_item_submenu**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_global_menu_get_item_submenu>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Returns the submenu ID of the item at index `idx`. See
`global_menu_add_submenu_item<class_DisplayServer_method_global_menu_add_submenu_item>`{.interpreted-text
role="ref"} for more info on how to add a submenu.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_get_item_tag}
::: {.rst-class}
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**global_menu_get_item_tag**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_global_menu_get_item_tag>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Returns the metadata of the specified item, which might be of any type.
You can set it with
`global_menu_set_item_tag<class_DisplayServer_method_global_menu_set_item_tag>`{.interpreted-text
role="ref"}, which provides a simple way of assigning context data to
items.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_get_item_text}
::: {.rst-class}
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**global_menu_get_item_text**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_global_menu_get_item_text>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Returns the text of the item at index `idx`.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_get_item_tooltip}
::: {.rst-class}
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**global_menu_get_item_tooltip**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_global_menu_get_item_tooltip>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Returns the tooltip associated with the specified index `idx`.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_get_system_menu_roots}
::: {.rst-class}
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**global_menu_get_system_menu_roots**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_global_menu_get_system_menu_roots>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Returns Dictionary of supported system menu IDs and names.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_is_item_checkable}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**global_menu_is_item_checkable**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_global_menu_is_item_checkable>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Returns `true` if the item at index `idx` is checkable in some way, i.e.
if it has a checkbox or radio button.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_is_item_checked}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**global_menu_is_item_checked**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_global_menu_is_item_checked>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Returns `true` if the item at index `idx` is checked.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_is_item_disabled}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**global_menu_is_item_disabled**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_global_menu_is_item_disabled>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Returns `true` if the item at index `idx` is disabled. When it is
disabled it can\'t be selected, or its action invoked.

See
`global_menu_set_item_disabled<class_DisplayServer_method_global_menu_set_item_disabled>`{.interpreted-text
role="ref"} for more info on how to disable an item.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_is_item_hidden}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**global_menu_is_item_hidden**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_global_menu_is_item_hidden>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Returns `true` if the item at index `idx` is hidden.

See
`global_menu_set_item_hidden<class_DisplayServer_method_global_menu_set_item_hidden>`{.interpreted-text
role="ref"} for more info on how to hide an item.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_is_item_radio_checkable}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**global_menu_is_item_radio_checkable**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_global_menu_is_item_radio_checkable>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Returns `true` if the item at index `idx` has radio button-style
checkability.

\*\*Note:\*\* This is purely cosmetic; you must add the logic for
checking/unchecking items in radio groups.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_remove_item}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**global_menu_remove_item**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_DisplayServer_method_global_menu_remove_item>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Removes the item at index `idx` from the global menu `menu_root`.

\*\*Note:\*\* The indices of items after the removed item will be
shifted by one.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_set_item_accelerator}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**global_menu_set_item_accelerator**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"}, keycode:
`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"})
`🔗<class_DisplayServer_method_global_menu_set_item_accelerator>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Sets the accelerator of the item at index `idx`. `keycode` can be a
single `Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}, or a
combination of
`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`{.interpreted-text
role="ref"}s and `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"}s using bitwise OR such as `KEY_MASK_CTRL | KEY_A`
(`Ctrl + A`{.interpreted-text role="kbd"}).

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_set_item_callback}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**global_menu_set_item_callback**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"}, callback:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_DisplayServer_method_global_menu_set_item_callback>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Sets the callback of the item at index `idx`. Callback is emitted when
an item is pressed.

\*\*Note:\*\* The `callback` Callable needs to accept exactly one
Variant parameter, the parameter passed to the Callable will be the
value passed to the `tag` parameter when the menu item was created.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_set_item_checkable}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**global_menu_set_item_checkable**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"}, checkable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_DisplayServer_method_global_menu_set_item_checkable>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Sets whether the item at index `idx` has a checkbox. If `false`, sets
the type of the item to plain text.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_set_item_checked}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**global_menu_set_item_checked**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"}, checked:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_DisplayServer_method_global_menu_set_item_checked>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Sets the checkstate status of the item at index `idx`.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_set_item_disabled}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**global_menu_set_item_disabled**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"}, disabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_DisplayServer_method_global_menu_set_item_disabled>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Enables/disables the item at index `idx`. When it is disabled, it can\'t
be selected and its action can\'t be invoked.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_set_item_hidden}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**global_menu_set_item_hidden**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"}, hidden:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_DisplayServer_method_global_menu_set_item_hidden>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Hides/shows the item at index `idx`. When it is hidden, an item does not
appear in a menu and its action cannot be invoked.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_set_item_hover_callbacks}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**global_menu_set_item_hover_callbacks**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"}, callback:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_DisplayServer_method_global_menu_set_item_hover_callbacks>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Sets the callback of the item at index `idx`. The callback is emitted
when an item is hovered.

\*\*Note:\*\* The `callback` Callable needs to accept exactly one
Variant parameter, the parameter passed to the Callable will be the
value passed to the `tag` parameter when the menu item was created.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_set_item_icon}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**global_menu_set_item_icon**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"}, icon:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
`🔗<class_DisplayServer_method_global_menu_set_item_icon>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Replaces the `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
icon of the specified `idx`.

\*\*Note:\*\* This method is implemented only on macOS.

\*\*Note:\*\* This method is not supported by macOS \"\_dock\" menu
items.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_set_item_indentation_level}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**global_menu_set_item_indentation_level**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"}, level:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_DisplayServer_method_global_menu_set_item_indentation_level>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Sets the horizontal offset of the item at the given `idx`.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_set_item_key_callback}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**global_menu_set_item_key_callback**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"}, key_callback:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_DisplayServer_method_global_menu_set_item_key_callback>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Sets the callback of the item at index `idx`. Callback is emitted when
its accelerator is activated.

\*\*Note:\*\* The `key_callback` Callable needs to accept exactly one
Variant parameter, the parameter passed to the Callable will be the
value passed to the `tag` parameter when the menu item was created.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_set_item_max_states}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**global_menu_set_item_max_states**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"}, max_states:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_DisplayServer_method_global_menu_set_item_max_states>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Sets number of state of a multistate item. See
`global_menu_add_multistate_item<class_DisplayServer_method_global_menu_add_multistate_item>`{.interpreted-text
role="ref"} for details.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_set_item_radio_checkable}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**global_menu_set_item_radio_checkable**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"}, checkable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_DisplayServer_method_global_menu_set_item_radio_checkable>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Sets the type of the item at the specified index `idx` to radio button.
If `false`, sets the type of the item to plain text.

\*\*Note:\*\* This is purely cosmetic; you must add the logic for
checking/unchecking items in radio groups.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_set_item_state}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**global_menu_set_item_state**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"}, state:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_DisplayServer_method_global_menu_set_item_state>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Sets the state of a multistate item. See
`global_menu_add_multistate_item<class_DisplayServer_method_global_menu_add_multistate_item>`{.interpreted-text
role="ref"} for details.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_set_item_submenu}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**global_menu_set_item_submenu**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"}, submenu:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_DisplayServer_method_global_menu_set_item_submenu>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Sets the submenu of the item at index `idx`. The submenu is the ID of a
global menu root that would be shown when the item is clicked.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_set_item_tag}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**global_menu_set_item_tag**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"}, tag:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_DisplayServer_method_global_menu_set_item_tag>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Sets the metadata of an item, which may be of any type. You can later
get it with
`global_menu_get_item_tag<class_DisplayServer_method_global_menu_get_item_tag>`{.interpreted-text
role="ref"}, which provides a simple way of assigning context data to
items.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_set_item_text}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**global_menu_set_item_text**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"}, text:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_DisplayServer_method_global_menu_set_item_text>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Sets the text of the item at index `idx`.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_set_item_tooltip}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**global_menu_set_item_tooltip**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"}, tooltip:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_DisplayServer_method_global_menu_set_item_tooltip>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Sets the `String<class_String>`{.interpreted-text role="ref"} tooltip of
the item at the specified index `idx`.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_global_menu_set_popup_callbacks}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**global_menu_set_popup_callbacks**(menu_root:
`String<class_String>`{.interpreted-text role="ref"}, open_callback:
`Callable<class_Callable>`{.interpreted-text role="ref"},
close_callback: `Callable<class_Callable>`{.interpreted-text
role="ref"})
`🔗<class_DisplayServer_method_global_menu_set_popup_callbacks>`{.interpreted-text
role="ref"}

**Deprecated:** Use `NativeMenu<class_NativeMenu>`{.interpreted-text
role="ref"} or `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"} instead.

Registers callables to emit when the menu is respectively about to show
or closed. Callback methods should have zero arguments.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_has_additional_outputs}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_additional_outputs**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_has_additional_outputs>`{.interpreted-text
role="ref"}

Returns `true` if any additional outputs have been registered via
`register_additional_output<class_DisplayServer_method_register_additional_output>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_has_feature}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_feature**(feature:
`Feature<enum_DisplayServer_Feature>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_has_feature>`{.interpreted-text
role="ref"}

Returns `true` if the specified `feature` is supported by the current
**DisplayServer**, `false` otherwise.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_has_hardware_keyboard}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_hardware_keyboard**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_has_hardware_keyboard>`{.interpreted-text
role="ref"}

Returns `true` if hardware keyboard is connected.

\*\*Note:\*\* This method is implemented on Android and iOS, on other
platforms this method always returns `true`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_help_set_search_callbacks}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**help_set_search_callbacks**(search_callback:
`Callable<class_Callable>`{.interpreted-text role="ref"},
action_callback: `Callable<class_Callable>`{.interpreted-text
role="ref"})
`🔗<class_DisplayServer_method_help_set_search_callbacks>`{.interpreted-text
role="ref"}

Sets native help system search callbacks.

`search_callback` has the following arguments:
`String search_string, int result_limit` and return a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} with \"key,
display name\" pairs for the search results. Called when the user enters
search terms in the `Help` menu.

`action_callback` has the following arguments: `String key`. Called when
the user selects a search result in the `Help` menu.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_ime_get_selection}
::: {.rst-class}
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**ime_get_selection**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_ime_get_selection>`{.interpreted-text
role="ref"}

Returns the text selection in the [Input Method
Editor](https://en.wikipedia.org/wiki/Input_method) composition string,
with the `Vector2i<class_Vector2i>`{.interpreted-text role="ref"}\'s `x`
component being the caret position and `y` being the length of the
selection.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_ime_get_text}
::: {.rst-class}
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **ime_get_text**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_ime_get_text>`{.interpreted-text
role="ref"}

Returns the composition string contained within the [Input Method
Editor](https://en.wikipedia.org/wiki/Input_method) window.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_is_dark_mode}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_dark_mode**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_is_dark_mode>`{.interpreted-text
role="ref"}

Returns `true` if OS is using dark mode.

\*\*Note:\*\* This method is implemented on Android, iOS, macOS,
Windows, and Linux (X11/Wayland).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_is_dark_mode_supported}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_dark_mode_supported**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_is_dark_mode_supported>`{.interpreted-text
role="ref"}

Returns `true` if OS supports dark mode.

\*\*Note:\*\* This method is implemented on Android, iOS, macOS,
Windows, and Linux (X11/Wayland).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_is_touchscreen_available}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_touchscreen_available**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_is_touchscreen_available>`{.interpreted-text
role="ref"}

Returns `true` if touch events are available (Android or iOS), the
capability is detected on the Web platform or if
`ProjectSettings.input_devices/pointing/emulate_touch_from_mouse<class_ProjectSettings_property_input_devices/pointing/emulate_touch_from_mouse>`{.interpreted-text
role="ref"} is `true`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_is_window_transparency_available}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_window_transparency_available**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_is_window_transparency_available>`{.interpreted-text
role="ref"}

Returns `true` if the window background can be made transparent. This
method returns `false` if
`ProjectSettings.display/window/per_pixel_transparency/allowed<class_ProjectSettings_property_display/window/per_pixel_transparency/allowed>`{.interpreted-text
role="ref"} is set to `false`, or if transparency is not supported by
the renderer or OS compositor.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_keyboard_get_current_layout}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**keyboard_get_current_layout**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_keyboard_get_current_layout>`{.interpreted-text
role="ref"}

Returns active keyboard layout index.

\*\*Note:\*\* This method is implemented on Linux (X11/Wayland), macOS,
and Windows.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_keyboard_get_keycode_from_physical}
::: {.rst-class}
classref-method
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**keyboard_get_keycode_from_physical**(keycode:
`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_keyboard_get_keycode_from_physical>`{.interpreted-text
role="ref"}

Converts a physical (US QWERTY) `keycode` to one in the active keyboard
layout.

\*\*Note:\*\* This method is implemented on Linux (X11/Wayland), macOS
and Windows.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_keyboard_get_label_from_physical}
::: {.rst-class}
classref-method
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**keyboard_get_label_from_physical**(keycode:
`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_keyboard_get_label_from_physical>`{.interpreted-text
role="ref"}

Converts a physical (US QWERTY) `keycode` to localized label printed on
the key in the active keyboard layout.

\*\*Note:\*\* This method is implemented on Linux (X11/Wayland), macOS
and Windows.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_keyboard_get_layout_count}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**keyboard_get_layout_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_keyboard_get_layout_count>`{.interpreted-text
role="ref"}

Returns the number of keyboard layouts.

\*\*Note:\*\* This method is implemented on Linux (X11/Wayland), macOS
and Windows.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_keyboard_get_layout_language}
::: {.rst-class}
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**keyboard_get_layout_language**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_keyboard_get_layout_language>`{.interpreted-text
role="ref"}

Returns the ISO-639/BCP-47 language code of the keyboard layout at
position `index`.

\*\*Note:\*\* This method is implemented on Linux (X11/Wayland), macOS
and Windows.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_keyboard_get_layout_name}
::: {.rst-class}
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**keyboard_get_layout_name**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_keyboard_get_layout_name>`{.interpreted-text
role="ref"}

Returns the localized name of the keyboard layout at position `index`.

\*\*Note:\*\* This method is implemented on Linux (X11/Wayland), macOS
and Windows.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_keyboard_set_current_layout}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**keyboard_set_current_layout**(index:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_DisplayServer_method_keyboard_set_current_layout>`{.interpreted-text
role="ref"}

Sets the active keyboard layout.

\*\*Note:\*\* This method is implemented on Linux (X11/Wayland), macOS
and Windows.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_mouse_get_button_state}
::: {.rst-class}
classref-method
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`MouseButtonMask<enum_@GlobalScope_MouseButtonMask>`{.interpreted-text
role="ref"}\] **mouse_get_button_state**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_mouse_get_button_state>`{.interpreted-text
role="ref"}

Returns the current state of mouse buttons (whether each button is
pressed) as a bitmask. If multiple mouse buttons are pressed at the same
time, the bits are added together. Equivalent to
`Input.get_mouse_button_mask<class_Input_method_get_mouse_button_mask>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_mouse_get_mode}
::: {.rst-class}
classref-method
:::
::::

`MouseMode<enum_DisplayServer_MouseMode>`{.interpreted-text role="ref"}
**mouse_get_mode**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_mouse_get_mode>`{.interpreted-text
role="ref"}

Returns the current mouse mode. See also
`mouse_set_mode<class_DisplayServer_method_mouse_set_mode>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_mouse_get_position}
::: {.rst-class}
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**mouse_get_position**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_mouse_get_position>`{.interpreted-text
role="ref"}

Returns the mouse cursor\'s current position in screen coordinates.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_mouse_set_mode}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**mouse_set_mode**(mouse_mode:
`MouseMode<enum_DisplayServer_MouseMode>`{.interpreted-text role="ref"})
`🔗<class_DisplayServer_method_mouse_set_mode>`{.interpreted-text
role="ref"}

Sets the current mouse mode. See also
`mouse_get_mode<class_DisplayServer_method_mouse_get_mode>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_process_events}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**process_events**()
`🔗<class_DisplayServer_method_process_events>`{.interpreted-text
role="ref"}

Perform window manager processing, including input flushing. See also
`force_process_and_drop_events<class_DisplayServer_method_force_process_and_drop_events>`{.interpreted-text
role="ref"},
`Input.flush_buffered_events<class_Input_method_flush_buffered_events>`{.interpreted-text
role="ref"} and
`Input.use_accumulated_input<class_Input_property_use_accumulated_input>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_register_additional_output}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**register_additional_output**(object:
`Object<class_Object>`{.interpreted-text role="ref"})
`🔗<class_DisplayServer_method_register_additional_output>`{.interpreted-text
role="ref"}

Registers an `Object<class_Object>`{.interpreted-text role="ref"} which
represents an additional output that will be rendered too, beyond normal
windows. The `Object<class_Object>`{.interpreted-text role="ref"} is
only used as an identifier, which can be later passed to
`unregister_additional_output<class_DisplayServer_method_unregister_additional_output>`{.interpreted-text
role="ref"}.

This can be used to prevent Godot from skipping rendering when no normal
windows are visible.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_screen_get_dpi}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**screen_get_dpi**(screen: `int<class_int>`{.interpreted-text
role="ref"} = -1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_screen_get_dpi>`{.interpreted-text
role="ref"}

Returns the dots per inch density of the specified screen. If `screen`
is
`SCREEN_OF_MAIN_WINDOW<class_DisplayServer_constant_SCREEN_OF_MAIN_WINDOW>`{.interpreted-text
role="ref"} (the default value), a screen with the main window will be
used.

\*\*Note:\*\* On macOS, returned value is inaccurate if fractional
display scaling mode is used.

\*\*Note:\*\* On Android devices, the actual screen densities are
grouped into six generalized densities:

``` text
ldpi - 120 dpi
mdpi - 160 dpi
hdpi - 240 dpi
xhdpi - 320 dpi
xxhdpi - 480 dpi
xxxhdpi - 640 dpi
```

\*\*Note:\*\* This method is implemented on Android, Linux
(X11/Wayland), macOS and Windows. Returns `72` on unsupported platforms.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_screen_get_image}
::: {.rst-class}
classref-method
:::
::::

`Image<class_Image>`{.interpreted-text role="ref"}
**screen_get_image**(screen: `int<class_int>`{.interpreted-text
role="ref"} = -1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_screen_get_image>`{.interpreted-text
role="ref"}

Returns screenshot of the `screen`.

\*\*Note:\*\* This method is implemented on Linux (X11), macOS, and
Windows.

\*\*Note:\*\* On macOS, this method requires \"Screen Recording\"
permission, if permission is not granted it will return desktop
wallpaper color.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_screen_get_max_scale}
::: {.rst-class}
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**screen_get_max_scale**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_screen_get_max_scale>`{.interpreted-text
role="ref"}

Returns the greatest scale factor of all screens.

\*\*Note:\*\* On macOS returned value is `2.0` if there is at least one
hiDPI (Retina) screen in the system, and `1.0` in all other cases.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_screen_get_orientation}
::: {.rst-class}
classref-method
:::
::::

`ScreenOrientation<enum_DisplayServer_ScreenOrientation>`{.interpreted-text
role="ref"} **screen_get_orientation**(screen:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_screen_get_orientation>`{.interpreted-text
role="ref"}

Returns the `screen`\'s current orientation. See also
`screen_set_orientation<class_DisplayServer_method_screen_set_orientation>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This method is implemented on Android and iOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_screen_get_pixel}
::: {.rst-class}
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**screen_get_pixel**(position:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_screen_get_pixel>`{.interpreted-text
role="ref"}

Returns color of the display pixel at the `position`.

\*\*Note:\*\* This method is implemented on Linux (X11), macOS, and
Windows.

\*\*Note:\*\* On macOS, this method requires \"Screen Recording\"
permission, if permission is not granted it will return desktop
wallpaper color.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_screen_get_position}
::: {.rst-class}
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**screen_get_position**(screen: `int<class_int>`{.interpreted-text
role="ref"} = -1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_screen_get_position>`{.interpreted-text
role="ref"}

Returns the screen\'s top-left corner position in pixels. On
multi-monitor setups, the screen position is relative to the virtual
desktop area. On multi-monitor setups with different screen resolutions
or orientations, the origin may be located outside any display like
this:

``` text
* (0, 0)        +-------+
                |       |
+-------------+ |       |
|             | |       |
|             | |       |
+-------------+ +-------+
```

See also
`screen_get_size<class_DisplayServer_method_screen_get_size>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* On Linux (Wayland) this method always returns `(0, 0)`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_screen_get_refresh_rate}
::: {.rst-class}
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**screen_get_refresh_rate**(screen: `int<class_int>`{.interpreted-text
role="ref"} = -1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_screen_get_refresh_rate>`{.interpreted-text
role="ref"}

Returns the current refresh rate of the specified screen. If `screen` is
`SCREEN_OF_MAIN_WINDOW<class_DisplayServer_constant_SCREEN_OF_MAIN_WINDOW>`{.interpreted-text
role="ref"} (the default value), a screen with the main window will be
used.

\*\*Note:\*\* Returns `-1.0` if the DisplayServer fails to find the
refresh rate for the specified screen. On Web,
`screen_get_refresh_rate<class_DisplayServer_method_screen_get_refresh_rate>`{.interpreted-text
role="ref"} will always return `-1.0` as there is no way to retrieve the
refresh rate on that platform.

To fallback to a default refresh rate if the method fails, try:

    var refresh_rate = DisplayServer.screen_get_refresh_rate()
    if refresh_rate < 0:
        refresh_rate = 60.0

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_screen_get_scale}
::: {.rst-class}
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**screen_get_scale**(screen: `int<class_int>`{.interpreted-text
role="ref"} = -1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_screen_get_scale>`{.interpreted-text
role="ref"}

Returns the scale factor of the specified screen by index.

\*\*Note:\*\* On macOS, the returned value is `2.0` for hiDPI (Retina)
screens, and `1.0` for all other cases.

\*\*Note:\*\* On Linux (Wayland), the returned value is accurate only
when `screen` is
`SCREEN_OF_MAIN_WINDOW<class_DisplayServer_constant_SCREEN_OF_MAIN_WINDOW>`{.interpreted-text
role="ref"}. Due to API limitations, passing a direct index will return
a rounded-up integer, if the screen has a fractional scale (e.g. `1.25`
would get rounded up to `2.0`).

\*\*Note:\*\* This method is implemented only on macOS and Linux
(Wayland).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_screen_get_size}
::: {.rst-class}
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**screen_get_size**(screen: `int<class_int>`{.interpreted-text
role="ref"} = -1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_screen_get_size>`{.interpreted-text
role="ref"}

Returns the screen\'s size in pixels. See also
`screen_get_position<class_DisplayServer_method_screen_get_position>`{.interpreted-text
role="ref"} and
`screen_get_usable_rect<class_DisplayServer_method_screen_get_usable_rect>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_screen_get_usable_rect}
::: {.rst-class}
classref-method
:::
::::

`Rect2i<class_Rect2i>`{.interpreted-text role="ref"}
**screen_get_usable_rect**(screen: `int<class_int>`{.interpreted-text
role="ref"} = -1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_screen_get_usable_rect>`{.interpreted-text
role="ref"}

Returns the portion of the screen that is not obstructed by a status bar
in pixels. See also
`screen_get_size<class_DisplayServer_method_screen_get_size>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_screen_is_kept_on}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **screen_is_kept_on**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_screen_is_kept_on>`{.interpreted-text
role="ref"}

Returns `true` if the screen should never be turned off by the operating
system\'s power-saving measures. See also
`screen_set_keep_on<class_DisplayServer_method_screen_set_keep_on>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_screen_set_keep_on}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**screen_set_keep_on**(enable: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_DisplayServer_method_screen_set_keep_on>`{.interpreted-text
role="ref"}

Sets whether the screen should never be turned off by the operating
system\'s power-saving measures. See also
`screen_is_kept_on<class_DisplayServer_method_screen_is_kept_on>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_screen_set_orientation}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**screen_set_orientation**(orientation:
`ScreenOrientation<enum_DisplayServer_ScreenOrientation>`{.interpreted-text
role="ref"}, screen: `int<class_int>`{.interpreted-text role="ref"} =
-1)
`🔗<class_DisplayServer_method_screen_set_orientation>`{.interpreted-text
role="ref"}

Sets the `screen`\'s `orientation`. See also
`screen_get_orientation<class_DisplayServer_method_screen_get_orientation>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* On iOS, this method has no effect if
`ProjectSettings.display/window/handheld/orientation<class_ProjectSettings_property_display/window/handheld/orientation>`{.interpreted-text
role="ref"} is not set to
`SCREEN_SENSOR<class_DisplayServer_constant_SCREEN_SENSOR>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_set_icon}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_icon**(image: `Image<class_Image>`{.interpreted-text role="ref"})
`🔗<class_DisplayServer_method_set_icon>`{.interpreted-text role="ref"}

Sets the window icon (usually displayed in the top-left corner) with an
`Image<class_Image>`{.interpreted-text role="ref"}. To use icons in the
operating system\'s native format, use
`set_native_icon<class_DisplayServer_method_set_native_icon>`{.interpreted-text
role="ref"} instead.

\*\*Note:\*\* Requires support for
`FEATURE_ICON<class_DisplayServer_constant_FEATURE_ICON>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_set_native_icon}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_native_icon**(filename: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_DisplayServer_method_set_native_icon>`{.interpreted-text
role="ref"}

Sets the window icon (usually displayed in the top-left corner) in the
operating system\'s *native* format. The file at `filename` must be in
`.ico` format on Windows or `.icns` on macOS. By using specially crafted
`.ico` or `.icns` icons,
`set_native_icon<class_DisplayServer_method_set_native_icon>`{.interpreted-text
role="ref"} allows specifying different icons depending on the size the
icon is displayed at. This size is determined by the operating system
and user preferences (including the display scale factor). To use icons
in other formats, use
`set_icon<class_DisplayServer_method_set_icon>`{.interpreted-text
role="ref"} instead.

\*\*Note:\*\* Requires support for
`FEATURE_NATIVE_ICON<class_DisplayServer_constant_FEATURE_NATIVE_ICON>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_set_system_theme_change_callback}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_system_theme_change_callback**(callable:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_DisplayServer_method_set_system_theme_change_callback>`{.interpreted-text
role="ref"}

Sets the `callable` that should be called when system theme settings are
changed. Callback method should have zero arguments.

\*\*Note:\*\* This method is implemented on Android, iOS, macOS,
Windows, and Linux (X11/Wayland).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_status_indicator_get_rect}
::: {.rst-class}
classref-method
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"}
**status_indicator_get_rect**(id: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_status_indicator_get_rect>`{.interpreted-text
role="ref"}

Returns the rectangle for the given status indicator `id` in screen
coordinates. If the status indicator is not visible, returns an empty
`Rect2<class_Rect2>`{.interpreted-text role="ref"}.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_status_indicator_set_callback}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**status_indicator_set_callback**(id: `int<class_int>`{.interpreted-text
role="ref"}, callback: `Callable<class_Callable>`{.interpreted-text
role="ref"})
`🔗<class_DisplayServer_method_status_indicator_set_callback>`{.interpreted-text
role="ref"}

Sets the application status indicator activation callback. `callback`
should take two arguments: `int<class_int>`{.interpreted-text
role="ref"} mouse button index (one of
`MouseButton<enum_@GlobalScope_MouseButton>`{.interpreted-text
role="ref"} values) and `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"} click position in screen coordinates.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_status_indicator_set_icon}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**status_indicator_set_icon**(id: `int<class_int>`{.interpreted-text
role="ref"}, icon: `Texture2D<class_Texture2D>`{.interpreted-text
role="ref"})
`🔗<class_DisplayServer_method_status_indicator_set_icon>`{.interpreted-text
role="ref"}

Sets the application status indicator icon.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_status_indicator_set_menu}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**status_indicator_set_menu**(id: `int<class_int>`{.interpreted-text
role="ref"}, menu_rid: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_DisplayServer_method_status_indicator_set_menu>`{.interpreted-text
role="ref"}

Sets the application status indicator native popup menu.

\*\*Note:\*\* On macOS, the menu is activated by any mouse button. Its
activation callback is *not* triggered.

\*\*Note:\*\* On Windows, the menu is activated by the right mouse
button, selecting the status icon and pressing
`Shift + F10`{.interpreted-text role="kbd"}, or the applications key.
The menu\'s activation callback for the other mouse buttons is still
triggered.

\*\*Note:\*\* Native popup is only supported if
`NativeMenu<class_NativeMenu>`{.interpreted-text role="ref"} supports
the
`NativeMenu.FEATURE_POPUP_MENU<class_NativeMenu_constant_FEATURE_POPUP_MENU>`{.interpreted-text
role="ref"} feature.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_status_indicator_set_tooltip}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**status_indicator_set_tooltip**(id: `int<class_int>`{.interpreted-text
role="ref"}, tooltip: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_DisplayServer_method_status_indicator_set_tooltip>`{.interpreted-text
role="ref"}

Sets the application status indicator tooltip.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_tablet_get_current_driver}
::: {.rst-class}
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**tablet_get_current_driver**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_tablet_get_current_driver>`{.interpreted-text
role="ref"}

Returns current active tablet driver name.

\*\*Note:\*\* This method is implemented only on Windows.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_tablet_get_driver_count}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**tablet_get_driver_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_tablet_get_driver_count>`{.interpreted-text
role="ref"}

Returns the total number of available tablet drivers.

\*\*Note:\*\* This method is implemented only on Windows.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_tablet_get_driver_name}
::: {.rst-class}
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**tablet_get_driver_name**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_tablet_get_driver_name>`{.interpreted-text
role="ref"}

Returns the tablet driver name for the given index.

\*\*Note:\*\* This method is implemented only on Windows.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_tablet_set_current_driver}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**tablet_set_current_driver**(name:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_DisplayServer_method_tablet_set_current_driver>`{.interpreted-text
role="ref"}

Set active tablet driver name.

Supported drivers:

- `winink`: Windows Ink API, default (Windows 8.1+ required).
- `wintab`: Wacom Wintab API (compatible device driver required).
- `dummy`: Dummy driver, tablet input is disabled.

\*\*Note:\*\* This method is implemented only on Windows.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_tts_get_voices}
::: {.rst-class}
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **tts_get_voices**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_tts_get_voices>`{.interpreted-text
role="ref"}

Returns an `Array<class_Array>`{.interpreted-text role="ref"} of voice
information dictionaries.

Each `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
contains two `String<class_String>`{.interpreted-text role="ref"}
entries:

- `name` is voice name.
- `id` is voice identifier.
- `language` is language code in `lang_Variant` format. The `lang` part
  is a 2 or 3-letter code based on the ISO-639 standard, in lowercase.
  The `Variant` part is an engine-dependent string describing country,
  region or/and dialect.

Note that Godot depends on system libraries for text-to-speech
functionality. These libraries are installed by default on Windows and
macOS, but not on all Linux distributions. If they are not present, this
method will return an empty list. This applies to both Godot users on
Linux, as well as end-users on Linux running Godot games that use
text-to-speech.

\*\*Note:\*\* This method is implemented on Android, iOS, Web, Linux
(X11/Wayland), macOS, and Windows.

\*\*Note:\*\*
`ProjectSettings.audio/general/text_to_speech<class_ProjectSettings_property_audio/general/text_to_speech>`{.interpreted-text
role="ref"} should be `true` to use text-to-speech.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_tts_get_voices_for_language}
::: {.rst-class}
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **tts_get_voices_for_language**(language:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_tts_get_voices_for_language>`{.interpreted-text
role="ref"}

Returns an
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} of voice identifiers for the `language`.

\*\*Note:\*\* This method is implemented on Android, iOS, Web, Linux
(X11/Wayland), macOS, and Windows.

\*\*Note:\*\*
`ProjectSettings.audio/general/text_to_speech<class_ProjectSettings_property_audio/general/text_to_speech>`{.interpreted-text
role="ref"} should be `true` to use text-to-speech.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_tts_is_paused}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **tts_is_paused**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_tts_is_paused>`{.interpreted-text
role="ref"}

Returns `true` if the synthesizer is in a paused state.

\*\*Note:\*\* This method is implemented on Android, iOS, Web, Linux
(X11/Wayland), macOS, and Windows.

\*\*Note:\*\*
`ProjectSettings.audio/general/text_to_speech<class_ProjectSettings_property_audio/general/text_to_speech>`{.interpreted-text
role="ref"} should be `true` to use text-to-speech.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_tts_is_speaking}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **tts_is_speaking**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_tts_is_speaking>`{.interpreted-text
role="ref"}

Returns `true` if the synthesizer is generating speech, or have
utterance waiting in the queue.

\*\*Note:\*\* This method is implemented on Android, iOS, Web, Linux
(X11/Wayland), macOS, and Windows.

\*\*Note:\*\*
`ProjectSettings.audio/general/text_to_speech<class_ProjectSettings_property_audio/general/text_to_speech>`{.interpreted-text
role="ref"} should be `true` to use text-to-speech.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_tts_pause}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **tts_pause**()
`🔗<class_DisplayServer_method_tts_pause>`{.interpreted-text role="ref"}

Puts the synthesizer into a paused state.

\*\*Note:\*\* This method is implemented on Android, iOS, Web, Linux
(X11/Wayland), macOS, and Windows.

\*\*Note:\*\*
`ProjectSettings.audio/general/text_to_speech<class_ProjectSettings_property_audio/general/text_to_speech>`{.interpreted-text
role="ref"} should be `true` to use text-to-speech.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_tts_resume}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**tts_resume**()
`🔗<class_DisplayServer_method_tts_resume>`{.interpreted-text
role="ref"}

Resumes the synthesizer if it was paused.

\*\*Note:\*\* This method is implemented on Android, iOS, Web, Linux
(X11/Wayland), macOS, and Windows.

\*\*Note:\*\*
`ProjectSettings.audio/general/text_to_speech<class_ProjectSettings_property_audio/general/text_to_speech>`{.interpreted-text
role="ref"} should be `true` to use text-to-speech.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_tts_set_utterance_callback}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**tts_set_utterance_callback**(event:
`TTSUtteranceEvent<enum_DisplayServer_TTSUtteranceEvent>`{.interpreted-text
role="ref"}, callable: `Callable<class_Callable>`{.interpreted-text
role="ref"})
`🔗<class_DisplayServer_method_tts_set_utterance_callback>`{.interpreted-text
role="ref"}

Adds a callback, which is called when the utterance has started,
finished, canceled or reached a text boundary.

- `TTS_UTTERANCE_STARTED<class_DisplayServer_constant_TTS_UTTERANCE_STARTED>`{.interpreted-text
  role="ref"},
  `TTS_UTTERANCE_ENDED<class_DisplayServer_constant_TTS_UTTERANCE_ENDED>`{.interpreted-text
  role="ref"}, and
  `TTS_UTTERANCE_CANCELED<class_DisplayServer_constant_TTS_UTTERANCE_CANCELED>`{.interpreted-text
  role="ref"} callable\'s method should take one
  `int<class_int>`{.interpreted-text role="ref"} parameter, the
  utterance ID.
- `TTS_UTTERANCE_BOUNDARY<class_DisplayServer_constant_TTS_UTTERANCE_BOUNDARY>`{.interpreted-text
  role="ref"} callable\'s method should take two
  `int<class_int>`{.interpreted-text role="ref"} parameters, the index
  of the character and the utterance ID.

\*\*Note:\*\* The granularity of the boundary callbacks is engine
dependent.

\*\*Note:\*\* This method is implemented on Android, iOS, Web, Linux
(X11/Wayland), macOS, and Windows.

\*\*Note:\*\*
`ProjectSettings.audio/general/text_to_speech<class_ProjectSettings_property_audio/general/text_to_speech>`{.interpreted-text
role="ref"} should be `true` to use text-to-speech.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_tts_speak}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**tts_speak**(text: `String<class_String>`{.interpreted-text
role="ref"}, voice: `String<class_String>`{.interpreted-text
role="ref"}, volume: `int<class_int>`{.interpreted-text role="ref"} =
50, pitch: `float<class_float>`{.interpreted-text role="ref"} = 1.0,
rate: `float<class_float>`{.interpreted-text role="ref"} = 1.0,
utterance_id: `int<class_int>`{.interpreted-text role="ref"} = 0,
interrupt: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_DisplayServer_method_tts_speak>`{.interpreted-text role="ref"}

Adds an utterance to the queue. If `interrupt` is `true`, the queue is
cleared first.

- `voice` identifier is one of the `"id"` values returned by
  `tts_get_voices<class_DisplayServer_method_tts_get_voices>`{.interpreted-text
  role="ref"} or one of the values returned by
  `tts_get_voices_for_language<class_DisplayServer_method_tts_get_voices_for_language>`{.interpreted-text
  role="ref"}.
- `volume` ranges from `0` (lowest) to `100` (highest).
- `pitch` ranges from `0.0` (lowest) to `2.0` (highest), `1.0` is
  default pitch for the current voice.
- `rate` ranges from `0.1` (lowest) to `10.0` (highest), `1.0` is a
  normal speaking rate. Other values act as a percentage relative.
- `utterance_id` is passed as a parameter to the callback functions.

\*\*Note:\*\* On Windows and Linux (X11/Wayland), utterance `text` can
use SSML markup. SSML support is engine and voice dependent. If the
engine does not support SSML, you should strip out all XML markup before
calling
`tts_speak<class_DisplayServer_method_tts_speak>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* The granularity of pitch, rate, and volume is engine and
voice dependent. Values may be truncated.

\*\*Note:\*\* This method is implemented on Android, iOS, Web, Linux
(X11/Wayland), macOS, and Windows.

\*\*Note:\*\*
`ProjectSettings.audio/general/text_to_speech<class_ProjectSettings_property_audio/general/text_to_speech>`{.interpreted-text
role="ref"} should be `true` to use text-to-speech.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_tts_stop}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **tts_stop**()
`🔗<class_DisplayServer_method_tts_stop>`{.interpreted-text role="ref"}

Stops synthesis in progress and removes all utterances from the queue.

\*\*Note:\*\* This method is implemented on Android, iOS, Web, Linux
(X11/Linux), macOS, and Windows.

\*\*Note:\*\*
`ProjectSettings.audio/general/text_to_speech<class_ProjectSettings_property_audio/general/text_to_speech>`{.interpreted-text
role="ref"} should be `true` to use text-to-speech.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_unregister_additional_output}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**unregister_additional_output**(object:
`Object<class_Object>`{.interpreted-text role="ref"})
`🔗<class_DisplayServer_method_unregister_additional_output>`{.interpreted-text
role="ref"}

Unregisters an `Object<class_Object>`{.interpreted-text role="ref"}
representing an additional output, that was registered via
`register_additional_output<class_DisplayServer_method_register_additional_output>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_virtual_keyboard_get_height}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**virtual_keyboard_get_height**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_virtual_keyboard_get_height>`{.interpreted-text
role="ref"}

Returns the on-screen keyboard\'s height in pixels. Returns 0 if there
is no keyboard or if it is currently hidden.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_virtual_keyboard_hide}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**virtual_keyboard_hide**()
`🔗<class_DisplayServer_method_virtual_keyboard_hide>`{.interpreted-text
role="ref"}

Hides the virtual keyboard if it is shown, does nothing otherwise.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_virtual_keyboard_show}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**virtual_keyboard_show**(existing_text:
`String<class_String>`{.interpreted-text role="ref"}, position:
`Rect2<class_Rect2>`{.interpreted-text role="ref"} = Rect2(0, 0, 0, 0),
type:
`VirtualKeyboardType<enum_DisplayServer_VirtualKeyboardType>`{.interpreted-text
role="ref"} = 0, max_length: `int<class_int>`{.interpreted-text
role="ref"} = -1, cursor_start: `int<class_int>`{.interpreted-text
role="ref"} = -1, cursor_end: `int<class_int>`{.interpreted-text
role="ref"} = -1)
`🔗<class_DisplayServer_method_virtual_keyboard_show>`{.interpreted-text
role="ref"}

Shows the virtual keyboard if the platform has one.

`existing_text` parameter is useful for implementing your own
`LineEdit<class_LineEdit>`{.interpreted-text role="ref"} or
`TextEdit<class_TextEdit>`{.interpreted-text role="ref"}, as it tells
the virtual keyboard what text has already been typed (the virtual
keyboard uses it for auto-correct and predictions).

`position` parameter is the screen space
`Rect2<class_Rect2>`{.interpreted-text role="ref"} of the edited text.

`type` parameter allows configuring which type of virtual keyboard to
show.

`max_length` limits the number of characters that can be entered if
different from `-1`.

`cursor_start` can optionally define the current text cursor position if
`cursor_end` is not set.

`cursor_start` and `cursor_end` can optionally define the current text
selection.

\*\*Note:\*\* This method is implemented on Android, iOS and Web.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_warp_mouse}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**warp_mouse**(position: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"})
`🔗<class_DisplayServer_method_warp_mouse>`{.interpreted-text
role="ref"}

Sets the mouse cursor position to the given `position` relative to an
origin at the upper left corner of the currently focused game Window
Manager window.

\*\*Note:\*\*
`warp_mouse<class_DisplayServer_method_warp_mouse>`{.interpreted-text
role="ref"} is only supported on Windows, macOS, and Linux
(X11/Wayland). It has no effect on Android, iOS, and Web.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_can_draw}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**window_can_draw**(window_id: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_window_can_draw>`{.interpreted-text
role="ref"}

Returns `true` if anything can be drawn in the window specified by
`window_id`, `false` otherwise. Using the `--disable-render-loop`
command line argument or a headless build will return `false`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_get_active_popup}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**window_get_active_popup**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_window_get_active_popup>`{.interpreted-text
role="ref"}

Returns ID of the active popup window, or
`INVALID_WINDOW_ID<class_DisplayServer_constant_INVALID_WINDOW_ID>`{.interpreted-text
role="ref"} if there is none.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_get_attached_instance_id}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**window_get_attached_instance_id**(window_id:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_window_get_attached_instance_id>`{.interpreted-text
role="ref"}

Returns the
`Object.get_instance_id<class_Object_method_get_instance_id>`{.interpreted-text
role="ref"} of the `Window<class_Window>`{.interpreted-text role="ref"}
the `window_id` is attached to.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_get_current_screen}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**window_get_current_screen**(window_id:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_window_get_current_screen>`{.interpreted-text
role="ref"}

Returns the screen the window specified by `window_id` is currently
positioned on. If the screen overlaps multiple displays, the screen
where the window\'s center is located is returned. See also
`window_set_current_screen<class_DisplayServer_method_window_set_current_screen>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_get_flag}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**window_get_flag**(flag:
`WindowFlags<enum_DisplayServer_WindowFlags>`{.interpreted-text
role="ref"}, window_id: `int<class_int>`{.interpreted-text role="ref"} =
0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_window_get_flag>`{.interpreted-text
role="ref"}

Returns the current value of the given window\'s `flag`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_get_max_size}
::: {.rst-class}
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**window_get_max_size**(window_id: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_window_get_max_size>`{.interpreted-text
role="ref"}

Returns the window\'s maximum size (in pixels). See also
`window_set_max_size<class_DisplayServer_method_window_set_max_size>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_get_min_size}
::: {.rst-class}
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**window_get_min_size**(window_id: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_window_get_min_size>`{.interpreted-text
role="ref"}

Returns the window\'s minimum size (in pixels). See also
`window_set_min_size<class_DisplayServer_method_window_set_min_size>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_get_mode}
::: {.rst-class}
classref-method
:::
::::

`WindowMode<enum_DisplayServer_WindowMode>`{.interpreted-text
role="ref"} **window_get_mode**(window_id:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_window_get_mode>`{.interpreted-text
role="ref"}

Returns the mode of the given window.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_get_native_handle}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**window_get_native_handle**(handle_type:
`HandleType<enum_DisplayServer_HandleType>`{.interpreted-text
role="ref"}, window_id: `int<class_int>`{.interpreted-text role="ref"} =
0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_window_get_native_handle>`{.interpreted-text
role="ref"}

Returns internal structure pointers for use in plugins.

\*\*Note:\*\* This method is implemented on Android, Linux
(X11/Wayland), macOS, and Windows.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_get_popup_safe_rect}
::: {.rst-class}
classref-method
:::
::::

`Rect2i<class_Rect2i>`{.interpreted-text role="ref"}
**window_get_popup_safe_rect**(window:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_window_get_popup_safe_rect>`{.interpreted-text
role="ref"}

Returns the bounding box of control, or menu item that was used to open
the popup window, in the screen coordinate system.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_get_position}
::: {.rst-class}
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**window_get_position**(window_id: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_window_get_position>`{.interpreted-text
role="ref"}

Returns the position of the client area of the given window on the
screen.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_get_position_with_decorations}
::: {.rst-class}
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**window_get_position_with_decorations**(window_id:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_window_get_position_with_decorations>`{.interpreted-text
role="ref"}

Returns the position of the given window on the screen including the
borders drawn by the operating system. See also
`window_get_position<class_DisplayServer_method_window_get_position>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_get_safe_title_margins}
::: {.rst-class}
classref-method
:::
::::

`Vector3i<class_Vector3i>`{.interpreted-text role="ref"}
**window_get_safe_title_margins**(window_id:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_window_get_safe_title_margins>`{.interpreted-text
role="ref"}

Returns left margins (`x`), right margins (`y`) and height (`z`) of the
title that are safe to use (contains no buttons or other elements) when
`WINDOW_FLAG_EXTEND_TO_TITLE<class_DisplayServer_constant_WINDOW_FLAG_EXTEND_TO_TITLE>`{.interpreted-text
role="ref"} flag is set.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_get_size}
::: {.rst-class}
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**window_get_size**(window_id: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_window_get_size>`{.interpreted-text
role="ref"}

Returns the size of the window specified by `window_id` (in pixels),
excluding the borders drawn by the operating system. This is also called
the \"client area\". See also
`window_get_size_with_decorations<class_DisplayServer_method_window_get_size_with_decorations>`{.interpreted-text
role="ref"},
`window_set_size<class_DisplayServer_method_window_set_size>`{.interpreted-text
role="ref"} and
`window_get_position<class_DisplayServer_method_window_get_position>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_get_size_with_decorations}
::: {.rst-class}
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**window_get_size_with_decorations**(window_id:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_window_get_size_with_decorations>`{.interpreted-text
role="ref"}

Returns the size of the window specified by `window_id` (in pixels),
including the borders drawn by the operating system. See also
`window_get_size<class_DisplayServer_method_window_get_size>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_get_title_size}
::: {.rst-class}
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**window_get_title_size**(title:
`String<class_String>`{.interpreted-text role="ref"}, window_id:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_window_get_title_size>`{.interpreted-text
role="ref"}

Returns the estimated window title bar size (including text and window
buttons) for the window specified by `window_id` (in pixels). This
method does not change the window title.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_get_vsync_mode}
::: {.rst-class}
classref-method
:::
::::

`VSyncMode<enum_DisplayServer_VSyncMode>`{.interpreted-text role="ref"}
**window_get_vsync_mode**(window_id: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_window_get_vsync_mode>`{.interpreted-text
role="ref"}

Returns the V-Sync mode of the given window.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_is_focused}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**window_is_focused**(window_id: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_window_is_focused>`{.interpreted-text
role="ref"}

Returns `true` if the window specified by `window_id` is focused.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_is_maximize_allowed}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**window_is_maximize_allowed**(window_id:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_window_is_maximize_allowed>`{.interpreted-text
role="ref"}

Returns `true` if the given window can be maximized (the maximize button
is enabled).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_maximize_on_title_dbl_click}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**window_maximize_on_title_dbl_click**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_window_maximize_on_title_dbl_click>`{.interpreted-text
role="ref"}

Returns `true`, if double-click on a window title should maximize it.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_minimize_on_title_dbl_click}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**window_minimize_on_title_dbl_click**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_DisplayServer_method_window_minimize_on_title_dbl_click>`{.interpreted-text
role="ref"}

Returns `true`, if double-click on a window title should minimize it.

\*\*Note:\*\* This method is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_move_to_foreground}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**window_move_to_foreground**(window_id:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_DisplayServer_method_window_move_to_foreground>`{.interpreted-text
role="ref"}

Moves the window specified by `window_id` to the foreground, so that it
is visible over other windows.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_request_attention}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**window_request_attention**(window_id:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_DisplayServer_method_window_request_attention>`{.interpreted-text
role="ref"}

Makes the window specified by `window_id` request attention, which is
materialized by the window title and taskbar entry blinking until the
window is focused. This usually has no visible effect if the window is
currently focused. The exact behavior varies depending on the operating
system.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_set_current_screen}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**window_set_current_screen**(screen: `int<class_int>`{.interpreted-text
role="ref"}, window_id: `int<class_int>`{.interpreted-text role="ref"} =
0)
`🔗<class_DisplayServer_method_window_set_current_screen>`{.interpreted-text
role="ref"}

Moves the window specified by `window_id` to the specified `screen`. See
also
`window_get_current_screen<class_DisplayServer_method_window_get_current_screen>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_set_drop_files_callback}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**window_set_drop_files_callback**(callback:
`Callable<class_Callable>`{.interpreted-text role="ref"}, window_id:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_DisplayServer_method_window_set_drop_files_callback>`{.interpreted-text
role="ref"}

Sets the `callback` that should be called when files are dropped from
the operating system\'s file manager to the window specified by
`window_id`. `callback` should take one
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} argument, which is the list of dropped files.

\*\*Warning:\*\* Advanced users only! Adding such a callback to a
`Window<class_Window>`{.interpreted-text role="ref"} node will override
its default implementation, which can introduce bugs.

\*\*Note:\*\* This method is implemented on Windows, macOS, Linux
(X11/Wayland), and Web.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_set_exclusive}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**window_set_exclusive**(window_id: `int<class_int>`{.interpreted-text
role="ref"}, exclusive: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_DisplayServer_method_window_set_exclusive>`{.interpreted-text
role="ref"}

If set to `true`, this window will always stay on top of its parent
window, parent window will ignore input while this window is opened.

\*\*Note:\*\* On macOS, exclusive windows are confined to the same space
(virtual desktop or screen) as the parent window.

\*\*Note:\*\* This method is implemented on macOS and Windows.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_set_flag}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**window_set_flag**(flag:
`WindowFlags<enum_DisplayServer_WindowFlags>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"},
window_id: `int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_DisplayServer_method_window_set_flag>`{.interpreted-text
role="ref"}

Enables or disables the given window\'s given `flag`. See
`WindowFlags<enum_DisplayServer_WindowFlags>`{.interpreted-text
role="ref"} for possible values and their behavior.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_set_ime_active}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**window_set_ime_active**(active: `bool<class_bool>`{.interpreted-text
role="ref"}, window_id: `int<class_int>`{.interpreted-text role="ref"} =
0)
`🔗<class_DisplayServer_method_window_set_ime_active>`{.interpreted-text
role="ref"}

Sets whether [Input Method
Editor](https://en.wikipedia.org/wiki/Input_method) should be enabled
for the window specified by `window_id`. See also
`window_set_ime_position<class_DisplayServer_method_window_set_ime_position>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_set_ime_position}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**window_set_ime_position**(position:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, window_id:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_DisplayServer_method_window_set_ime_position>`{.interpreted-text
role="ref"}

Sets the position of the [Input Method
Editor](https://en.wikipedia.org/wiki/Input_method) popup for the
specified `window_id`. Only effective if
`window_set_ime_active<class_DisplayServer_method_window_set_ime_active>`{.interpreted-text
role="ref"} was set to `true` for the specified `window_id`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_set_input_event_callback}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**window_set_input_event_callback**(callback:
`Callable<class_Callable>`{.interpreted-text role="ref"}, window_id:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_DisplayServer_method_window_set_input_event_callback>`{.interpreted-text
role="ref"}

Sets the `callback` that should be called when any
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"} is sent to
the window specified by `window_id`.

\*\*Warning:\*\* Advanced users only! Adding such a callback to a
`Window<class_Window>`{.interpreted-text role="ref"} node will override
its default implementation, which can introduce bugs.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_set_input_text_callback}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**window_set_input_text_callback**(callback:
`Callable<class_Callable>`{.interpreted-text role="ref"}, window_id:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_DisplayServer_method_window_set_input_text_callback>`{.interpreted-text
role="ref"}

Sets the `callback` that should be called when text is entered using the
virtual keyboard to the window specified by `window_id`.

\*\*Warning:\*\* Advanced users only! Adding such a callback to a
`Window<class_Window>`{.interpreted-text role="ref"} node will override
its default implementation, which can introduce bugs.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_set_max_size}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**window_set_max_size**(max_size:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, window_id:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_DisplayServer_method_window_set_max_size>`{.interpreted-text
role="ref"}

Sets the maximum size of the window specified by `window_id` in pixels.
Normally, the user will not be able to drag the window to make it larger
than the specified size. See also
`window_get_max_size<class_DisplayServer_method_window_get_max_size>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* It\'s recommended to change this value using
`Window.max_size<class_Window_property_max_size>`{.interpreted-text
role="ref"} instead.

\*\*Note:\*\* Using third-party tools, it is possible for users to
disable window geometry restrictions and therefore bypass this limit.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_set_min_size}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**window_set_min_size**(min_size:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, window_id:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_DisplayServer_method_window_set_min_size>`{.interpreted-text
role="ref"}

Sets the minimum size for the given window to `min_size` in pixels.
Normally, the user will not be able to drag the window to make it
smaller than the specified size. See also
`window_get_min_size<class_DisplayServer_method_window_get_min_size>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* It\'s recommended to change this value using
`Window.min_size<class_Window_property_min_size>`{.interpreted-text
role="ref"} instead.

\*\*Note:\*\* By default, the main window has a minimum size of
`Vector2i(64, 64)`. This prevents issues that can arise when the window
is resized to a near-zero size.

\*\*Note:\*\* Using third-party tools, it is possible for users to
disable window geometry restrictions and therefore bypass this limit.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_set_mode}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**window_set_mode**(mode:
`WindowMode<enum_DisplayServer_WindowMode>`{.interpreted-text
role="ref"}, window_id: `int<class_int>`{.interpreted-text role="ref"} =
0) `🔗<class_DisplayServer_method_window_set_mode>`{.interpreted-text
role="ref"}

Sets window mode for the given window to `mode`. See
`WindowMode<enum_DisplayServer_WindowMode>`{.interpreted-text
role="ref"} for possible values and how each mode behaves.

\*\*Note:\*\* On Android, setting it to
`WINDOW_MODE_FULLSCREEN<class_DisplayServer_constant_WINDOW_MODE_FULLSCREEN>`{.interpreted-text
role="ref"} or
`WINDOW_MODE_EXCLUSIVE_FULLSCREEN<class_DisplayServer_constant_WINDOW_MODE_EXCLUSIVE_FULLSCREEN>`{.interpreted-text
role="ref"} will enable immersive mode.

\*\*Note:\*\* Setting the window to full screen forcibly sets the
borderless flag to `true`, so make sure to set it back to `false` when
not wanted.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_set_mouse_passthrough}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**window_set_mouse_passthrough**(region:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}, window_id: `int<class_int>`{.interpreted-text role="ref"} =
0)
`🔗<class_DisplayServer_method_window_set_mouse_passthrough>`{.interpreted-text
role="ref"}

Sets a polygonal region of the window which accepts mouse events. Mouse
events outside the region will be passed through.

Passing an empty array will disable passthrough support (all mouse
events will be intercepted by the window, which is the default
behavior).

::::: {.tabs}
::: {.code-tab}
gdscript

\# Set region, using Path2D node.
DisplayServer.window_set_mouse_passthrough(\$Path2D.curve.get_baked_points())

\# Set region, using Polygon2D node.
DisplayServer.window_set_mouse_passthrough(\$Polygon2D.polygon)

\# Reset region to default.
DisplayServer.window_set_mouse_passthrough(\[\])
:::

::: {.code-tab}
csharp

// Set region, using Path2D node.
DisplayServer.WindowSetMousePassthrough(GetNode\<Path2D\>(\"Path2D\").Curve.GetBakedPoints());

// Set region, using Polygon2D node.
DisplayServer.WindowSetMousePassthrough(GetNode\<Polygon2D\>(\"Polygon2D\").Polygon);

// Reset region to default. DisplayServer.WindowSetMousePassthrough(new
Vector2\[\] {});
:::
:::::

\*\*Note:\*\* On Windows, the portion of a window that lies outside the
region is not drawn, while on Linux (X11) and macOS it is.

\*\*Note:\*\* This method is implemented on Linux (X11), macOS and
Windows.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_set_popup_safe_rect}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**window_set_popup_safe_rect**(window:
`int<class_int>`{.interpreted-text role="ref"}, rect:
`Rect2i<class_Rect2i>`{.interpreted-text role="ref"})
`🔗<class_DisplayServer_method_window_set_popup_safe_rect>`{.interpreted-text
role="ref"}

Sets the bounding box of control, or menu item that was used to open the
popup window, in the screen coordinate system. Clicking this area will
not auto-close this popup.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_set_position}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**window_set_position**(position:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, window_id:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_DisplayServer_method_window_set_position>`{.interpreted-text
role="ref"}

Sets the position of the given window to `position`. On multi-monitor
setups, the screen position is relative to the virtual desktop area. On
multi-monitor setups with different screen resolutions or orientations,
the origin may be located outside any display like this:

``` text
* (0, 0)        +-------+
                |       |
+-------------+ |       |
|             | |       |
|             | |       |
+-------------+ +-------+
```

See also
`window_get_position<class_DisplayServer_method_window_get_position>`{.interpreted-text
role="ref"} and
`window_set_size<class_DisplayServer_method_window_set_size>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* It\'s recommended to change this value using
`Window.position<class_Window_property_position>`{.interpreted-text
role="ref"} instead.

\*\*Note:\*\* On Linux (Wayland): this method is a no-op.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_set_rect_changed_callback}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**window_set_rect_changed_callback**(callback:
`Callable<class_Callable>`{.interpreted-text role="ref"}, window_id:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_DisplayServer_method_window_set_rect_changed_callback>`{.interpreted-text
role="ref"}

Sets the `callback` that will be called when the window specified by
`window_id` is moved or resized.

\*\*Warning:\*\* Advanced users only! Adding such a callback to a
`Window<class_Window>`{.interpreted-text role="ref"} node will override
its default implementation, which can introduce bugs.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_set_size}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**window_set_size**(size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, window_id: `int<class_int>`{.interpreted-text role="ref"} =
0) `🔗<class_DisplayServer_method_window_set_size>`{.interpreted-text
role="ref"}

Sets the size of the given window to `size` (in pixels). See also
`window_get_size<class_DisplayServer_method_window_get_size>`{.interpreted-text
role="ref"} and
`window_get_position<class_DisplayServer_method_window_get_position>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* It\'s recommended to change this value using
`Window.size<class_Window_property_size>`{.interpreted-text role="ref"}
instead.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_set_title}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**window_set_title**(title: `String<class_String>`{.interpreted-text
role="ref"}, window_id: `int<class_int>`{.interpreted-text role="ref"} =
0) `🔗<class_DisplayServer_method_window_set_title>`{.interpreted-text
role="ref"}

Sets the title of the given window to `title`.

\*\*Note:\*\* It\'s recommended to change this value using
`Window.title<class_Window_property_title>`{.interpreted-text
role="ref"} instead.

\*\*Note:\*\* Avoid changing the window title every frame, as this can
cause performance issues on certain window managers. Try to change the
window title only a few times per second at most.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_set_transient}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**window_set_transient**(window_id: `int<class_int>`{.interpreted-text
role="ref"}, parent_window_id: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_DisplayServer_method_window_set_transient>`{.interpreted-text
role="ref"}

Sets window transient parent. Transient window will be destroyed with
its transient parent and will return focus to their parent when closed.
The transient window is displayed on top of a non-exclusive full-screen
parent window. Transient windows can\'t enter full-screen mode.

\*\*Note:\*\* It\'s recommended to change this value using
`Window.transient<class_Window_property_transient>`{.interpreted-text
role="ref"} instead.

\*\*Note:\*\* The behavior might be different depending on the platform.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_set_vsync_mode}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**window_set_vsync_mode**(vsync_mode:
`VSyncMode<enum_DisplayServer_VSyncMode>`{.interpreted-text role="ref"},
window_id: `int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_DisplayServer_method_window_set_vsync_mode>`{.interpreted-text
role="ref"}

Sets the V-Sync mode of the given window. See also
`ProjectSettings.display/window/vsync/vsync_mode<class_ProjectSettings_property_display/window/vsync/vsync_mode>`{.interpreted-text
role="ref"}.

See `VSyncMode<enum_DisplayServer_VSyncMode>`{.interpreted-text
role="ref"} for possible values and how they affect the behavior of your
application.

Depending on the platform and used renderer, the engine will fall back
to
`VSYNC_ENABLED<class_DisplayServer_constant_VSYNC_ENABLED>`{.interpreted-text
role="ref"} if the desired mode is not supported.

\*\*Note:\*\* V-Sync modes other than
`VSYNC_ENABLED<class_DisplayServer_constant_VSYNC_ENABLED>`{.interpreted-text
role="ref"} are only supported in the Forward+ and Mobile rendering
methods, not Compatibility.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_set_window_buttons_offset}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**window_set_window_buttons_offset**(offset:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, window_id:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_DisplayServer_method_window_set_window_buttons_offset>`{.interpreted-text
role="ref"}

When
`WINDOW_FLAG_EXTEND_TO_TITLE<class_DisplayServer_constant_WINDOW_FLAG_EXTEND_TO_TITLE>`{.interpreted-text
role="ref"} flag is set, set offset to the center of the first titlebar
button.

\*\*Note:\*\* This flag is implemented only on macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DisplayServer_method_window_set_window_event_callback}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**window_set_window_event_callback**(callback:
`Callable<class_Callable>`{.interpreted-text role="ref"}, window_id:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_DisplayServer_method_window_set_window_event_callback>`{.interpreted-text
role="ref"}

Sets the `callback` that will be called when an event occurs in the
window specified by `window_id`.

\*\*Warning:\*\* Advanced users only! Adding such a callback to a
`Window<class_Window>`{.interpreted-text role="ref"} node will override
its default implementation, which can introduce bugs.
