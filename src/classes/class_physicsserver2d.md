github_url

:   hide

# PhysicsServer2D {#class_PhysicsServer2D}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`PhysicsServer2DExtension<class_PhysicsServer2DExtension>`{.interpreted-text
role="ref"}

A server interface for low-level 2D physics access.

::: {.rst-class}
classref-introduction-group
:::

## Description

PhysicsServer2D is the server responsible for all 2D physics. It can
directly create and manipulate all physics objects:

- A *space* is a self-contained world for a physics simulation. It
  contains bodies, areas, and joints. Its state can be queried for
  collision and intersection information, and several parameters of the
  simulation can be modified.
- A *shape* is a geometric shape such as a circle, a rectangle, a
  capsule, or a polygon. It can be used for collision detection by
  adding it to a body/area, possibly with an extra transformation
  relative to the body/area\'s origin. Bodies/areas can have multiple
  (transformed) shapes added to them, and a single shape can be added to
  bodies/areas multiple times with different local transformations.
- A *body* is a physical object which can be in static, kinematic, or
  rigid mode. Its state (such as position and velocity) can be queried
  and updated. A force integration callback can be set to customize the
  body\'s physics.
- An *area* is a region in space which can be used to detect bodies and
  areas entering and exiting it. A body monitoring callback can be set
  to report entering/exiting body shapes, and similarly an area
  monitoring callback can be set. Gravity and damping can be overridden
  within the area by setting area parameters.
- A *joint* is a constraint, either between two bodies or on one body
  relative to a point. Parameters such as the joint bias and the rest
  length of a spring joint can be adjusted.

Physics objects in **PhysicsServer2D** may be created and manipulated
independently; they do not have to be tied to nodes in the scene tree.

\*\*Note:\*\* All the 2D physics nodes use the physics server
internally. Adding a physics node to the scene tree will cause a
corresponding physics object to be created in the physics server. A
rigid body node registers a callback that updates the node\'s transform
with the transform of the respective body object in the physics server
(every physics update). An area node registers a callback to inform the
area node about overlaps with the respective area object in the physics
server. The raycast node queries the direct state of the relevant space
in the physics server.

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
||

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Enumerations

