github_url

:   hide

# CapsuleShape2D {#class_CapsuleShape2D}

**Inherits:** `Shape2D<class_Shape2D>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 2D capsule shape used for physics collision.

::: {.rst-class}
classref-introduction-group
:::

## Description

A 2D capsule shape, intended for use in physics. Usually used to provide
a shape for a
`CollisionShape2D<class_CollisionShape2D>`{.interpreted-text
role="ref"}.

\*\*Performance:\*\* **CapsuleShape2D** is fast to check collisions
against, but it is slower than
`RectangleShape2D<class_RectangleShape2D>`{.interpreted-text role="ref"}
and `CircleShape2D<class_CircleShape2D>`{.interpreted-text role="ref"}.

::: {.rst-class}
classref-reftable-group
:::

## Properties

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

:::: {#class_CapsuleShape2D_property_height}
::: {.rst-class}
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **height** = `30.0`
`🔗<class_CapsuleShape2D_property_height>`{.interpreted-text role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_height**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_height**()

The capsule\'s height.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CapsuleShape2D_property_radius}
::: {.rst-class}
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **radius** = `10.0`
`🔗<class_CapsuleShape2D_property_radius>`{.interpreted-text role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_radius**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_radius**()

The capsule\'s radius.
