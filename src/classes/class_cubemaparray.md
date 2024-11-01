github_url

:   hide

# CubemapArray {#class_CubemapArray}

**Inherits:**
`ImageTextureLayered<class_ImageTextureLayered>`{.interpreted-text
role="ref"} **\<**
`TextureLayered<class_TextureLayered>`{.interpreted-text role="ref"}
**\<** `Texture<class_Texture>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

An array of `Cubemap<class_Cubemap>`{.interpreted-text role="ref"}s,
stored together and with a single reference.

::: {.rst-class}
classref-introduction-group
:::

## Description

**CubemapArray**s are made of an array of
`Cubemap<class_Cubemap>`{.interpreted-text role="ref"}s. Like
`Cubemap<class_Cubemap>`{.interpreted-text role="ref"}s, they are made
of multiple textures, the amount of which must be divisible by 6 (one
for each face of the cube).

The primary benefit of **CubemapArray**s is that they can be accessed in
shader code using a single texture reference. In other words, you can
pass multiple `Cubemap<class_Cubemap>`{.interpreted-text role="ref"}s
into a shader using a single **CubemapArray**.
`Cubemap<class_Cubemap>`{.interpreted-text role="ref"}s are allocated in
adjacent cache regions on the GPU, which makes **CubemapArray**s the
most efficient way to store multiple
`Cubemap<class_Cubemap>`{.interpreted-text role="ref"}s.

\*\*Note:\*\* Godot uses **CubemapArray**s internally for many effects,
including the `Sky<class_Sky>`{.interpreted-text role="ref"} if you set
`ProjectSettings.rendering/reflections/sky_reflections/texture_array_reflections<class_ProjectSettings_property_rendering/reflections/sky_reflections/texture_array_reflections>`{.interpreted-text
role="ref"} to `true`. To create such a texture file yourself, reimport
your image files using the import presets of the File System dock.

\*\*Note:\*\* **CubemapArray** is not supported in the OpenGL 3
rendering backend.

::: {.rst-class}
classref-reftable-group
:::

## Methods

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

:::: {#class_CubemapArray_method_create_placeholder}
::: {.rst-class}
classref-method
:::
::::

`Resource<class_Resource>`{.interpreted-text role="ref"}
**create_placeholder**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CubemapArray_method_create_placeholder>`{.interpreted-text
role="ref"}

Creates a placeholder version of this resource
(`PlaceholderCubemapArray<class_PlaceholderCubemapArray>`{.interpreted-text
role="ref"}).