:::: {#enum_PhysicsServer2D_SpaceParameter}
::: {.rst-class}
classref-enumeration
:::
::::

enum **SpaceParameter**:
`🔗<enum_PhysicsServer2D_SpaceParameter>`{.interpreted-text role="ref"}

:::: {#class_PhysicsServer2D_constant_SPACE_PARAM_CONTACT_RECYCLE_RADIUS}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`SpaceParameter<enum_PhysicsServer2D_SpaceParameter>`{.interpreted-text
role="ref"} **SPACE_PARAM_CONTACT_RECYCLE_RADIUS** = `0`

Constant to set/get the maximum distance a pair of bodies has to move
before their collision status has to be recalculated. The default value
of this parameter is
`ProjectSettings.physics/2d/solver/contact_recycle_radius<class_ProjectSettings_property_physics/2d/solver/contact_recycle_radius>`{.interpreted-text
role="ref"}.

:::: {#class_PhysicsServer2D_constant_SPACE_PARAM_CONTACT_MAX_SEPARATION}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`SpaceParameter<enum_PhysicsServer2D_SpaceParameter>`{.interpreted-text
role="ref"} **SPACE_PARAM_CONTACT_MAX_SEPARATION** = `1`

Constant to set/get the maximum distance a shape can be from another
before they are considered separated and the contact is discarded. The
default value of this parameter is
`ProjectSettings.physics/2d/solver/contact_max_separation<class_ProjectSettings_property_physics/2d/solver/contact_max_separation>`{.interpreted-text
role="ref"}.

:::: {#class_PhysicsServer2D_constant_SPACE_PARAM_CONTACT_MAX_ALLOWED_PENETRATION}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`SpaceParameter<enum_PhysicsServer2D_SpaceParameter>`{.interpreted-text
role="ref"} **SPACE_PARAM_CONTACT_MAX_ALLOWED_PENETRATION** = `2`

Constant to set/get the maximum distance a shape can penetrate another
shape before it is considered a collision. The default value of this
parameter is
`ProjectSettings.physics/2d/solver/contact_max_allowed_penetration<class_ProjectSettings_property_physics/2d/solver/contact_max_allowed_penetration>`{.interpreted-text
role="ref"}.

:::: {#class_PhysicsServer2D_constant_SPACE_PARAM_CONTACT_DEFAULT_BIAS}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`SpaceParameter<enum_PhysicsServer2D_SpaceParameter>`{.interpreted-text
role="ref"} **SPACE_PARAM_CONTACT_DEFAULT_BIAS** = `3`

Constant to set/get the default solver bias for all physics contacts. A
solver bias is a factor controlling how much two objects \"rebound\",
after overlapping, to avoid leaving them in that state because of
numerical imprecision. The default value of this parameter is
`ProjectSettings.physics/2d/solver/default_contact_bias<class_ProjectSettings_property_physics/2d/solver/default_contact_bias>`{.interpreted-text
role="ref"}.

:::: {#class_PhysicsServer2D_constant_SPACE_PARAM_BODY_LINEAR_VELOCITY_SLEEP_THRESHOLD}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`SpaceParameter<enum_PhysicsServer2D_SpaceParameter>`{.interpreted-text
role="ref"} **SPACE_PARAM_BODY_LINEAR_VELOCITY_SLEEP_THRESHOLD** = `4`

Constant to set/get the threshold linear velocity of activity. A body
marked as potentially inactive for both linear and angular velocity will
be put to sleep after the time given. The default value of this
parameter is
`ProjectSettings.physics/2d/sleep_threshold_linear<class_ProjectSettings_property_physics/2d/sleep_threshold_linear>`{.interpreted-text
role="ref"}.

:::: {#class_PhysicsServer2D_constant_SPACE_PARAM_BODY_ANGULAR_VELOCITY_SLEEP_THRESHOLD}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`SpaceParameter<enum_PhysicsServer2D_SpaceParameter>`{.interpreted-text
role="ref"} **SPACE_PARAM_BODY_ANGULAR_VELOCITY_SLEEP_THRESHOLD** = `5`

Constant to set/get the threshold angular velocity of activity. A body
marked as potentially inactive for both linear and angular velocity will
be put to sleep after the time given. The default value of this
parameter is
`ProjectSettings.physics/2d/sleep_threshold_angular<class_ProjectSettings_property_physics/2d/sleep_threshold_angular>`{.interpreted-text
role="ref"}.

:::: {#class_PhysicsServer2D_constant_SPACE_PARAM_BODY_TIME_TO_SLEEP}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`SpaceParameter<enum_PhysicsServer2D_SpaceParameter>`{.interpreted-text
role="ref"} **SPACE_PARAM_BODY_TIME_TO_SLEEP** = `6`

Constant to set/get the maximum time of activity. A body marked as
potentially inactive for both linear and angular velocity will be put to
sleep after this time. The default value of this parameter is
`ProjectSettings.physics/2d/time_before_sleep<class_ProjectSettings_property_physics/2d/time_before_sleep>`{.interpreted-text
role="ref"}.

:::: {#class_PhysicsServer2D_constant_SPACE_PARAM_CONSTRAINT_DEFAULT_BIAS}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`SpaceParameter<enum_PhysicsServer2D_SpaceParameter>`{.interpreted-text
role="ref"} **SPACE_PARAM_CONSTRAINT_DEFAULT_BIAS** = `7`

Constant to set/get the default solver bias for all physics constraints.
A solver bias is a factor controlling how much two objects \"rebound\",
after violating a constraint, to avoid leaving them in that state
because of numerical imprecision. The default value of this parameter is
`ProjectSettings.physics/2d/solver/default_constraint_bias<class_ProjectSettings_property_physics/2d/solver/default_constraint_bias>`{.interpreted-text
role="ref"}.

:::: {#class_PhysicsServer2D_constant_SPACE_PARAM_SOLVER_ITERATIONS}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`SpaceParameter<enum_PhysicsServer2D_SpaceParameter>`{.interpreted-text
role="ref"} **SPACE_PARAM_SOLVER_ITERATIONS** = `8`

Constant to set/get the number of solver iterations for all contacts and
constraints. The greater the number of iterations, the more accurate the
collisions will be. However, a greater number of iterations requires
more CPU power, which can decrease performance. The default value of
this parameter is
`ProjectSettings.physics/2d/solver/solver_iterations<class_ProjectSettings_property_physics/2d/solver/solver_iterations>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer2D_ShapeType}
::: {.rst-class}
classref-enumeration
:::
::::

enum **ShapeType**:
`🔗<enum_PhysicsServer2D_ShapeType>`{.interpreted-text role="ref"}

:::: {#class_PhysicsServer2D_constant_SHAPE_WORLD_BOUNDARY}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`ShapeType<enum_PhysicsServer2D_ShapeType>`{.interpreted-text
role="ref"} **SHAPE_WORLD_BOUNDARY** = `0`

This is the constant for creating world boundary shapes. A world
boundary shape is an *infinite* line with an origin point, and a normal.
Thus, it can be used for front/behind checks.

:::: {#class_PhysicsServer2D_constant_SHAPE_SEPARATION_RAY}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`ShapeType<enum_PhysicsServer2D_ShapeType>`{.interpreted-text
role="ref"} **SHAPE_SEPARATION_RAY** = `1`

This is the constant for creating separation ray shapes. A separation
ray is defined by a length and separates itself from what is touching
its far endpoint. Useful for character controllers.

:::: {#class_PhysicsServer2D_constant_SHAPE_SEGMENT}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`ShapeType<enum_PhysicsServer2D_ShapeType>`{.interpreted-text
role="ref"} **SHAPE_SEGMENT** = `2`

This is the constant for creating segment shapes. A segment shape is a
*finite* line from a point A to a point B. It can be checked for
intersections.

:::: {#class_PhysicsServer2D_constant_SHAPE_CIRCLE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`ShapeType<enum_PhysicsServer2D_ShapeType>`{.interpreted-text
role="ref"} **SHAPE_CIRCLE** = `3`

This is the constant for creating circle shapes. A circle shape only has
a radius. It can be used for intersections and inside/outside checks.

:::: {#class_PhysicsServer2D_constant_SHAPE_RECTANGLE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`ShapeType<enum_PhysicsServer2D_ShapeType>`{.interpreted-text
role="ref"} **SHAPE_RECTANGLE** = `4`

This is the constant for creating rectangle shapes. A rectangle shape is
defined by a width and a height. It can be used for intersections and
inside/outside checks.

:::: {#class_PhysicsServer2D_constant_SHAPE_CAPSULE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`ShapeType<enum_PhysicsServer2D_ShapeType>`{.interpreted-text
role="ref"} **SHAPE_CAPSULE** = `5`

This is the constant for creating capsule shapes. A capsule shape is
defined by a radius and a length. It can be used for intersections and
inside/outside checks.

:::: {#class_PhysicsServer2D_constant_SHAPE_CONVEX_POLYGON}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`ShapeType<enum_PhysicsServer2D_ShapeType>`{.interpreted-text
role="ref"} **SHAPE_CONVEX_POLYGON** = `6`

This is the constant for creating convex polygon shapes. A polygon is
defined by a list of points. It can be used for intersections and
inside/outside checks.

:::: {#class_PhysicsServer2D_constant_SHAPE_CONCAVE_POLYGON}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`ShapeType<enum_PhysicsServer2D_ShapeType>`{.interpreted-text
role="ref"} **SHAPE_CONCAVE_POLYGON** = `7`

This is the constant for creating concave polygon shapes. A polygon is
defined by a list of points. It can be used for intersections checks,
but not for inside/outside checks.

:::: {#class_PhysicsServer2D_constant_SHAPE_CUSTOM}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`ShapeType<enum_PhysicsServer2D_ShapeType>`{.interpreted-text
role="ref"} **SHAPE_CUSTOM** = `8`

This constant is used internally by the engine. Any attempt to create
this kind of shape results in an error.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer2D_AreaParameter}
::: {.rst-class}
classref-enumeration
:::
::::

enum **AreaParameter**:
`🔗<enum_PhysicsServer2D_AreaParameter>`{.interpreted-text role="ref"}

:::: {#class_PhysicsServer2D_constant_AREA_PARAM_GRAVITY_OVERRIDE_MODE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`AreaParameter<enum_PhysicsServer2D_AreaParameter>`{.interpreted-text
role="ref"} **AREA_PARAM_GRAVITY_OVERRIDE_MODE** = `0`

Constant to set/get gravity override mode in an area. See
`AreaSpaceOverrideMode<enum_PhysicsServer2D_AreaSpaceOverrideMode>`{.interpreted-text
role="ref"} for possible values. The default value of this parameter is
`AREA_SPACE_OVERRIDE_DISABLED<class_PhysicsServer2D_constant_AREA_SPACE_OVERRIDE_DISABLED>`{.interpreted-text
role="ref"}.

:::: {#class_PhysicsServer2D_constant_AREA_PARAM_GRAVITY}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`AreaParameter<enum_PhysicsServer2D_AreaParameter>`{.interpreted-text
role="ref"} **AREA_PARAM_GRAVITY** = `1`

Constant to set/get gravity strength in an area. The default value of
this parameter is `9.80665`.

:::: {#class_PhysicsServer2D_constant_AREA_PARAM_GRAVITY_VECTOR}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`AreaParameter<enum_PhysicsServer2D_AreaParameter>`{.interpreted-text
role="ref"} **AREA_PARAM_GRAVITY_VECTOR** = `2`

Constant to set/get gravity vector/center in an area. The default value
of this parameter is `Vector2(0, -1)`.

:::: {#class_PhysicsServer2D_constant_AREA_PARAM_GRAVITY_IS_POINT}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`AreaParameter<enum_PhysicsServer2D_AreaParameter>`{.interpreted-text
role="ref"} **AREA_PARAM_GRAVITY_IS_POINT** = `3`

Constant to set/get whether the gravity vector of an area is a
direction, or a center point. The default value of this parameter is
`false`.

:::: {#class_PhysicsServer2D_constant_AREA_PARAM_GRAVITY_POINT_UNIT_DISTANCE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`AreaParameter<enum_PhysicsServer2D_AreaParameter>`{.interpreted-text
role="ref"} **AREA_PARAM_GRAVITY_POINT_UNIT_DISTANCE** = `4`

Constant to set/get the distance at which the gravity strength is equal
to the gravity controlled by
`AREA_PARAM_GRAVITY<class_PhysicsServer2D_constant_AREA_PARAM_GRAVITY>`{.interpreted-text
role="ref"}. For example, on a planet 100 pixels in radius with a
surface gravity of 4.0 px/s², set the gravity to 4.0 and the unit
distance to 100.0. The gravity will have falloff according to the
inverse square law, so in the example, at 200 pixels from the center the
gravity will be 1.0 px/s² (twice the distance, 1/4th the gravity), at 50
pixels it will be 16.0 px/s² (half the distance, 4x the gravity), and so
on.

The above is true only when the unit distance is a positive number. When
the unit distance is set to 0.0, the gravity will be constant regardless
of distance. The default value of this parameter is `0.0`.

:::: {#class_PhysicsServer2D_constant_AREA_PARAM_LINEAR_DAMP_OVERRIDE_MODE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`AreaParameter<enum_PhysicsServer2D_AreaParameter>`{.interpreted-text
role="ref"} **AREA_PARAM_LINEAR_DAMP_OVERRIDE_MODE** = `5`

Constant to set/get linear damping override mode in an area. See
`AreaSpaceOverrideMode<enum_PhysicsServer2D_AreaSpaceOverrideMode>`{.interpreted-text
role="ref"} for possible values. The default value of this parameter is
`AREA_SPACE_OVERRIDE_DISABLED<class_PhysicsServer2D_constant_AREA_SPACE_OVERRIDE_DISABLED>`{.interpreted-text
role="ref"}.

:::: {#class_PhysicsServer2D_constant_AREA_PARAM_LINEAR_DAMP}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`AreaParameter<enum_PhysicsServer2D_AreaParameter>`{.interpreted-text
role="ref"} **AREA_PARAM_LINEAR_DAMP** = `6`

Constant to set/get the linear damping factor of an area. The default
value of this parameter is `0.1`.

:::: {#class_PhysicsServer2D_constant_AREA_PARAM_ANGULAR_DAMP_OVERRIDE_MODE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`AreaParameter<enum_PhysicsServer2D_AreaParameter>`{.interpreted-text
role="ref"} **AREA_PARAM_ANGULAR_DAMP_OVERRIDE_MODE** = `7`

Constant to set/get angular damping override mode in an area. See
`AreaSpaceOverrideMode<enum_PhysicsServer2D_AreaSpaceOverrideMode>`{.interpreted-text
role="ref"} for possible values. The default value of this parameter is
`AREA_SPACE_OVERRIDE_DISABLED<class_PhysicsServer2D_constant_AREA_SPACE_OVERRIDE_DISABLED>`{.interpreted-text
role="ref"}.

:::: {#class_PhysicsServer2D_constant_AREA_PARAM_ANGULAR_DAMP}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`AreaParameter<enum_PhysicsServer2D_AreaParameter>`{.interpreted-text
role="ref"} **AREA_PARAM_ANGULAR_DAMP** = `8`

Constant to set/get the angular damping factor of an area. The default
value of this parameter is `1.0`.

:::: {#class_PhysicsServer2D_constant_AREA_PARAM_PRIORITY}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`AreaParameter<enum_PhysicsServer2D_AreaParameter>`{.interpreted-text
role="ref"} **AREA_PARAM_PRIORITY** = `9`

Constant to set/get the priority (order of processing) of an area. The
default value of this parameter is `0`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer2D_AreaSpaceOverrideMode}
::: {.rst-class}
classref-enumeration
:::
::::

enum **AreaSpaceOverrideMode**:
`🔗<enum_PhysicsServer2D_AreaSpaceOverrideMode>`{.interpreted-text
role="ref"}

:::: {#class_PhysicsServer2D_constant_AREA_SPACE_OVERRIDE_DISABLED}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`AreaSpaceOverrideMode<enum_PhysicsServer2D_AreaSpaceOverrideMode>`{.interpreted-text
role="ref"} **AREA_SPACE_OVERRIDE_DISABLED** = `0`

This area does not affect gravity/damp. These are generally areas that
exist only to detect collisions, and objects entering or exiting them.

:::: {#class_PhysicsServer2D_constant_AREA_SPACE_OVERRIDE_COMBINE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`AreaSpaceOverrideMode<enum_PhysicsServer2D_AreaSpaceOverrideMode>`{.interpreted-text
role="ref"} **AREA_SPACE_OVERRIDE_COMBINE** = `1`

This area adds its gravity/damp values to whatever has been calculated
so far. This way, many overlapping areas can combine their physics to
make interesting effects.

:::: {#class_PhysicsServer2D_constant_AREA_SPACE_OVERRIDE_COMBINE_REPLACE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`AreaSpaceOverrideMode<enum_PhysicsServer2D_AreaSpaceOverrideMode>`{.interpreted-text
role="ref"} **AREA_SPACE_OVERRIDE_COMBINE_REPLACE** = `2`

This area adds its gravity/damp values to whatever has been calculated
so far. Then stops taking into account the rest of the areas, even the
default one.

:::: {#class_PhysicsServer2D_constant_AREA_SPACE_OVERRIDE_REPLACE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`AreaSpaceOverrideMode<enum_PhysicsServer2D_AreaSpaceOverrideMode>`{.interpreted-text
role="ref"} **AREA_SPACE_OVERRIDE_REPLACE** = `3`

This area replaces any gravity/damp, even the default one, and stops
taking into account the rest of the areas.

:::: {#class_PhysicsServer2D_constant_AREA_SPACE_OVERRIDE_REPLACE_COMBINE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`AreaSpaceOverrideMode<enum_PhysicsServer2D_AreaSpaceOverrideMode>`{.interpreted-text
role="ref"} **AREA_SPACE_OVERRIDE_REPLACE_COMBINE** = `4`

This area replaces any gravity/damp calculated so far, but keeps
calculating the rest of the areas, down to the default one.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer2D_BodyMode}
::: {.rst-class}
classref-enumeration
:::
::::

enum **BodyMode**: `🔗<enum_PhysicsServer2D_BodyMode>`{.interpreted-text
role="ref"}

:::: {#class_PhysicsServer2D_constant_BODY_MODE_STATIC}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`BodyMode<enum_PhysicsServer2D_BodyMode>`{.interpreted-text role="ref"}
**BODY_MODE_STATIC** = `0`

Constant for static bodies. In this mode, a body can be only moved by
user code and doesn\'t collide with other bodies along its path when
moved.

:::: {#class_PhysicsServer2D_constant_BODY_MODE_KINEMATIC}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`BodyMode<enum_PhysicsServer2D_BodyMode>`{.interpreted-text role="ref"}
**BODY_MODE_KINEMATIC** = `1`

Constant for kinematic bodies. In this mode, a body can be only moved by
user code and collides with other bodies along its path.

:::: {#class_PhysicsServer2D_constant_BODY_MODE_RIGID}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`BodyMode<enum_PhysicsServer2D_BodyMode>`{.interpreted-text role="ref"}
**BODY_MODE_RIGID** = `2`

Constant for rigid bodies. In this mode, a body can be pushed by other
bodies and has forces applied.

:::: {#class_PhysicsServer2D_constant_BODY_MODE_RIGID_LINEAR}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`BodyMode<enum_PhysicsServer2D_BodyMode>`{.interpreted-text role="ref"}
**BODY_MODE_RIGID_LINEAR** = `3`

Constant for linear rigid bodies. In this mode, a body can not rotate,
and only its linear velocity is affected by external forces.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer2D_BodyParameter}
::: {.rst-class}
classref-enumeration
:::
::::

enum **BodyParameter**:
`🔗<enum_PhysicsServer2D_BodyParameter>`{.interpreted-text role="ref"}

:::: {#class_PhysicsServer2D_constant_BODY_PARAM_BOUNCE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`BodyParameter<enum_PhysicsServer2D_BodyParameter>`{.interpreted-text
role="ref"} **BODY_PARAM_BOUNCE** = `0`

Constant to set/get a body\'s bounce factor. The default value of this
parameter is `0.0`.

:::: {#class_PhysicsServer2D_constant_BODY_PARAM_FRICTION}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`BodyParameter<enum_PhysicsServer2D_BodyParameter>`{.interpreted-text
role="ref"} **BODY_PARAM_FRICTION** = `1`

Constant to set/get a body\'s friction. The default value of this
parameter is `1.0`.

:::: {#class_PhysicsServer2D_constant_BODY_PARAM_MASS}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`BodyParameter<enum_PhysicsServer2D_BodyParameter>`{.interpreted-text
role="ref"} **BODY_PARAM_MASS** = `2`

Constant to set/get a body\'s mass. The default value of this parameter
is `1.0`. If the body\'s mode is set to
`BODY_MODE_RIGID<class_PhysicsServer2D_constant_BODY_MODE_RIGID>`{.interpreted-text
role="ref"}, then setting this parameter will have the following
additional effects:

- If the parameter
  `BODY_PARAM_CENTER_OF_MASS<class_PhysicsServer2D_constant_BODY_PARAM_CENTER_OF_MASS>`{.interpreted-text
  role="ref"} has never been set explicitly, then the value of that
  parameter will be recalculated based on the body\'s shapes.
- If the parameter
  `BODY_PARAM_INERTIA<class_PhysicsServer2D_constant_BODY_PARAM_INERTIA>`{.interpreted-text
  role="ref"} is set to a value `<= 0.0`, then the value of that
  parameter will be recalculated based on the body\'s shapes, mass, and
  center of mass.

:::: {#class_PhysicsServer2D_constant_BODY_PARAM_INERTIA}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`BodyParameter<enum_PhysicsServer2D_BodyParameter>`{.interpreted-text
role="ref"} **BODY_PARAM_INERTIA** = `3`

Constant to set/get a body\'s inertia. The default value of this
parameter is `0.0`. If the body\'s inertia is set to a value `<= 0.0`,
then the inertia will be recalculated based on the body\'s shapes, mass,
and center of mass.

:::: {#class_PhysicsServer2D_constant_BODY_PARAM_CENTER_OF_MASS}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`BodyParameter<enum_PhysicsServer2D_BodyParameter>`{.interpreted-text
role="ref"} **BODY_PARAM_CENTER_OF_MASS** = `4`

Constant to set/get a body\'s center of mass position in the body\'s
local coordinate system. The default value of this parameter is
`Vector2(0,0)`. If this parameter is never set explicitly, then it is
recalculated based on the body\'s shapes when setting the parameter
`BODY_PARAM_MASS<class_PhysicsServer2D_constant_BODY_PARAM_MASS>`{.interpreted-text
role="ref"} or when calling
`body_set_space<class_PhysicsServer2D_method_body_set_space>`{.interpreted-text
role="ref"}.

:::: {#class_PhysicsServer2D_constant_BODY_PARAM_GRAVITY_SCALE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`BodyParameter<enum_PhysicsServer2D_BodyParameter>`{.interpreted-text
role="ref"} **BODY_PARAM_GRAVITY_SCALE** = `5`

Constant to set/get a body\'s gravity multiplier. The default value of
this parameter is `1.0`.

:::: {#class_PhysicsServer2D_constant_BODY_PARAM_LINEAR_DAMP_MODE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`BodyParameter<enum_PhysicsServer2D_BodyParameter>`{.interpreted-text
role="ref"} **BODY_PARAM_LINEAR_DAMP_MODE** = `6`

Constant to set/get a body\'s linear damping mode. See
`BodyDampMode<enum_PhysicsServer2D_BodyDampMode>`{.interpreted-text
role="ref"} for possible values. The default value of this parameter is
`BODY_DAMP_MODE_COMBINE<class_PhysicsServer2D_constant_BODY_DAMP_MODE_COMBINE>`{.interpreted-text
role="ref"}.

:::: {#class_PhysicsServer2D_constant_BODY_PARAM_ANGULAR_DAMP_MODE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`BodyParameter<enum_PhysicsServer2D_BodyParameter>`{.interpreted-text
role="ref"} **BODY_PARAM_ANGULAR_DAMP_MODE** = `7`

Constant to set/get a body\'s angular damping mode. See
`BodyDampMode<enum_PhysicsServer2D_BodyDampMode>`{.interpreted-text
role="ref"} for possible values. The default value of this parameter is
`BODY_DAMP_MODE_COMBINE<class_PhysicsServer2D_constant_BODY_DAMP_MODE_COMBINE>`{.interpreted-text
role="ref"}.

:::: {#class_PhysicsServer2D_constant_BODY_PARAM_LINEAR_DAMP}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`BodyParameter<enum_PhysicsServer2D_BodyParameter>`{.interpreted-text
role="ref"} **BODY_PARAM_LINEAR_DAMP** = `8`

Constant to set/get a body\'s linear damping factor. The default value
of this parameter is `0.0`.

:::: {#class_PhysicsServer2D_constant_BODY_PARAM_ANGULAR_DAMP}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`BodyParameter<enum_PhysicsServer2D_BodyParameter>`{.interpreted-text
role="ref"} **BODY_PARAM_ANGULAR_DAMP** = `9`

Constant to set/get a body\'s angular damping factor. The default value
of this parameter is `0.0`.

:::: {#class_PhysicsServer2D_constant_BODY_PARAM_MAX}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`BodyParameter<enum_PhysicsServer2D_BodyParameter>`{.interpreted-text
role="ref"} **BODY_PARAM_MAX** = `10`

Represents the size of the
`BodyParameter<enum_PhysicsServer2D_BodyParameter>`{.interpreted-text
role="ref"} enum.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer2D_BodyDampMode}
::: {.rst-class}
classref-enumeration
:::
::::

enum **BodyDampMode**:
`🔗<enum_PhysicsServer2D_BodyDampMode>`{.interpreted-text role="ref"}

:::: {#class_PhysicsServer2D_constant_BODY_DAMP_MODE_COMBINE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`BodyDampMode<enum_PhysicsServer2D_BodyDampMode>`{.interpreted-text
role="ref"} **BODY_DAMP_MODE_COMBINE** = `0`

The body\'s damping value is added to any value set in areas or the
default value.

:::: {#class_PhysicsServer2D_constant_BODY_DAMP_MODE_REPLACE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`BodyDampMode<enum_PhysicsServer2D_BodyDampMode>`{.interpreted-text
role="ref"} **BODY_DAMP_MODE_REPLACE** = `1`

The body\'s damping value replaces any value set in areas or the default
value.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer2D_BodyState}
::: {.rst-class}
classref-enumeration
:::
::::

enum **BodyState**:
`🔗<enum_PhysicsServer2D_BodyState>`{.interpreted-text role="ref"}

:::: {#class_PhysicsServer2D_constant_BODY_STATE_TRANSFORM}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`BodyState<enum_PhysicsServer2D_BodyState>`{.interpreted-text
role="ref"} **BODY_STATE_TRANSFORM** = `0`

Constant to set/get the current transform matrix of the body.

:::: {#class_PhysicsServer2D_constant_BODY_STATE_LINEAR_VELOCITY}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`BodyState<enum_PhysicsServer2D_BodyState>`{.interpreted-text
role="ref"} **BODY_STATE_LINEAR_VELOCITY** = `1`

Constant to set/get the current linear velocity of the body.

:::: {#class_PhysicsServer2D_constant_BODY_STATE_ANGULAR_VELOCITY}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`BodyState<enum_PhysicsServer2D_BodyState>`{.interpreted-text
role="ref"} **BODY_STATE_ANGULAR_VELOCITY** = `2`

Constant to set/get the current angular velocity of the body.

:::: {#class_PhysicsServer2D_constant_BODY_STATE_SLEEPING}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`BodyState<enum_PhysicsServer2D_BodyState>`{.interpreted-text
role="ref"} **BODY_STATE_SLEEPING** = `3`

Constant to sleep/wake up a body, or to get whether it is sleeping.

:::: {#class_PhysicsServer2D_constant_BODY_STATE_CAN_SLEEP}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`BodyState<enum_PhysicsServer2D_BodyState>`{.interpreted-text
role="ref"} **BODY_STATE_CAN_SLEEP** = `4`

Constant to set/get whether the body can sleep.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer2D_JointType}
::: {.rst-class}
classref-enumeration
:::
::::

enum **JointType**:
`🔗<enum_PhysicsServer2D_JointType>`{.interpreted-text role="ref"}

:::: {#class_PhysicsServer2D_constant_JOINT_TYPE_PIN}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`JointType<enum_PhysicsServer2D_JointType>`{.interpreted-text
role="ref"} **JOINT_TYPE_PIN** = `0`

Constant to create pin joints.

:::: {#class_PhysicsServer2D_constant_JOINT_TYPE_GROOVE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`JointType<enum_PhysicsServer2D_JointType>`{.interpreted-text
role="ref"} **JOINT_TYPE_GROOVE** = `1`

Constant to create groove joints.

:::: {#class_PhysicsServer2D_constant_JOINT_TYPE_DAMPED_SPRING}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`JointType<enum_PhysicsServer2D_JointType>`{.interpreted-text
role="ref"} **JOINT_TYPE_DAMPED_SPRING** = `2`

Constant to create damped spring joints.

:::: {#class_PhysicsServer2D_constant_JOINT_TYPE_MAX}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`JointType<enum_PhysicsServer2D_JointType>`{.interpreted-text
role="ref"} **JOINT_TYPE_MAX** = `3`

Represents the size of the
`JointType<enum_PhysicsServer2D_JointType>`{.interpreted-text
role="ref"} enum.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer2D_JointParam}
::: {.rst-class}
classref-enumeration
:::
::::

enum **JointParam**:
`🔗<enum_PhysicsServer2D_JointParam>`{.interpreted-text role="ref"}

:::: {#class_PhysicsServer2D_constant_JOINT_PARAM_BIAS}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`JointParam<enum_PhysicsServer2D_JointParam>`{.interpreted-text
role="ref"} **JOINT_PARAM_BIAS** = `0`

Constant to set/get how fast the joint pulls the bodies back to satisfy
the joint constraint. The lower the value, the more the two bodies can
pull on the joint. The default value of this parameter is `0.0`.

\*\*Note:\*\* In Godot Physics, this parameter is only used for pin
joints and groove joints.

:::: {#class_PhysicsServer2D_constant_JOINT_PARAM_MAX_BIAS}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`JointParam<enum_PhysicsServer2D_JointParam>`{.interpreted-text
role="ref"} **JOINT_PARAM_MAX_BIAS** = `1`

Constant to set/get the maximum speed with which the joint can apply
corrections. The default value of this parameter is `3.40282e+38`.

\*\*Note:\*\* In Godot Physics, this parameter is only used for groove
joints.

:::: {#class_PhysicsServer2D_constant_JOINT_PARAM_MAX_FORCE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`JointParam<enum_PhysicsServer2D_JointParam>`{.interpreted-text
role="ref"} **JOINT_PARAM_MAX_FORCE** = `2`

Constant to set/get the maximum force that the joint can use to act on
the two bodies. The default value of this parameter is `3.40282e+38`.

\*\*Note:\*\* In Godot Physics, this parameter is only used for groove
joints.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer2D_PinJointParam}
::: {.rst-class}
classref-enumeration
:::
::::

enum **PinJointParam**:
`🔗<enum_PhysicsServer2D_PinJointParam>`{.interpreted-text role="ref"}

:::: {#class_PhysicsServer2D_constant_PIN_JOINT_SOFTNESS}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`PinJointParam<enum_PhysicsServer2D_PinJointParam>`{.interpreted-text
role="ref"} **PIN_JOINT_SOFTNESS** = `0`

Constant to set/get a how much the bond of the pin joint can flex. The
default value of this parameter is `0.0`.

:::: {#class_PhysicsServer2D_constant_PIN_JOINT_LIMIT_UPPER}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`PinJointParam<enum_PhysicsServer2D_PinJointParam>`{.interpreted-text
role="ref"} **PIN_JOINT_LIMIT_UPPER** = `1`

The maximum rotation around the pin.

:::: {#class_PhysicsServer2D_constant_PIN_JOINT_LIMIT_LOWER}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`PinJointParam<enum_PhysicsServer2D_PinJointParam>`{.interpreted-text
role="ref"} **PIN_JOINT_LIMIT_LOWER** = `2`

The minimum rotation around the pin.

:::: {#class_PhysicsServer2D_constant_PIN_JOINT_MOTOR_TARGET_VELOCITY}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`PinJointParam<enum_PhysicsServer2D_PinJointParam>`{.interpreted-text
role="ref"} **PIN_JOINT_MOTOR_TARGET_VELOCITY** = `3`

Target speed for the motor. In radians per second.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer2D_PinJointFlag}
::: {.rst-class}
classref-enumeration
:::
::::

enum **PinJointFlag**:
`🔗<enum_PhysicsServer2D_PinJointFlag>`{.interpreted-text role="ref"}

:::: {#class_PhysicsServer2D_constant_PIN_JOINT_FLAG_ANGULAR_LIMIT_ENABLED}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`PinJointFlag<enum_PhysicsServer2D_PinJointFlag>`{.interpreted-text
role="ref"} **PIN_JOINT_FLAG_ANGULAR_LIMIT_ENABLED** = `0`

If `true`, the pin has a maximum and a minimum rotation.

:::: {#class_PhysicsServer2D_constant_PIN_JOINT_FLAG_MOTOR_ENABLED}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`PinJointFlag<enum_PhysicsServer2D_PinJointFlag>`{.interpreted-text
role="ref"} **PIN_JOINT_FLAG_MOTOR_ENABLED** = `1`

If `true`, a motor turns the pin.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer2D_DampedSpringParam}
::: {.rst-class}
classref-enumeration
:::
::::

enum **DampedSpringParam**:
`🔗<enum_PhysicsServer2D_DampedSpringParam>`{.interpreted-text
role="ref"}

:::: {#class_PhysicsServer2D_constant_DAMPED_SPRING_REST_LENGTH}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`DampedSpringParam<enum_PhysicsServer2D_DampedSpringParam>`{.interpreted-text
role="ref"} **DAMPED_SPRING_REST_LENGTH** = `0`

Sets the resting length of the spring joint. The joint will always try
to go to back this length when pulled apart. The default value of this
parameter is the distance between the joint\'s anchor points.

:::: {#class_PhysicsServer2D_constant_DAMPED_SPRING_STIFFNESS}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`DampedSpringParam<enum_PhysicsServer2D_DampedSpringParam>`{.interpreted-text
role="ref"} **DAMPED_SPRING_STIFFNESS** = `1`

Sets the stiffness of the spring joint. The joint applies a force equal
to the stiffness times the distance from its resting length. The default
value of this parameter is `20.0`.

:::: {#class_PhysicsServer2D_constant_DAMPED_SPRING_DAMPING}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`DampedSpringParam<enum_PhysicsServer2D_DampedSpringParam>`{.interpreted-text
role="ref"} **DAMPED_SPRING_DAMPING** = `2`

Sets the damping ratio of the spring joint. A value of 0 indicates an
undamped spring, while 1 causes the system to reach equilibrium as fast
as possible (critical damping). The default value of this parameter is
`1.5`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer2D_CCDMode}
::: {.rst-class}
classref-enumeration
:::
::::

enum **CCDMode**: `🔗<enum_PhysicsServer2D_CCDMode>`{.interpreted-text
role="ref"}

:::: {#class_PhysicsServer2D_constant_CCD_MODE_DISABLED}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`CCDMode<enum_PhysicsServer2D_CCDMode>`{.interpreted-text role="ref"}
**CCD_MODE_DISABLED** = `0`

Disables continuous collision detection. This is the fastest way to
detect body collisions, but it can miss small and/or fast-moving
objects.

:::: {#class_PhysicsServer2D_constant_CCD_MODE_CAST_RAY}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`CCDMode<enum_PhysicsServer2D_CCDMode>`{.interpreted-text role="ref"}
**CCD_MODE_CAST_RAY** = `1`

Enables continuous collision detection by raycasting. It is faster than
shapecasting, but less precise.

:::: {#class_PhysicsServer2D_constant_CCD_MODE_CAST_SHAPE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`CCDMode<enum_PhysicsServer2D_CCDMode>`{.interpreted-text role="ref"}
**CCD_MODE_CAST_SHAPE** = `2`

Enables continuous collision detection by shapecasting. It is the
slowest CCD method, and the most precise.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer2D_AreaBodyStatus}
::: {.rst-class}
classref-enumeration
:::
::::

enum **AreaBodyStatus**:
`🔗<enum_PhysicsServer2D_AreaBodyStatus>`{.interpreted-text role="ref"}

:::: {#class_PhysicsServer2D_constant_AREA_BODY_ADDED}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`AreaBodyStatus<enum_PhysicsServer2D_AreaBodyStatus>`{.interpreted-text
role="ref"} **AREA_BODY_ADDED** = `0`

The value of the first parameter and area callback function receives,
when an object enters one of its shapes.

:::: {#class_PhysicsServer2D_constant_AREA_BODY_REMOVED}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`AreaBodyStatus<enum_PhysicsServer2D_AreaBodyStatus>`{.interpreted-text
role="ref"} **AREA_BODY_REMOVED** = `1`

The value of the first parameter and area callback function receives,
when an object exits one of its shapes.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer2D_ProcessInfo}
::: {.rst-class}
classref-enumeration
:::
::::

enum **ProcessInfo**:
`🔗<enum_PhysicsServer2D_ProcessInfo>`{.interpreted-text role="ref"}

:::: {#class_PhysicsServer2D_constant_INFO_ACTIVE_OBJECTS}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`ProcessInfo<enum_PhysicsServer2D_ProcessInfo>`{.interpreted-text
role="ref"} **INFO_ACTIVE_OBJECTS** = `0`

Constant to get the number of objects that are not sleeping.

:::: {#class_PhysicsServer2D_constant_INFO_COLLISION_PAIRS}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`ProcessInfo<enum_PhysicsServer2D_ProcessInfo>`{.interpreted-text
role="ref"} **INFO_COLLISION_PAIRS** = `1`

Constant to get the number of possible collisions.

:::: {#class_PhysicsServer2D_constant_INFO_ISLAND_COUNT}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`ProcessInfo<enum_PhysicsServer2D_ProcessInfo>`{.interpreted-text
role="ref"} **INFO_ISLAND_COUNT** = `2`

Constant to get the number of space regions where a collision could
occur.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_PhysicsServer2D_method_area_add_shape}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_add_shape**(area: `RID<class_RID>`{.interpreted-text role="ref"},
shape: `RID<class_RID>`{.interpreted-text role="ref"}, transform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"} =
Transform2D(1, 0, 0, 1, 0, 0), disabled:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_PhysicsServer2D_method_area_add_shape>`{.interpreted-text
role="ref"}

Adds a shape to the area, with the given local transform. The shape
(together with its `transform` and `disabled` properties) is added to an
array of shapes, and the shapes of an area are usually referenced by
their index in this array.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_area_attach_canvas_instance_id}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_attach_canvas_instance_id**(area:
`RID<class_RID>`{.interpreted-text role="ref"}, id:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_area_attach_canvas_instance_id>`{.interpreted-text
role="ref"}

Attaches the `ObjectID` of a canvas to the area. Use
`Object.get_instance_id<class_Object_method_get_instance_id>`{.interpreted-text
role="ref"} to get the `ObjectID` of a
`CanvasLayer<class_CanvasLayer>`{.interpreted-text role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_area_attach_object_instance_id}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_attach_object_instance_id**(area:
`RID<class_RID>`{.interpreted-text role="ref"}, id:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_area_attach_object_instance_id>`{.interpreted-text
role="ref"}

Attaches the `ObjectID` of an `Object<class_Object>`{.interpreted-text
role="ref"} to the area. Use
`Object.get_instance_id<class_Object_method_get_instance_id>`{.interpreted-text
role="ref"} to get the `ObjectID` of a
`CollisionObject2D<class_CollisionObject2D>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_area_clear_shapes}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_clear_shapes**(area: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer2D_method_area_clear_shapes>`{.interpreted-text
role="ref"}

Removes all shapes from the area. This does not delete the shapes
themselves, so they can continue to be used elsewhere or added back
later.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_area_create}
::: {.rst-class}
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **area_create**()
`🔗<class_PhysicsServer2D_method_area_create>`{.interpreted-text
role="ref"}

