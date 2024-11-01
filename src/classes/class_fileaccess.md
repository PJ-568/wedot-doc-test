github_url

:   hide

# FileAccess {#class_FileAccess}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Provides methods for file reading and writing operations.

::: {.rst-class}
classref-introduction-group
:::

## Description

This class can be used to permanently store data in the user device\'s
file system and to read from it. This is useful for store game save data
or player configuration files.

Here\'s a sample on how to write and read from a file:

::::: {.tabs}
::: {.code-tab}
gdscript

func save_to_file(content):

:   var file = FileAccess.open(\"user://save_game.dat\",
    FileAccess.WRITE) file.store_string(content)

func load_from_file():

:   var file = FileAccess.open(\"user://save_game.dat\",
    FileAccess.READ) var content = file.get_as_text() return content
:::

::: {.code-tab}
csharp

public void SaveToFile(string content) { using var file =
FileAccess.Open(\"user://save_game.dat\", FileAccess.ModeFlags.Write);
file.StoreString(content); }

public string LoadFromFile() { using var file =
FileAccess.Open(\"user://save_game.dat\", FileAccess.ModeFlags.Read);
string content = file.GetAsText(); return content; }
:::
:::::

In the example above, the file will be saved in the user data folder as
specified in the
`Data paths <../tutorials/io/data_paths>`{.interpreted-text role="doc"}
documentation.

\*\*FileAccess\*\* will close when it\'s freed, which happens when it
goes out of scope or when it gets assigned with `null`.
`close<class_FileAccess_method_close>`{.interpreted-text role="ref"} can
be used to close it before then explicitly. In C# the reference must be
disposed manually, which can be done with the `using` statement or by
calling the `Dispose` method directly.

\*\*Note:\*\* To access project resources once exported, it is
recommended to use
`ResourceLoader<class_ResourceLoader>`{.interpreted-text role="ref"}
instead of **FileAccess**, as some files are converted to
engine-specific formats and their original source files might not be
present in the exported PCK package.

\*\*Note:\*\* Files are automatically closed only if the process exits
\"normally\" (such as by clicking the window manager\'s close button or
pressing **Alt + F4**). If you stop the project execution by pressing
**F8** while the project is running, the file won\'t be closed as the
game process will be killed. You can work around this by calling
`flush<class_FileAccess_method_flush>`{.interpreted-text role="ref"} at
regular intervals.

::: {.rst-class}
classref-introduction-group
:::

## Tutorials

- `File system <../tutorials/scripting/filesystem>`{.interpreted-text
  role="doc"}
- `Runtime file loading and saving <../tutorials/io/runtime_file_loading_and_saving>`{.interpreted-text
  role="doc"}
- [3D Voxel Demo](https://godotengine.org/asset-library/asset/2755)

::: {.rst-class}
classref-reftable-group
:::

## Properties

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

:::: {#enum_FileAccess_ModeFlags}
::: {.rst-class}
classref-enumeration
:::
::::

enum **ModeFlags**: `🔗<enum_FileAccess_ModeFlags>`{.interpreted-text
role="ref"}

:::: {#class_FileAccess_constant_READ}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`ModeFlags<enum_FileAccess_ModeFlags>`{.interpreted-text role="ref"}
**READ** = `1`

Opens the file for read operations. The cursor is positioned at the
beginning of the file.

:::: {#class_FileAccess_constant_WRITE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`ModeFlags<enum_FileAccess_ModeFlags>`{.interpreted-text role="ref"}
**WRITE** = `2`

Opens the file for write operations. The file is created if it does not
exist, and truncated if it does.

\*\*Note:\*\* When creating a file it must be in an already existing
directory. To recursively create directories for a file path, see
`DirAccess.make_dir_recursive<class_DirAccess_method_make_dir_recursive>`{.interpreted-text
role="ref"}.

:::: {#class_FileAccess_constant_READ_WRITE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`ModeFlags<enum_FileAccess_ModeFlags>`{.interpreted-text role="ref"}
**READ_WRITE** = `3`

Opens the file for read and write operations. Does not truncate the
file. The cursor is positioned at the beginning of the file.

:::: {#class_FileAccess_constant_WRITE_READ}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`ModeFlags<enum_FileAccess_ModeFlags>`{.interpreted-text role="ref"}
**WRITE_READ** = `7`

Opens the file for read and write operations. The file is created if it
does not exist, and truncated if it does. The cursor is positioned at
the beginning of the file.

\*\*Note:\*\* When creating a file it must be in an already existing
directory. To recursively create directories for a file path, see
`DirAccess.make_dir_recursive<class_DirAccess_method_make_dir_recursive>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_FileAccess_CompressionMode}
::: {.rst-class}
classref-enumeration
:::
::::

enum **CompressionMode**:
`🔗<enum_FileAccess_CompressionMode>`{.interpreted-text role="ref"}

:::: {#class_FileAccess_constant_COMPRESSION_FASTLZ}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`CompressionMode<enum_FileAccess_CompressionMode>`{.interpreted-text
role="ref"} **COMPRESSION_FASTLZ** = `0`

Uses the [FastLZ](https://fastlz.org/) compression method.

:::: {#class_FileAccess_constant_COMPRESSION_DEFLATE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`CompressionMode<enum_FileAccess_CompressionMode>`{.interpreted-text
role="ref"} **COMPRESSION_DEFLATE** = `1`

Uses the [DEFLATE](https://en.wikipedia.org/wiki/DEFLATE) compression
method.

:::: {#class_FileAccess_constant_COMPRESSION_ZSTD}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`CompressionMode<enum_FileAccess_CompressionMode>`{.interpreted-text
role="ref"} **COMPRESSION_ZSTD** = `2`

Uses the [Zstandard](https://facebook.github.io/zstd/) compression
method.

:::: {#class_FileAccess_constant_COMPRESSION_GZIP}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`CompressionMode<enum_FileAccess_CompressionMode>`{.interpreted-text
role="ref"} **COMPRESSION_GZIP** = `3`

Uses the [gzip](https://www.gzip.org/) compression method.

:::: {#class_FileAccess_constant_COMPRESSION_BROTLI}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`CompressionMode<enum_FileAccess_CompressionMode>`{.interpreted-text
role="ref"} **COMPRESSION_BROTLI** = `4`

Uses the [brotli](https://github.com/google/brotli) compression method
(only decompression is supported).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_FileAccess_UnixPermissionFlags}
::: {.rst-class}
classref-enumeration
:::
::::

flags **UnixPermissionFlags**:
`🔗<enum_FileAccess_UnixPermissionFlags>`{.interpreted-text role="ref"}

:::: {#class_FileAccess_constant_UNIX_READ_OWNER}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`UnixPermissionFlags<enum_FileAccess_UnixPermissionFlags>`{.interpreted-text
role="ref"} **UNIX_READ_OWNER** = `256`

Read for owner bit.

:::: {#class_FileAccess_constant_UNIX_WRITE_OWNER}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`UnixPermissionFlags<enum_FileAccess_UnixPermissionFlags>`{.interpreted-text
role="ref"} **UNIX_WRITE_OWNER** = `128`

Write for owner bit.

:::: {#class_FileAccess_constant_UNIX_EXECUTE_OWNER}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`UnixPermissionFlags<enum_FileAccess_UnixPermissionFlags>`{.interpreted-text
role="ref"} **UNIX_EXECUTE_OWNER** = `64`

Execute for owner bit.

:::: {#class_FileAccess_constant_UNIX_READ_GROUP}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`UnixPermissionFlags<enum_FileAccess_UnixPermissionFlags>`{.interpreted-text
role="ref"} **UNIX_READ_GROUP** = `32`

Read for group bit.

:::: {#class_FileAccess_constant_UNIX_WRITE_GROUP}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`UnixPermissionFlags<enum_FileAccess_UnixPermissionFlags>`{.interpreted-text
role="ref"} **UNIX_WRITE_GROUP** = `16`

Write for group bit.

:::: {#class_FileAccess_constant_UNIX_EXECUTE_GROUP}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`UnixPermissionFlags<enum_FileAccess_UnixPermissionFlags>`{.interpreted-text
role="ref"} **UNIX_EXECUTE_GROUP** = `8`

Execute for group bit.

:::: {#class_FileAccess_constant_UNIX_READ_OTHER}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`UnixPermissionFlags<enum_FileAccess_UnixPermissionFlags>`{.interpreted-text
role="ref"} **UNIX_READ_OTHER** = `4`

Read for other bit.

:::: {#class_FileAccess_constant_UNIX_WRITE_OTHER}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`UnixPermissionFlags<enum_FileAccess_UnixPermissionFlags>`{.interpreted-text
role="ref"} **UNIX_WRITE_OTHER** = `2`

Write for other bit.

:::: {#class_FileAccess_constant_UNIX_EXECUTE_OTHER}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`UnixPermissionFlags<enum_FileAccess_UnixPermissionFlags>`{.interpreted-text
role="ref"} **UNIX_EXECUTE_OTHER** = `1`

Execute for other bit.

:::: {#class_FileAccess_constant_UNIX_SET_USER_ID}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`UnixPermissionFlags<enum_FileAccess_UnixPermissionFlags>`{.interpreted-text
role="ref"} **UNIX_SET_USER_ID** = `2048`

Set user id on execution bit.

:::: {#class_FileAccess_constant_UNIX_SET_GROUP_ID}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`UnixPermissionFlags<enum_FileAccess_UnixPermissionFlags>`{.interpreted-text
role="ref"} **UNIX_SET_GROUP_ID** = `1024`

Set group id on execution bit.

:::: {#class_FileAccess_constant_UNIX_RESTRICTED_DELETE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`UnixPermissionFlags<enum_FileAccess_UnixPermissionFlags>`{.interpreted-text
role="ref"} **UNIX_RESTRICTED_DELETE** = `512`

Restricted deletion (sticky) bit.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_FileAccess_property_big_endian}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **big_endian**
`🔗<class_FileAccess_property_big_endian>`{.interpreted-text role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_big_endian**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_big_endian**()

If `true`, the file is read with big-endian
[endianness](https://en.wikipedia.org/wiki/Endianness). If `false`, the
file is read with little-endian endianness. If in doubt, leave this to
`false` as most files are written with little-endian endianness.

\*\*Note:\*\*
`big_endian<class_FileAccess_property_big_endian>`{.interpreted-text
role="ref"} is only about the file format, not the CPU type. The CPU
endianness doesn\'t affect the default endianness for files written.

\*\*Note:\*\* This is always reset to `false` whenever you open the
file. Therefore, you must set
`big_endian<class_FileAccess_property_big_endian>`{.interpreted-text
role="ref"} *after* opening the file, not before.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_FileAccess_method_close}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **close**()
`🔗<class_FileAccess_method_close>`{.interpreted-text role="ref"}

Closes the currently opened file and prevents subsequent read/write
operations. Use `flush<class_FileAccess_method_flush>`{.interpreted-text
role="ref"} to persist the data to disk without closing the file.

\*\*Note:\*\* **FileAccess** will automatically close when it\'s freed,
which happens when it goes out of scope or when it gets assigned with
`null`. In C# the reference must be disposed after we are done using it,
this can be done with the `using` statement or calling the `Dispose`
method directly.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_eof_reached}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **eof_reached**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_FileAccess_method_eof_reached>`{.interpreted-text
role="ref"}

Returns `true` if the file cursor has already read past the end of the
file.

\*\*Note:\*\* `eof_reached() == false` cannot be used to check whether
there is more data available. To loop while there is more data
available, use:

::::: {.tabs}
::: {.code-tab}
gdscript

while file.get_position() \< file.get_length():

:   \# Read data
:::

::: {.code-tab}
csharp

while (file.GetPosition() \< file.GetLength()) { // Read data }
:::
:::::

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_file_exists}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **file_exists**(path:
`String<class_String>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_FileAccess_method_file_exists>`{.interpreted-text
role="ref"}

Returns `true` if the file exists in the given path.

\*\*Note:\*\* Many resources types are imported (e.g. textures or sound
files), and their source asset will not be included in the exported
game, as only the imported version is used. See
`ResourceLoader.exists<class_ResourceLoader_method_exists>`{.interpreted-text
role="ref"} for an alternative approach that takes resource remapping
into account.

For a non-static, relative equivalent, use
`DirAccess.file_exists<class_DirAccess_method_file_exists>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_flush}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **flush**()
`🔗<class_FileAccess_method_flush>`{.interpreted-text role="ref"}

Writes the file\'s buffer to disk. Flushing is automatically performed
when the file is closed. This means you don\'t need to call
`flush<class_FileAccess_method_flush>`{.interpreted-text role="ref"}
manually before closing a file. Still, calling
`flush<class_FileAccess_method_flush>`{.interpreted-text role="ref"} can
be used to ensure the data is safe even if the project crashes instead
of being closed gracefully.

\*\*Note:\*\* Only call
`flush<class_FileAccess_method_flush>`{.interpreted-text role="ref"}
when you actually need it. Otherwise, it will decrease performance due
to constant disk writes.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_get_8}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_8**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_FileAccess_method_get_8>`{.interpreted-text
role="ref"}

Returns the next 8 bits from the file as an integer. See
`store_8<class_FileAccess_method_store_8>`{.interpreted-text role="ref"}
for details on what values can be stored and retrieved this way.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_get_16}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_16**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_FileAccess_method_get_16>`{.interpreted-text
role="ref"}

Returns the next 16 bits from the file as an integer. See
`store_16<class_FileAccess_method_store_16>`{.interpreted-text
role="ref"} for details on what values can be stored and retrieved this
way.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_get_32}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_32**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_FileAccess_method_get_32>`{.interpreted-text
role="ref"}

Returns the next 32 bits from the file as an integer. See
`store_32<class_FileAccess_method_store_32>`{.interpreted-text
role="ref"} for details on what values can be stored and retrieved this
way.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_get_64}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_64**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_FileAccess_method_get_64>`{.interpreted-text
role="ref"}

Returns the next 64 bits from the file as an integer. See
`store_64<class_FileAccess_method_store_64>`{.interpreted-text
role="ref"} for details on what values can be stored and retrieved this
way.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_get_as_text}
::: {.rst-class}
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_as_text**(skip_cr: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_FileAccess_method_get_as_text>`{.interpreted-text
role="ref"}

Returns the whole file as a `String<class_String>`{.interpreted-text
role="ref"}. Text is interpreted as being UTF-8 encoded.

If `skip_cr` is `true`, carriage return characters (`\r`, CR) will be
ignored when parsing the UTF-8, so that only line feed characters (`\n`,
LF) represent a new line (Unix convention).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_get_buffer}
::: {.rst-class}
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**get_buffer**(length: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_FileAccess_method_get_buffer>`{.interpreted-text
role="ref"}

Returns next `length` bytes of the file as a
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_get_csv_line}
::: {.rst-class}
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_csv_line**(delim:
`String<class_String>`{.interpreted-text role="ref"} = \",\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FileAccess_method_get_csv_line>`{.interpreted-text role="ref"}

Returns the next value of the file in CSV (Comma-Separated Values)
format. You can pass a different delimiter `delim` to use other than the
default `","` (comma). This delimiter must be one-character long, and
cannot be a double quotation mark.

Text is interpreted as being UTF-8 encoded. Text values must be enclosed
in double quotes if they include the delimiter character. Double quotes
within a text value can be escaped by doubling their occurrence.

For example, the following CSV lines are valid and will be properly
parsed as two strings each:

``` text
Alice,"Hello, Bob!"
Bob,Alice! What a surprise!
Alice,"I thought you'd reply with ""Hello, world""."
```

Note how the second line can omit the enclosing quotes as it does not
include the delimiter. However it *could* very well use quotes, it was
only written without for demonstration purposes. The third line must use
`""` for each quotation mark that needs to be interpreted as such
instead of the end of a text value.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_get_double}
::: {.rst-class}
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_double**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_FileAccess_method_get_double>`{.interpreted-text
role="ref"}

Returns the next 64 bits from the file as a floating-point number.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_get_error}
::: {.rst-class}
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**get_error**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_FileAccess_method_get_error>`{.interpreted-text
role="ref"}

Returns the last error that happened when trying to perform operations.
Compare with the `ERR_FILE_*` constants from
`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_get_file_as_bytes}
::: {.rst-class}
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**get_file_as_bytes**(path: `String<class_String>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_FileAccess_method_get_file_as_bytes>`{.interpreted-text
role="ref"}

Returns the whole `path` file contents as a
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
without any decoding.

Returns an empty
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
if an error occurred while opening the file. You can use
`get_open_error<class_FileAccess_method_get_open_error>`{.interpreted-text
role="ref"} to check the error that occurred.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_get_file_as_string}
::: {.rst-class}
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_file_as_string**(path: `String<class_String>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_FileAccess_method_get_file_as_string>`{.interpreted-text
role="ref"}

Returns the whole `path` file contents as a
`String<class_String>`{.interpreted-text role="ref"}. Text is
interpreted as being UTF-8 encoded.

Returns an empty `String<class_String>`{.interpreted-text role="ref"} if
an error occurred while opening the file. You can use
`get_open_error<class_FileAccess_method_get_open_error>`{.interpreted-text
role="ref"} to check the error that occurred.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_get_float}
::: {.rst-class}
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_float**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_FileAccess_method_get_float>`{.interpreted-text
role="ref"}

Returns the next 32 bits from the file as a floating-point number.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_get_hidden_attribute}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_hidden_attribute**(file: `String<class_String>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_FileAccess_method_get_hidden_attribute>`{.interpreted-text
role="ref"}

Returns `true`, if file `hidden` attribute is set.

\*\*Note:\*\* This method is implemented on iOS, BSD, macOS, and
Windows.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_get_length}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_length**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_FileAccess_method_get_length>`{.interpreted-text
role="ref"}

Returns the size of the file in bytes.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_get_line}
::: {.rst-class}
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_line**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_FileAccess_method_get_line>`{.interpreted-text
role="ref"}

Returns the next line of the file as a
`String<class_String>`{.interpreted-text role="ref"}. The returned
string doesn\'t include newline (`\n`) or carriage return (`\r`)
characters, but does include any other leading or trailing whitespace.

Text is interpreted as being UTF-8 encoded.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_get_md5}
::: {.rst-class}
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_md5**(path:
`String<class_String>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_FileAccess_method_get_md5>`{.interpreted-text
role="ref"}

Returns an MD5 String representing the file at the given path or an
empty `String<class_String>`{.interpreted-text role="ref"} on failure.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_get_modified_time}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_modified_time**(file: `String<class_String>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_FileAccess_method_get_modified_time>`{.interpreted-text
role="ref"}

Returns the last time the `file` was modified in Unix timestamp format,
or `0` on error. This Unix timestamp can be converted to another format
using the `Time<class_Time>`{.interpreted-text role="ref"} singleton.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_get_open_error}
::: {.rst-class}
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**get_open_error**()
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_FileAccess_method_get_open_error>`{.interpreted-text
role="ref"}

Returns the result of the last
`open<class_FileAccess_method_open>`{.interpreted-text role="ref"} call
in the current thread.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_get_pascal_string}
::: {.rst-class}
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_pascal_string**()
`🔗<class_FileAccess_method_get_pascal_string>`{.interpreted-text
role="ref"}

Returns a `String<class_String>`{.interpreted-text role="ref"} saved in
Pascal format from the file.

Text is interpreted as being UTF-8 encoded.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_get_path}
::: {.rst-class}
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_path**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_FileAccess_method_get_path>`{.interpreted-text
role="ref"}

Returns the path as a `String<class_String>`{.interpreted-text
role="ref"} for the current open file.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_get_path_absolute}
::: {.rst-class}
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_path_absolute**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FileAccess_method_get_path_absolute>`{.interpreted-text
role="ref"}

Returns the absolute path as a `String<class_String>`{.interpreted-text
role="ref"} for the current open file.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_get_position}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_position**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FileAccess_method_get_position>`{.interpreted-text role="ref"}

Returns the file cursor\'s position.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_get_read_only_attribute}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_read_only_attribute**(file:
`String<class_String>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_FileAccess_method_get_read_only_attribute>`{.interpreted-text
role="ref"}

Returns `true`, if file `read only` attribute is set.

\*\*Note:\*\* This method is implemented on iOS, BSD, macOS, and
Windows.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_get_real}
::: {.rst-class}
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_real**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_FileAccess_method_get_real>`{.interpreted-text
role="ref"}

Returns the next bits from the file as a floating-point number.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_get_sha256}
::: {.rst-class}
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_sha256**(path: `String<class_String>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_FileAccess_method_get_sha256>`{.interpreted-text
role="ref"}

Returns an SHA-256 `String<class_String>`{.interpreted-text role="ref"}
representing the file at the given path or an empty
`String<class_String>`{.interpreted-text role="ref"} on failure.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_get_unix_permissions}
::: {.rst-class}
classref-method
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`UnixPermissionFlags<enum_FileAccess_UnixPermissionFlags>`{.interpreted-text
role="ref"}\] **get_unix_permissions**(file:
`String<class_String>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_FileAccess_method_get_unix_permissions>`{.interpreted-text
role="ref"}

Returns file UNIX permissions.

\*\*Note:\*\* This method is implemented on iOS, Linux/BSD, and macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_get_var}
::: {.rst-class}
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_var**(allow_objects: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_FileAccess_method_get_var>`{.interpreted-text
role="ref"}

Returns the next `Variant<class_Variant>`{.interpreted-text role="ref"}
value from the file. If `allow_objects` is `true`, decoding objects is
allowed.

Internally, this uses the same decoding mechanism as the
`@GlobalScope.bytes_to_var<class_@GlobalScope_method_bytes_to_var>`{.interpreted-text
role="ref"} method.

\*\*Warning:\*\* Deserialized objects can contain code which gets
executed. Do not use this option if the serialized object comes from
untrusted sources to avoid potential security threats such as remote
code execution.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_is_open}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_open**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_FileAccess_method_is_open>`{.interpreted-text
role="ref"}

Returns `true` if the file is currently opened.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_open}
::: {.rst-class}
classref-method
:::
::::

`FileAccess<class_FileAccess>`{.interpreted-text role="ref"}
**open**(path: `String<class_String>`{.interpreted-text role="ref"},
flags: `ModeFlags<enum_FileAccess_ModeFlags>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_FileAccess_method_open>`{.interpreted-text
role="ref"}

Creates a new **FileAccess** object and opens the file for writing or
reading, depending on the flags.

Returns `null` if opening the file failed. You can use
`get_open_error<class_FileAccess_method_get_open_error>`{.interpreted-text
role="ref"} to check the error that occurred.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_open_compressed}
::: {.rst-class}
classref-method
:::
::::

`FileAccess<class_FileAccess>`{.interpreted-text role="ref"}
**open_compressed**(path: `String<class_String>`{.interpreted-text
role="ref"}, mode_flags:
`ModeFlags<enum_FileAccess_ModeFlags>`{.interpreted-text role="ref"},
compression_mode:
`CompressionMode<enum_FileAccess_CompressionMode>`{.interpreted-text
role="ref"} = 0)
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_FileAccess_method_open_compressed>`{.interpreted-text
role="ref"}

