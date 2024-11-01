github_url

:   hide

# Node3D {#class_Node3D}

**Inherits:** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`AudioListener3D<class_AudioListener3D>`{.interpreted-text role="ref"},
`AudioStreamPlayer3D<class_AudioStreamPlayer3D>`{.interpreted-text
role="ref"},
`BoneAttachment3D<class_BoneAttachment3D>`{.interpreted-text
role="ref"}, `Camera3D<class_Camera3D>`{.interpreted-text role="ref"},
`CollisionObject3D<class_CollisionObject3D>`{.interpreted-text
role="ref"},
`CollisionPolygon3D<class_CollisionPolygon3D>`{.interpreted-text
role="ref"},
`CollisionShape3D<class_CollisionShape3D>`{.interpreted-text
role="ref"}, `GridMap<class_GridMap>`{.interpreted-text role="ref"},
`ImporterMeshInstance3D<class_ImporterMeshInstance3D>`{.interpreted-text
role="ref"}, `Joint3D<class_Joint3D>`{.interpreted-text role="ref"},
`LightmapProbe<class_LightmapProbe>`{.interpreted-text role="ref"},
`Marker3D<class_Marker3D>`{.interpreted-text role="ref"},
`NavigationLink3D<class_NavigationLink3D>`{.interpreted-text
role="ref"},
`NavigationObstacle3D<class_NavigationObstacle3D>`{.interpreted-text
role="ref"},
`NavigationRegion3D<class_NavigationRegion3D>`{.interpreted-text
role="ref"},
`OpenXRCompositionLayer<class_OpenXRCompositionLayer>`{.interpreted-text
role="ref"}, `OpenXRHand<class_OpenXRHand>`{.interpreted-text
role="ref"}, `Path3D<class_Path3D>`{.interpreted-text role="ref"},
`PathFollow3D<class_PathFollow3D>`{.interpreted-text role="ref"},
`RayCast3D<class_RayCast3D>`{.interpreted-text role="ref"},
`RemoteTransform3D<class_RemoteTransform3D>`{.interpreted-text
role="ref"}, `ShapeCast3D<class_ShapeCast3D>`{.interpreted-text
role="ref"}, `Skeleton3D<class_Skeleton3D>`{.interpreted-text
role="ref"},
`SkeletonModifier3D<class_SkeletonModifier3D>`{.interpreted-text
role="ref"}, `SpringArm3D<class_SpringArm3D>`{.interpreted-text
role="ref"}, `VehicleWheel3D<class_VehicleWheel3D>`{.interpreted-text
role="ref"},
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text
role="ref"},
`XRFaceModifier3D<class_XRFaceModifier3D>`{.interpreted-text
role="ref"}, `XRNode3D<class_XRNode3D>`{.interpreted-text role="ref"},
`XROrigin3D<class_XROrigin3D>`{.interpreted-text role="ref"}

Most basic 3D game object, parent of all 3D-related nodes.

::: {.rst-class}
classref-introduction-group
:::

## Description

Most basic 3D game object, with a
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"} and
visibility settings. All other 3D game objects inherit from **Node3D**.
Use **Node3D** as a parent node to move, scale, rotate and show/hide
children in a 3D project.

Affine operations (rotate, scale, translate) happen in parent\'s local
coordinate system, unless the **Node3D** object is set as top-level.
Affine operations in this coordinate system correspond to direct affine
operations on the **Node3D**\'s transform. The word local below refers
to this coordinate system. The coordinate system that is attached to the
**Node3D** object itself is referred to as object-local coordinate
system.