Creates a 2D area object in the physics server, and returns the
`RID<class_RID>`{.interpreted-text role="ref"} that identifies it. The
default settings for the created area include a collision layer and mask
set to `1`, and `monitorable` set to `false`.

Use
`area_add_shape<class_PhysicsServer2D_method_area_add_shape>`{.interpreted-text
role="ref"} to add shapes to it, use
`area_set_transform<class_PhysicsServer2D_method_area_set_transform>`{.interpreted-text
role="ref"} to set its transform, and use
`area_set_space<class_PhysicsServer2D_method_area_set_space>`{.interpreted-text
role="ref"} to add the area to a space. If you want the area to be
detectable use
`area_set_monitorable<class_PhysicsServer2D_method_area_set_monitorable>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_area_get_canvas_instance_id}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**area_get_canvas_instance_id**(area: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_area_get_canvas_instance_id>`{.interpreted-text
role="ref"}

Returns the `ObjectID` of the canvas attached to the area. Use
`@GlobalScope.instance_from_id<class_@GlobalScope_method_instance_from_id>`{.interpreted-text
role="ref"} to retrieve a
`CanvasLayer<class_CanvasLayer>`{.interpreted-text role="ref"} from a
nonzero `ObjectID`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_area_get_collision_layer}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**area_get_collision_layer**(area: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_area_get_collision_layer>`{.interpreted-text
role="ref"}

Returns the physics layer or layers the area belongs to, as a bitmask.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_area_get_collision_mask}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**area_get_collision_mask**(area: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_area_get_collision_mask>`{.interpreted-text
role="ref"}

Returns the physics layer or layers the area can contact with, as a
bitmask.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_area_get_object_instance_id}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**area_get_object_instance_id**(area: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_area_get_object_instance_id>`{.interpreted-text
role="ref"}

Returns the `ObjectID` attached to the area. Use
`@GlobalScope.instance_from_id<class_@GlobalScope_method_instance_from_id>`{.interpreted-text
role="ref"} to retrieve an `Object<class_Object>`{.interpreted-text
role="ref"} from a nonzero `ObjectID`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_area_get_param}
::: {.rst-class}
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**area_get_param**(area: `RID<class_RID>`{.interpreted-text role="ref"},
param:
`AreaParameter<enum_PhysicsServer2D_AreaParameter>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_area_get_param>`{.interpreted-text
role="ref"}

Returns the value of the given area parameter. See
`AreaParameter<enum_PhysicsServer2D_AreaParameter>`{.interpreted-text
role="ref"} for the list of available parameters.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_area_get_shape}
::: {.rst-class}
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **area_get_shape**(area:
`RID<class_RID>`{.interpreted-text role="ref"}, shape_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_area_get_shape>`{.interpreted-text
role="ref"}

Returns the `RID<class_RID>`{.interpreted-text role="ref"} of the shape
with the given index in the area\'s array of shapes.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_area_get_shape_count}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**area_get_shape_count**(area: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_area_get_shape_count>`{.interpreted-text
role="ref"}