Creates a new **FileAccess** object and opens a compressed file for
reading or writing.

\*\*Note:\*\*
`open_compressed<class_FileAccess_method_open_compressed>`{.interpreted-text
role="ref"} can only read files that were saved by Godot, not
third-party compression formats. See [GitHub issue
\#28999](https://github.com/godotengine/godot/issues/28999) for a
workaround.

Returns `null` if opening the file failed. You can use
`get_open_error<class_FileAccess_method_get_open_error>`{.interpreted-text
role="ref"} to check the error that occurred.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_open_encrypted}
::: {.rst-class}
classref-method
:::
::::

`FileAccess<class_FileAccess>`{.interpreted-text role="ref"}
**open_encrypted**(path: `String<class_String>`{.interpreted-text
role="ref"}, mode_flags:
`ModeFlags<enum_FileAccess_ModeFlags>`{.interpreted-text role="ref"},
key: `PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_FileAccess_method_open_encrypted>`{.interpreted-text
role="ref"}

Creates a new **FileAccess** object and opens an encrypted file in write
or read mode. You need to pass a binary key to encrypt/decrypt it.

\*\*Note:\*\* The provided key must be 32 bytes long.

Returns `null` if opening the file failed. You can use
`get_open_error<class_FileAccess_method_get_open_error>`{.interpreted-text
role="ref"} to check the error that occurred.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_open_encrypted_with_pass}
::: {.rst-class}
classref-method
:::
::::

