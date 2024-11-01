github_url

:   hide

# Quaternion {#class_Quaternion}

A unit quaternion used for representing 3D rotations.

::: {.rst-class}
classref-introduction-group
:::

## Description

The **Quaternion** built-in `Variant<class_Variant>`{.interpreted-text
role="ref"} type is a 4D data structure that represents rotation in the
form of a [Hamilton convention
quaternion](https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation).
Compared to the `Basis<class_Basis>`{.interpreted-text role="ref"} type
which can store both rotation and scale, quaternions can *only* store
rotation.

A **Quaternion** is composed by 4 floating-point components:
`w<class_Quaternion_property_w>`{.interpreted-text role="ref"},
`x<class_Quaternion_property_x>`{.interpreted-text role="ref"},
`y<class_Quaternion_property_y>`{.interpreted-text role="ref"}, and
`z<class_Quaternion_property_z>`{.interpreted-text role="ref"}. These
components are very compact in memory, and because of this some
operations are more efficient and less likely to cause floating-point
errors. Methods such as
`get_angle<class_Quaternion_method_get_angle>`{.interpreted-text
role="ref"},
`get_axis<class_Quaternion_method_get_axis>`{.interpreted-text
role="ref"}, and
`slerp<class_Quaternion_method_slerp>`{.interpreted-text role="ref"} are
faster than their `Basis<class_Basis>`{.interpreted-text role="ref"}
counterparts.