Returns the number of shapes added to the area.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_area_get_shape_transform}
::: {.rst-class}
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**area_get_shape_transform**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_area_get_shape_transform>`{.interpreted-text
role="ref"}

Returns the local transform matrix of the shape with the given index in
the area\'s array of shapes.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_area_get_space}
::: {.rst-class}
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **area_get_space**(area:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_area_get_space>`{.interpreted-text
role="ref"}

Returns the `RID<class_RID>`{.interpreted-text role="ref"} of the space
assigned to the area. Returns an empty
`RID<class_RID>`{.interpreted-text role="ref"} if no space is assigned.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_area_get_transform}
::: {.rst-class}
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**area_get_transform**(area: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_area_get_transform>`{.interpreted-text
role="ref"}

Returns the transform matrix of the area.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_area_remove_shape}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_remove_shape**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_area_remove_shape>`{.interpreted-text
role="ref"}

Removes the shape with the given index from the area\'s array of shapes.
The shape itself is not deleted, so it can continue to be used elsewhere
or added back later. As a result of this operation, the area\'s shapes
which used to have indices higher than `shape_idx` will have their index
decreased by one.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_area_set_area_monitor_callback}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_set_area_monitor_callback**(area:
`RID<class_RID>`{.interpreted-text role="ref"}, callback:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_area_set_area_monitor_callback>`{.interpreted-text
role="ref"}

Sets the area\'s area monitor callback. This callback will be called
when any other (shape of an) area enters or exits (a shape of) the given
area, and must take the following five parameters:

1.  an integer `status`: either
    `AREA_BODY_ADDED<class_PhysicsServer2D_constant_AREA_BODY_ADDED>`{.interpreted-text
    role="ref"} or
    `AREA_BODY_REMOVED<class_PhysicsServer2D_constant_AREA_BODY_REMOVED>`{.interpreted-text
    role="ref"} depending on whether the other area\'s shape entered or
    exited the area,
2.  an `RID<class_RID>`{.interpreted-text role="ref"} `area_rid`: the
    `RID<class_RID>`{.interpreted-text role="ref"} of the other area
    that entered or exited the area,
3.  an integer `instance_id`: the `ObjectID` attached to the other area,
4.  an integer `area_shape_idx`: the index of the shape of the other
    area that entered or exited the area,
5.  an integer `self_shape_idx`: the index of the shape of the area
    where the other area entered or exited.

By counting (or keeping track of) the shapes that enter and exit, it can
be determined if an area (with all its shapes) is entering for the first
time or exiting for the last time.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_area_set_collision_layer}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_set_collision_layer**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, layer: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_area_set_collision_layer>`{.interpreted-text
role="ref"}

Assigns the area to one or many physics layers, via a bitmask.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_area_set_collision_mask}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_set_collision_mask**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, mask: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_area_set_collision_mask>`{.interpreted-text
role="ref"}

Sets which physics layers the area will monitor, via a bitmask.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_area_set_monitor_callback}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_set_monitor_callback**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, callback: `Callable<class_Callable>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer2D_method_area_set_monitor_callback>`{.interpreted-text
role="ref"}

Sets the area\'s body monitor callback. This callback will be called
when any other (shape of a) body enters or exits (a shape of) the given
area, and must take the following five parameters:

1.  an integer `status`: either
    `AREA_BODY_ADDED<class_PhysicsServer2D_constant_AREA_BODY_ADDED>`{.interpreted-text
    role="ref"} or
    `AREA_BODY_REMOVED<class_PhysicsServer2D_constant_AREA_BODY_REMOVED>`{.interpreted-text
    role="ref"} depending on whether the other body shape entered or
    exited the area,
2.  an `RID<class_RID>`{.interpreted-text role="ref"} `body_rid`: the
    `RID<class_RID>`{.interpreted-text role="ref"} of the body that
    entered or exited the area,
3.  an integer `instance_id`: the `ObjectID` attached to the body,
4.  an integer `body_shape_idx`: the index of the shape of the body that
    entered or exited the area,
5.  an integer `self_shape_idx`: the index of the shape of the area
    where the body entered or exited.

By counting (or keeping track of) the shapes that enter and exit, it can
be determined if a body (with all its shapes) is entering for the first
time or exiting for the last time.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_area_set_monitorable}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_set_monitorable**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, monitorable: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer2D_method_area_set_monitorable>`{.interpreted-text
role="ref"}

