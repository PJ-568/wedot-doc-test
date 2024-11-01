github_url

:   hide

# Cubemap {#class_Cubemap}

**Inherits:**
`ImageTextureLayered<class_ImageTextureLayered>`{.interpreted-text
role="ref"} **\<**
`TextureLayered<class_TextureLayered>`{.interpreted-text role="ref"}
**\<** `Texture<class_Texture>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Six square textures representing the faces of a cube. Commonly used as a
skybox.

::: {.rst-class}
classref-introduction-group
:::

## Description

A cubemap is made of 6 textures organized in layers. They are typically
used for faking reflections in 3D rendering (see
`ReflectionProbe<class_ReflectionProbe>`{.interpreted-text role="ref"}).
It can be used to make an object look as if it\'s reflecting its
surroundings. This usually delivers much better performance than other
reflection methods.

This resource is typically used as a uniform in custom shaders. Few core
Godot methods make use of **Cubemap** resources.

To create such a texture file yourself, reimport your image files using
the Godot Editor import presets.

\*\*Note:\*\* Godot doesn\'t support using cubemaps in a
`PanoramaSkyMaterial<class_PanoramaSkyMaterial>`{.interpreted-text
role="ref"}. You can use [this
tool](https://danilw.github.io/GLSL-howto/cubemap_to_panorama_js/cubemap_to_panorama.html)
to convert a cubemap to an equirectangular sky map.

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

:::: {#class_Cubemap_method_create_placeholder}
::: {.rst-class}
classref-method
:::
::::

`Resource<class_Resource>`{.interpreted-text role="ref"}
**create_placeholder**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Cubemap_method_create_placeholder>`{.interpreted-text
role="ref"}

Creates a placeholder version of this resource
(`PlaceholderCubemap<class_PlaceholderCubemap>`{.interpreted-text
role="ref"}).