`FileAccess<class_FileAccess>`{.interpreted-text role="ref"}
**open_encrypted_with_pass**(path:
`String<class_String>`{.interpreted-text role="ref"}, mode_flags:
`ModeFlags<enum_FileAccess_ModeFlags>`{.interpreted-text role="ref"},
pass: `String<class_String>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_FileAccess_method_open_encrypted_with_pass>`{.interpreted-text
role="ref"}

Creates a new **FileAccess** object and opens an encrypted file in write
or read mode. You need to pass a password to encrypt/decrypt it.

Returns `null` if opening the file failed. You can use
`get_open_error<class_FileAccess_method_get_open_error>`{.interpreted-text
role="ref"} to check the error that occurred.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_resize}
::: {.rst-class}
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**resize**(length: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_FileAccess_method_resize>`{.interpreted-text role="ref"}

Resizes the file to a specified length. The file must be open in a mode
that permits writing. If the file is extended, NUL characters are
appended. If the file is truncated, all data from the end file to the
original length of the file is lost.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_seek}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**seek**(position: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_FileAccess_method_seek>`{.interpreted-text role="ref"}

Changes the file reading/writing cursor to the specified position (in
bytes from the beginning of the file).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_seek_end}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**seek_end**(position: `int<class_int>`{.interpreted-text role="ref"} =
0) `🔗<class_FileAccess_method_seek_end>`{.interpreted-text role="ref"}