\*\*Note:\*\* Unless otherwise specified, all methods that have angle
parameters must have angles specified as *radians*. To convert degrees
to radians, use
`@GlobalScope.deg_to_rad<class_@GlobalScope_method_deg_to_rad>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Be aware that \"Spatial\" nodes are now called \"Node3D\"
starting with Godot 4. Any Godot 3.x references to \"Spatial\" nodes
refer to \"Node3D\" in Godot 4.

::: {.rst-class}
classref-introduction-group
:::

## Tutorials

- `Introduction to 3D <../tutorials/3d/introduction_to_3d>`{.interpreted-text
  role="doc"}
- [All 3D
  Demos](https://github.com/godotengine/godot-demo-projects/tree/master/3d)

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

## Signals

:::: {#class_Node3D_signal_visibility_changed}
::: {.rst-class}
classref-signal
:::
::::

**visibility_changed**()
`🔗<class_Node3D_signal_visibility_changed>`{.interpreted-text
role="ref"}

Emitted when node visibility changes.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Enumerations

:::: {#enum_Node3D_RotationEditMode}
::: {.rst-class}
classref-enumeration
:::
::::

enum **RotationEditMode**:
`🔗<enum_Node3D_RotationEditMode>`{.interpreted-text role="ref"}

:::: {#class_Node3D_constant_ROTATION_EDIT_MODE_EULER}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`RotationEditMode<enum_Node3D_RotationEditMode>`{.interpreted-text
role="ref"} **ROTATION_EDIT_MODE_EULER** = `0`

The rotation is edited using `Vector3<class_Vector3>`{.interpreted-text
role="ref"} Euler angles.

:::: {#class_Node3D_constant_ROTATION_EDIT_MODE_QUATERNION}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`RotationEditMode<enum_Node3D_RotationEditMode>`{.interpreted-text
role="ref"} **ROTATION_EDIT_MODE_QUATERNION** = `1`

The rotation is edited using a
`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}.

:::: {#class_Node3D_constant_ROTATION_EDIT_MODE_BASIS}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`RotationEditMode<enum_Node3D_RotationEditMode>`{.interpreted-text
role="ref"} **ROTATION_EDIT_MODE_BASIS** = `2`

The rotation is edited using a `Basis<class_Basis>`{.interpreted-text
role="ref"}. In this mode,
`scale<class_Node3D_property_scale>`{.interpreted-text role="ref"}
can\'t be edited separately.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Constants

