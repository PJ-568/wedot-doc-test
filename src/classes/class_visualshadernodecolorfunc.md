github_url

:   hide

# VisualShaderNodeColorFunc {#class_VisualShaderNodeColorFunc}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A `Color<class_Color>`{.interpreted-text role="ref"} function to be used
within the visual shader graph.

::: {.rst-class}
classref-introduction-group
:::

## Description

Accept a `Color<class_Color>`{.interpreted-text role="ref"} to the input
port and transform it according to
`function<class_VisualShaderNodeColorFunc_property_function>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-reftable-group
:::

## Properties

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

:::: {#enum_VisualShaderNodeColorFunc_Function}
::: {.rst-class}
classref-enumeration
:::
::::

enum **Function**:
`🔗<enum_VisualShaderNodeColorFunc_Function>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeColorFunc_constant_FUNC_GRAYSCALE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeColorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_GRAYSCALE** = `0`

Converts the color to grayscale using the following formula:

    vec3 c = input;
    float max1 = max(c.r, c.g);
    float max2 = max(max1, c.b);
    float max3 = max(max1, max2);
    return vec3(max3, max3, max3);

:::: {#class_VisualShaderNodeColorFunc_constant_FUNC_HSV2RGB}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeColorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_HSV2RGB** = `1`

Converts HSV vector to RGB equivalent.

:::: {#class_VisualShaderNodeColorFunc_constant_FUNC_RGB2HSV}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeColorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_RGB2HSV** = `2`

Converts RGB vector to HSV equivalent.

:::: {#class_VisualShaderNodeColorFunc_constant_FUNC_SEPIA}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeColorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_SEPIA** = `3`

Applies sepia tone effect using the following formula:

    vec3 c = input;
    float r = (c.r * 0.393) + (c.g * 0.769) + (c.b * 0.189);
    float g = (c.r * 0.349) + (c.g * 0.686) + (c.b * 0.168);
    float b = (c.r * 0.272) + (c.g * 0.534) + (c.b * 0.131);
    return vec3(r, g, b);

:::: {#class_VisualShaderNodeColorFunc_constant_FUNC_MAX}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeColorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_MAX** = `4`

Represents the size of the
`Function<enum_VisualShaderNodeColorFunc_Function>`{.interpreted-text
role="ref"} enum.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeColorFunc_property_function}
::: {.rst-class}
classref-property
:::
::::

`Function<enum_VisualShaderNodeColorFunc_Function>`{.interpreted-text
role="ref"} **function** = `0`
`🔗<class_VisualShaderNodeColorFunc_property_function>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_function**(value:
  `Function<enum_VisualShaderNodeColorFunc_Function>`{.interpreted-text
  role="ref"})
- `Function<enum_VisualShaderNodeColorFunc_Function>`{.interpreted-text
  role="ref"} **get_function**()

A function to be applied to the input color. See
`Function<enum_VisualShaderNodeColorFunc_Function>`{.interpreted-text
role="ref"} for options.
