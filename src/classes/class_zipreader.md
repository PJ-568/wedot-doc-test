github_url

:   hide

# ZIPReader {#class_ZIPReader}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Allows reading the content of a zip file.

::: {.rst-class}
classref-introduction-group
:::

## Description

This class implements a reader that can extract the content of
individual files inside a zip archive.

    func read_zip_file():
        var reader := ZIPReader.new()
        var err := reader.open("user://archive.zip")
        if err != OK:
            return PackedByteArray()
        var res := reader.read_file("hello.txt")
        reader.close()
        return res

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

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_ZIPReader_method_close}
::: {.rst-class}
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**close**() `🔗<class_ZIPReader_method_close>`{.interpreted-text
role="ref"}

Closes the underlying resources used by this instance.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ZIPReader_method_file_exists}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **file_exists**(path:
`String<class_String>`{.interpreted-text role="ref"}, case_sensitive:
`bool<class_bool>`{.interpreted-text role="ref"} = true)
`🔗<class_ZIPReader_method_file_exists>`{.interpreted-text role="ref"}

Returns `true` if the file exists in the loaded zip archive.

Must be called after
`open<class_ZIPReader_method_open>`{.interpreted-text role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ZIPReader_method_get_files}
::: {.rst-class}
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_files**()
`🔗<class_ZIPReader_method_get_files>`{.interpreted-text role="ref"}

Returns the list of names of all files in the loaded archive.

Must be called after
`open<class_ZIPReader_method_open>`{.interpreted-text role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ZIPReader_method_open}
::: {.rst-class}
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**open**(path: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_ZIPReader_method_open>`{.interpreted-text role="ref"}

Opens the zip archive at the given `path` and reads its file index.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ZIPReader_method_read_file}
::: {.rst-class}
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**read_file**(path: `String<class_String>`{.interpreted-text
role="ref"}, case_sensitive: `bool<class_bool>`{.interpreted-text
role="ref"} = true)
`🔗<class_ZIPReader_method_read_file>`{.interpreted-text role="ref"}

Loads the whole content of a file in the loaded zip archive into memory
and returns it.

Must be called after
`open<class_ZIPReader_method_open>`{.interpreted-text role="ref"}.