:::: {#class_Node3D_constant_NOTIFICATION_TRANSFORM_CHANGED}
::: {.rst-class}
classref-constant
:::
::::

**NOTIFICATION_TRANSFORM_CHANGED** = `2000`
`🔗<class_Node3D_constant_NOTIFICATION_TRANSFORM_CHANGED>`{.interpreted-text
role="ref"}

**Node3D** nodes receive this notification when their global transform
changes. This means that either the current or a parent node changed its
transform.

In order for
`NOTIFICATION_TRANSFORM_CHANGED<class_Node3D_constant_NOTIFICATION_TRANSFORM_CHANGED>`{.interpreted-text
role="ref"} to work, users first need to ask for it, with
`set_notify_transform<class_Node3D_method_set_notify_transform>`{.interpreted-text
role="ref"}. The notification is also sent if the node is in the editor
context and it has at least one valid gizmo.

:::: {#class_Node3D_constant_NOTIFICATION_ENTER_WORLD}
::: {.rst-class}
classref-constant
:::
::::

**NOTIFICATION_ENTER_WORLD** = `41`
`🔗<class_Node3D_constant_NOTIFICATION_ENTER_WORLD>`{.interpreted-text
role="ref"}

**Node3D** nodes receive this notification when they are registered to
new `World3D<class_World3D>`{.interpreted-text role="ref"} resource.

:::: {#class_Node3D_constant_NOTIFICATION_EXIT_WORLD}
::: {.rst-class}
classref-constant
:::
::::

**NOTIFICATION_EXIT_WORLD** = `42`
`🔗<class_Node3D_constant_NOTIFICATION_EXIT_WORLD>`{.interpreted-text
role="ref"}

**Node3D** nodes receive this notification when they are unregistered
from current `World3D<class_World3D>`{.interpreted-text role="ref"}
resource.

:::: {#class_Node3D_constant_NOTIFICATION_VISIBILITY_CHANGED}
::: {.rst-class}
classref-constant
:::
::::

**NOTIFICATION_VISIBILITY_CHANGED** = `43`
`🔗<class_Node3D_constant_NOTIFICATION_VISIBILITY_CHANGED>`{.interpreted-text
role="ref"}

**Node3D** nodes receive this notification when their visibility
changes.

:::: {#class_Node3D_constant_NOTIFICATION_LOCAL_TRANSFORM_CHANGED}
::: {.rst-class}
classref-constant
:::
::::

**NOTIFICATION_LOCAL_TRANSFORM_CHANGED** = `44`
`🔗<class_Node3D_constant_NOTIFICATION_LOCAL_TRANSFORM_CHANGED>`{.interpreted-text
role="ref"}

**Node3D** nodes receive this notification when their local transform
changes. This is not received when the transform of a parent node is
changed.

In order for
`NOTIFICATION_LOCAL_TRANSFORM_CHANGED<class_Node3D_constant_NOTIFICATION_LOCAL_TRANSFORM_CHANGED>`{.interpreted-text
role="ref"} to work, users first need to ask for it, with
`set_notify_local_transform<class_Node3D_method_set_notify_local_transform>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Node3D_property_basis}
::: {.rst-class}
classref-property
:::
::::

`Basis<class_Basis>`{.interpreted-text role="ref"} **basis**
`🔗<class_Node3D_property_basis>`{.interpreted-text role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_basis**(value: `Basis<class_Basis>`{.interpreted-text
  role="ref"})
- `Basis<class_Basis>`{.interpreted-text role="ref"} **get_basis**()

Basis of the
`transform<class_Node3D_property_transform>`{.interpreted-text
role="ref"} property. Represents the rotation, scale, and shear of this
node.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_global_basis}
::: {.rst-class}
classref-property
:::
::::

`Basis<class_Basis>`{.interpreted-text role="ref"} **global_basis**
`🔗<class_Node3D_property_global_basis>`{.interpreted-text role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_global_basis**(value: `Basis<class_Basis>`{.interpreted-text
  role="ref"})
- `Basis<class_Basis>`{.interpreted-text role="ref"}
  **get_global_basis**()

Global basis of this node. This is equivalent to
`global_transform.basis`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_global_position}
::: {.rst-class}
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**global_position**
`🔗<class_Node3D_property_global_position>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_global_position**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_global_position**()

Global position of this node. This is equivalent to
`global_transform.origin`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_global_rotation}
::: {.rst-class}
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**global_rotation**
`🔗<class_Node3D_property_global_rotation>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_global_rotation**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_global_rotation**()

Rotation part of the global transformation in radians, specified in
terms of YXZ-Euler angles in the format (X angle, Y angle, Z angle).

\*\*Note:\*\* In the mathematical sense, rotation is a matrix and not a
vector. The three Euler angles, which are the three independent
parameters of the Euler-angle parametrization of the rotation matrix,
are stored in a `Vector3<class_Vector3>`{.interpreted-text role="ref"}
data structure not because the rotation is a vector, but only because
`Vector3<class_Vector3>`{.interpreted-text role="ref"} exists as a
convenient data-structure to store 3 floating-point numbers. Therefore,
applying affine operations on the rotation \"vector\" is not meaningful.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_global_rotation_degrees}
::: {.rst-class}
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**global_rotation_degrees**
`🔗<class_Node3D_property_global_rotation_degrees>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_global_rotation_degrees**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_global_rotation_degrees**()

Helper property to access
`global_rotation<class_Node3D_property_global_rotation>`{.interpreted-text
role="ref"} in degrees instead of radians.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_global_transform}
::: {.rst-class}
classref-property
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**global_transform**
`🔗<class_Node3D_property_global_transform>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_global_transform**(value:
  `Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
- `Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
  **get_global_transform**()

World3D space (global)
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"} of this
node.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_position}
::: {.rst-class}
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **position** =
`Vector3(0, 0, 0)`
`🔗<class_Node3D_property_position>`{.interpreted-text role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_position**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_position**()

Local position or translation of this node relative to the parent. This
is equivalent to `transform.origin`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_quaternion}
::: {.rst-class}
classref-property
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
**quaternion** `🔗<class_Node3D_property_quaternion>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_quaternion**(value:
  `Quaternion<class_Quaternion>`{.interpreted-text role="ref"})
- `Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
  **get_quaternion**()

Access to the node rotation as a
`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}. This
property is ideal for tweening complex rotations.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_rotation}
::: {.rst-class}
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **rotation** =
`Vector3(0, 0, 0)`
`🔗<class_Node3D_property_rotation>`{.interpreted-text role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rotation**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_rotation**()

Rotation part of the local transformation in radians, specified in terms
of Euler angles. The angles construct a rotation in the order specified
by the
`rotation_order<class_Node3D_property_rotation_order>`{.interpreted-text
role="ref"} property.

\*\*Note:\*\* In the mathematical sense, rotation is a matrix and not a
vector. The three Euler angles, which are the three independent
parameters of the Euler-angle parametrization of the rotation matrix,
are stored in a `Vector3<class_Vector3>`{.interpreted-text role="ref"}
data structure not because the rotation is a vector, but only because
`Vector3<class_Vector3>`{.interpreted-text role="ref"} exists as a
convenient data-structure to store 3 floating-point numbers. Therefore,
applying affine operations on the rotation \"vector\" is not meaningful.

\*\*Note:\*\* This property is edited in the inspector in degrees. If
you want to use degrees in a script, use
`rotation_degrees<class_Node3D_property_rotation_degrees>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_rotation_degrees}
::: {.rst-class}
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**rotation_degrees**
`🔗<class_Node3D_property_rotation_degrees>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rotation_degrees**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_rotation_degrees**()

Helper property to access
`rotation<class_Node3D_property_rotation>`{.interpreted-text role="ref"}
in degrees instead of radians.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_rotation_edit_mode}
::: {.rst-class}
classref-property
:::
::::

`RotationEditMode<enum_Node3D_RotationEditMode>`{.interpreted-text
role="ref"} **rotation_edit_mode** = `0`
`🔗<class_Node3D_property_rotation_edit_mode>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rotation_edit_mode**(value:
  `RotationEditMode<enum_Node3D_RotationEditMode>`{.interpreted-text
  role="ref"})
- `RotationEditMode<enum_Node3D_RotationEditMode>`{.interpreted-text
  role="ref"} **get_rotation_edit_mode**()

Specify how rotation (and scale) will be presented in the editor.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_rotation_order}
::: {.rst-class}
classref-property
:::
::::

`EulerOrder<enum_@GlobalScope_EulerOrder>`{.interpreted-text role="ref"}
**rotation_order** = `2`
`🔗<class_Node3D_property_rotation_order>`{.interpreted-text role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rotation_order**(value:
  `EulerOrder<enum_@GlobalScope_EulerOrder>`{.interpreted-text
  role="ref"})
- `EulerOrder<enum_@GlobalScope_EulerOrder>`{.interpreted-text
  role="ref"} **get_rotation_order**()

Specify the axis rotation order of the
`rotation<class_Node3D_property_rotation>`{.interpreted-text role="ref"}
property. The final orientation is constructed by rotating the Euler
angles in the order specified by this property.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_scale}
::: {.rst-class}
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **scale** =
`Vector3(1, 1, 1)` `🔗<class_Node3D_property_scale>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_scale**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"} **get_scale**()

Scale part of the local transformation.

\*\*Note:\*\* Mixed negative scales in 3D are not decomposable from the
transformation matrix. Due to the way scale is represented with
transformation matrices in Godot, the scale values will either be all
positive or all negative.

\*\*Note:\*\* Not all nodes are visually scaled by the
`scale<class_Node3D_property_scale>`{.interpreted-text role="ref"}
property. For example, `Light3D<class_Light3D>`{.interpreted-text
role="ref"}s are not visually affected by
`scale<class_Node3D_property_scale>`{.interpreted-text role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_top_level}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **top_level** = `false`
`🔗<class_Node3D_property_top_level>`{.interpreted-text role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_as_top_level**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_set_as_top_level**()

If `true`, the node will not inherit its transformations from its
parent. Node transformations are only in global space.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_transform}
::: {.rst-class}
classref-property
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**transform** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`
`🔗<class_Node3D_property_transform>`{.interpreted-text role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_transform**(value:
  `Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
- `Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
  **get_transform**()

Local space `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"} of this node, with respect to the parent node.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_visibility_parent}
::: {.rst-class}
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**visibility_parent** = `NodePath("")`
`🔗<class_Node3D_property_visibility_parent>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_visibility_parent**(value:
  `NodePath<class_NodePath>`{.interpreted-text role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_visibility_parent**()

Defines the visibility range parent for this node and its subtree. The
visibility parent must be a GeometryInstance3D. Any visual instance will
only be visible if the visibility parent (and all of its visibility
ancestors) is hidden by being closer to the camera than its own
`GeometryInstance3D.visibility_range_begin<class_GeometryInstance3D_property_visibility_range_begin>`{.interpreted-text
role="ref"}. Nodes hidden via the
`visible<class_Node3D_property_visible>`{.interpreted-text role="ref"}
property are essentially removed from the visibility dependency tree, so
dependent instances will not take the hidden node or its ancestors into
account.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_property_visible}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **visible** = `true`
`🔗<class_Node3D_property_visible>`{.interpreted-text role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_visible**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_visible**()

If `true`, this node is drawn. The node is only visible if all of its
ancestors are visible as well (in other words,
`is_visible_in_tree<class_Node3D_method_is_visible_in_tree>`{.interpreted-text
role="ref"} must return `true`).

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Node3D_method_add_gizmo}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_gizmo**(gizmo: `Node3DGizmo<class_Node3DGizmo>`{.interpreted-text
role="ref"}) `🔗<class_Node3D_method_add_gizmo>`{.interpreted-text
role="ref"}

Attach an editor gizmo to this **Node3D**.

\*\*Note:\*\* The gizmo object would typically be an instance of
`EditorNode3DGizmo<class_EditorNode3DGizmo>`{.interpreted-text
role="ref"}, but the argument type is kept generic to avoid creating a
dependency on editor classes in **Node3D**.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_clear_gizmos}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_gizmos**()
`🔗<class_Node3D_method_clear_gizmos>`{.interpreted-text role="ref"}

Clear all gizmos attached to this **Node3D**.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_clear_subgizmo_selection}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_subgizmo_selection**()
`🔗<class_Node3D_method_clear_subgizmo_selection>`{.interpreted-text
role="ref"}

Clears subgizmo selection for this node in the editor. Useful when
subgizmo IDs become invalid after a property change.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_force_update_transform}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**force_update_transform**()
`🔗<class_Node3D_method_force_update_transform>`{.interpreted-text
role="ref"}

Forces the transform to update. Transform changes in physics are not
instant for performance reasons. Transforms are accumulated and then
set. Use this if you need an up-to-date transform when doing physics
operations.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_get_gizmos}
::: {.rst-class}
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Node3DGizmo<class_Node3DGizmo>`{.interpreted-text
role="ref"}\] **get_gizmos**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node3D_method_get_gizmos>`{.interpreted-text
role="ref"}

Returns all the gizmos attached to this **Node3D**.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_get_global_transform_interpolated}
::: {.rst-class}
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**get_global_transform_interpolated**()
`🔗<class_Node3D_method_get_global_transform_interpolated>`{.interpreted-text
role="ref"}

When using physics interpolation, there will be circumstances in which
you want to know the interpolated (displayed) transform of a node rather
than the standard transform (which may only be accurate to the most
recent physics tick).

This is particularly important for frame-based operations that take
place in
`Node._process<class_Node_private_method__process>`{.interpreted-text
role="ref"}, rather than
`Node._physics_process<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"}. Examples include
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"}s focusing on a
node, or finding where to fire lasers from on a frame rather than
physics tick.

