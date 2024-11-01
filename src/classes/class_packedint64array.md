github_url

:   hide

# PackedInt64Array {#class_PackedInt64Array}

A packed array of 64-bit integers.

::: {.rst-class}
classref-introduction-group
:::

## Description

An array specifically designed to hold 64-bit integer values. Packs data
tightly, so it saves memory for large array sizes.

\*\*Note:\*\* This type stores signed 64-bit integers, which means it
can take values in the interval `[-2^63, 2^63 - 1]`, i.e.
`[-9223372036854775808, 9223372036854775807]`. Exceeding those bounds
will wrap around. If you only need to pack 32-bit integers tightly, see
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
for a more memory-friendly alternative.

\*\*Differences between packed arrays, typed arrays, and untyped
arrays:\*\* Packed arrays are generally faster to iterate on and modify
compared to a typed array of the same type (e.g.
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
versus `Array[int]`). Also, packed arrays consume less memory. As a
downside, packed arrays are less flexible as they don\'t offer as many
convenience methods such as
`Array.map<class_Array_method_map>`{.interpreted-text role="ref"}. Typed
arrays are in turn faster to iterate on and modify than untyped arrays.

\*\*Note:\*\* Packed arrays are always passed by reference. To get a
copy of an array that can be modified independently of the original
array, use
`duplicate<class_PackedInt64Array_method_duplicate>`{.interpreted-text
role="ref"}. This is *not* the case for built-in properties and methods.
The returned packed array of these are a copies, and changing it will
*not* affect the original value. To update a built-in property you need
to modify the returned array, and then assign it to the property again.

> [!NOTE]
> There are notable differences when using this API with C#. See
> `doc_c_sharp_differences`{.interpreted-text role="ref"} for more
> information.

::: {.rst-class}
classref-reftable-group
:::

## Constructors

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
classref-reftable-group
:::

## Operators

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

## Constructor Descriptions

:::: {#class_PackedInt64Array_constructor_PackedInt64Array}
::: {.rst-class}
classref-constructor
:::
::::

`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text role="ref"}
**PackedInt64Array**()
`🔗<class_PackedInt64Array_constructor_PackedInt64Array>`{.interpreted-text
role="ref"}

Constructs an empty **PackedInt64Array**.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-constructor
:::

`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text role="ref"}
**PackedInt64Array**(from:
`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text
role="ref"})

Constructs a **PackedInt64Array** as a copy of the given
**PackedInt64Array**.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-constructor
:::

`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text role="ref"}
**PackedInt64Array**(from: `Array<class_Array>`{.interpreted-text
role="ref"})

Constructs a new **PackedInt64Array**. Optionally, you can pass in a
generic `Array<class_Array>`{.interpreted-text role="ref"} that will be
converted.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_PackedInt64Array_method_append}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **append**(value:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedInt64Array_method_append>`{.interpreted-text role="ref"}

Appends an element at the end of the array (alias of
`push_back<class_PackedInt64Array_method_push_back>`{.interpreted-text
role="ref"}).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedInt64Array_method_append_array}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**append_array**(array:
`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text
role="ref"})
`🔗<class_PackedInt64Array_method_append_array>`{.interpreted-text
role="ref"}

Appends a **PackedInt64Array** at the end of this array.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedInt64Array_method_bsearch}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **bsearch**(value:
`int<class_int>`{.interpreted-text role="ref"}, before:
`bool<class_bool>`{.interpreted-text role="ref"} = true)
`🔗<class_PackedInt64Array_method_bsearch>`{.interpreted-text
role="ref"}

Finds the index of an existing value (or the insertion index that
maintains sorting order, if the value is not yet present in the array)
using binary search. Optionally, a `before` specifier can be passed. If
`false`, the returned index comes after all existing entries of the
value in the array.

\*\*Note:\*\* Calling
`bsearch<class_PackedInt64Array_method_bsearch>`{.interpreted-text
role="ref"} on an unsorted array results in unexpected behavior.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedInt64Array_method_clear}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_PackedInt64Array_method_clear>`{.interpreted-text role="ref"}

Clears the array. This is equivalent to using
`resize<class_PackedInt64Array_method_resize>`{.interpreted-text
role="ref"} with a size of `0`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedInt64Array_method_count}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **count**(value:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_PackedInt64Array_method_count>`{.interpreted-text
role="ref"}

Returns the number of times an element is in the array.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedInt64Array_method_duplicate}
::: {.rst-class}
classref-method
:::
::::

`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text role="ref"}
**duplicate**()
`🔗<class_PackedInt64Array_method_duplicate>`{.interpreted-text
role="ref"}

Creates a copy of the array, and returns it.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedInt64Array_method_fill}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **fill**(value:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedInt64Array_method_fill>`{.interpreted-text role="ref"}

