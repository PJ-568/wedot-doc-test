github_url

:   hide

# AudioStreamMP3 {#class_AudioStreamMP3}

**Inherits:** `AudioStream<class_AudioStream>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

MP3 audio stream driver.

::: {.rst-class}
classref-introduction-group
:::

## Description

MP3 audio stream driver. See
`data<class_AudioStreamMP3_property_data>`{.interpreted-text role="ref"}
if you want to load an MP3 file at run-time.

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
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AudioStreamMP3_property_bar_beats}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **bar_beats** = `4`
`🔗<class_AudioStreamMP3_property_bar_beats>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bar_beats**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_bar_beats**()

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamMP3_property_beat_count}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **beat_count** = `0`
`🔗<class_AudioStreamMP3_property_beat_count>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_beat_count**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_beat_count**()

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamMP3_property_bpm}
::: {.rst-class}
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **bpm** = `0.0`
`🔗<class_AudioStreamMP3_property_bpm>`{.interpreted-text role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bpm**(value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_bpm**()

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamMP3_property_data}
::: {.rst-class}
classref-property
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**data** = `PackedByteArray()`
`🔗<class_AudioStreamMP3_property_data>`{.interpreted-text role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_data**(value:
  `PackedByteArray<class_PackedByteArray>`{.interpreted-text
  role="ref"})
- `PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
  **get_data**()

Contains the audio data in bytes.

You can load a file without having to import it beforehand using the
code snippet below. Keep in mind that this snippet loads the whole file
into memory and may not be ideal for huge files (hundreds of megabytes
or more).

::::: {.tabs}
::: {.code-tab}
gdscript

func load_mp3(path):

:   var file = FileAccess.open(path, FileAccess.READ) var sound =
    AudioStreamMP3.new() sound.data = file.get_buffer(file.get_length())
    return sound
:::

::: {.code-tab}
csharp

public AudioStreamMP3 LoadMP3(string path) { using var file =
FileAccess.Open(path, FileAccess.ModeFlags.Read); var sound = new
AudioStreamMP3(); sound.Data = file.GetBuffer(file.GetLength()); return
sound; }
:::
:::::

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
for more details.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamMP3_property_loop}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **loop** = `false`
`🔗<class_AudioStreamMP3_property_loop>`{.interpreted-text role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_loop**(value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **has_loop**()

If `true`, the stream will automatically loop when it reaches the end.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamMP3_property_loop_offset}
::: {.rst-class}
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **loop_offset** =
`0.0` `🔗<class_AudioStreamMP3_property_loop_offset>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_loop_offset**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_loop_offset**()

Time in seconds at which the stream starts after being looped.