\*\*Note:\*\* This function creates an interpolation pump on the
**Node3D** the first time it is called, which can respond to physics
interpolation resets. If you get problems with \"streaking\" when
initially following a **Node3D**, be sure to call
`get_global_transform_interpolated<class_Node3D_method_get_global_transform_interpolated>`{.interpreted-text
role="ref"} at least once *before* resetting the **Node3D** physics
interpolation.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_get_parent_node_3d}
::: {.rst-class}
classref-method
:::
::::

`Node3D<class_Node3D>`{.interpreted-text role="ref"}
**get_parent_node_3d**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node3D_method_get_parent_node_3d>`{.interpreted-text
role="ref"}

Returns the parent **Node3D**, or `null` if no parent exists, the parent
is not of type **Node3D**, or
`top_level<class_Node3D_property_top_level>`{.interpreted-text
role="ref"} is `true`.

\*\*Note:\*\* Calling this method is not equivalent to
`get_parent() as Node3D`, which does not take
`top_level<class_Node3D_property_top_level>`{.interpreted-text
role="ref"} into account.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_get_world_3d}
::: {.rst-class}
classref-method
:::
::::

`World3D<class_World3D>`{.interpreted-text role="ref"}
**get_world_3d**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node3D_method_get_world_3d>`{.interpreted-text
role="ref"}

