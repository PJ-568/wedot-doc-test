github_url

:   hide

# RayCast2D {#class_RayCast2D}

**Inherits:** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A ray in 2D space, used to find the first
`CollisionObject2D<class_CollisionObject2D>`{.interpreted-text
role="ref"} it intersects.

::: {.rst-class}
classref-introduction-group
:::

## Description

A raycast represents a ray from its origin to its
`target_position<class_RayCast2D_property_target_position>`{.interpreted-text
role="ref"} that finds the closest
`CollisionObject2D<class_CollisionObject2D>`{.interpreted-text
role="ref"} along its path, if it intersects any.

\*\*RayCast2D\*\* can ignore some objects by adding them to an exception
list, by making its detection reporting ignore
`Area2D<class_Area2D>`{.interpreted-text role="ref"}s
(`collide_with_areas<class_RayCast2D_property_collide_with_areas>`{.interpreted-text
role="ref"}) or `PhysicsBody2D<class_PhysicsBody2D>`{.interpreted-text
role="ref"}s
(`collide_with_bodies<class_RayCast2D_property_collide_with_bodies>`{.interpreted-text
role="ref"}), or by configuring physics layers.

\*\*RayCast2D\*\* calculates intersection every physics frame, and it
holds the result until the next physics frame. For an immediate raycast,
or if you want to configure a **RayCast2D** multiple times within the
same physics frame, use
`force_raycast_update<class_RayCast2D_method_force_raycast_update>`{.interpreted-text
role="ref"}.

To sweep over a region of 2D space, you can approximate the region with
multiple **RayCast2D**s or use
`ShapeCast2D<class_ShapeCast2D>`{.interpreted-text role="ref"}.

::: {.rst-class}
classref-introduction-group
:::

## Tutorials

- `Ray-casting <../tutorials/physics/ray-casting>`{.interpreted-text
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

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_RayCast2D_property_collide_with_areas}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **collide_with_areas**
= `false`
`🔗<class_RayCast2D_property_collide_with_areas>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collide_with_areas**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_collide_with_areas_enabled**()

If `true`, collisions with `Area2D<class_Area2D>`{.interpreted-text
role="ref"}s will be reported.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RayCast2D_property_collide_with_bodies}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **collide_with_bodies**
= `true`
`🔗<class_RayCast2D_property_collide_with_bodies>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collide_with_bodies**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_collide_with_bodies_enabled**()

If `true`, collisions with
`PhysicsBody2D<class_PhysicsBody2D>`{.interpreted-text role="ref"}s will
be reported.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RayCast2D_property_collision_mask}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **collision_mask** = `1`
`🔗<class_RayCast2D_property_collision_mask>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collision_mask**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_collision_mask**()

The ray\'s collision mask. Only objects in at least one collision layer
enabled in the mask will be detected. See [Collision layers and
masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks)
in the documentation for more information.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RayCast2D_property_enabled}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **enabled** = `true`
`🔗<class_RayCast2D_property_enabled>`{.interpreted-text role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_enabled**()

If `true`, collisions will be reported.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RayCast2D_property_exclude_parent}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **exclude_parent** =
`true` `🔗<class_RayCast2D_property_exclude_parent>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_exclude_parent_body**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_exclude_parent_body**()

If `true`, the parent node will be excluded from collision detection.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RayCast2D_property_hit_from_inside}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **hit_from_inside** =
`false` `🔗<class_RayCast2D_property_hit_from_inside>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_hit_from_inside**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_hit_from_inside_enabled**()

If `true`, the ray will detect a hit when starting inside shapes. In
this case the collision normal will be `Vector2(0, 0)`. Does not affect
concave polygon shapes.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RayCast2D_property_target_position}
::: {.rst-class}
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**target_position** = `Vector2(0, 50)`
`🔗<class_RayCast2D_property_target_position>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_target_position**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_target_position**()

The ray\'s destination point, relative to the RayCast\'s `position`.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_RayCast2D_method_add_exception}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_exception**(node:
`CollisionObject2D<class_CollisionObject2D>`{.interpreted-text
role="ref"})
`🔗<class_RayCast2D_method_add_exception>`{.interpreted-text role="ref"}