Sets whether the area is monitorable or not. If `monitorable` is `true`,
the area monitoring callback of other areas will be called when this
area enters or exits them.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_area_set_param}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_set_param**(area: `RID<class_RID>`{.interpreted-text role="ref"},
param:
`AreaParameter<enum_PhysicsServer2D_AreaParameter>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer2D_method_area_set_param>`{.interpreted-text
role="ref"}

Sets the value of the given area parameter. See
`AreaParameter<enum_PhysicsServer2D_AreaParameter>`{.interpreted-text
role="ref"} for the list of available parameters.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_area_set_shape}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_set_shape**(area: `RID<class_RID>`{.interpreted-text role="ref"},
shape_idx: `int<class_int>`{.interpreted-text role="ref"}, shape:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_area_set_shape>`{.interpreted-text
role="ref"}

Replaces the area\'s shape at the given index by another shape, while
not affecting the `transform` and `disabled` properties at the same
index.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_area_set_shape_disabled}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_set_shape_disabled**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"},
disabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_area_set_shape_disabled>`{.interpreted-text
role="ref"}

Sets the disabled property of the area\'s shape with the given index. If
`disabled` is `true`, then the shape will not detect any other shapes
entering or exiting it.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_area_set_shape_transform}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_set_shape_transform**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"},
transform: `Transform2D<class_Transform2D>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer2D_method_area_set_shape_transform>`{.interpreted-text
role="ref"}

Sets the local transform matrix of the area\'s shape with the given
index.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_area_set_space}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_set_space**(area: `RID<class_RID>`{.interpreted-text role="ref"},
space: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_area_set_space>`{.interpreted-text
role="ref"}

Adds the area to the given space, after removing the area from the
previously assigned space (if any).

\*\*Note:\*\* To remove an area from a space without immediately adding
it back elsewhere, use `PhysicsServer2D.area_set_space(area, RID())`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_area_set_transform}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_set_transform**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, transform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_area_set_transform>`{.interpreted-text
role="ref"}

Sets the transform matrix of the area.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_add_collision_exception}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_add_collision_exception**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, excepted_body:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_body_add_collision_exception>`{.interpreted-text
role="ref"}

Adds `excepted_body` to the body\'s list of collision exceptions, so
that collisions with it are ignored.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_add_constant_central_force}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_add_constant_central_force**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, force:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_body_add_constant_central_force>`{.interpreted-text
role="ref"}

Adds a constant directional force to the body. The force does not affect
rotation. The force remains applied over time until cleared with
`PhysicsServer2D.body_set_constant_force(body, Vector2(0, 0))`.

This is equivalent to using
`body_add_constant_force<class_PhysicsServer2D_method_body_add_constant_force>`{.interpreted-text
role="ref"} at the body\'s center of mass.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_add_constant_force}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_add_constant_force**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, force: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, position: `Vector2<class_Vector2>`{.interpreted-text
role="ref"} = Vector2(0, 0))
`🔗<class_PhysicsServer2D_method_body_add_constant_force>`{.interpreted-text
role="ref"}

Adds a constant positioned force to the body. The force can affect
rotation if `position` is different from the body\'s center of mass. The
force remains applied over time until cleared with
`PhysicsServer2D.body_set_constant_force(body, Vector2(0, 0))`.

`position` is the offset from the body origin in global coordinates.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_add_constant_torque}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_add_constant_torque**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, torque: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_body_add_constant_torque>`{.interpreted-text
role="ref"}

Adds a constant rotational force to the body. The force does not affect
position. The force remains applied over time until cleared with
`PhysicsServer2D.body_set_constant_torque(body, 0)`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_add_shape}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_add_shape**(body: `RID<class_RID>`{.interpreted-text role="ref"},
shape: `RID<class_RID>`{.interpreted-text role="ref"}, transform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"} =
Transform2D(1, 0, 0, 1, 0, 0), disabled:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_PhysicsServer2D_method_body_add_shape>`{.interpreted-text
role="ref"}

Adds a shape to the area, with the given local transform. The shape
(together with its `transform` and `disabled` properties) is added to an
array of shapes, and the shapes of a body are usually referenced by
their index in this array.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_apply_central_force}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_apply_central_force**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, force: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer2D_method_body_apply_central_force>`{.interpreted-text
role="ref"}

Applies a directional force to the body, at the body\'s center of mass.
The force does not affect rotation. A force is time dependent and meant
to be applied every physics update.

This is equivalent to using
`body_apply_force<class_PhysicsServer2D_method_body_apply_force>`{.interpreted-text
role="ref"} at the body\'s center of mass.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_apply_central_impulse}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_apply_central_impulse**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, impulse: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer2D_method_body_apply_central_impulse>`{.interpreted-text
role="ref"}

Applies a directional impulse to the body, at the body\'s center of
mass. The impulse does not affect rotation.

An impulse is time-independent! Applying an impulse every frame would
result in a framerate-dependent force. For this reason, it should only
be used when simulating one-time impacts (use the \"\_force\" functions
otherwise).

This is equivalent to using
`body_apply_impulse<class_PhysicsServer2D_method_body_apply_impulse>`{.interpreted-text
role="ref"} at the body\'s center of mass.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_apply_force}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_apply_force**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, force: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, position: `Vector2<class_Vector2>`{.interpreted-text
role="ref"} = Vector2(0, 0))
`🔗<class_PhysicsServer2D_method_body_apply_force>`{.interpreted-text
role="ref"}

Applies a positioned force to the body. The force can affect rotation if
`position` is different from the body\'s center of mass. A force is time
dependent and meant to be applied every physics update.

`position` is the offset from the body origin in global coordinates.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_apply_impulse}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_apply_impulse**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, impulse: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, position: `Vector2<class_Vector2>`{.interpreted-text
role="ref"} = Vector2(0, 0))
`🔗<class_PhysicsServer2D_method_body_apply_impulse>`{.interpreted-text
role="ref"}

Applies a positioned impulse to the body. The impulse can affect
rotation if `position` is different from the body\'s center of mass.

An impulse is time-independent! Applying an impulse every frame would
result in a framerate-dependent force. For this reason, it should only
be used when simulating one-time impacts (use the \"\_force\" functions
otherwise).

`position` is the offset from the body origin in global coordinates.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_apply_torque}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_apply_torque**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, torque: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_body_apply_torque>`{.interpreted-text
role="ref"}

Applies a rotational force to the body. The force does not affect
position. A force is time dependent and meant to be applied every
physics update.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_apply_torque_impulse}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_apply_torque_impulse**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, impulse: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer2D_method_body_apply_torque_impulse>`{.interpreted-text
role="ref"}

Applies a rotational impulse to the body. The impulse does not affect
position.

An impulse is time-independent! Applying an impulse every frame would
result in a framerate-dependent force. For this reason, it should only
be used when simulating one-time impacts (use the \"\_force\" functions
otherwise).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_attach_canvas_instance_id}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_attach_canvas_instance_id**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, id:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_body_attach_canvas_instance_id>`{.interpreted-text
role="ref"}

Attaches the `ObjectID` of a canvas to the body. Use
`Object.get_instance_id<class_Object_method_get_instance_id>`{.interpreted-text
role="ref"} to get the `ObjectID` of a
`CanvasLayer<class_CanvasLayer>`{.interpreted-text role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_attach_object_instance_id}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_attach_object_instance_id**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, id:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_body_attach_object_instance_id>`{.interpreted-text
role="ref"}

Attaches the `ObjectID` of an `Object<class_Object>`{.interpreted-text
role="ref"} to the body. Use
`Object.get_instance_id<class_Object_method_get_instance_id>`{.interpreted-text
role="ref"} to get the `ObjectID` of a
`CollisionObject2D<class_CollisionObject2D>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_clear_shapes}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_clear_shapes**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer2D_method_body_clear_shapes>`{.interpreted-text
role="ref"}

Removes all shapes from the body. This does not delete the shapes
themselves, so they can continue to be used elsewhere or added back
later.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_create}
::: {.rst-class}
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **body_create**()
`🔗<class_PhysicsServer2D_method_body_create>`{.interpreted-text
role="ref"}

Creates a 2D body object in the physics server, and returns the
`RID<class_RID>`{.interpreted-text role="ref"} that identifies it. The
default settings for the created area include a collision layer and mask
set to `1`, and body mode set to
`BODY_MODE_RIGID<class_PhysicsServer2D_constant_BODY_MODE_RIGID>`{.interpreted-text
role="ref"}.

Use
`body_add_shape<class_PhysicsServer2D_method_body_add_shape>`{.interpreted-text
role="ref"} to add shapes to it, use
`body_set_state<class_PhysicsServer2D_method_body_set_state>`{.interpreted-text
role="ref"} to set its transform, and use
`body_set_space<class_PhysicsServer2D_method_body_set_space>`{.interpreted-text
role="ref"} to add the body to a space.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_get_canvas_instance_id}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**body_get_canvas_instance_id**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_body_get_canvas_instance_id>`{.interpreted-text
role="ref"}

Returns the `ObjectID` of the canvas attached to the body. Use
`@GlobalScope.instance_from_id<class_@GlobalScope_method_instance_from_id>`{.interpreted-text
role="ref"} to retrieve a
`CanvasLayer<class_CanvasLayer>`{.interpreted-text role="ref"} from a
nonzero `ObjectID`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_get_collision_layer}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**body_get_collision_layer**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_body_get_collision_layer>`{.interpreted-text
role="ref"}

