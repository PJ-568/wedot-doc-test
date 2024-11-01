github_url

:   hide

# LightmapGIData {#class_LightmapGIData}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Contains baked lightmap and dynamic object probe data for
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"}.

::: {.rst-class}
classref-introduction-group
:::

## Description

**LightmapGIData** contains baked lightmap and dynamic object probe data
for `LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"}. It is
replaced every time lightmaps are baked in
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"}.

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

:::: {#class_LightmapGIData_property_light_texture}
::: {.rst-class}
classref-property
:::
::::

`TextureLayered<class_TextureLayered>`{.interpreted-text role="ref"}
**light_texture**
`🔗<class_LightmapGIData_property_light_texture>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_light_texture**(value:
  `TextureLayered<class_TextureLayered>`{.interpreted-text role="ref"})
- `TextureLayered<class_TextureLayered>`{.interpreted-text role="ref"}
  **get_light_texture**()

**Deprecated:** The lightmap atlas can now contain multiple textures.
See
`lightmap_textures<class_LightmapGIData_property_lightmap_textures>`{.interpreted-text
role="ref"}.

The lightmap atlas texture generated by the lightmapper.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LightmapGIData_property_lightmap_textures}
::: {.rst-class}
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`TextureLayered<class_TextureLayered>`{.interpreted-text
role="ref"}\] **lightmap_textures** = `[]`
`🔗<class_LightmapGIData_property_lightmap_textures>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_lightmap_textures**(value:
  `Array<class_Array>`{.interpreted-text
  role="ref"}\[`TextureLayered<class_TextureLayered>`{.interpreted-text
  role="ref"}\])
- `Array<class_Array>`{.interpreted-text
  role="ref"}\[`TextureLayered<class_TextureLayered>`{.interpreted-text
  role="ref"}\] **get_lightmap_textures**()

The lightmap atlas textures generated by the lightmapper.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_LightmapGIData_method_add_user}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_user**(path: `NodePath<class_NodePath>`{.interpreted-text
role="ref"}, uv_scale: `Rect2<class_Rect2>`{.interpreted-text
role="ref"}, slice_index: `int<class_int>`{.interpreted-text
role="ref"}, sub_instance: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_LightmapGIData_method_add_user>`{.interpreted-text role="ref"}

Adds an object that is considered baked within this **LightmapGIData**.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LightmapGIData_method_clear_users}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_users**()
`🔗<class_LightmapGIData_method_clear_users>`{.interpreted-text
role="ref"}

Clear all objects that are considered baked within this
**LightmapGIData**.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LightmapGIData_method_get_user_count}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_user_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_LightmapGIData_method_get_user_count>`{.interpreted-text
role="ref"}

Returns the number of objects that are considered baked within this
**LightmapGIData**.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LightmapGIData_method_get_user_path}
::: {.rst-class}
classref-method
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**get_user_path**(user_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_LightmapGIData_method_get_user_path>`{.interpreted-text
role="ref"}

Returns the `NodePath<class_NodePath>`{.interpreted-text role="ref"} of
the baked object at index `user_idx`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LightmapGIData_method_is_using_spherical_harmonics}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_using_spherical_harmonics**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_LightmapGIData_method_is_using_spherical_harmonics>`{.interpreted-text
role="ref"}

If `true`, lightmaps were baked with directional information. See also
`LightmapGI.directional<class_LightmapGI_property_directional>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LightmapGIData_method_set_uses_spherical_harmonics}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_uses_spherical_harmonics**(uses_spherical_harmonics:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_LightmapGIData_method_set_uses_spherical_harmonics>`{.interpreted-text
role="ref"}

If `uses_spherical_harmonics` is `true`, tells the engine to treat the
lightmap data as if it was baked with directional information.

\*\*Note:\*\* Changing this value on already baked lightmaps will not
cause them to be baked again. This means the material appearance will
look incorrect until lightmaps are baked again, in which case the value
set here is discarded as the entire **LightmapGIData** resource is
replaced by the lightmapper.
