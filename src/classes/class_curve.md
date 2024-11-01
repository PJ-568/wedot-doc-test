github_url

:   hide

# Curve {#class_Curve}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

A mathematical curve.

::: {.rst-class}
classref-introduction-group
:::

## Description

This resource describes a mathematical curve by defining a set of points
and tangents at each point. By default, it ranges between `0` and `1` on
the Y axis and positions points relative to the `0.5` Y position.

See also `Gradient<class_Gradient>`{.interpreted-text role="ref"} which
is designed for color interpolation. See also
`Curve2D<class_Curve2D>`{.interpreted-text role="ref"} and
`Curve3D<class_Curve3D>`{.interpreted-text role="ref"}.

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

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Signals

:::: {#class_Curve_signal_range_changed}
::: {.rst-class}
classref-signal
:::
::::

**range_changed**()
`🔗<class_Curve_signal_range_changed>`{.interpreted-text role="ref"}

Emitted when
`max_value<class_Curve_property_max_value>`{.interpreted-text
role="ref"} or
`min_value<class_Curve_property_min_value>`{.interpreted-text
role="ref"} is changed.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Enumerations

:::: {#enum_Curve_TangentMode}
::: {.rst-class}
classref-enumeration
:::
::::

enum **TangentMode**: `🔗<enum_Curve_TangentMode>`{.interpreted-text
role="ref"}

:::: {#class_Curve_constant_TANGENT_FREE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`TangentMode<enum_Curve_TangentMode>`{.interpreted-text role="ref"}
**TANGENT_FREE** = `0`

The tangent on this side of the point is user-defined.

:::: {#class_Curve_constant_TANGENT_LINEAR}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`TangentMode<enum_Curve_TangentMode>`{.interpreted-text role="ref"}
**TANGENT_LINEAR** = `1`

The curve calculates the tangent on this side of the point as the slope
halfway towards the adjacent point.

:::: {#class_Curve_constant_TANGENT_MODE_COUNT}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`TangentMode<enum_Curve_TangentMode>`{.interpreted-text role="ref"}
**TANGENT_MODE_COUNT** = `2`

The total number of available tangent modes.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Curve_property_bake_resolution}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **bake_resolution** =
`100` `🔗<class_Curve_property_bake_resolution>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bake_resolution**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_bake_resolution**()

The number of points to include in the baked (i.e. cached) curve data.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve_property_max_value}
::: {.rst-class}
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **max_value** = `1.0`
`🔗<class_Curve_property_max_value>`{.interpreted-text role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_value**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_max_value**()

The maximum value the curve can reach.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve_property_min_value}
::: {.rst-class}
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **min_value** = `0.0`
`🔗<class_Curve_property_min_value>`{.interpreted-text role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_min_value**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_min_value**()

The minimum value the curve can reach.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve_property_point_count}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **point_count** = `0`
`🔗<class_Curve_property_point_count>`{.interpreted-text role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_point_count**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_point_count**()

The number of points describing the curve.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Curve_method_add_point}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **add_point**(position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, left_tangent:
`float<class_float>`{.interpreted-text role="ref"} = 0, right_tangent:
`float<class_float>`{.interpreted-text role="ref"} = 0, left_mode:
`TangentMode<enum_Curve_TangentMode>`{.interpreted-text role="ref"} = 0,
right_mode: `TangentMode<enum_Curve_TangentMode>`{.interpreted-text
role="ref"} = 0) `🔗<class_Curve_method_add_point>`{.interpreted-text
role="ref"}

Adds a point to the curve. For each side, if the `*_mode` is
`TANGENT_LINEAR<class_Curve_constant_TANGENT_LINEAR>`{.interpreted-text
role="ref"}, the `*_tangent` angle (in degrees) uses the slope of the
curve halfway to the adjacent point. Allows custom assignments to the
`*_tangent` angle if `*_mode` is set to
`TANGENT_FREE<class_Curve_constant_TANGENT_FREE>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve_method_bake}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **bake**()
`🔗<class_Curve_method_bake>`{.interpreted-text role="ref"}

Recomputes the baked cache of points for the curve.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve_method_clean_dupes}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clean_dupes**() `🔗<class_Curve_method_clean_dupes>`{.interpreted-text
role="ref"}

Removes duplicate points, i.e. points that are less than 0.00001 units
(engine epsilon value) away from their neighbor on the curve.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve_method_clear_points}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_points**()
`🔗<class_Curve_method_clear_points>`{.interpreted-text role="ref"}

Removes all points from the curve.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve_method_get_point_left_mode}
::: {.rst-class}
classref-method
:::
::::