Returns the physics layer or layers the body belongs to, as a bitmask.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_get_collision_mask}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**body_get_collision_mask**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_body_get_collision_mask>`{.interpreted-text
role="ref"}

Returns the physics layer or layers the body can collide with, as a
bitmask.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_get_collision_priority}
::: {.rst-class}
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**body_get_collision_priority**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_body_get_collision_priority>`{.interpreted-text
role="ref"}

Returns the body\'s collision priority. This is used in the
depenetration phase of
`body_test_motion<class_PhysicsServer2D_method_body_test_motion>`{.interpreted-text
role="ref"}. The higher the priority is, the lower the penetration into
the body will be.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_get_constant_force}
::: {.rst-class}
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**body_get_constant_force**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_body_get_constant_force>`{.interpreted-text
role="ref"}

Returns the body\'s total constant positional force applied during each
physics update.

See
`body_add_constant_force<class_PhysicsServer2D_method_body_add_constant_force>`{.interpreted-text
role="ref"} and
`body_add_constant_central_force<class_PhysicsServer2D_method_body_add_constant_central_force>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_get_constant_torque}
::: {.rst-class}
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**body_get_constant_torque**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_body_get_constant_torque>`{.interpreted-text
role="ref"}

Returns the body\'s total constant rotational force applied during each
physics update.

See
`body_add_constant_torque<class_PhysicsServer2D_method_body_add_constant_torque>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_get_continuous_collision_detection_mode}
::: {.rst-class}
classref-method
:::
::::

`CCDMode<enum_PhysicsServer2D_CCDMode>`{.interpreted-text role="ref"}
**body_get_continuous_collision_detection_mode**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_body_get_continuous_collision_detection_mode>`{.interpreted-text
role="ref"}

Returns the body\'s continuous collision detection mode (see
`CCDMode<enum_PhysicsServer2D_CCDMode>`{.interpreted-text role="ref"}).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_get_direct_state}
::: {.rst-class}
classref-method
:::
::::

`PhysicsDirectBodyState2D<class_PhysicsDirectBodyState2D>`{.interpreted-text
role="ref"} **body_get_direct_state**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_body_get_direct_state>`{.interpreted-text
role="ref"}

Returns the
`PhysicsDirectBodyState2D<class_PhysicsDirectBodyState2D>`{.interpreted-text
role="ref"} of the body. Returns `null` if the body is destroyed or not
assigned to a space.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_get_max_contacts_reported}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**body_get_max_contacts_reported**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_body_get_max_contacts_reported>`{.interpreted-text
role="ref"}

Returns the maximum number of contacts that the body can report. See
`body_set_max_contacts_reported<class_PhysicsServer2D_method_body_set_max_contacts_reported>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_get_mode}
::: {.rst-class}
classref-method
:::
::::

`BodyMode<enum_PhysicsServer2D_BodyMode>`{.interpreted-text role="ref"}
**body_get_mode**(body: `RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_body_get_mode>`{.interpreted-text
role="ref"}

Returns the body\'s mode (see
`BodyMode<enum_PhysicsServer2D_BodyMode>`{.interpreted-text
role="ref"}).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_get_object_instance_id}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**body_get_object_instance_id**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_body_get_object_instance_id>`{.interpreted-text
role="ref"}

Returns the `ObjectID` attached to the body. Use
`@GlobalScope.instance_from_id<class_@GlobalScope_method_instance_from_id>`{.interpreted-text
role="ref"} to retrieve an `Object<class_Object>`{.interpreted-text
role="ref"} from a nonzero `ObjectID`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_get_param}
::: {.rst-class}
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**body_get_param**(body: `RID<class_RID>`{.interpreted-text role="ref"},
param:
`BodyParameter<enum_PhysicsServer2D_BodyParameter>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_body_get_param>`{.interpreted-text
role="ref"}

Returns the value of the given body parameter. See
`BodyParameter<enum_PhysicsServer2D_BodyParameter>`{.interpreted-text
role="ref"} for the list of available parameters.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_get_shape}
::: {.rst-class}
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **body_get_shape**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, shape_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_body_get_shape>`{.interpreted-text
role="ref"}

Returns the `RID<class_RID>`{.interpreted-text role="ref"} of the shape
with the given index in the body\'s array of shapes.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_get_shape_count}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**body_get_shape_count**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_body_get_shape_count>`{.interpreted-text
role="ref"}

Returns the number of shapes added to the body.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_get_shape_transform}
::: {.rst-class}
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**body_get_shape_transform**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_body_get_shape_transform>`{.interpreted-text
role="ref"}

Returns the local transform matrix of the shape with the given index in
the area\'s array of shapes.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_get_space}
::: {.rst-class}
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **body_get_space**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_body_get_space>`{.interpreted-text
role="ref"}

Returns the `RID<class_RID>`{.interpreted-text role="ref"} of the space
assigned to the body. Returns an empty
`RID<class_RID>`{.interpreted-text role="ref"} if no space is assigned.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_get_state}
::: {.rst-class}
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**body_get_state**(body: `RID<class_RID>`{.interpreted-text role="ref"},
state: `BodyState<enum_PhysicsServer2D_BodyState>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_body_get_state>`{.interpreted-text
role="ref"}

Returns the value of the given state of the body. See
`BodyState<enum_PhysicsServer2D_BodyState>`{.interpreted-text
role="ref"} for the list of available states.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_is_omitting_force_integration}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**body_is_omitting_force_integration**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_body_is_omitting_force_integration>`{.interpreted-text
role="ref"}

Returns `true` if the body is omitting the standard force integration.
See
`body_set_omit_force_integration<class_PhysicsServer2D_method_body_set_omit_force_integration>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_remove_collision_exception}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_remove_collision_exception**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, excepted_body:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_body_remove_collision_exception>`{.interpreted-text
role="ref"}

Removes `excepted_body` from the body\'s list of collision exceptions,
so that collisions with it are no longer ignored.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_remove_shape}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_remove_shape**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_body_remove_shape>`{.interpreted-text
role="ref"}

Removes the shape with the given index from the body\'s array of shapes.
The shape itself is not deleted, so it can continue to be used elsewhere
or added back later. As a result of this operation, the body\'s shapes
which used to have indices higher than `shape_idx` will have their index
decreased by one.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_reset_mass_properties}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_reset_mass_properties**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer2D_method_body_reset_mass_properties>`{.interpreted-text
role="ref"}

Restores the default inertia and center of mass of the body based on its
shapes. This undoes any custom values previously set using
`body_set_param<class_PhysicsServer2D_method_body_set_param>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_set_axis_velocity}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_axis_velocity**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, axis_velocity: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer2D_method_body_set_axis_velocity>`{.interpreted-text
role="ref"}

Modifies the body\'s linear velocity so that its projection to the axis
`axis_velocity.normalized()` is exactly `axis_velocity.length()`. This
is useful for jumping behavior.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_set_collision_layer}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_collision_layer**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, layer: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_body_set_collision_layer>`{.interpreted-text
role="ref"}

Sets the physics layer or layers the body belongs to, via a bitmask.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_set_collision_mask}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_collision_mask**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, mask: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_body_set_collision_mask>`{.interpreted-text
role="ref"}

Sets the physics layer or layers the body can collide with, via a
bitmask.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_set_collision_priority}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_collision_priority**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, priority: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer2D_method_body_set_collision_priority>`{.interpreted-text
role="ref"}

Sets the body\'s collision priority. This is used in the depenetration
phase of
`body_test_motion<class_PhysicsServer2D_method_body_test_motion>`{.interpreted-text
role="ref"}. The higher the priority is, the lower the penetration into
the body will be.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_set_constant_force}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_constant_force**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, force: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer2D_method_body_set_constant_force>`{.interpreted-text
role="ref"}

Sets the body\'s total constant positional force applied during each
physics update.

See
`body_add_constant_force<class_PhysicsServer2D_method_body_add_constant_force>`{.interpreted-text
role="ref"} and
`body_add_constant_central_force<class_PhysicsServer2D_method_body_add_constant_central_force>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_set_constant_torque}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_constant_torque**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, torque: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_body_set_constant_torque>`{.interpreted-text
role="ref"}

Sets the body\'s total constant rotational force applied during each
physics update.

See
`body_add_constant_torque<class_PhysicsServer2D_method_body_add_constant_torque>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_set_continuous_collision_detection_mode}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_continuous_collision_detection_mode**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, mode:
`CCDMode<enum_PhysicsServer2D_CCDMode>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_body_set_continuous_collision_detection_mode>`{.interpreted-text
role="ref"}

Sets the continuous collision detection mode using one of the
`CCDMode<enum_PhysicsServer2D_CCDMode>`{.interpreted-text role="ref"}
constants.

Continuous collision detection tries to predict where a moving body
would collide in between physics updates, instead of moving it and
correcting its movement if it collided.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_set_force_integration_callback}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_force_integration_callback**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, callable:
`Callable<class_Callable>`{.interpreted-text role="ref"}, userdata:
`Variant<class_Variant>`{.interpreted-text role="ref"} = null)
`🔗<class_PhysicsServer2D_method_body_set_force_integration_callback>`{.interpreted-text
role="ref"}

Sets the body\'s custom force integration callback function to
`callable`. Use an empty `Callable<class_Callable>`{.interpreted-text
role="ref"} (`Callable()`) to clear the custom callback.

The function `callable` will be called every physics tick, before the
standard force integration (see
`body_set_omit_force_integration<class_PhysicsServer2D_method_body_set_omit_force_integration>`{.interpreted-text
role="ref"}). It can be used for example to update the body\'s linear
and angular velocity based on contact with other bodies.

If `userdata` is not `null`, the function `callable` must take the
following two parameters:

1.  `state`: a
    `PhysicsDirectBodyState2D<class_PhysicsDirectBodyState2D>`{.interpreted-text
    role="ref"} used to retrieve and modify the body\'s state,
2.  `userdata`: a `Variant<class_Variant>`{.interpreted-text
    role="ref"}; its value will be the `userdata` passed into this
    method.

If `userdata` is `null`, then `callable` must take only the `state`
parameter.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_set_max_contacts_reported}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_max_contacts_reported**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, amount:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_body_set_max_contacts_reported>`{.interpreted-text
role="ref"}

Sets the maximum number of contacts that the body can report. If
`amount` is greater than zero, then the body will keep track of at most
this many contacts with other bodies.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_set_mode}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_mode**(body: `RID<class_RID>`{.interpreted-text role="ref"},
mode: `BodyMode<enum_PhysicsServer2D_BodyMode>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer2D_method_body_set_mode>`{.interpreted-text
role="ref"}

Sets the body\'s mode. See
`BodyMode<enum_PhysicsServer2D_BodyMode>`{.interpreted-text role="ref"}
for the list of available modes.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_set_omit_force_integration}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_omit_force_integration**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_body_set_omit_force_integration>`{.interpreted-text
role="ref"}

Sets whether the body omits the standard force integration. If `enable`
is `true`, the body will not automatically use applied forces, torques,
and damping to update the body\'s linear and angular velocity. In this
case,
`body_set_force_integration_callback<class_PhysicsServer2D_method_body_set_force_integration_callback>`{.interpreted-text
role="ref"} can be used to manually update the linear and angular
velocity instead.

