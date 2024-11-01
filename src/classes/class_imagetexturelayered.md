github_url

:   hide

# ImageTextureLayered {#class_ImageTextureLayered}

**Inherits:** `TextureLayered<class_TextureLayered>`{.interpreted-text
role="ref"} **\<** `Texture<class_Texture>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `Cubemap<class_Cubemap>`{.interpreted-text
role="ref"}, `CubemapArray<class_CubemapArray>`{.interpreted-text
role="ref"}, `Texture2DArray<class_Texture2DArray>`{.interpreted-text
role="ref"}

Base class for texture types which contain the data of multiple
`ImageTexture<class_ImageTexture>`{.interpreted-text role="ref"}s. Each
image is of the same size and format.

::: {.rst-class}
classref-introduction-group
:::

## Description

Base class for `Texture2DArray<class_Texture2DArray>`{.interpreted-text
role="ref"}, `Cubemap<class_Cubemap>`{.interpreted-text role="ref"} and
`CubemapArray<class_CubemapArray>`{.interpreted-text role="ref"}. Cannot
be used directly, but contains all the functions necessary for accessing
the derived resource types. See also
`Texture3D<class_Texture3D>`{.interpreted-text role="ref"}.

::: {.rst-class}
classref-reftable-group
:::

## Methods

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

:::: {#class_ImageTextureLayered_method_create_from_images}
::: {.rst-class}
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**create_from_images**(images: `Array<class_Array>`{.interpreted-text
role="ref"}\[`Image<class_Image>`{.interpreted-text role="ref"}\])
`🔗<class_ImageTextureLayered_method_create_from_images>`{.interpreted-text
role="ref"}

Creates an **ImageTextureLayered** from an array of
`Image<class_Image>`{.interpreted-text role="ref"}s. See
`Image.create<class_Image_method_create>`{.interpreted-text role="ref"}
for the expected data format. The first image decides the width, height,
image format and mipmapping setting. The other images *must* have the
same width, height, image format and mipmapping setting.

Each `Image<class_Image>`{.interpreted-text role="ref"} represents one
`layer`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImageTextureLayered_method_update_layer}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**update_layer**(image: `Image<class_Image>`{.interpreted-text
role="ref"}, layer: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_ImageTextureLayered_method_update_layer>`{.interpreted-text
role="ref"}

Replaces the existing `Image<class_Image>`{.interpreted-text role="ref"}
data at the given `layer` with this new image.

The given `Image<class_Image>`{.interpreted-text role="ref"} must have
the same width, height, image format, and mipmapping flag as the rest of
the referenced images.

If the image format is unsupported, it will be decompressed and
converted to a similar and supported
`Format<enum_Image_Format>`{.interpreted-text role="ref"}.

The update is immediate: it\'s synchronized with drawing.