Assigns the given value to all elements in the array. This can typically
be used together with
`resize<class_PackedInt64Array_method_resize>`{.interpreted-text
role="ref"} to create an array with a given size and initialized
elements.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedInt64Array_method_find}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **find**(value:
`int<class_int>`{.interpreted-text role="ref"}, from:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_PackedInt64Array_method_find>`{.interpreted-text
role="ref"}

Searches the array for a value and returns its index or `-1` if not
found. Optionally, the initial search index can be passed.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedInt64Array_method_get}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_PackedInt64Array_method_get>`{.interpreted-text
role="ref"}

Returns the 64-bit integer at the given `index` in the array. This is
the same as using the `[]` operator (`array[index]`).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedInt64Array_method_has}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has**(value:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_PackedInt64Array_method_has>`{.interpreted-text
role="ref"}

Returns `true` if the array contains `value`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedInt64Array_method_insert}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **insert**(at_index:
`int<class_int>`{.interpreted-text role="ref"}, value:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedInt64Array_method_insert>`{.interpreted-text role="ref"}

Inserts a new integer at a given position in the array. The position
must be valid, or at the end of the array (`idx == size()`).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedInt64Array_method_is_empty}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_empty**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedInt64Array_method_is_empty>`{.interpreted-text
role="ref"}

Returns `true` if the array is empty.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedInt64Array_method_push_back}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **push_back**(value:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedInt64Array_method_push_back>`{.interpreted-text
role="ref"}

Appends a value to the array.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedInt64Array_method_remove_at}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_at**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedInt64Array_method_remove_at>`{.interpreted-text
role="ref"}

Removes an element from the array by index.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedInt64Array_method_resize}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **resize**(new_size:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedInt64Array_method_resize>`{.interpreted-text role="ref"}

Sets the size of the array. If the array is grown, reserves elements at
the end of the array. If the array is shrunk, truncates the array to the
new size. Calling
`resize<class_PackedInt64Array_method_resize>`{.interpreted-text
role="ref"} once and assigning the new values is faster than adding new
elements one by one.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedInt64Array_method_reverse}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **reverse**()
`🔗<class_PackedInt64Array_method_reverse>`{.interpreted-text
role="ref"}

Reverses the order of the elements in the array.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedInt64Array_method_rfind}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **rfind**(value:
`int<class_int>`{.interpreted-text role="ref"}, from:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_PackedInt64Array_method_rfind>`{.interpreted-text
role="ref"}

Searches the array in reverse order. Optionally, a start search index
can be passed. If negative, the start index is considered relative to
the end of the array.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedInt64Array_method_set}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **set**(index:
`int<class_int>`{.interpreted-text role="ref"}, value:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedInt64Array_method_set>`{.interpreted-text role="ref"}

Changes the integer at the given index.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedInt64Array_method_size}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_PackedInt64Array_method_size>`{.interpreted-text
role="ref"}

Returns the number of elements in the array.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedInt64Array_method_slice}
::: {.rst-class}
classref-method
:::
::::

`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text role="ref"}
**slice**(begin: `int<class_int>`{.interpreted-text role="ref"}, end:
`int<class_int>`{.interpreted-text role="ref"} = 2147483647)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_PackedInt64Array_method_slice>`{.interpreted-text
role="ref"}

Returns the slice of the **PackedInt64Array**, from `begin` (inclusive)
to `end` (exclusive), as a new **PackedInt64Array**.

The absolute value of `begin` and `end` will be clamped to the array
size, so the default value for `end` makes it slice to the size of the
array by default (i.e. `arr.slice(1)` is a shorthand for
`arr.slice(1, arr.size())`).

If either `begin` or `end` are negative, they will be relative to the
end of the array (i.e. `arr.slice(0, -2)` is a shorthand for
`arr.slice(0, arr.size() - 2)`).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedInt64Array_method_sort}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **sort**()
`🔗<class_PackedInt64Array_method_sort>`{.interpreted-text role="ref"}

Sorts the elements of the array in ascending order.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedInt64Array_method_to_byte_array}
::: {.rst-class}
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**to_byte_array**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedInt64Array_method_to_byte_array>`{.interpreted-text
role="ref"}

Returns a copy of the data converted to a
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"},
where each element have been encoded as 8 bytes.

The size of the new array will be `int64_array.size() * 8`.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Operator Descriptions

:::: {#class_PackedInt64Array_operator_neq_PackedInt64Array}
::: {.rst-class}
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text
role="ref"})
`🔗<class_PackedInt64Array_operator_neq_PackedInt64Array>`{.interpreted-text
role="ref"}

Returns `true` if contents of the arrays differ.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedInt64Array_operator_sum_PackedInt64Array}
::: {.rst-class}
classref-operator
:::
::::

`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text role="ref"}
**operator +**(right:
`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text
role="ref"})
`🔗<class_PackedInt64Array_operator_sum_PackedInt64Array>`{.interpreted-text
role="ref"}

Returns a new **PackedInt64Array** with contents of `right` added at the
end of this array. For better performance, consider using
`append_array<class_PackedInt64Array_method_append_array>`{.interpreted-text
role="ref"} instead.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedInt64Array_operator_eq_PackedInt64Array}
::: {.rst-class}
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text
role="ref"})
`🔗<class_PackedInt64Array_operator_eq_PackedInt64Array>`{.interpreted-text
role="ref"}

Returns `true` if contents of both arrays are the same, i.e. they have
all equal ints at the corresponding indices.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedInt64Array_operator_idx_int}
::: {.rst-class}
classref-operator
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **operator \[\]**(index:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedInt64Array_operator_idx_int>`{.interpreted-text
role="ref"}

Returns the `int<class_int>`{.interpreted-text role="ref"} at index
`index`. Negative indices can be used to access the elements starting
from the end. Using index out of array\'s bounds will result in an
error.
