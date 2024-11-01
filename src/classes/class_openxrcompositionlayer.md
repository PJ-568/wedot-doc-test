github_url

:   hide

# OpenXRCompositionLayer {#class_OpenXRCompositionLayer}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`OpenXRCompositionLayerCylinder<class_OpenXRCompositionLayerCylinder>`{.interpreted-text
role="ref"},
`OpenXRCompositionLayerEquirect<class_OpenXRCompositionLayerEquirect>`{.interpreted-text
role="ref"},
`OpenXRCompositionLayerQuad<class_OpenXRCompositionLayerQuad>`{.interpreted-text
role="ref"}

The parent class of all OpenXR composition layer nodes.

::: {.rst-class}
classref-introduction-group
:::

## Description

Composition layers allow 2D viewports to be displayed inside of the
headset by the XR compositor through special projections that retain
their quality. This allows for rendering clear text while keeping the
layer at a native resolution.

\*\*Note:\*\* If the OpenXR runtime doesn\'t support the given
composition layer type, a fallback mesh can be generated with a
`ViewportTexture<class_ViewportTexture>`{.interpreted-text role="ref"},
in order to emulate the composition layer.

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

::: {.rst-class}
classref-reftable-group
:::

## Methods

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

:::: {#class_OpenXRCompositionLayer_property_alpha_blend}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **alpha_blend** =
`false`
`🔗<class_OpenXRCompositionLayer_property_alpha_blend>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_alpha_blend**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_alpha_blend**()

Enables the blending the layer using its alpha channel.

Can be combined with
`Viewport.transparent_bg<class_Viewport_property_transparent_bg>`{.interpreted-text
role="ref"} to give the layer a transparent background.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRCompositionLayer_property_android_surface_size}
::: {.rst-class}
classref-property
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**android_surface_size** = `Vector2i(1024, 1024)`
`🔗<class_OpenXRCompositionLayer_property_android_surface_size>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_android_surface_size**(value:
  `Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
- `Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
  **get_android_surface_size**()

The size of the Android surface to create if
`use_android_surface<class_OpenXRCompositionLayer_property_use_android_surface>`{.interpreted-text
role="ref"} is enabled.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRCompositionLayer_property_enable_hole_punch}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **enable_hole_punch** =
`false`
`🔗<class_OpenXRCompositionLayer_property_enable_hole_punch>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enable_hole_punch**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_enable_hole_punch**()

Enables a technique called \"hole punching\", which allows putting the
composition layer behind the main projection layer (i.e. setting
`sort_order<class_OpenXRCompositionLayer_property_sort_order>`{.interpreted-text
role="ref"} to a negative value) while \"punching a hole\" through
everything rendered by Godot so that the layer is still visible.

This can be used to create the illusion that the composition layer
exists in the same 3D space as everything rendered by Godot, allowing
objects to appear to pass both behind or in front of the composition
layer.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRCompositionLayer_property_layer_viewport}
::: {.rst-class}
classref-property
:::
::::

`SubViewport<class_SubViewport>`{.interpreted-text role="ref"}
**layer_viewport**
`🔗<class_OpenXRCompositionLayer_property_layer_viewport>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_layer_viewport**(value:
  `SubViewport<class_SubViewport>`{.interpreted-text role="ref"})
- `SubViewport<class_SubViewport>`{.interpreted-text role="ref"}
  **get_layer_viewport**()

The `SubViewport<class_SubViewport>`{.interpreted-text role="ref"} to
render on the composition layer.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRCompositionLayer_property_sort_order}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **sort_order** = `1`
`🔗<class_OpenXRCompositionLayer_property_sort_order>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sort_order**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_sort_order**()

The sort order for this composition layer. Higher numbers will be shown
in front of lower numbers.

\*\*Note:\*\* This will have no effect if a fallback mesh is being used.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRCompositionLayer_property_use_android_surface}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **use_android_surface**
= `false`
`🔗<class_OpenXRCompositionLayer_property_use_android_surface>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_android_surface**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_use_android_surface**()

If enabled, an Android surface will be created (with the dimensions from
`android_surface_size<class_OpenXRCompositionLayer_property_android_surface_size>`{.interpreted-text
role="ref"}) which will provide the 2D content for the composition
layer, rather than using
`layer_viewport<class_OpenXRCompositionLayer_property_layer_viewport>`{.interpreted-text
role="ref"}.

See
`get_android_surface<class_OpenXRCompositionLayer_method_get_android_surface>`{.interpreted-text
role="ref"} for information about how to get the surface so that your
application can draw to it.

\*\*Note:\*\* This will only work in Android builds.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_OpenXRCompositionLayer_method_get_android_surface}
::: {.rst-class}
classref-method
:::
::::

`JavaObject<class_JavaObject>`{.interpreted-text role="ref"}
**get_android_surface**()
`🔗<class_OpenXRCompositionLayer_method_get_android_surface>`{.interpreted-text
role="ref"}

Returns a `JavaObject<class_JavaObject>`{.interpreted-text role="ref"}
representing an `android.view.Surface` if
`use_android_surface<class_OpenXRCompositionLayer_property_use_android_surface>`{.interpreted-text
role="ref"} is enabled and OpenXR has created the surface. Otherwise,
this will return `null`.

\*\*Note:\*\* The surface can only be created during an active OpenXR
session. So, if
`use_android_surface<class_OpenXRCompositionLayer_property_use_android_surface>`{.interpreted-text
role="ref"} is enabled outside of an OpenXR session, it won\'t be
created until a new session fully starts.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRCompositionLayer_method_intersects_ray}
::: {.rst-class}
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**intersects_ray**(origin: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, direction: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRCompositionLayer_method_intersects_ray>`{.interpreted-text
role="ref"}

Returns UV coordinates where the given ray intersects with the
composition layer. `origin` and `direction` must be in global space.

Returns `Vector2(-1.0, -1.0)` if the ray doesn\'t intersect.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRCompositionLayer_method_is_natively_supported}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_natively_supported**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRCompositionLayer_method_is_natively_supported>`{.interpreted-text
role="ref"}

Returns true if the OpenXR runtime natively supports this composition
layer type.

\*\*Note:\*\* This will only return an accurate result after the OpenXR
session has started.