This method is called when the property
`RigidBody2D.custom_integrator<class_RigidBody2D_property_custom_integrator>`{.interpreted-text
role="ref"} is set.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_set_param}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_param**(body: `RID<class_RID>`{.interpreted-text role="ref"},
param:
`BodyParameter<enum_PhysicsServer2D_BodyParameter>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer2D_method_body_set_param>`{.interpreted-text
role="ref"}

Sets the value of the given body parameter. See
`BodyParameter<enum_PhysicsServer2D_BodyParameter>`{.interpreted-text
role="ref"} for the list of available parameters.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_set_shape}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_shape**(body: `RID<class_RID>`{.interpreted-text role="ref"},
shape_idx: `int<class_int>`{.interpreted-text role="ref"}, shape:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_body_set_shape>`{.interpreted-text
role="ref"}

Replaces the body\'s shape at the given index by another shape, while
not affecting the `transform`, `disabled`, and one-way collision
properties at the same index.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_set_shape_as_one_way_collision}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_shape_as_one_way_collision**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, shape_idx:
`int<class_int>`{.interpreted-text role="ref"}, enable:
`bool<class_bool>`{.interpreted-text role="ref"}, margin:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_body_set_shape_as_one_way_collision>`{.interpreted-text
role="ref"}

Sets the one-way collision properties of the body\'s shape with the
given index. If `enable` is `true`, the one-way collision direction
given by the shape\'s local upward axis
`body_get_shape_transform(body, shape_idx).y` will be used to ignore
collisions with the shape in the opposite direction, and to ensure
depenetration of kinematic bodies happens in this direction.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_set_shape_disabled}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_shape_disabled**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"},
disabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_body_set_shape_disabled>`{.interpreted-text
role="ref"}

Sets the disabled property of the body\'s shape with the given index. If
`disabled` is `true`, then the shape will be ignored in all collision
detection.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_set_shape_transform}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_shape_transform**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"},
transform: `Transform2D<class_Transform2D>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer2D_method_body_set_shape_transform>`{.interpreted-text
role="ref"}

Sets the local transform matrix of the body\'s shape with the given
index.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_set_space}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_space**(body: `RID<class_RID>`{.interpreted-text role="ref"},
space: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_body_set_space>`{.interpreted-text
role="ref"}

Adds the body to the given space, after removing the body from the
previously assigned space (if any). If the body\'s mode is set to
`BODY_MODE_RIGID<class_PhysicsServer2D_constant_BODY_MODE_RIGID>`{.interpreted-text
role="ref"}, then adding the body to a space will have the following
additional effects:

- If the parameter
  `BODY_PARAM_CENTER_OF_MASS<class_PhysicsServer2D_constant_BODY_PARAM_CENTER_OF_MASS>`{.interpreted-text
  role="ref"} has never been set explicitly, then the value of that
  parameter will be recalculated based on the body\'s shapes.
- If the parameter
  `BODY_PARAM_INERTIA<class_PhysicsServer2D_constant_BODY_PARAM_INERTIA>`{.interpreted-text
  role="ref"} is set to a value `<= 0.0`, then the value of that
  parameter will be recalculated based on the body\'s shapes, mass, and
  center of mass.

\*\*Note:\*\* To remove a body from a space without immediately adding
it back elsewhere, use `PhysicsServer2D.body_set_space(body, RID())`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_set_state}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_state**(body: `RID<class_RID>`{.interpreted-text role="ref"},
state: `BodyState<enum_PhysicsServer2D_BodyState>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer2D_method_body_set_state>`{.interpreted-text
role="ref"}

Sets the value of a body\'s state. See
`BodyState<enum_PhysicsServer2D_BodyState>`{.interpreted-text
role="ref"} for the list of available states.

\*\*Note:\*\* The state change doesn\'t take effect immediately. The
state will change on the next physics frame.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_set_state_sync_callback}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_state_sync_callback**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, callable:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_body_set_state_sync_callback>`{.interpreted-text
role="ref"}

Sets the body\'s state synchronization callback function to `callable`.
Use an empty `Callable<class_Callable>`{.interpreted-text role="ref"}
(`Callable()`) to clear the callback.

The function `callable` will be called every physics frame, assuming
that the body was active during the previous physics tick, and can be
used to fetch the latest state from the physics server.

The function `callable` must take the following parameters:

1.  `state`: a
    `PhysicsDirectBodyState2D<class_PhysicsDirectBodyState2D>`{.interpreted-text
    role="ref"}, used to retrieve the body\'s state.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_body_test_motion}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**body_test_motion**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, parameters:
`PhysicsTestMotionParameters2D<class_PhysicsTestMotionParameters2D>`{.interpreted-text
role="ref"}, result:
`PhysicsTestMotionResult2D<class_PhysicsTestMotionResult2D>`{.interpreted-text
role="ref"} = null)
`🔗<class_PhysicsServer2D_method_body_test_motion>`{.interpreted-text
role="ref"}

Returns `true` if a collision would result from moving the body along a
motion vector from a given point in space. See
`PhysicsTestMotionParameters2D<class_PhysicsTestMotionParameters2D>`{.interpreted-text
role="ref"} for the available motion parameters. Optionally a
`PhysicsTestMotionResult2D<class_PhysicsTestMotionResult2D>`{.interpreted-text
role="ref"} object can be passed, which will be used to store the
information about the resulting collision.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_capsule_shape_create}
::: {.rst-class}
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**capsule_shape_create**()
`🔗<class_PhysicsServer2D_method_capsule_shape_create>`{.interpreted-text
role="ref"}

Creates a 2D capsule shape in the physics server, and returns the
`RID<class_RID>`{.interpreted-text role="ref"} that identifies it. Use
`shape_set_data<class_PhysicsServer2D_method_shape_set_data>`{.interpreted-text
role="ref"} to set the capsule\'s height and radius.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_circle_shape_create}
::: {.rst-class}
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **circle_shape_create**()
`🔗<class_PhysicsServer2D_method_circle_shape_create>`{.interpreted-text
role="ref"}

Creates a 2D circle shape in the physics server, and returns the
`RID<class_RID>`{.interpreted-text role="ref"} that identifies it. Use
`shape_set_data<class_PhysicsServer2D_method_shape_set_data>`{.interpreted-text
role="ref"} to set the circle\'s radius.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_concave_polygon_shape_create}
::: {.rst-class}
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**concave_polygon_shape_create**()
`🔗<class_PhysicsServer2D_method_concave_polygon_shape_create>`{.interpreted-text
role="ref"}

Creates a 2D concave polygon shape in the physics server, and returns
the `RID<class_RID>`{.interpreted-text role="ref"} that identifies it.
Use
`shape_set_data<class_PhysicsServer2D_method_shape_set_data>`{.interpreted-text
role="ref"} to set the concave polygon\'s segments.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_convex_polygon_shape_create}
::: {.rst-class}
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**convex_polygon_shape_create**()
`🔗<class_PhysicsServer2D_method_convex_polygon_shape_create>`{.interpreted-text
role="ref"}

Creates a 2D convex polygon shape in the physics server, and returns the
`RID<class_RID>`{.interpreted-text role="ref"} that identifies it. Use
`shape_set_data<class_PhysicsServer2D_method_shape_set_data>`{.interpreted-text
role="ref"} to set the convex polygon\'s points.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_damped_spring_joint_get_param}
::: {.rst-class}
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**damped_spring_joint_get_param**(joint:
`RID<class_RID>`{.interpreted-text role="ref"}, param:
`DampedSpringParam<enum_PhysicsServer2D_DampedSpringParam>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_damped_spring_joint_get_param>`{.interpreted-text
role="ref"}

Returns the value of the given damped spring joint parameter. See
`DampedSpringParam<enum_PhysicsServer2D_DampedSpringParam>`{.interpreted-text
role="ref"} for the list of available parameters.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_damped_spring_joint_set_param}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**damped_spring_joint_set_param**(joint:
`RID<class_RID>`{.interpreted-text role="ref"}, param:
`DampedSpringParam<enum_PhysicsServer2D_DampedSpringParam>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_damped_spring_joint_set_param>`{.interpreted-text
role="ref"}

Sets the value of the given damped spring joint parameter. See
`DampedSpringParam<enum_PhysicsServer2D_DampedSpringParam>`{.interpreted-text
role="ref"} for the list of available parameters.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_free_rid}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**free_rid**(rid: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_free_rid>`{.interpreted-text
role="ref"}

Destroys any of the objects created by PhysicsServer2D. If the
`RID<class_RID>`{.interpreted-text role="ref"} passed is not one of the
objects that can be created by PhysicsServer2D, an error will be printed
to the console.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_get_process_info}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_process_info**(process_info:
`ProcessInfo<enum_PhysicsServer2D_ProcessInfo>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer2D_method_get_process_info>`{.interpreted-text
role="ref"}

Returns information about the current state of the 2D physics engine.
See `ProcessInfo<enum_PhysicsServer2D_ProcessInfo>`{.interpreted-text
role="ref"} for the list of available states.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_joint_clear}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**joint_clear**(joint: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_joint_clear>`{.interpreted-text
role="ref"}

Destroys the joint with the given `RID<class_RID>`{.interpreted-text
role="ref"}, creates a new uninitialized joint, and makes the
`RID<class_RID>`{.interpreted-text role="ref"} refer to this new joint.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_joint_create}
::: {.rst-class}
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **joint_create**()
`🔗<class_PhysicsServer2D_method_joint_create>`{.interpreted-text
role="ref"}

Creates a 2D joint in the physics server, and returns the
`RID<class_RID>`{.interpreted-text role="ref"} that identifies it. To
set the joint type, use
`joint_make_damped_spring<class_PhysicsServer2D_method_joint_make_damped_spring>`{.interpreted-text
role="ref"},
`joint_make_groove<class_PhysicsServer2D_method_joint_make_groove>`{.interpreted-text
role="ref"} or
`joint_make_pin<class_PhysicsServer2D_method_joint_make_pin>`{.interpreted-text
role="ref"}. Use
`joint_set_param<class_PhysicsServer2D_method_joint_set_param>`{.interpreted-text
role="ref"} to set generic joint parameters.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_joint_disable_collisions_between_bodies}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**joint_disable_collisions_between_bodies**(joint:
`RID<class_RID>`{.interpreted-text role="ref"}, disable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_joint_disable_collisions_between_bodies>`{.interpreted-text
role="ref"}

Sets whether the bodies attached to the
`Joint2D<class_Joint2D>`{.interpreted-text role="ref"} will collide with
each other.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_joint_get_param}
::: {.rst-class}
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**joint_get_param**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`JointParam<enum_PhysicsServer2D_JointParam>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_joint_get_param>`{.interpreted-text
role="ref"}

Returns the value of the given joint parameter. See
`JointParam<enum_PhysicsServer2D_JointParam>`{.interpreted-text
role="ref"} for the list of available parameters.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_joint_get_type}
::: {.rst-class}
classref-method
:::
::::

`JointType<enum_PhysicsServer2D_JointType>`{.interpreted-text
role="ref"} **joint_get_type**(joint: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_joint_get_type>`{.interpreted-text
role="ref"}

Returns the joint\'s type (see
`JointType<enum_PhysicsServer2D_JointType>`{.interpreted-text
role="ref"}).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_joint_is_disabled_collisions_between_bodies}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**joint_is_disabled_collisions_between_bodies**(joint:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_joint_is_disabled_collisions_between_bodies>`{.interpreted-text
role="ref"}

Returns whether the bodies attached to the
`Joint2D<class_Joint2D>`{.interpreted-text role="ref"} will collide with
each other.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_joint_make_damped_spring}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**joint_make_damped_spring**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, anchor_a: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, anchor_b: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, body_a: `RID<class_RID>`{.interpreted-text role="ref"},
body_b: `RID<class_RID>`{.interpreted-text role="ref"} = RID())
`🔗<class_PhysicsServer2D_method_joint_make_damped_spring>`{.interpreted-text
role="ref"}

