github_url

:   hide

# CollisionPolygon3D {#class_CollisionPolygon3D}

**Inherits:** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A node that provides a thickened polygon shape (a prism) to a
`CollisionObject3D<class_CollisionObject3D>`{.interpreted-text
role="ref"} parent.

::: {.rst-class}
classref-introduction-group
:::

## Description

A node that provides a thickened polygon shape (a prism) to a
`CollisionObject3D<class_CollisionObject3D>`{.interpreted-text
role="ref"} parent and allows to edit it. The polygon can be concave or
convex. This can give a detection shape to an
`Area3D<class_Area3D>`{.interpreted-text role="ref"} or turn
`PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text role="ref"} into
a solid object.

\*\*Warning:\*\* A non-uniformly scaled
`CollisionShape3D<class_CollisionShape3D>`{.interpreted-text role="ref"}
will likely not behave as expected. Make sure to keep its scale the same
on all axes and adjust its shape resource instead.

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
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_CollisionPolygon3D_property_depth}
::: {.rst-class}
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **depth** = `1.0`
`🔗<class_CollisionPolygon3D_property_depth>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_depth**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_depth**()

Length that the resulting collision extends in either direction
perpendicular to its 2D polygon.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionPolygon3D_property_disabled}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **disabled** = `false`
`🔗<class_CollisionPolygon3D_property_disabled>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_disabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_disabled**()

If `true`, no collision will be produced.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionPolygon3D_property_margin}
::: {.rst-class}
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **margin** = `0.04`
`🔗<class_CollisionPolygon3D_property_margin>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_margin**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_margin**()

The collision margin for the generated
`Shape3D<class_Shape3D>`{.interpreted-text role="ref"}. See
`Shape3D.margin<class_Shape3D_property_margin>`{.interpreted-text
role="ref"} for more details.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionPolygon3D_property_polygon}
::: {.rst-class}
classref-property
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **polygon** = `PackedVector2Array()`
`🔗<class_CollisionPolygon3D_property_polygon>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_polygon**(value:
  `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"})
- `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"} **get_polygon**()

Array of vertices which define the 2D polygon in the local XY plane.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} for more details.
