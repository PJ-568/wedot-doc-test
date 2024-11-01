github_url

:   hide

# CollisionShape3D {#class_CollisionShape3D}

**Inherits:** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A node that provides a `Shape3D<class_Shape3D>`{.interpreted-text
role="ref"} to a
`CollisionObject3D<class_CollisionObject3D>`{.interpreted-text
role="ref"} parent.

::: {.rst-class}
classref-introduction-group
:::

## Description

A node that provides a `Shape3D<class_Shape3D>`{.interpreted-text
role="ref"} to a
`CollisionObject3D<class_CollisionObject3D>`{.interpreted-text
role="ref"} parent and allows to edit it. This can give a detection
shape to an `Area3D<class_Area3D>`{.interpreted-text role="ref"} or turn
a `PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text role="ref"}
into a solid object.

\*\*Warning:\*\* A non-uniformly scaled **CollisionShape3D** will likely
not behave as expected. Make sure to keep its scale the same on all axes
and adjust its
`shape<class_CollisionShape3D_property_shape>`{.interpreted-text
role="ref"} resource instead.

::: {.rst-class}
classref-introduction-group
:::

## Tutorials

- `Physics introduction <../tutorials/physics/physics_introduction>`{.interpreted-text
  role="doc"}
- [3D Kinematic Character
  Demo](https://godotengine.org/asset-library/asset/2739)
- [3D Platformer Demo](https://godotengine.org/asset-library/asset/2748)
- [Third Person Shooter (TPS)
  Demo](https://godotengine.org/asset-library/asset/2710)

::: {.rst-class}
classref-reftable-group
:::

## Properties

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

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_CollisionShape3D_property_disabled}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **disabled** = `false`
`🔗<class_CollisionShape3D_property_disabled>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_disabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_disabled**()

A disabled collision shape has no effect in the world.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionShape3D_property_shape}
::: {.rst-class}
classref-property
:::
::::

`Shape3D<class_Shape3D>`{.interpreted-text role="ref"} **shape**
`🔗<class_CollisionShape3D_property_shape>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shape**(value: `Shape3D<class_Shape3D>`{.interpreted-text
  role="ref"})
- `Shape3D<class_Shape3D>`{.interpreted-text role="ref"} **get_shape**()

The actual shape owned by this collision shape.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_CollisionShape3D_method_make_convex_from_siblings}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**make_convex_from_siblings**()
`🔗<class_CollisionShape3D_method_make_convex_from_siblings>`{.interpreted-text
role="ref"}

Sets the collision shape\'s shape to the addition of all its convexed
`MeshInstance3D<class_MeshInstance3D>`{.interpreted-text role="ref"}
siblings geometry.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionShape3D_method_resource_changed}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**resource_changed**(resource:
`Resource<class_Resource>`{.interpreted-text role="ref"})
`🔗<class_CollisionShape3D_method_resource_changed>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`Resource.changed<class_Resource_signal_changed>`{.interpreted-text
role="ref"} instead.

This method does nothing.