For a great introduction to quaternions, see [this video by
3Blue1Brown](https://www.youtube.com/watch?v=d4EgbgTm0Bg). You do not
need to know the math behind quaternions, as Godot provides several
helper methods that handle it for you. These include
`slerp<class_Quaternion_method_slerp>`{.interpreted-text role="ref"} and
`spherical_cubic_interpolate<class_Quaternion_method_spherical_cubic_interpolate>`{.interpreted-text
role="ref"}, as well as the `*` operator.

\*\*Note:\*\* Quaternions must be normalized before being used for
rotation (see
`normalized<class_Quaternion_method_normalized>`{.interpreted-text
role="ref"}).

\*\*Note:\*\* Similarly to `Vector2<class_Vector2>`{.interpreted-text
role="ref"} and `Vector3<class_Vector3>`{.interpreted-text role="ref"},
the components of a quaternion use 32-bit precision by default, unlike
`float<class_float>`{.interpreted-text role="ref"} which is always
64-bit. If double precision is needed, compile the engine with the
option `precision=double`.

> [!NOTE]
> There are notable differences when using this API with C#. See
> `doc_c_sharp_differences`{.interpreted-text role="ref"} for more
> information.

::: {.rst-class}
classref-introduction-group
:::

## Tutorials

- [3Blue1Brown\'s video on
  Quaternions](https://www.youtube.com/watch?v=d4EgbgTm0Bg)
- [Online Quaternion Visualization](https://quaternions.online/)
- [Using 3D
  transforms](../tutorials/3d/using_transforms.html#interpolating-with-quaternions)
- [Third Person Shooter (TPS)
  Demo](https://godotengine.org/asset-library/asset/2710)
- [Advanced Quaternion
  Visualization](https://iwatake2222.github.io/rotation_master/rotation_master.html)

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

## Constructors

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

::: {.rst-class}
classref-reftable-group
:::

## Operators

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

## Constants

:::: {#class_Quaternion_constant_IDENTITY}
::: {.rst-class}
classref-constant
:::
::::

**IDENTITY** = `Quaternion(0, 0, 0, 1)`
`🔗<class_Quaternion_constant_IDENTITY>`{.interpreted-text role="ref"}

The identity quaternion, representing no rotation. This has the same
rotation as
`Basis.IDENTITY<class_Basis_constant_IDENTITY>`{.interpreted-text
role="ref"}.

If a `Vector3<class_Vector3>`{.interpreted-text role="ref"} is rotated
(multiplied) by this quaternion, it does not change.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Quaternion_property_w}
::: {.rst-class}
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **w** = `1.0`
`🔗<class_Quaternion_property_w>`{.interpreted-text role="ref"}

W component of the quaternion. This is the \"real\" part.

\*\*Note:\*\* Quaternion components should usually not be manipulated
directly.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_property_x}
::: {.rst-class}
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **x** = `0.0`
`🔗<class_Quaternion_property_x>`{.interpreted-text role="ref"}

X component of the quaternion. This is the value along the \"imaginary\"
`i` axis.

\*\*Note:\*\* Quaternion components should usually not be manipulated
directly.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_property_y}
::: {.rst-class}
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **y** = `0.0`
`🔗<class_Quaternion_property_y>`{.interpreted-text role="ref"}

Y component of the quaternion. This is the value along the \"imaginary\"
`j` axis.

\*\*Note:\*\* Quaternion components should usually not be manipulated
directly.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_property_z}
::: {.rst-class}
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **z** = `0.0`
`🔗<class_Quaternion_property_z>`{.interpreted-text role="ref"}

Z component of the quaternion. This is the value along the \"imaginary\"
`k` axis.

\*\*Note:\*\* Quaternion components should usually not be manipulated
directly.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Constructor Descriptions

:::: {#class_Quaternion_constructor_Quaternion}
::: {.rst-class}
classref-constructor
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
**Quaternion**()
`🔗<class_Quaternion_constructor_Quaternion>`{.interpreted-text
role="ref"}

Constructs a **Quaternion** identical to the
`IDENTITY<class_Quaternion_constant_IDENTITY>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-constructor
:::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
**Quaternion**(from: `Quaternion<class_Quaternion>`{.interpreted-text
role="ref"})

Constructs a **Quaternion** as a copy of the given **Quaternion**.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-constructor
:::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
**Quaternion**(arc_from: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, arc_to: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})

Constructs a **Quaternion** representing the shortest arc between
`arc_from` and `arc_to`. These can be imagined as two points
intersecting a sphere\'s surface, with a radius of `1.0`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-constructor
:::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
**Quaternion**(axis: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, angle: `float<class_float>`{.interpreted-text role="ref"})

Constructs a **Quaternion** representing rotation around the `axis` by
the given `angle`, in radians. The axis must be a normalized vector.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-constructor
:::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
**Quaternion**(from: `Basis<class_Basis>`{.interpreted-text role="ref"})

Constructs a **Quaternion** from the given rotation
`Basis<class_Basis>`{.interpreted-text role="ref"}.

This constructor is faster than
`Basis.get_rotation_quaternion<class_Basis_method_get_rotation_quaternion>`{.interpreted-text
role="ref"}, but the given basis must be *orthonormalized* (see
`Basis.orthonormalized<class_Basis_method_orthonormalized>`{.interpreted-text
role="ref"}). Otherwise, the constructor fails and returns
`IDENTITY<class_Quaternion_constant_IDENTITY>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-constructor
:::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
**Quaternion**(x: `float<class_float>`{.interpreted-text role="ref"}, y:
`float<class_float>`{.interpreted-text role="ref"}, z:
`float<class_float>`{.interpreted-text role="ref"}, w:
`float<class_float>`{.interpreted-text role="ref"})

Constructs a **Quaternion** defined by the given values.

\*\*Note:\*\* Only normalized quaternions represent rotation; if these
values are not normalized, the new **Quaternion** will not be a valid
rotation.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Quaternion_method_angle_to}
::: {.rst-class}
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **angle_to**(to:
`Quaternion<class_Quaternion>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Quaternion_method_angle_to>`{.interpreted-text
role="ref"}

Returns the angle between this quaternion and `to`. This is the
magnitude of the angle you would need to rotate by to get from one to
the other.

\*\*Note:\*\* The magnitude of the floating-point error for this method
is abnormally high, so methods such as `is_zero_approx` will not work
reliably.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_method_dot}
::: {.rst-class}
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **dot**(with:
`Quaternion<class_Quaternion>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Quaternion_method_dot>`{.interpreted-text
role="ref"}

Returns the dot product between this quaternion and `with`.

This is equivalent to
`(quat.x * with.x) + (quat.y * with.y) + (quat.z * with.z) + (quat.w * with.w)`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_method_exp}
::: {.rst-class}
classref-method
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"} **exp**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Quaternion_method_exp>`{.interpreted-text
role="ref"}

Returns the exponential of this quaternion. The rotation axis of the
result is the normalized rotation axis of this quaternion, the angle of
the result is the length of the vector part of this quaternion.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_method_from_euler}
::: {.rst-class}
classref-method
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
**from_euler**(euler: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_Quaternion_method_from_euler>`{.interpreted-text
role="ref"}

Constructs a new **Quaternion** from the given
`Vector3<class_Vector3>`{.interpreted-text role="ref"} of [Euler
angles](https://en.wikipedia.org/wiki/Euler_angles), in radians. This
method always uses the YXZ convention
(`@GlobalScope.EULER_ORDER_YXZ<class_@GlobalScope_constant_EULER_ORDER_YXZ>`{.interpreted-text
role="ref"}).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_method_get_angle}
::: {.rst-class}
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_angle**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Quaternion_method_get_angle>`{.interpreted-text
role="ref"}

Returns the angle of the rotation represented by this quaternion.

\*\*Note:\*\* The quaternion must be normalized.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_method_get_axis}
::: {.rst-class}
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **get_axis**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Quaternion_method_get_axis>`{.interpreted-text
role="ref"}

Returns the rotation axis of the rotation represented by this
quaternion.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_method_get_euler}
::: {.rst-class}
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_euler**(order: `int<class_int>`{.interpreted-text role="ref"} = 2)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Quaternion_method_get_euler>`{.interpreted-text
role="ref"}

Returns this quaternion\'s rotation as a
`Vector3<class_Vector3>`{.interpreted-text role="ref"} of [Euler
angles](https://en.wikipedia.org/wiki/Euler_angles), in radians.

The order of each consecutive rotation can be changed with `order` (see
`EulerOrder<enum_@GlobalScope_EulerOrder>`{.interpreted-text role="ref"}
constants). By default, the YXZ convention is used
(`@GlobalScope.EULER_ORDER_YXZ<class_@GlobalScope_constant_EULER_ORDER_YXZ>`{.interpreted-text
role="ref"}): Z (roll) is calculated first, then X (pitch), and lastly Y
(yaw). When using the opposite method
`from_euler<class_Quaternion_method_from_euler>`{.interpreted-text
role="ref"}, this order is reversed.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_method_inverse}
::: {.rst-class}
classref-method
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
**inverse**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Quaternion_method_inverse>`{.interpreted-text
role="ref"}

Returns the inverse version of this quaternion, inverting the sign of
every component except
`w<class_Quaternion_property_w>`{.interpreted-text role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_method_is_equal_approx}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_equal_approx**(to:
`Quaternion<class_Quaternion>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Quaternion_method_is_equal_approx>`{.interpreted-text
role="ref"}

Returns `true` if this quaternion and `to` are approximately equal, by
running
`@GlobalScope.is_equal_approx<class_@GlobalScope_method_is_equal_approx>`{.interpreted-text
role="ref"} on each component.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_method_is_finite}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_finite**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Quaternion_method_is_finite>`{.interpreted-text
role="ref"}

Returns `true` if this quaternion is finite, by calling
`@GlobalScope.is_finite<class_@GlobalScope_method_is_finite>`{.interpreted-text
role="ref"} on each component.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_method_is_normalized}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_normalized**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Quaternion_method_is_normalized>`{.interpreted-text
role="ref"}

Returns `true` if this quaternion is normalized. See also
`normalized<class_Quaternion_method_normalized>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_method_length}
::: {.rst-class}
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **length**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Quaternion_method_length>`{.interpreted-text
role="ref"}

Returns this quaternion\'s length, also called magnitude.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_method_length_squared}
::: {.rst-class}
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **length_squared**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Quaternion_method_length_squared>`{.interpreted-text
role="ref"}