Changes the file reading/writing cursor to the specified position (in
bytes from the end of the file).

\*\*Note:\*\* This is an offset, so you should use negative numbers or
the cursor will be at the end of the file.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_set_hidden_attribute}
::: {.rst-class}
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**set_hidden_attribute**(file: `String<class_String>`{.interpreted-text
role="ref"}, hidden: `bool<class_bool>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_FileAccess_method_set_hidden_attribute>`{.interpreted-text
role="ref"}

Sets file **hidden** attribute.

\*\*Note:\*\* This method is implemented on iOS, BSD, macOS, and
Windows.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_set_read_only_attribute}
::: {.rst-class}
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**set_read_only_attribute**(file:
`String<class_String>`{.interpreted-text role="ref"}, ro:
`bool<class_bool>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_FileAccess_method_set_read_only_attribute>`{.interpreted-text
role="ref"}

Sets file **read only** attribute.

\*\*Note:\*\* This method is implemented on iOS, BSD, macOS, and
Windows.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_set_unix_permissions}
::: {.rst-class}
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**set_unix_permissions**(file: `String<class_String>`{.interpreted-text
role="ref"}, permissions:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`UnixPermissionFlags<enum_FileAccess_UnixPermissionFlags>`{.interpreted-text
role="ref"}\])
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_FileAccess_method_set_unix_permissions>`{.interpreted-text
role="ref"}

Sets file UNIX permissions.

\*\*Note:\*\* This method is implemented on iOS, Linux/BSD, and macOS.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_store_8}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**store_8**(value: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_FileAccess_method_store_8>`{.interpreted-text role="ref"}

