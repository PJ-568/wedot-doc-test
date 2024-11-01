github_url

:   hide

# GLTFDocument {#class_GLTFDocument}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `FBXDocument<class_FBXDocument>`{.interpreted-text
role="ref"}

Class for importing and exporting glTF files in and out of Godot.

::: {.rst-class}
classref-introduction-group
:::

## Description

GLTFDocument supports reading data from a glTF file, buffer, or Godot
scene. This data can then be written to the filesystem, buffer, or used
to create a Godot scene.

All of the data in a glTF scene is stored in the
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"} class.
GLTFDocument processes state objects, but does not contain any scene
data itself. GLTFDocument has member variables to store export
configuration settings such as the image format, but is otherwise
stateless. Multiple scenes can be processed with the same settings using
the same GLTFDocument object and different
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"} objects.

GLTFDocument can be extended with arbitrary functionality by extending
the
`GLTFDocumentExtension<class_GLTFDocumentExtension>`{.interpreted-text
role="ref"} class and registering it with GLTFDocument via
`register_gltf_document_extension<class_GLTFDocument_method_register_gltf_document_extension>`{.interpreted-text
role="ref"}. This allows for custom data to be imported and exported.

::: {.rst-class}
classref-introduction-group
:::

## Tutorials

- `Runtime file loading and saving <../tutorials/io/runtime_file_loading_and_saving>`{.interpreted-text
  role="doc"}
- [glTF \'What the duck?\'
  guide](https://www.khronos.org/files/gltf20-reference-guide.pdf)
- [Khronos glTF specification](https://registry.khronos.org/glTF/)

::: {.rst-class}
classref-reftable-group
:::

## Properties

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

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Enumerations

:::: {#enum_GLTFDocument_RootNodeMode}
::: {.rst-class}
classref-enumeration
:::
::::

enum **RootNodeMode**:
`🔗<enum_GLTFDocument_RootNodeMode>`{.interpreted-text role="ref"}

:::: {#class_GLTFDocument_constant_ROOT_NODE_MODE_SINGLE_ROOT}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`RootNodeMode<enum_GLTFDocument_RootNodeMode>`{.interpreted-text
role="ref"} **ROOT_NODE_MODE_SINGLE_ROOT** = `0`

Treat the Godot scene\'s root node as the root node of the glTF file,
and mark it as the single root node via the `GODOT_single_root` glTF
extension. This will be parsed the same as
`ROOT_NODE_MODE_KEEP_ROOT<class_GLTFDocument_constant_ROOT_NODE_MODE_KEEP_ROOT>`{.interpreted-text
role="ref"} if the implementation does not support `GODOT_single_root`.

:::: {#class_GLTFDocument_constant_ROOT_NODE_MODE_KEEP_ROOT}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`RootNodeMode<enum_GLTFDocument_RootNodeMode>`{.interpreted-text
role="ref"} **ROOT_NODE_MODE_KEEP_ROOT** = `1`

Treat the Godot scene\'s root node as the root node of the glTF file,
but do not mark it as anything special. An extra root node will be
generated when importing into Godot. This uses only vanilla glTF
features. This is equivalent to the behavior in Godot 4.1 and earlier.

:::: {#class_GLTFDocument_constant_ROOT_NODE_MODE_MULTI_ROOT}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`RootNodeMode<enum_GLTFDocument_RootNodeMode>`{.interpreted-text
role="ref"} **ROOT_NODE_MODE_MULTI_ROOT** = `2`

Treat the Godot scene\'s root node as the name of the glTF scene, and
add all of its children as root nodes of the glTF file. This uses only
vanilla glTF features. This avoids an extra root node, but only the name
of the Godot scene\'s root node will be preserved, as it will not be
saved as a node.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_GLTFDocument_property_image_format}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **image_format** =
`"PNG"` `🔗<class_GLTFDocument_property_image_format>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_image_format**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_image_format**()

The user-friendly name of the export image format. This is used when
exporting the glTF file, including writing to a file and writing to a
byte array.

By default, Godot allows the following options: \"None\", \"PNG\",
\"JPEG\", \"Lossless WebP\", and \"Lossy WebP\". Support for more image
formats can be added in
`GLTFDocumentExtension<class_GLTFDocumentExtension>`{.interpreted-text
role="ref"} classes.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocument_property_lossy_quality}
::: {.rst-class}
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **lossy_quality** =
`0.75` `🔗<class_GLTFDocument_property_lossy_quality>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_lossy_quality**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_lossy_quality**()

If
`image_format<class_GLTFDocument_property_image_format>`{.interpreted-text
role="ref"} is a lossy image format, this determines the lossy quality
of the image. On a range of `0.0` to `1.0`, where `0.0` is the lowest
quality and `1.0` is the highest quality. A lossy quality of `1.0` is
not the same as lossless.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocument_property_root_node_mode}
::: {.rst-class}
classref-property
:::
::::

`RootNodeMode<enum_GLTFDocument_RootNodeMode>`{.interpreted-text
role="ref"} **root_node_mode** = `0`
`🔗<class_GLTFDocument_property_root_node_mode>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_root_node_mode**(value:
  `RootNodeMode<enum_GLTFDocument_RootNodeMode>`{.interpreted-text
  role="ref"})
- `RootNodeMode<enum_GLTFDocument_RootNodeMode>`{.interpreted-text
  role="ref"} **get_root_node_mode**()

How to process the root node during export. See
`RootNodeMode<enum_GLTFDocument_RootNodeMode>`{.interpreted-text
role="ref"} for details. The default and recommended value is
`ROOT_NODE_MODE_SINGLE_ROOT<class_GLTFDocument_constant_ROOT_NODE_MODE_SINGLE_ROOT>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Regardless of how the glTF file is exported, when
importing, the root node type and name can be overridden in the scene
import settings tab.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_GLTFDocument_method_append_from_buffer}
::: {.rst-class}
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**append_from_buffer**(bytes:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"},
base_path: `String<class_String>`{.interpreted-text role="ref"}, state:
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"}, flags:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_GLTFDocument_method_append_from_buffer>`{.interpreted-text
role="ref"}

