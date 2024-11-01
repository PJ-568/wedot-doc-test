github_url

:   hide

# Shortcut {#class_Shortcut}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

A shortcut for binding input.

::: {.rst-class}
classref-introduction-group
:::

## Description

Shortcuts are commonly used for interacting with a
`Control<class_Control>`{.interpreted-text role="ref"} element from an
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"} (also known
as hotkeys).

One shortcut can contain multiple
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"}\'s,
allowing the possibility of triggering one action with multiple
different inputs.

::: {.rst-class}
classref-reftable-group
:::

## Properties

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

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Shortcut_property_events}
::: {.rst-class}
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **events** = `[]`
`🔗<class_Shortcut_property_events>`{.interpreted-text role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_events**(value: `Array<class_Array>`{.interpreted-text
  role="ref"})
- `Array<class_Array>`{.interpreted-text role="ref"} **get_events**()

The shortcut\'s `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"} array.

Generally the `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"} used is an
`InputEventKey<class_InputEventKey>`{.interpreted-text role="ref"},
though it can be any `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"}, including an
`InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Shortcut_method_get_as_text}
::: {.rst-class}
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_as_text**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Shortcut_method_get_as_text>`{.interpreted-text
role="ref"}

Returns the shortcut\'s first valid
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"} as a
`String<class_String>`{.interpreted-text role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Shortcut_method_has_valid_event}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_valid_event**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Shortcut_method_has_valid_event>`{.interpreted-text
role="ref"}

Returns whether
`events<class_Shortcut_property_events>`{.interpreted-text role="ref"}
contains an `InputEvent<class_InputEvent>`{.interpreted-text role="ref"}
which is valid.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Shortcut_method_matches_event}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**matches_event**(event:
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Shortcut_method_matches_event>`{.interpreted-text
role="ref"}

Returns whether any `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"} in
`events<class_Shortcut_property_events>`{.interpreted-text role="ref"}
equals `event`. This uses
`InputEvent.is_match<class_InputEvent_method_is_match>`{.interpreted-text
role="ref"} to compare events.