Returns the current `World3D<class_World3D>`{.interpreted-text
role="ref"} resource this **Node3D** node is registered to.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_global_rotate}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**global_rotate**(axis: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, angle: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Node3D_method_global_rotate>`{.interpreted-text role="ref"}

Rotates the global (world) transformation around axis, a unit
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, by specified
angle in radians. The rotation axis is in global coordinate system.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_global_scale}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**global_scale**(scale: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}) `🔗<class_Node3D_method_global_scale>`{.interpreted-text
role="ref"}

Scales the global (world) transformation by the given
`Vector3<class_Vector3>`{.interpreted-text role="ref"} scale factors.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_global_translate}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**global_translate**(offset: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_Node3D_method_global_translate>`{.interpreted-text role="ref"}

Moves the global (world) transformation by
`Vector3<class_Vector3>`{.interpreted-text role="ref"} offset. The
offset is in global coordinate system.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_hide}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **hide**()
`🔗<class_Node3D_method_hide>`{.interpreted-text role="ref"}

Disables rendering of this node. Changes
`visible<class_Node3D_property_visible>`{.interpreted-text role="ref"}
to `false`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_is_local_transform_notification_enabled}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_local_transform_notification_enabled**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node3D_method_is_local_transform_notification_enabled>`{.interpreted-text
role="ref"}

Returns whether node notifies about its local transformation changes.
**Node3D** will not propagate this by default.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_is_scale_disabled}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_scale_disabled**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node3D_method_is_scale_disabled>`{.interpreted-text
role="ref"}

