github_url

:   hide

# LabelSettings {#class_LabelSettings}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Provides common settings to customize the text in a
`Label<class_Label>`{.interpreted-text role="ref"}.

::: {.rst-class}
classref-introduction-group
:::

## Description

**LabelSettings** is a resource that provides common settings to
customize the text in a `Label<class_Label>`{.interpreted-text
role="ref"}. It will take priority over the properties defined in
`Control.theme<class_Control_property_theme>`{.interpreted-text
role="ref"}. The resource can be shared between multiple labels and
changed on the fly, so it\'s convenient and flexible way to setup text
style.

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

:::: {#class_LabelSettings_property_font}
::: {.rst-class}
classref-property
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"} **font**
`🔗<class_LabelSettings_property_font>`{.interpreted-text role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_font**(value: `Font<class_Font>`{.interpreted-text role="ref"})
- `Font<class_Font>`{.interpreted-text role="ref"} **get_font**()

`Font<class_Font>`{.interpreted-text role="ref"} used for the text.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_property_font_color}
::: {.rst-class}
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **font_color** =
`Color(1, 1, 1, 1)`
`🔗<class_LabelSettings_property_font_color>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_font_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_font_color**()

Color of the text.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_property_font_size}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **font_size** = `16`
`🔗<class_LabelSettings_property_font_size>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_font_size**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_font_size**()

Size of the text.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_property_line_spacing}
::: {.rst-class}
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **line_spacing** =
`3.0` `🔗<class_LabelSettings_property_line_spacing>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_line_spacing**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_line_spacing**()

Vertical space between lines when the text is multiline.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_property_outline_color}
::: {.rst-class}
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **outline_color** =
`Color(1, 1, 1, 1)`
`🔗<class_LabelSettings_property_outline_color>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_outline_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_outline_color**()

The color of the outline.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_property_outline_size}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **outline_size** = `0`
`🔗<class_LabelSettings_property_outline_size>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_outline_size**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_outline_size**()

Text outline size.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_property_shadow_color}
::: {.rst-class}
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **shadow_color** =
`Color(0, 0, 0, 0)`
`🔗<class_LabelSettings_property_shadow_color>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shadow_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_shadow_color**()

Color of the shadow effect. If alpha is `0`, no shadow will be drawn.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_property_shadow_offset}
::: {.rst-class}
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **shadow_offset**
= `Vector2(1, 1)`
`🔗<class_LabelSettings_property_shadow_offset>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shadow_offset**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_shadow_offset**()

Offset of the shadow effect, in pixels.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LabelSettings_property_shadow_size}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **shadow_size** = `1`
`🔗<class_LabelSettings_property_shadow_size>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shadow_size**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_shadow_size**()

Size of the shadow effect.