Stores an integer as 8 bits in the file.

\*\*Note:\*\* The `value` should lie in the interval `[0, 255]`. Any
other value will overflow and wrap around.

To store a signed integer, use
`store_64<class_FileAccess_method_store_64>`{.interpreted-text
role="ref"}, or convert it manually (see
`store_16<class_FileAccess_method_store_16>`{.interpreted-text
role="ref"} for an example).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_store_16}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**store_16**(value: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_FileAccess_method_store_16>`{.interpreted-text role="ref"}

Stores an integer as 16 bits in the file.

\*\*Note:\*\* The `value` should lie in the interval `[0, 2^16 - 1]`.
Any other value will overflow and wrap around.

To store a signed integer, use
`store_64<class_FileAccess_method_store_64>`{.interpreted-text
role="ref"} or store a signed integer from the interval
`[-2^15, 2^15 - 1]` (i.e. keeping one bit for the signedness) and
compute its sign manually when reading. For example:

::::: {.tabs}
::: {.code-tab}
gdscript

const MAX_15B = 1 \<\< 15 const MAX_16B = 1 \<\< 16

func unsigned16_to_signed(unsigned):

:   return (unsigned + MAX_15B) % MAX_16B - MAX_15B

func \_ready():

:   var f = FileAccess.open(\"user://file.dat\", FileAccess.WRITE_READ)
    f.store_16(-42) \# This wraps around and stores 65494 (2\^16 - 42).
    f.store_16(121) \# In bounds, will store 121. f.seek(0) \# Go back
    to start to read the stored value. var read1 = f.get_16() \# 65494
    var read2 = f.get_16() \# 121 var converted1 =
    unsigned16_to_signed(read1) \# -42 var converted2 =
    unsigned16_to_signed(read2) \# 121
:::

::: {.code-tab}
csharp

public override void \_Ready() { using var f =
FileAccess.Open(\"user://file.dat\", FileAccess.ModeFlags.WriteRead);
f.Store16(unchecked((ushort)-42)); // This wraps around and stores 65494
(2\^16 - 42). f.Store16(121); // In bounds, will store 121. f.Seek(0);
// Go back to start to read the stored value. ushort read1 = f.Get16();
// 65494 ushort read2 = f.Get16(); // 121 short converted1 =
(short)read1; // -42 short converted2 = (short)read2; // 121 }
:::
:::::

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_store_32}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**store_32**(value: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_FileAccess_method_store_32>`{.interpreted-text role="ref"}

Stores an integer as 32 bits in the file.

\*\*Note:\*\* The `value` should lie in the interval `[0, 2^32 - 1]`.
Any other value will overflow and wrap around.

To store a signed integer, use
`store_64<class_FileAccess_method_store_64>`{.interpreted-text
role="ref"}, or convert it manually (see
`store_16<class_FileAccess_method_store_16>`{.interpreted-text
role="ref"} for an example).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_store_64}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**store_64**(value: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_FileAccess_method_store_64>`{.interpreted-text role="ref"}

Stores an integer as 64 bits in the file.

\*\*Note:\*\* The `value` must lie in the interval `[-2^63, 2^63 - 1]`
(i.e. be a valid `int<class_int>`{.interpreted-text role="ref"} value).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_store_buffer}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**store_buffer**(buffer:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_FileAccess_method_store_buffer>`{.interpreted-text role="ref"}

Stores the given array of bytes in the file.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_store_csv_line}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**store_csv_line**(values:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}, delim: `String<class_String>`{.interpreted-text role="ref"}
= \",\") `🔗<class_FileAccess_method_store_csv_line>`{.interpreted-text
role="ref"}