Returns whether this node uses a scale of `(1, 1, 1)` or its local
transformation scale.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_is_transform_notification_enabled}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_transform_notification_enabled**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node3D_method_is_transform_notification_enabled>`{.interpreted-text
role="ref"}

Returns whether the node notifies about its global and local
transformation changes. **Node3D** will not propagate this by default.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_is_visible_in_tree}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_visible_in_tree**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node3D_method_is_visible_in_tree>`{.interpreted-text
role="ref"}

Returns `true` if the node is present in the
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"}, its
`visible<class_Node3D_property_visible>`{.interpreted-text role="ref"}
property is `true` and all its ancestors are also visible. If any
ancestor is hidden, this node will not be visible in the scene tree.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_look_at}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**look_at**(target: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, up: `Vector3<class_Vector3>`{.interpreted-text role="ref"}
= Vector3(0, 1, 0), use_model_front:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_Node3D_method_look_at>`{.interpreted-text role="ref"}

Rotates the node so that the local forward axis (-Z,
`Vector3.FORWARD<class_Vector3_constant_FORWARD>`{.interpreted-text
role="ref"}) points toward the `target` position.

The local up axis (+Y) points as close to the `up` vector as possible
while staying perpendicular to the local forward axis. The resulting
transform is orthogonal, and the scale is preserved. Non-uniform scaling
may not work correctly.

The `target` position cannot be the same as the node\'s position, the
`up` vector cannot be zero, and the direction from the node\'s position
to the `target` vector cannot be parallel to the `up` vector.

Operations take place in global space, which means that the node must be
in the scene tree.

If `use_model_front` is `true`, the +Z axis (asset front) is treated as
forward (implies +X is left) and points toward the `target` position. By
default, the -Z axis (camera forward) is treated as forward (implies +X
is right).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_look_at_from_position}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**look_at_from_position**(position:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, target:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, up:
`Vector3<class_Vector3>`{.interpreted-text role="ref"} = Vector3(0, 1,
0), use_model_front: `bool<class_bool>`{.interpreted-text role="ref"} =
false) `🔗<class_Node3D_method_look_at_from_position>`{.interpreted-text
role="ref"}

Moves the node to the specified `position`, and then rotates the node to
point toward the `target` as per
`look_at<class_Node3D_method_look_at>`{.interpreted-text role="ref"}.
Operations take place in global space.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_orthonormalize}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**orthonormalize**()
`🔗<class_Node3D_method_orthonormalize>`{.interpreted-text role="ref"}

Resets this node\'s transformations (like scale, skew and taper)
preserving its rotation and translation by performing Gram-Schmidt
orthonormalization on this node\'s
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_rotate}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**rotate**(axis: `Vector3<class_Vector3>`{.interpreted-text role="ref"},
angle: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Node3D_method_rotate>`{.interpreted-text role="ref"}

Rotates the local transformation around axis, a unit
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, by specified
angle in radians.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_rotate_object_local}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**rotate_object_local**(axis: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, angle: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Node3D_method_rotate_object_local>`{.interpreted-text
role="ref"}

Rotates the local transformation around axis, a unit
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, by specified
angle in radians. The rotation axis is in object-local coordinate
system.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_rotate_x}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**rotate_x**(angle: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Node3D_method_rotate_x>`{.interpreted-text role="ref"}

Rotates the local transformation around the X axis by angle in radians.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_rotate_y}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**rotate_y**(angle: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Node3D_method_rotate_y>`{.interpreted-text role="ref"}

Rotates the local transformation around the Y axis by angle in radians.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_rotate_z}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**rotate_z**(angle: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Node3D_method_rotate_z>`{.interpreted-text role="ref"}

Rotates the local transformation around the Z axis by angle in radians.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_scale_object_local}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**scale_object_local**(scale: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_Node3D_method_scale_object_local>`{.interpreted-text
role="ref"}

Scales the local transformation by given 3D scale factors in
object-local coordinate system.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_set_disable_scale}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_disable_scale**(disable: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_Node3D_method_set_disable_scale>`{.interpreted-text
role="ref"}

Sets whether the node uses a scale of `(1, 1, 1)` or its local
transformation scale. Changes to the local transformation scale are
preserved.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_set_identity}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_identity**()
`🔗<class_Node3D_method_set_identity>`{.interpreted-text role="ref"}