`TangentMode<enum_Curve_TangentMode>`{.interpreted-text role="ref"}
**get_point_left_mode**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Curve_method_get_point_left_mode>`{.interpreted-text
role="ref"}

Returns the left `TangentMode<enum_Curve_TangentMode>`{.interpreted-text
role="ref"} for the point at `index`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve_method_get_point_left_tangent}
::: {.rst-class}
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_point_left_tangent**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Curve_method_get_point_left_tangent>`{.interpreted-text
role="ref"}

Returns the left tangent angle (in degrees) for the point at `index`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve_method_get_point_position}
::: {.rst-class}
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_point_position**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Curve_method_get_point_position>`{.interpreted-text
role="ref"}

Returns the curve coordinates for the point at `index`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve_method_get_point_right_mode}
::: {.rst-class}
classref-method
:::
::::

`TangentMode<enum_Curve_TangentMode>`{.interpreted-text role="ref"}
**get_point_right_mode**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Curve_method_get_point_right_mode>`{.interpreted-text
role="ref"}

Returns the right
`TangentMode<enum_Curve_TangentMode>`{.interpreted-text role="ref"} for
the point at `index`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve_method_get_point_right_tangent}
::: {.rst-class}
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_point_right_tangent**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Curve_method_get_point_right_tangent>`{.interpreted-text
role="ref"}

Returns the right tangent angle (in degrees) for the point at `index`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve_method_remove_point}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_point**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Curve_method_remove_point>`{.interpreted-text role="ref"}

Removes the point at `index` from the curve.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve_method_sample}
::: {.rst-class}
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **sample**(offset:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Curve_method_sample>`{.interpreted-text
role="ref"}

Returns the Y value for the point that would exist at the X position
`offset` along the curve.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve_method_sample_baked}
::: {.rst-class}
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**sample_baked**(offset: `float<class_float>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Curve_method_sample_baked>`{.interpreted-text
role="ref"}

Returns the Y value for the point that would exist at the X position
`offset` along the curve using the baked cache. Bakes the curve\'s
points if not already baked.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve_method_set_point_left_mode}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_point_left_mode**(index: `int<class_int>`{.interpreted-text
role="ref"}, mode:
`TangentMode<enum_Curve_TangentMode>`{.interpreted-text role="ref"})
`🔗<class_Curve_method_set_point_left_mode>`{.interpreted-text
role="ref"}

Sets the left `TangentMode<enum_Curve_TangentMode>`{.interpreted-text
role="ref"} for the point at `index` to `mode`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve_method_set_point_left_tangent}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_point_left_tangent**(index: `int<class_int>`{.interpreted-text
role="ref"}, tangent: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_Curve_method_set_point_left_tangent>`{.interpreted-text
role="ref"}

Sets the left tangent angle for the point at `index` to `tangent`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve_method_set_point_offset}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**set_point_offset**(index: `int<class_int>`{.interpreted-text
role="ref"}, offset: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Curve_method_set_point_offset>`{.interpreted-text role="ref"}

Sets the offset from `0.5`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve_method_set_point_right_mode}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_point_right_mode**(index: `int<class_int>`{.interpreted-text
role="ref"}, mode:
`TangentMode<enum_Curve_TangentMode>`{.interpreted-text role="ref"})
`🔗<class_Curve_method_set_point_right_mode>`{.interpreted-text
role="ref"}

Sets the right `TangentMode<enum_Curve_TangentMode>`{.interpreted-text
role="ref"} for the point at `index` to `mode`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve_method_set_point_right_tangent}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_point_right_tangent**(index: `int<class_int>`{.interpreted-text
role="ref"}, tangent: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_Curve_method_set_point_right_tangent>`{.interpreted-text
role="ref"}

Sets the right tangent angle for the point at `index` to `tangent`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Curve_method_set_point_value}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_point_value**(index: `int<class_int>`{.interpreted-text
role="ref"}, y: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Curve_method_set_point_value>`{.interpreted-text role="ref"}

Assigns the vertical position `y` to the point at `index`.