Store the given
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} in the file as a line formatted in the CSV (Comma-Separated
Values) format. You can pass a different delimiter `delim` to use other
than the default `","` (comma). This delimiter must be one-character
long.

Text will be encoded as UTF-8.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_store_double}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**store_double**(value: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_FileAccess_method_store_double>`{.interpreted-text role="ref"}

Stores a floating-point number as 64 bits in the file.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_store_float}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**store_float**(value: `float<class_float>`{.interpreted-text
role="ref"}) `🔗<class_FileAccess_method_store_float>`{.interpreted-text
role="ref"}

Stores a floating-point number as 32 bits in the file.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_store_line}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**store_line**(line: `String<class_String>`{.interpreted-text
role="ref"}) `🔗<class_FileAccess_method_store_line>`{.interpreted-text
role="ref"}

Stores `line` in the file followed by a newline character (`\n`),
encoding the text as UTF-8.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_store_pascal_string}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**store_pascal_string**(string: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_FileAccess_method_store_pascal_string>`{.interpreted-text
role="ref"}

Stores the given `String<class_String>`{.interpreted-text role="ref"} as
a line in the file in Pascal format (i.e. also store the length of the
string).

Text will be encoded as UTF-8.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_store_real}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**store_real**(value: `float<class_float>`{.interpreted-text
role="ref"}) `🔗<class_FileAccess_method_store_real>`{.interpreted-text
role="ref"}

