github_url

:   hide

# Rect2i {#class_Rect2i}

A 2D axis-aligned bounding box using integer coordinates.

::: {.rst-class}
classref-introduction-group
:::

## Description

The **Rect2i** built-in `Variant<class_Variant>`{.interpreted-text
role="ref"} type represents an axis-aligned rectangle in a 2D space,
using integer coordinates. It is defined by its
`position<class_Rect2i_property_position>`{.interpreted-text role="ref"}
and `size<class_Rect2i_property_size>`{.interpreted-text role="ref"},
which are `Vector2i<class_Vector2i>`{.interpreted-text role="ref"}.
Because it does not rotate, it is frequently used for fast overlap tests
(see `intersects<class_Rect2i_method_intersects>`{.interpreted-text
role="ref"}).

For floating-point coordinates, see
`Rect2<class_Rect2>`{.interpreted-text role="ref"}.

\*\*Note:\*\* Negative values for
`size<class_Rect2i_property_size>`{.interpreted-text role="ref"} are not
supported. With negative size, most **Rect2i** methods do not work
correctly. Use `abs<class_Rect2i_method_abs>`{.interpreted-text
role="ref"} to get an equivalent **Rect2i** with a non-negative size.

\*\*Note:\*\* In a boolean context, a **Rect2i** evaluates to `false` if
both `position<class_Rect2i_property_position>`{.interpreted-text
role="ref"} and `size<class_Rect2i_property_size>`{.interpreted-text
role="ref"} are zero (equal to
`Vector2i.ZERO<class_Vector2i_constant_ZERO>`{.interpreted-text
role="ref"}). Otherwise, it always evaluates to `true`.

> [!NOTE]
> There are notable differences when using this API with C#. See
> `doc_c_sharp_differences`{.interpreted-text role="ref"} for more
> information.

::: {.rst-class}
classref-introduction-group
:::

## Tutorials

- `Math documentation index <../tutorials/math/index>`{.interpreted-text
  role="doc"}
