github_url

:   hide

# PhysicsDirectSpaceState3D {#class_PhysicsDirectSpaceState3D}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`PhysicsDirectSpaceState3DExtension<class_PhysicsDirectSpaceState3DExtension>`{.interpreted-text
role="ref"}

Provides direct access to a physics space in the
`PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text role="ref"}.

::: {.rst-class}
classref-introduction-group
:::

## Description

Provides direct access to a physics space in the
`PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text role="ref"}.
It\'s used mainly to do queries against objects and areas residing in a
given space.

::: {.rst-class}
classref-introduction-group
:::

## Tutorials

- `Physics introduction <../tutorials/physics/physics_introduction>`{.interpreted-text
  role="doc"}
- `Ray-casting <../tutorials/physics/ray-casting>`{.interpreted-text
  role="doc"}

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

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_PhysicsDirectSpaceState3D_method_cast_motion}
::: {.rst-class}
classref-method
:::
::::

`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} **cast_motion**(parameters:
`PhysicsShapeQueryParameters3D<class_PhysicsShapeQueryParameters3D>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsDirectSpaceState3D_method_cast_motion>`{.interpreted-text
role="ref"}

Checks how far a `Shape3D<class_Shape3D>`{.interpreted-text role="ref"}
can move without colliding. All the parameters for the query, including
the shape, are supplied through a
`PhysicsShapeQueryParameters3D<class_PhysicsShapeQueryParameters3D>`{.interpreted-text
role="ref"} object.

Returns an array with the safe and unsafe proportions (between 0 and 1)
of the motion. The safe proportion is the maximum fraction of the motion
that can be made without a collision. The unsafe proportion is the
minimum fraction of the distance that must be moved for a collision. If
no collision is detected a result of `[1.0, 1.0]` will be returned.

\*\*Note:\*\* Any `Shape3D<class_Shape3D>`{.interpreted-text
role="ref"}s that the shape is already colliding with e.g. inside of,
will be ignored. Use
`collide_shape<class_PhysicsDirectSpaceState3D_method_collide_shape>`{.interpreted-text
role="ref"} to determine the `Shape3D<class_Shape3D>`{.interpreted-text
role="ref"}s that the shape is already colliding with.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectSpaceState3D_method_collide_shape}
::: {.rst-class}
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Vector3<class_Vector3>`{.interpreted-text role="ref"}\]
**collide_shape**(parameters:
`PhysicsShapeQueryParameters3D<class_PhysicsShapeQueryParameters3D>`{.interpreted-text
role="ref"}, max_results: `int<class_int>`{.interpreted-text role="ref"}
= 32)
`🔗<class_PhysicsDirectSpaceState3D_method_collide_shape>`{.interpreted-text
role="ref"}

Checks the intersections of a shape, given through a
`PhysicsShapeQueryParameters3D<class_PhysicsShapeQueryParameters3D>`{.interpreted-text
role="ref"} object, against the space. The resulting array contains a
list of points where the shape intersects another. Like with
`intersect_shape<class_PhysicsDirectSpaceState3D_method_intersect_shape>`{.interpreted-text
role="ref"}, the number of returned results can be limited to save
processing time.

Returned points are a list of pairs of contact points. For each pair the
first one is in the shape passed in
`PhysicsShapeQueryParameters3D<class_PhysicsShapeQueryParameters3D>`{.interpreted-text
role="ref"} object, second one is in the collided shape from the physics
space.

\*\*Note:\*\* This method does not take into account the `motion`
property of the object.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectSpaceState3D_method_get_rest_info}
::: {.rst-class}
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_rest_info**(parameters:
`PhysicsShapeQueryParameters3D<class_PhysicsShapeQueryParameters3D>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsDirectSpaceState3D_method_get_rest_info>`{.interpreted-text
role="ref"}

Checks the intersections of a shape, given through a
`PhysicsShapeQueryParameters3D<class_PhysicsShapeQueryParameters3D>`{.interpreted-text
role="ref"} object, against the space. If it collides with more than one
shape, the nearest one is selected. The returned object is a dictionary
containing the following fields:

`collider_id`: The colliding object\'s ID.

`linear_velocity`: The colliding object\'s velocity
`Vector3<class_Vector3>`{.interpreted-text role="ref"}. If the object is
an `Area3D<class_Area3D>`{.interpreted-text role="ref"}, the result is
`(0, 0, 0)`.

`normal`: The object\'s surface normal at the intersection point.

`point`: The intersection point.

`rid`: The intersecting object\'s `RID<class_RID>`{.interpreted-text
role="ref"}.