Returns this quaternion\'s length, squared.

\*\*Note:\*\* This method is faster than
`length<class_Quaternion_method_length>`{.interpreted-text role="ref"},
so prefer it if you only need to compare quaternion lengths.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_method_log}
::: {.rst-class}
classref-method
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"} **log**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Quaternion_method_log>`{.interpreted-text
role="ref"}

Returns the logarithm of this quaternion. Multiplies this quaternion\'s
rotation axis by its rotation angle, and stores the result in the
returned quaternion\'s vector part
(`x<class_Quaternion_property_x>`{.interpreted-text role="ref"},
`y<class_Quaternion_property_y>`{.interpreted-text role="ref"}, and
`z<class_Quaternion_property_z>`{.interpreted-text role="ref"}). The
returned quaternion\'s real part
(`w<class_Quaternion_property_w>`{.interpreted-text role="ref"}) is
always `0.0`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_method_normalized}
::: {.rst-class}
classref-method
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
**normalized**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Quaternion_method_normalized>`{.interpreted-text
role="ref"}

Returns a copy of this quaternion, normalized so that its length is
`1.0`. See also
`is_normalized<class_Quaternion_method_is_normalized>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_method_slerp}
::: {.rst-class}
classref-method
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
**slerp**(to: `Quaternion<class_Quaternion>`{.interpreted-text
role="ref"}, weight: `float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Quaternion_method_slerp>`{.interpreted-text
role="ref"}

Performs a spherical-linear interpolation with the `to` quaternion,
given a `weight` and returns the result. Both this quaternion and `to`
must be normalized.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_method_slerpni}
::: {.rst-class}
classref-method
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
**slerpni**(to: `Quaternion<class_Quaternion>`{.interpreted-text
role="ref"}, weight: `float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Quaternion_method_slerpni>`{.interpreted-text
role="ref"}

Performs a spherical-linear interpolation with the `to` quaternion,
given a `weight` and returns the result. Unlike
`slerp<class_Quaternion_method_slerp>`{.interpreted-text role="ref"},
this method does not check if the rotation path is smaller than 90
degrees. Both this quaternion and `to` must be normalized.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_method_spherical_cubic_interpolate}
::: {.rst-class}
classref-method
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
**spherical_cubic_interpolate**(b:
`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}, pre_a:
`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}, post_b:
`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}, weight:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Quaternion_method_spherical_cubic_interpolate>`{.interpreted-text
role="ref"}