- `Vector math <../tutorials/math/vector_math>`{.interpreted-text
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

::: {.rst-class}
classref-reftable-group
:::

## Constructors

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

::: {.rst-class}
classref-reftable-group
:::

## Operators

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

:::: {#class_Rect2i_property_end}
::: {.rst-class}
classref-property
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} **end** =
`Vector2i(0, 0)` `🔗<class_Rect2i_property_end>`{.interpreted-text
role="ref"}

The ending point. This is usually the bottom-right corner of the
rectangle, and is equivalent to `position + size`. Setting this point
affects the `size<class_Rect2i_property_size>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Rect2i_property_position}
::: {.rst-class}
classref-property
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} **position** =
`Vector2i(0, 0)` `🔗<class_Rect2i_property_position>`{.interpreted-text
role="ref"}

The origin point. This is usually the top-left corner of the rectangle.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Rect2i_property_size}
::: {.rst-class}
classref-property
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} **size** =
`Vector2i(0, 0)` `🔗<class_Rect2i_property_size>`{.interpreted-text
role="ref"}

The rectangle\'s width and height, starting from
`position<class_Rect2i_property_position>`{.interpreted-text
role="ref"}. Setting this value also affects the
`end<class_Rect2i_property_end>`{.interpreted-text role="ref"} point.

\*\*Note:\*\* It\'s recommended setting the width and height to
non-negative values, as most methods in Godot assume that the
`position<class_Rect2i_property_position>`{.interpreted-text role="ref"}
is the top-left corner, and the
`end<class_Rect2i_property_end>`{.interpreted-text role="ref"} is the
bottom-right corner. To get an equivalent rectangle with non-negative
size, use `abs<class_Rect2i_method_abs>`{.interpreted-text role="ref"}.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Constructor Descriptions

:::: {#class_Rect2i_constructor_Rect2i}
::: {.rst-class}
classref-constructor
:::
::::

`Rect2i<class_Rect2i>`{.interpreted-text role="ref"} **Rect2i**()
`🔗<class_Rect2i_constructor_Rect2i>`{.interpreted-text role="ref"}

Constructs a **Rect2i** with its
`position<class_Rect2i_property_position>`{.interpreted-text role="ref"}
and `size<class_Rect2i_property_size>`{.interpreted-text role="ref"} set
to `Vector2i.ZERO<class_Vector2i_constant_ZERO>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-constructor
:::

`Rect2i<class_Rect2i>`{.interpreted-text role="ref"} **Rect2i**(from:
`Rect2i<class_Rect2i>`{.interpreted-text role="ref"})

Constructs a **Rect2i** as a copy of the given **Rect2i**.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-constructor
:::

`Rect2i<class_Rect2i>`{.interpreted-text role="ref"} **Rect2i**(from:
`Rect2<class_Rect2>`{.interpreted-text role="ref"})

Constructs a **Rect2i** from a `Rect2<class_Rect2>`{.interpreted-text
role="ref"}. The floating-point coordinates are truncated.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-constructor
:::

`Rect2i<class_Rect2i>`{.interpreted-text role="ref"}
**Rect2i**(position: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"})

Constructs a **Rect2i** by `position` and `size`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-constructor
:::

`Rect2i<class_Rect2i>`{.interpreted-text role="ref"} **Rect2i**(x:
`int<class_int>`{.interpreted-text role="ref"}, y:
`int<class_int>`{.interpreted-text role="ref"}, width:
`int<class_int>`{.interpreted-text role="ref"}, height:
`int<class_int>`{.interpreted-text role="ref"})

Constructs a **Rect2i** by setting its
`position<class_Rect2i_property_position>`{.interpreted-text role="ref"}
to (`x`, `y`), and its
`size<class_Rect2i_property_size>`{.interpreted-text role="ref"} to
(`width`, `height`).

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Rect2i_method_abs}
::: {.rst-class}
classref-method
:::
::::

`Rect2i<class_Rect2i>`{.interpreted-text role="ref"} **abs**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Rect2i_method_abs>`{.interpreted-text role="ref"}

Returns a **Rect2i** equivalent to this rectangle, with its width and
height modified to be non-negative values, and with its
`position<class_Rect2i_property_position>`{.interpreted-text role="ref"}
being the top-left corner of the rectangle.

::::: {.tabs}
::: {.code-tab}
gdscript

var rect = Rect2i(25, 25, -100, -50) var absolute = rect.abs() \#
absolute is Rect2i(-75, -25, 100, 50)
:::

::: {.code-tab}
csharp

var rect = new Rect2I(25, 25, -100, -50); var absolute = rect.Abs(); //
absolute is Rect2I(-75, -25, 100, 50)
:::
:::::

\*\*Note:\*\* It\'s recommended to use this method when
`size<class_Rect2i_property_size>`{.interpreted-text role="ref"} is
negative, as most other methods in Godot assume that the
`position<class_Rect2i_property_position>`{.interpreted-text role="ref"}
is the top-left corner, and the
`end<class_Rect2i_property_end>`{.interpreted-text role="ref"} is the
bottom-right corner.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Rect2i_method_encloses}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **encloses**(b:
`Rect2i<class_Rect2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Rect2i_method_encloses>`{.interpreted-text
role="ref"}

Returns `true` if this **Rect2i** completely encloses another one.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Rect2i_method_expand}
::: {.rst-class}
classref-method
:::
::::

`Rect2i<class_Rect2i>`{.interpreted-text role="ref"} **expand**(to:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Rect2i_method_expand>`{.interpreted-text
role="ref"}

Returns a copy of this rectangle expanded to align the edges with the
given `to` point, if necessary.

::::: {.tabs}
::: {.code-tab}
gdscript

var rect = Rect2i(0, 0, 5, 2)

rect = rect.expand(Vector2i(10, 0)) \# rect is Rect2i(0, 0, 10, 2) rect
= rect.expand(Vector2i(-5, 5)) \# rect is Rect2i(-5, 0, 15, 5)
:::

::: {.code-tab}
csharp

var rect = new Rect2I(0, 0, 5, 2);

rect = rect.Expand(new Vector2I(10, 0)); // rect is Rect2I(0, 0, 10, 2)
rect = rect.Expand(new Vector2I(-5, 5)); // rect is Rect2I(-5, 0, 15, 5)
:::
:::::

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Rect2i_method_get_area}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_area**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Rect2i_method_get_area>`{.interpreted-text
role="ref"}

Returns the rectangle\'s area. This is equivalent to `size.x * size.y`.
See also `has_area<class_Rect2i_method_has_area>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Rect2i_method_get_center}
::: {.rst-class}
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**get_center**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Rect2i_method_get_center>`{.interpreted-text
role="ref"}

Returns the center point of the rectangle. This is the same as
`position + (size / 2)`.

\*\*Note:\*\* If the
`size<class_Rect2i_property_size>`{.interpreted-text role="ref"} is odd,
the result will be rounded towards
`position<class_Rect2i_property_position>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Rect2i_method_grow}
::: {.rst-class}
classref-method
:::
::::