Makes the joint a damped spring joint, attached at the point `anchor_a`
(given in global coordinates) on the body `body_a` and at the point
`anchor_b` (given in global coordinates) on the body `body_b`. To set
the parameters which are specific to the damped spring, see
`damped_spring_joint_set_param<class_PhysicsServer2D_method_damped_spring_joint_set_param>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_joint_make_groove}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**joint_make_groove**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, groove1_a: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, groove2_a: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, anchor_b: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, body_a: `RID<class_RID>`{.interpreted-text role="ref"} =
RID(), body_b: `RID<class_RID>`{.interpreted-text role="ref"} = RID())
`🔗<class_PhysicsServer2D_method_joint_make_groove>`{.interpreted-text
role="ref"}

Makes the joint a groove joint.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_joint_make_pin}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**joint_make_pin**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, anchor: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, body_a: `RID<class_RID>`{.interpreted-text role="ref"},
body_b: `RID<class_RID>`{.interpreted-text role="ref"} = RID())
`🔗<class_PhysicsServer2D_method_joint_make_pin>`{.interpreted-text
role="ref"}

Makes the joint a pin joint. If `body_b` is an empty
`RID<class_RID>`{.interpreted-text role="ref"}, then `body_a` is pinned
to the point `anchor` (given in global coordinates); otherwise, `body_a`
is pinned to `body_b` at the point `anchor` (given in global
coordinates). To set the parameters which are specific to the pin joint,
see
`pin_joint_set_param<class_PhysicsServer2D_method_pin_joint_set_param>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_joint_set_param}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**joint_set_param**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`JointParam<enum_PhysicsServer2D_JointParam>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_joint_set_param>`{.interpreted-text
role="ref"}

Sets the value of the given joint parameter. See
`JointParam<enum_PhysicsServer2D_JointParam>`{.interpreted-text
role="ref"} for the list of available parameters.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_pin_joint_get_flag}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**pin_joint_get_flag**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, flag:
`PinJointFlag<enum_PhysicsServer2D_PinJointFlag>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_pin_joint_get_flag>`{.interpreted-text
role="ref"}

Gets a pin joint flag (see
`PinJointFlag<enum_PhysicsServer2D_PinJointFlag>`{.interpreted-text
role="ref"} constants).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_pin_joint_get_param}
::: {.rst-class}
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**pin_joint_get_param**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`PinJointParam<enum_PhysicsServer2D_PinJointParam>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_pin_joint_get_param>`{.interpreted-text
role="ref"}

Returns the value of a pin joint parameter. See
`PinJointParam<enum_PhysicsServer2D_PinJointParam>`{.interpreted-text
role="ref"} for a list of available parameters.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_pin_joint_set_flag}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**pin_joint_set_flag**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, flag:
`PinJointFlag<enum_PhysicsServer2D_PinJointFlag>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_pin_joint_set_flag>`{.interpreted-text
role="ref"}

Sets a pin joint flag (see
`PinJointFlag<enum_PhysicsServer2D_PinJointFlag>`{.interpreted-text
role="ref"} constants).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_pin_joint_set_param}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**pin_joint_set_param**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`PinJointParam<enum_PhysicsServer2D_PinJointParam>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_pin_joint_set_param>`{.interpreted-text
role="ref"}

Sets a pin joint parameter. See
`PinJointParam<enum_PhysicsServer2D_PinJointParam>`{.interpreted-text
role="ref"} for a list of available parameters.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_rectangle_shape_create}
::: {.rst-class}
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**rectangle_shape_create**()
`🔗<class_PhysicsServer2D_method_rectangle_shape_create>`{.interpreted-text
role="ref"}

Creates a 2D rectangle shape in the physics server, and returns the
`RID<class_RID>`{.interpreted-text role="ref"} that identifies it. Use
`shape_set_data<class_PhysicsServer2D_method_shape_set_data>`{.interpreted-text
role="ref"} to set the rectangle\'s half-extents.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_segment_shape_create}
::: {.rst-class}
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**segment_shape_create**()
`🔗<class_PhysicsServer2D_method_segment_shape_create>`{.interpreted-text
role="ref"}

Creates a 2D segment shape in the physics server, and returns the
`RID<class_RID>`{.interpreted-text role="ref"} that identifies it. Use
`shape_set_data<class_PhysicsServer2D_method_shape_set_data>`{.interpreted-text
role="ref"} to set the segment\'s start and end points.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_separation_ray_shape_create}
::: {.rst-class}
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**separation_ray_shape_create**()
`🔗<class_PhysicsServer2D_method_separation_ray_shape_create>`{.interpreted-text
role="ref"}

Creates a 2D separation ray shape in the physics server, and returns the
`RID<class_RID>`{.interpreted-text role="ref"} that identifies it. Use
`shape_set_data<class_PhysicsServer2D_method_shape_set_data>`{.interpreted-text
role="ref"} to set the shape\'s `length` and `slide_on_slope`
properties.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_set_active}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_active**(active: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_set_active>`{.interpreted-text
role="ref"}

Activates or deactivates the 2D physics server. If `active` is `false`,
then the physics server will not do anything in its physics step.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_shape_get_data}
::: {.rst-class}
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**shape_get_data**(shape: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_shape_get_data>`{.interpreted-text
role="ref"}

Returns the shape data that defines the configuration of the shape, such
as the half-extents of a rectangle or the segments of a concave shape.
See
`shape_set_data<class_PhysicsServer2D_method_shape_set_data>`{.interpreted-text
role="ref"} for the precise format of this data in each case.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_shape_get_type}
::: {.rst-class}
classref-method
:::
::::

`ShapeType<enum_PhysicsServer2D_ShapeType>`{.interpreted-text
role="ref"} **shape_get_type**(shape: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_shape_get_type>`{.interpreted-text
role="ref"}

Returns the shape\'s type (see
`ShapeType<enum_PhysicsServer2D_ShapeType>`{.interpreted-text
role="ref"}).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_shape_set_data}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**shape_set_data**(shape: `RID<class_RID>`{.interpreted-text
role="ref"}, data: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer2D_method_shape_set_data>`{.interpreted-text
role="ref"}

Sets the shape data that defines the configuration of the shape. The
`data` to be passed depends on the shape\'s type (see
`shape_get_type<class_PhysicsServer2D_method_shape_get_type>`{.interpreted-text
role="ref"}):

- `SHAPE_WORLD_BOUNDARY<class_PhysicsServer2D_constant_SHAPE_WORLD_BOUNDARY>`{.interpreted-text
  role="ref"}: an array of length two containing a
  `Vector2<class_Vector2>`{.interpreted-text role="ref"} `normal`
  direction and a `float<class_float>`{.interpreted-text role="ref"}
  distance `d`,
- `SHAPE_SEPARATION_RAY<class_PhysicsServer2D_constant_SHAPE_SEPARATION_RAY>`{.interpreted-text
  role="ref"}: a dictionary containing the key `length` with a
  `float<class_float>`{.interpreted-text role="ref"} value and the key
  `slide_on_slope` with a `bool<class_bool>`{.interpreted-text
  role="ref"} value,
- `SHAPE_SEGMENT<class_PhysicsServer2D_constant_SHAPE_SEGMENT>`{.interpreted-text
  role="ref"}: a `Rect2<class_Rect2>`{.interpreted-text role="ref"}
  `rect` containing the first point of the segment in `rect.position`
  and the second point of the segment in `rect.size`,
- `SHAPE_CIRCLE<class_PhysicsServer2D_constant_SHAPE_CIRCLE>`{.interpreted-text
  role="ref"}: a `float<class_float>`{.interpreted-text role="ref"}
  `radius`,
- `SHAPE_RECTANGLE<class_PhysicsServer2D_constant_SHAPE_RECTANGLE>`{.interpreted-text
  role="ref"}: a `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  `half_extents`,
- `SHAPE_CAPSULE<class_PhysicsServer2D_constant_SHAPE_CAPSULE>`{.interpreted-text
  role="ref"}: an array of length two (or a
  `Vector2<class_Vector2>`{.interpreted-text role="ref"}) containing a
  `float<class_float>`{.interpreted-text role="ref"} `height` and a
  `float<class_float>`{.interpreted-text role="ref"} `radius`,
- `SHAPE_CONVEX_POLYGON<class_PhysicsServer2D_constant_SHAPE_CONVEX_POLYGON>`{.interpreted-text
  role="ref"}: either a
  `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"} of points defining a convex polygon in counterclockwise
  order (the clockwise outward normal of each segment formed by
  consecutive points is calculated internally), or a
  `PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
  role="ref"} of length divisible by four so that every 4-tuple of
  `float<class_float>`{.interpreted-text role="ref"}s contains the
  coordinates of a point followed by the coordinates of the clockwise
  outward normal vector to the segment between the current point and the
  next point,
- `SHAPE_CONCAVE_POLYGON<class_PhysicsServer2D_constant_SHAPE_CONCAVE_POLYGON>`{.interpreted-text
  role="ref"}: a
  `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"} of length divisible by two (each pair of points forms one
  segment).

\*\*Warning:\*\* In the case of
`SHAPE_CONVEX_POLYGON<class_PhysicsServer2D_constant_SHAPE_CONVEX_POLYGON>`{.interpreted-text
role="ref"}, this method does not check if the points supplied actually
form a convex polygon (unlike the
`CollisionPolygon2D.polygon<class_CollisionPolygon2D_property_polygon>`{.interpreted-text
role="ref"} property).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_space_create}
::: {.rst-class}
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **space_create**()
`🔗<class_PhysicsServer2D_method_space_create>`{.interpreted-text
role="ref"}

Creates a 2D space in the physics server, and returns the
`RID<class_RID>`{.interpreted-text role="ref"} that identifies it. A
space contains bodies and areas, and controls the stepping of the
physics simulation of the objects in it.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_space_get_direct_state}
::: {.rst-class}
classref-method
:::
::::

`PhysicsDirectSpaceState2D<class_PhysicsDirectSpaceState2D>`{.interpreted-text
role="ref"} **space_get_direct_state**(space:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_space_get_direct_state>`{.interpreted-text
role="ref"}

Returns the state of a space, a
`PhysicsDirectSpaceState2D<class_PhysicsDirectSpaceState2D>`{.interpreted-text
role="ref"}. This object can be used for collision/intersection queries.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_space_get_param}
::: {.rst-class}
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**space_get_param**(space: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`SpaceParameter<enum_PhysicsServer2D_SpaceParameter>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_space_get_param>`{.interpreted-text
role="ref"}

Returns the value of the given space parameter. See
`SpaceParameter<enum_PhysicsServer2D_SpaceParameter>`{.interpreted-text
role="ref"} for the list of available parameters.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_space_is_active}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**space_is_active**(space: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2D_method_space_is_active>`{.interpreted-text
role="ref"}

Returns `true` if the space is active.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_space_set_active}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**space_set_active**(space: `RID<class_RID>`{.interpreted-text
role="ref"}, active: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_space_set_active>`{.interpreted-text
role="ref"}

Activates or deactivates the space. If `active` is `false`, then the
physics server will not do anything with this space in its physics step.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_space_set_param}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**space_set_param**(space: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`SpaceParameter<enum_PhysicsServer2D_SpaceParameter>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer2D_method_space_set_param>`{.interpreted-text
role="ref"}

Sets the value of the given space parameter. See
`SpaceParameter<enum_PhysicsServer2D_SpaceParameter>`{.interpreted-text
role="ref"} for the list of available parameters.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2D_method_world_boundary_shape_create}
::: {.rst-class}
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**world_boundary_shape_create**()
`🔗<class_PhysicsServer2D_method_world_boundary_shape_create>`{.interpreted-text
role="ref"}

Creates a 2D world boundary shape in the physics server, and returns the
`RID<class_RID>`{.interpreted-text role="ref"} that identifies it. Use
`shape_set_data<class_PhysicsServer2D_method_shape_set_data>`{.interpreted-text
role="ref"} to set the shape\'s normal direction and distance
properties.