Adds a collision exception so the ray does not report collisions with
the specified
`CollisionObject2D<class_CollisionObject2D>`{.interpreted-text
role="ref"} node.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RayCast2D_method_add_exception_rid}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_exception_rid**(rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_RayCast2D_method_add_exception_rid>`{.interpreted-text
role="ref"}

Adds a collision exception so the ray does not report collisions with
the specified `RID<class_RID>`{.interpreted-text role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RayCast2D_method_clear_exceptions}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_exceptions**()
`🔗<class_RayCast2D_method_clear_exceptions>`{.interpreted-text
role="ref"}

Removes all collision exceptions for this ray.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RayCast2D_method_force_raycast_update}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**force_raycast_update**()
`🔗<class_RayCast2D_method_force_raycast_update>`{.interpreted-text
role="ref"}

Updates the collision information for the ray immediately, without
waiting for the next `_physics_process` call. Use this method, for
example, when the ray or its parent has changed state.

\*\*Note:\*\*
`enabled<class_RayCast2D_property_enabled>`{.interpreted-text
role="ref"} does not need to be `true` for this to work.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RayCast2D_method_get_collider}
::: {.rst-class}
classref-method
:::
::::

`Object<class_Object>`{.interpreted-text role="ref"} **get_collider**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_RayCast2D_method_get_collider>`{.interpreted-text
role="ref"}

Returns the first object that the ray intersects, or `null` if no object
is intersecting the ray (i.e.
`is_colliding<class_RayCast2D_method_is_colliding>`{.interpreted-text
role="ref"} returns `false`).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RayCast2D_method_get_collider_rid}
::: {.rst-class}
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_collider_rid**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RayCast2D_method_get_collider_rid>`{.interpreted-text
role="ref"}

Returns the `RID<class_RID>`{.interpreted-text role="ref"} of the first
object that the ray intersects, or an empty
`RID<class_RID>`{.interpreted-text role="ref"} if no object is
intersecting the ray (i.e.
`is_colliding<class_RayCast2D_method_is_colliding>`{.interpreted-text
role="ref"} returns `false`).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RayCast2D_method_get_collider_shape}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_collider_shape**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RayCast2D_method_get_collider_shape>`{.interpreted-text
role="ref"}

Returns the shape ID of the first object that the ray intersects, or `0`
if no object is intersecting the ray (i.e.
`is_colliding<class_RayCast2D_method_is_colliding>`{.interpreted-text
role="ref"} returns `false`).

To get the intersected shape node, for a
`CollisionObject2D<class_CollisionObject2D>`{.interpreted-text
role="ref"} target, use:

::::: {.tabs}
::: {.code-tab}
gdscript

var target = get_collider() \# A CollisionObject2D. var shape_id =
get_collider_shape() \# The shape index in the collider. var owner_id =
target.shape_find_owner(shape_id) \# The owner ID in the collider. var
shape = target.shape_owner_get_owner(owner_id)
:::

::: {.code-tab}
csharp

var target = (CollisionObject2D)GetCollider(); // A CollisionObject2D.
var shapeId = GetColliderShape(); // The shape index in the collider.
var ownerId = target.ShapeFindOwner(shapeId); // The owner ID in the
collider. var shape = target.ShapeOwnerGetOwner(ownerId);
:::
:::::

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RayCast2D_method_get_collision_mask_value}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_collision_mask_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RayCast2D_method_get_collision_mask_value>`{.interpreted-text
role="ref"}

Returns whether or not the specified layer of the
`collision_mask<class_RayCast2D_property_collision_mask>`{.interpreted-text
role="ref"} is enabled, given a `layer_number` between 1 and 32.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RayCast2D_method_get_collision_normal}
::: {.rst-class}
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_collision_normal**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RayCast2D_method_get_collision_normal>`{.interpreted-text
role="ref"}

Returns the normal of the intersecting object\'s shape at the collision
point, or `Vector2(0, 0)` if the ray starts inside the shape and
`hit_from_inside<class_RayCast2D_property_hit_from_inside>`{.interpreted-text
role="ref"} is `true`.

\*\*Note:\*\* Check that
`is_colliding<class_RayCast2D_method_is_colliding>`{.interpreted-text
role="ref"} returns `true` before calling this method to ensure the
returned normal is valid and up-to-date.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RayCast2D_method_get_collision_point}
::: {.rst-class}
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_collision_point**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RayCast2D_method_get_collision_point>`{.interpreted-text
role="ref"}

Returns the collision point at which the ray intersects the closest
object, in the global coordinate system. If
`hit_from_inside<class_RayCast2D_property_hit_from_inside>`{.interpreted-text
role="ref"} is `true` and the ray starts inside of a collision shape,
this function will return the origin point of the ray.

\*\*Note:\*\* Check that
`is_colliding<class_RayCast2D_method_is_colliding>`{.interpreted-text
role="ref"} returns `true` before calling this method to ensure the
returned point is valid and up-to-date.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RayCast2D_method_is_colliding}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_colliding**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_RayCast2D_method_is_colliding>`{.interpreted-text
role="ref"}

Returns whether any object is intersecting with the ray\'s vector
(considering the vector length).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RayCast2D_method_remove_exception}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_exception**(node:
`CollisionObject2D<class_CollisionObject2D>`{.interpreted-text
role="ref"})
`🔗<class_RayCast2D_method_remove_exception>`{.interpreted-text
role="ref"}

Removes a collision exception so the ray does report collisions with the
specified `CollisionObject2D<class_CollisionObject2D>`{.interpreted-text
role="ref"} node.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RayCast2D_method_remove_exception_rid}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_exception_rid**(rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_RayCast2D_method_remove_exception_rid>`{.interpreted-text
role="ref"}

Removes a collision exception so the ray does report collisions with the
specified `RID<class_RID>`{.interpreted-text role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RayCast2D_method_set_collision_mask_value}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_collision_mask_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"}, value:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RayCast2D_method_set_collision_mask_value>`{.interpreted-text
role="ref"}

Based on `value`, enables or disables the specified layer in the
`collision_mask<class_RayCast2D_property_collision_mask>`{.interpreted-text
role="ref"}, given a `layer_number` between 1 and 32.