`Rect2i<class_Rect2i>`{.interpreted-text role="ref"} **grow**(amount:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Rect2i_method_grow>`{.interpreted-text
role="ref"}

Returns a copy of this rectangle extended on all sides by the given
`amount`. A negative `amount` shrinks the rectangle instead. See also
`grow_individual<class_Rect2i_method_grow_individual>`{.interpreted-text
role="ref"} and
`grow_side<class_Rect2i_method_grow_side>`{.interpreted-text
role="ref"}.

::::: {.tabs}
::: {.code-tab}
gdscript

var a = Rect2i(4, 4, 8, 8).grow(4) \# a is Rect2i(0, 0, 16, 16) var b =
Rect2i(0, 0, 8, 4).grow(2) \# b is Rect2i(-2, -2, 12, 8)
:::

::: {.code-tab}
csharp

var a = new Rect2I(4, 4, 8, 8).Grow(4); // a is Rect2I(0, 0, 16, 16) var
b = new Rect2I(0, 0, 8, 4).Grow(2); // b is Rect2I(-2, -2, 12, 8)
:::
:::::

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Rect2i_method_grow_individual}
::: {.rst-class}
classref-method
:::
::::

`Rect2i<class_Rect2i>`{.interpreted-text role="ref"}
**grow_individual**(left: `int<class_int>`{.interpreted-text
role="ref"}, top: `int<class_int>`{.interpreted-text role="ref"}, right:
`int<class_int>`{.interpreted-text role="ref"}, bottom:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Rect2i_method_grow_individual>`{.interpreted-text
role="ref"}

Returns a copy of this rectangle with its `left`, `top`, `right`, and
`bottom` sides extended by the given amounts. Negative values shrink the
sides, instead. See also
`grow<class_Rect2i_method_grow>`{.interpreted-text role="ref"} and
`grow_side<class_Rect2i_method_grow_side>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Rect2i_method_grow_side}
::: {.rst-class}
classref-method
:::
::::

`Rect2i<class_Rect2i>`{.interpreted-text role="ref"} **grow_side**(side:
`int<class_int>`{.interpreted-text role="ref"}, amount:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Rect2i_method_grow_side>`{.interpreted-text
role="ref"}

Returns a copy of this rectangle with its `side` extended by the given
`amount` (see `Side<enum_@GlobalScope_Side>`{.interpreted-text
role="ref"} constants). A negative `amount` shrinks the rectangle,
instead. See also `grow<class_Rect2i_method_grow>`{.interpreted-text
role="ref"} and
`grow_individual<class_Rect2i_method_grow_individual>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Rect2i_method_has_area}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_area**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Rect2i_method_has_area>`{.interpreted-text
role="ref"}

Returns `true` if this rectangle has positive width and height. See also
`get_area<class_Rect2i_method_get_area>`{.interpreted-text role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Rect2i_method_has_point}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_point**(point:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Rect2i_method_has_point>`{.interpreted-text
role="ref"}

Returns `true` if the rectangle contains the given `point`. By
convention, points on the right and bottom edges are **not** included.

\*\*Note:\*\* This method is not reliable for **Rect2i** with a
*negative* `size<class_Rect2i_property_size>`{.interpreted-text
role="ref"}. Use `abs<class_Rect2i_method_abs>`{.interpreted-text
role="ref"} first to get a valid rectangle.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Rect2i_method_intersection}
::: {.rst-class}
classref-method
:::
::::

`Rect2i<class_Rect2i>`{.interpreted-text role="ref"} **intersection**(b:
`Rect2i<class_Rect2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Rect2i_method_intersection>`{.interpreted-text
role="ref"}

Returns the intersection between this rectangle and `b`. If the
rectangles do not intersect, returns an empty **Rect2i**.

::::: {.tabs}
::: {.code-tab}
gdscript

var a = Rect2i(0, 0, 5, 10) var b = Rect2i(2, 0, 8, 4)

var c = a.intersection(b) \# c is Rect2i(2, 0, 3, 4)
:::

::: {.code-tab}
csharp

var a = new Rect2I(0, 0, 5, 10); var b = new Rect2I(2, 0, 8, 4);

var c = rect1.Intersection(rect2); // c is Rect2I(2, 0, 3, 4)
:::
:::::

\*\*Note:\*\* If you only need to know whether two rectangles are
overlapping, use
`intersects<class_Rect2i_method_intersects>`{.interpreted-text
role="ref"}, instead.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Rect2i_method_intersects}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **intersects**(b:
`Rect2i<class_Rect2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Rect2i_method_intersects>`{.interpreted-text
role="ref"}

Returns `true` if this rectangle overlaps with the `b` rectangle. The
edges of both rectangles are excluded.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Rect2i_method_merge}
::: {.rst-class}
classref-method
:::
::::

`Rect2i<class_Rect2i>`{.interpreted-text role="ref"} **merge**(b:
`Rect2i<class_Rect2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Rect2i_method_merge>`{.interpreted-text
role="ref"}

Returns a **Rect2i** that encloses both this rectangle and `b` around
the edges. See also
`encloses<class_Rect2i_method_encloses>`{.interpreted-text role="ref"}.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Operator Descriptions

:::: {#class_Rect2i_operator_neq_Rect2i}
::: {.rst-class}
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`Rect2i<class_Rect2i>`{.interpreted-text role="ref"})
`🔗<class_Rect2i_operator_neq_Rect2i>`{.interpreted-text role="ref"}

Returns `true` if the
`position<class_Rect2i_property_position>`{.interpreted-text role="ref"}
or `size<class_Rect2i_property_size>`{.interpreted-text role="ref"} of
both rectangles are not equal.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Rect2i_operator_eq_Rect2i}
::: {.rst-class}
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`Rect2i<class_Rect2i>`{.interpreted-text role="ref"})
`🔗<class_Rect2i_operator_eq_Rect2i>`{.interpreted-text role="ref"}

Returns `true` if both
`position<class_Rect2i_property_position>`{.interpreted-text role="ref"}
and `size<class_Rect2i_property_size>`{.interpreted-text role="ref"} of
the rectangles are equal, respectively.