Performs a spherical cubic interpolation between quaternions `pre_a`,
this vector, `b`, and `post_b`, by the given amount `weight`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_method_spherical_cubic_interpolate_in_time}
::: {.rst-class}
classref-method
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
**spherical_cubic_interpolate_in_time**(b:
`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}, pre_a:
`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}, post_b:
`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}, weight:
`float<class_float>`{.interpreted-text role="ref"}, b_t:
`float<class_float>`{.interpreted-text role="ref"}, pre_a_t:
`float<class_float>`{.interpreted-text role="ref"}, post_b_t:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Quaternion_method_spherical_cubic_interpolate_in_time>`{.interpreted-text
role="ref"}

Performs a spherical cubic interpolation between quaternions `pre_a`,
this vector, `b`, and `post_b`, by the given amount `weight`.

It can perform smoother interpolation than
`spherical_cubic_interpolate<class_Quaternion_method_spherical_cubic_interpolate>`{.interpreted-text
role="ref"} by the time values.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Operator Descriptions

:::: {#class_Quaternion_operator_neq_Quaternion}
::: {.rst-class}
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`Quaternion<class_Quaternion>`{.interpreted-text role="ref"})
`🔗<class_Quaternion_operator_neq_Quaternion>`{.interpreted-text
role="ref"}

Returns `true` if the components of both quaternions are not exactly
equal.

\*\*Note:\*\* Due to floating-point precision errors, consider using
`is_equal_approx<class_Quaternion_method_is_equal_approx>`{.interpreted-text
role="ref"} instead, which is more reliable.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_operator_mul_Quaternion}
::: {.rst-class}
classref-operator
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
**operator**\*(right: `Quaternion<class_Quaternion>`{.interpreted-text
role="ref"})
`🔗<class_Quaternion_operator_mul_Quaternion>`{.interpreted-text
role="ref"}