`shape`: The shape index of the colliding shape.

If the shape did not intersect anything, then an empty dictionary is
returned instead.

\*\*Note:\*\* This method does not take into account the `motion`
property of the object.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectSpaceState3D_method_intersect_point}
::: {.rst-class}
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **intersect_point**(parameters:
`PhysicsPointQueryParameters3D<class_PhysicsPointQueryParameters3D>`{.interpreted-text
role="ref"}, max_results: `int<class_int>`{.interpreted-text role="ref"}
= 32)
`🔗<class_PhysicsDirectSpaceState3D_method_intersect_point>`{.interpreted-text
role="ref"}

Checks whether a point is inside any solid shape. Position and other
parameters are defined through
`PhysicsPointQueryParameters3D<class_PhysicsPointQueryParameters3D>`{.interpreted-text
role="ref"}. The shapes the point is inside of are returned in an array
containing dictionaries with the following fields:

`collider`: The colliding object.

`collider_id`: The colliding object\'s ID.

`rid`: The intersecting object\'s `RID<class_RID>`{.interpreted-text
role="ref"}.

`shape`: The shape index of the colliding shape.

The number of intersections can be limited with the `max_results`
parameter, to reduce the processing time.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectSpaceState3D_method_intersect_ray}
::: {.rst-class}
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**intersect_ray**(parameters:
`PhysicsRayQueryParameters3D<class_PhysicsRayQueryParameters3D>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsDirectSpaceState3D_method_intersect_ray>`{.interpreted-text
role="ref"}

Intersects a ray in a given space. Ray position and other parameters are
defined through
`PhysicsRayQueryParameters3D<class_PhysicsRayQueryParameters3D>`{.interpreted-text
role="ref"}. The returned object is a dictionary with the following
fields:

`collider`: The colliding object.

`collider_id`: The colliding object\'s ID.

`normal`: The object\'s surface normal at the intersection point, or
`Vector3(0, 0, 0)` if the ray starts inside the shape and
`PhysicsRayQueryParameters3D.hit_from_inside<class_PhysicsRayQueryParameters3D_property_hit_from_inside>`{.interpreted-text
role="ref"} is `true`.

`position`: The intersection point.

`face_index`: The face index at the intersection point.

\*\*Note:\*\* Returns a valid number only if the intersected shape is a
`ConcavePolygonShape3D<class_ConcavePolygonShape3D>`{.interpreted-text
role="ref"}. Otherwise, `-1` is returned.

`rid`: The intersecting object\'s `RID<class_RID>`{.interpreted-text
role="ref"}.

`shape`: The shape index of the colliding shape.

If the ray did not intersect anything, then an empty dictionary is
returned instead.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectSpaceState3D_method_intersect_shape}
::: {.rst-class}
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **intersect_shape**(parameters:
`PhysicsShapeQueryParameters3D<class_PhysicsShapeQueryParameters3D>`{.interpreted-text
role="ref"}, max_results: `int<class_int>`{.interpreted-text role="ref"}
= 32)
`🔗<class_PhysicsDirectSpaceState3D_method_intersect_shape>`{.interpreted-text
role="ref"}

Checks the intersections of a shape, given through a
`PhysicsShapeQueryParameters3D<class_PhysicsShapeQueryParameters3D>`{.interpreted-text
role="ref"} object, against the space. The intersected shapes are
returned in an array containing dictionaries with the following fields:

`collider`: The colliding object.

`collider_id`: The colliding object\'s ID.

`rid`: The intersecting object\'s `RID<class_RID>`{.interpreted-text
role="ref"}.

`shape`: The shape index of the colliding shape.

The number of intersections can be limited with the `max_results`
parameter, to reduce the processing time.

\*\*Note:\*\* This method does not take into account the `motion`
property of the object.