Takes a `PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"} defining a glTF and imports the data to the given
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"} object
through the `state` parameter.

\*\*Note:\*\* The `base_path` tells
`append_from_buffer<class_GLTFDocument_method_append_from_buffer>`{.interpreted-text
role="ref"} where to find dependencies and can be empty.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocument_method_append_from_file}
::: {.rst-class}
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**append_from_file**(path: `String<class_String>`{.interpreted-text
role="ref"}, state: `GLTFState<class_GLTFState>`{.interpreted-text
role="ref"}, flags: `int<class_int>`{.interpreted-text role="ref"} = 0,
base_path: `String<class_String>`{.interpreted-text role="ref"} = \"\")
`🔗<class_GLTFDocument_method_append_from_file>`{.interpreted-text
role="ref"}

Takes a path to a glTF file and imports the data at that file path to
the given `GLTFState<class_GLTFState>`{.interpreted-text role="ref"}
object through the `state` parameter.

\*\*Note:\*\* The `base_path` tells
`append_from_file<class_GLTFDocument_method_append_from_file>`{.interpreted-text
role="ref"} where to find dependencies and can be empty.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocument_method_append_from_scene}
::: {.rst-class}
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**append_from_scene**(node: `Node<class_Node>`{.interpreted-text
role="ref"}, state: `GLTFState<class_GLTFState>`{.interpreted-text
role="ref"}, flags: `int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_GLTFDocument_method_append_from_scene>`{.interpreted-text
role="ref"}

Takes a Godot Engine scene node and exports it and its descendants to
the given `GLTFState<class_GLTFState>`{.interpreted-text role="ref"}
object through the `state` parameter.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocument_method_generate_buffer}
::: {.rst-class}
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**generate_buffer**(state:
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"})
`🔗<class_GLTFDocument_method_generate_buffer>`{.interpreted-text
role="ref"}

Takes a `GLTFState<class_GLTFState>`{.interpreted-text role="ref"}
object through the `state` parameter and returns a glTF
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocument_method_generate_scene}
::: {.rst-class}
classref-method
:::
::::

`Node<class_Node>`{.interpreted-text role="ref"}
**generate_scene**(state: `GLTFState<class_GLTFState>`{.interpreted-text
role="ref"}, bake_fps: `float<class_float>`{.interpreted-text
role="ref"} = 30, trimming: `bool<class_bool>`{.interpreted-text
role="ref"} = false, remove_immutable_tracks:
`bool<class_bool>`{.interpreted-text role="ref"} = true)
`🔗<class_GLTFDocument_method_generate_scene>`{.interpreted-text
role="ref"}

Takes a `GLTFState<class_GLTFState>`{.interpreted-text role="ref"}
object through the `state` parameter and returns a Godot Engine scene
node.

The `bake_fps` parameter overrides the bake_fps in `state`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocument_method_get_supported_gltf_extensions}
::: {.rst-class}
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_supported_gltf_extensions**()
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFDocument_method_get_supported_gltf_extensions>`{.interpreted-text
role="ref"}

Returns a list of all support glTF extensions, including extensions
supported directly by the engine, and extensions supported by user
plugins registering
`GLTFDocumentExtension<class_GLTFDocumentExtension>`{.interpreted-text
role="ref"} classes.

\*\*Note:\*\* If this method is run before a GLTFDocumentExtension is
registered, its extensions won\'t be included in the list. Be sure to
only run this method after all extensions are registered. If you run
this when the engine starts, consider waiting a frame before calling
this method to ensure all extensions are registered.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocument_method_register_gltf_document_extension}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**register_gltf_document_extension**(extension:
`GLTFDocumentExtension<class_GLTFDocumentExtension>`{.interpreted-text
role="ref"}, first_priority: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFDocument_method_register_gltf_document_extension>`{.interpreted-text
role="ref"}

Registers the given
`GLTFDocumentExtension<class_GLTFDocumentExtension>`{.interpreted-text
role="ref"} instance with GLTFDocument. If `first_priority` is true,
this extension will be run first. Otherwise, it will be run last.

\*\*Note:\*\* Like GLTFDocument itself, all GLTFDocumentExtension
classes must be stateless in order to function properly. If you need to
store data, use the `set_additional_data` and `get_additional_data`
methods in `GLTFState<class_GLTFState>`{.interpreted-text role="ref"} or
`GLTFNode<class_GLTFNode>`{.interpreted-text role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocument_method_unregister_gltf_document_extension}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**unregister_gltf_document_extension**(extension:
`GLTFDocumentExtension<class_GLTFDocumentExtension>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFDocument_method_unregister_gltf_document_extension>`{.interpreted-text
role="ref"}

Unregisters the given
`GLTFDocumentExtension<class_GLTFDocumentExtension>`{.interpreted-text
role="ref"} instance.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocument_method_write_to_filesystem}
::: {.rst-class}
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**write_to_filesystem**(state:
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"}, path:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_GLTFDocument_method_write_to_filesystem>`{.interpreted-text
role="ref"}

Takes a `GLTFState<class_GLTFState>`{.interpreted-text role="ref"}
object through the `state` parameter and writes a glTF file to the
filesystem.

\*\*Note:\*\* The extension of the glTF file determines if it is a .glb
binary file or a .gltf text file.