Composes (multiplies) two quaternions. This rotates the `right`
quaternion (the child) by this quaternion (the parent).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_operator_mul_Vector3}
::: {.rst-class}
classref-operator
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**operator**\*(right: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_Quaternion_operator_mul_Vector3>`{.interpreted-text
role="ref"}

Rotates (multiplies) the `right` vector by this quaternion, returning a
`Vector3<class_Vector3>`{.interpreted-text role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_operator_mul_float}
::: {.rst-class}
classref-operator
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
**operator**\*(right: `float<class_float>`{.interpreted-text
role="ref"}) `🔗<class_Quaternion_operator_mul_float>`{.interpreted-text
role="ref"}

Multiplies each component of the **Quaternion** by the right
`float<class_float>`{.interpreted-text role="ref"} value.

This operation is not meaningful on its own, but it can be used as a
part of a larger expression.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_operator_mul_int}
::: {.rst-class}
classref-operator
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
**operator**\*(right: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Quaternion_operator_mul_int>`{.interpreted-text role="ref"}

Multiplies each component of the **Quaternion** by the right
`int<class_int>`{.interpreted-text role="ref"} value.

This operation is not meaningful on its own, but it can be used as a
part of a larger expression.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_operator_sum_Quaternion}
::: {.rst-class}
classref-operator
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"} **operator
+**(right: `Quaternion<class_Quaternion>`{.interpreted-text role="ref"})
`🔗<class_Quaternion_operator_sum_Quaternion>`{.interpreted-text
role="ref"}

Adds each component of the left **Quaternion** to the right
**Quaternion**.

This operation is not meaningful on its own, but it can be used as a
part of a larger expression, such as approximating an intermediate
rotation between two nearby rotations.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_operator_dif_Quaternion}
::: {.rst-class}
classref-operator
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"} **operator
-**(right: `Quaternion<class_Quaternion>`{.interpreted-text role="ref"})
`🔗<class_Quaternion_operator_dif_Quaternion>`{.interpreted-text
role="ref"}

Subtracts each component of the left **Quaternion** by the right
**Quaternion**.

This operation is not meaningful on its own, but it can be used as a
part of a larger expression.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_operator_div_float}
::: {.rst-class}
classref-operator
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"} **operator
/**(right: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Quaternion_operator_div_float>`{.interpreted-text role="ref"}

Divides each component of the **Quaternion** by the right
`float<class_float>`{.interpreted-text role="ref"} value.

This operation is not meaningful on its own, but it can be used as a
part of a larger expression.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_operator_div_int}
::: {.rst-class}
classref-operator
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"} **operator
/**(right: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Quaternion_operator_div_int>`{.interpreted-text role="ref"}

Divides each component of the **Quaternion** by the right
`int<class_int>`{.interpreted-text role="ref"} value.

This operation is not meaningful on its own, but it can be used as a
part of a larger expression.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_operator_eq_Quaternion}
::: {.rst-class}
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`Quaternion<class_Quaternion>`{.interpreted-text role="ref"})
`🔗<class_Quaternion_operator_eq_Quaternion>`{.interpreted-text
role="ref"}

Returns `true` if the components of both quaternions are exactly equal.

\*\*Note:\*\* Due to floating-point precision errors, consider using
`is_equal_approx<class_Quaternion_method_is_equal_approx>`{.interpreted-text
role="ref"} instead, which is more reliable.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_operator_idx_int}
::: {.rst-class}
classref-operator
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **operator
\[\]**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Quaternion_operator_idx_int>`{.interpreted-text role="ref"}

Accesses each component of this quaternion by their index.

Index `0` is the same as
`x<class_Quaternion_property_x>`{.interpreted-text role="ref"}, index
`1` is the same as `y<class_Quaternion_property_y>`{.interpreted-text
role="ref"}, index `2` is the same as
`z<class_Quaternion_property_z>`{.interpreted-text role="ref"}, and
index `3` is the same as
`w<class_Quaternion_property_w>`{.interpreted-text role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_operator_unplus}
::: {.rst-class}
classref-operator
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"} **operator
unary+**() `🔗<class_Quaternion_operator_unplus>`{.interpreted-text
role="ref"}

Returns the same value as if the `+` was not there. Unary `+` does
nothing, but sometimes it can make your code more readable.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Quaternion_operator_unminus}
::: {.rst-class}
classref-operator
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"} **operator
unary-**() `🔗<class_Quaternion_operator_unminus>`{.interpreted-text
role="ref"}

Returns the negative value of the **Quaternion**. This is the same as
multiplying all components by `-1`. This operation results in a
quaternion that represents the same rotation.
