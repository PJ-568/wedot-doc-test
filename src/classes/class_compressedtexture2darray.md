github_url

:   hide

# CompressedTexture2DArray {#class_CompressedTexture2DArray}

**Inherits:**
`CompressedTextureLayered<class_CompressedTextureLayered>`{.interpreted-text
role="ref"} **\<**
`TextureLayered<class_TextureLayered>`{.interpreted-text role="ref"}
**\<** `Texture<class_Texture>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Array of 2-dimensional textures, optionally compressed.

::: {.rst-class}
classref-introduction-group
:::

## Description

A texture array that is loaded from a `.ctexarray` file. This file
format is internal to Godot; it is created by importing other image
formats with the import system. **CompressedTexture2DArray** can use one
of 4 compression methods:

- Lossless (WebP or PNG, uncompressed on the GPU)
- Lossy (WebP, uncompressed on the GPU)
- VRAM Compressed (compressed on the GPU)
- VRAM Uncompressed (uncompressed on the GPU)
- Basis Universal (compressed on the GPU. Lower file sizes than VRAM
  Compressed, but slower to compress and lower quality than VRAM
  Compressed)

Only **VRAM Compressed** actually reduces the memory usage on the GPU.
The **Lossless** and **Lossy** compression methods will reduce the
required storage on disk, but they will not reduce memory usage on the
GPU as the texture is sent to the GPU uncompressed.

Using **VRAM Compressed** also improves loading times, as
VRAM-compressed textures are faster to load compared to textures using
lossless or lossy compression. VRAM compression can exhibit noticeable
artifacts and is intended to be used for 3D rendering, not 2D.

See `Texture2DArray<class_Texture2DArray>`{.interpreted-text role="ref"}
for a general description of texture arrays.