Stores a floating-point number in the file.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_store_string}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**store_string**(string: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_FileAccess_method_store_string>`{.interpreted-text role="ref"}

Stores `string` in the file without a newline character (`\n`), encoding
the text as UTF-8.

\*\*Note:\*\* This method is intended to be used to write text files.
The string is stored as a UTF-8 encoded buffer without string length or
terminating zero, which means that it can\'t be loaded back easily. If
you want to store a retrievable string in a binary file, consider using
`store_pascal_string<class_FileAccess_method_store_pascal_string>`{.interpreted-text
role="ref"} instead. For retrieving strings from a text file, you can
use `get_buffer(length).get_string_from_utf8()` (if you know the length)
or `get_as_text<class_FileAccess_method_get_as_text>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileAccess_method_store_var}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**store_var**(value: `Variant<class_Variant>`{.interpreted-text
role="ref"}, full_objects: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_FileAccess_method_store_var>`{.interpreted-text role="ref"}

Stores any Variant value in the file. If `full_objects` is `true`,
encoding objects is allowed (and can potentially include code).

Internally, this uses the same encoding mechanism as the
`@GlobalScope.var_to_bytes<class_@GlobalScope_method_var_to_bytes>`{.interpreted-text
role="ref"} method.

\*\*Note:\*\* Not all properties are included. Only properties that are
configured with the
`@GlobalScope.PROPERTY_USAGE_STORAGE<class_@GlobalScope_constant_PROPERTY_USAGE_STORAGE>`{.interpreted-text
role="ref"} flag set will be serialized. You can add a new usage flag to
a property by overriding the
`Object._get_property_list<class_Object_private_method__get_property_list>`{.interpreted-text
role="ref"} method in your class. You can also check how property usage
is configured by calling
`Object._get_property_list<class_Object_private_method__get_property_list>`{.interpreted-text
role="ref"}. See
`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} for the possible usage flags.