Reset all transformations for this node (sets its
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"} to the
identity matrix).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_set_ignore_transform_notification}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_ignore_transform_notification**(enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_Node3D_method_set_ignore_transform_notification>`{.interpreted-text
role="ref"}

Sets whether the node ignores notification that its transformation
(global or local) changed.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_set_notify_local_transform}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_notify_local_transform**(enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_Node3D_method_set_notify_local_transform>`{.interpreted-text
role="ref"}

Sets whether the node notifies about its local transformation changes.
**Node3D** will not propagate this by default.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_set_notify_transform}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_notify_transform**(enable: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_Node3D_method_set_notify_transform>`{.interpreted-text
role="ref"}

Sets whether the node notifies about its global and local transformation
changes. **Node3D** will not propagate this by default, unless it is in
the editor context and it has a valid gizmo.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_set_subgizmo_selection}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_subgizmo_selection**(gizmo:
`Node3DGizmo<class_Node3DGizmo>`{.interpreted-text role="ref"}, id:
`int<class_int>`{.interpreted-text role="ref"}, transform:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
`🔗<class_Node3D_method_set_subgizmo_selection>`{.interpreted-text
role="ref"}

Set subgizmo selection for this node in the editor.

\*\*Note:\*\* The gizmo object would typically be an instance of
`EditorNode3DGizmo<class_EditorNode3DGizmo>`{.interpreted-text
role="ref"}, but the argument type is kept generic to avoid creating a
dependency on editor classes in **Node3D**.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_show}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **show**()
`🔗<class_Node3D_method_show>`{.interpreted-text role="ref"}

Enables rendering of this node. Changes
`visible<class_Node3D_property_visible>`{.interpreted-text role="ref"}
to `true`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_to_global}
::: {.rst-class}
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**to_global**(local_point: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node3D_method_to_global>`{.interpreted-text
role="ref"}

Transforms `local_point` from this node\'s local space to world space.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_to_local}
::: {.rst-class}
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**to_local**(global_point: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node3D_method_to_local>`{.interpreted-text
role="ref"}

Transforms `global_point` from world space to this node\'s local space.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_translate}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**translate**(offset: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}) `🔗<class_Node3D_method_translate>`{.interpreted-text
role="ref"}

Changes the node\'s position by the given offset
`Vector3<class_Vector3>`{.interpreted-text role="ref"}.

Note that the translation `offset` is affected by the node\'s scale, so
if scaled by e.g. `(10, 1, 1)`, a translation by an offset of
`(2, 0, 0)` would actually add 20 (`2 * 10`) to the X coordinate.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_translate_object_local}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**translate_object_local**(offset:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_Node3D_method_translate_object_local>`{.interpreted-text
role="ref"}

Changes the node\'s position by the given offset
`Vector3<class_Vector3>`{.interpreted-text role="ref"} in local space.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node3D_method_update_gizmos}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**update_gizmos**()
`🔗<class_Node3D_method_update_gizmos>`{.interpreted-text role="ref"}

Updates all the **Node3D** gizmos attached to this node.
