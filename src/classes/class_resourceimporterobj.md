github_url

:   hide

# ResourceImporterOBJ {#class_ResourceImporterOBJ}

**Inherits:**
`ResourceImporter<class_ResourceImporter>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Imports an OBJ 3D model as an independent
`Mesh<class_Mesh>`{.interpreted-text role="ref"} or scene.

::: {.rst-class}
classref-introduction-group
:::

## Description

Unlike
`ResourceImporterScene<class_ResourceImporterScene>`{.interpreted-text
role="ref"}, **ResourceImporterOBJ** will import a single
`Mesh<class_Mesh>`{.interpreted-text role="ref"} resource by default
instead of importing a
`PackedScene<class_PackedScene>`{.interpreted-text role="ref"}. This
makes it easier to use the `Mesh<class_Mesh>`{.interpreted-text
role="ref"} resource in nodes that expect direct
`Mesh<class_Mesh>`{.interpreted-text role="ref"} resources, such as
`GridMap<class_GridMap>`{.interpreted-text role="ref"},
`GPUParticles3D<class_GPUParticles3D>`{.interpreted-text role="ref"} or
`CPUParticles3D<class_CPUParticles3D>`{.interpreted-text role="ref"}.
Note that it is still possible to save mesh resources from 3D scenes
using the **Advanced Import Settings** dialog, regardless of the source
format.

See also
`ResourceImporterScene<class_ResourceImporterScene>`{.interpreted-text
role="ref"}, which is used for more advanced 3D formats such as glTF.

::: {.rst-class}
classref-introduction-group
:::

## Tutorials

- `Importing 3D scenes <../tutorials/assets_pipeline/importing_3d_scenes/index>`{.interpreted-text
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
||

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_ResourceImporterOBJ_property_force_disable_mesh_compression}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**force_disable_mesh_compression** = `false`
`🔗<class_ResourceImporterOBJ_property_force_disable_mesh_compression>`{.interpreted-text
role="ref"}

If `true`, mesh compression will not be used. Consider enabling if you
notice blocky artifacts in your mesh normals or UVs, or if you have
meshes that are larger than a few thousand meters in each direction.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterOBJ_property_generate_lightmap_uv2}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**generate_lightmap_uv2** = `false`
`🔗<class_ResourceImporterOBJ_property_generate_lightmap_uv2>`{.interpreted-text
role="ref"}

If `true`, generates UV2 on import for
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"} baking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterOBJ_property_generate_lightmap_uv2_texel_size}
::: {.rst-class}
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**generate_lightmap_uv2_texel_size** = `0.2`
`🔗<class_ResourceImporterOBJ_property_generate_lightmap_uv2_texel_size>`{.interpreted-text
role="ref"}

Controls the size of each texel on the baked lightmap. A smaller value
results in more precise lightmaps, at the cost of larger lightmap sizes
and longer bake times.

\*\*Note:\*\* Only effective if
`generate_lightmap_uv2<class_ResourceImporterOBJ_property_generate_lightmap_uv2>`{.interpreted-text
role="ref"} is `true`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterOBJ_property_generate_lods}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **generate_lods** =
`true`
`🔗<class_ResourceImporterOBJ_property_generate_lods>`{.interpreted-text
role="ref"}

If `true`, generates lower detail variants of the mesh which will be
displayed in the distance to improve rendering performance. Not all
meshes benefit from LOD, especially if they are never rendered from far
away. Disabling this can reduce output file size and speed up importing.
See [Mesh level of detail
(LOD)](../tutorials/3d/mesh_lod.html#doc-mesh-lod) for more information.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterOBJ_property_generate_shadow_mesh}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**generate_shadow_mesh** = `true`
`🔗<class_ResourceImporterOBJ_property_generate_shadow_mesh>`{.interpreted-text
role="ref"}

If `true`, enables the generation of shadow meshes on import. This
optimizes shadow rendering without reducing quality by welding vertices
together when possible. This in turn reduces the memory bandwidth
required to render shadows. Shadow mesh generation currently doesn\'t
support using a lower detail level than the source mesh (but shadow
rendering will make use of LODs when relevant).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterOBJ_property_generate_tangents}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **generate_tangents** =
`true`
`🔗<class_ResourceImporterOBJ_property_generate_tangents>`{.interpreted-text
role="ref"}

If `true`, generate vertex tangents using
[Mikktspace](http://www.mikktspace.com/) if the source mesh doesn\'t
have tangent data. When possible, it\'s recommended to let the 3D
modeling software generate tangents on export instead on relying on this
option. Tangents are required for correct display of normal and height
maps, along with any material/shader features that require tangents.

If you don\'t need material features that require tangents, disabling
this can reduce output file size and speed up importing if the source 3D
file doesn\'t contain tangents.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterOBJ_property_offset_mesh}
::: {.rst-class}
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **offset_mesh** =
`Vector3(0, 0, 0)`
`🔗<class_ResourceImporterOBJ_property_offset_mesh>`{.interpreted-text
role="ref"}

Offsets the mesh\'s data by the specified value. This can be used to
work around misaligned meshes without having to modify the source file.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterOBJ_property_scale_mesh}
::: {.rst-class}
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **scale_mesh** =
`Vector3(1, 1, 1)`
`🔗<class_ResourceImporterOBJ_property_scale_mesh>`{.interpreted-text
role="ref"}

Scales the mesh\'s data by the specified value. This can be used to work
around misscaled meshes without having to modify the source file.