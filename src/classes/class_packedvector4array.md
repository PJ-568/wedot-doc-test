github_url

:   hide

# PackedVector4Array {#class_PackedVector4Array}

A packed array of `Vector4<class_Vector4>`{.interpreted-text
role="ref"}s.

::: {.rst-class}
classref-introduction-group
:::

## Description

An array specifically designed to hold
`Vector4<class_Vector4>`{.interpreted-text role="ref"}. Packs data
tightly, so it saves memory for large array sizes.

\*\*Note:\*\* Packed arrays are always passed by reference. To get a
copy of an array that can be modified independently of the original
array, use
`duplicate<class_PackedVector4Array_method_duplicate>`{.interpreted-text
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

:::: {#class_PackedVector4Array_constructor_PackedVector4Array}
::: {.rst-class}
classref-constructor
:::
::::

`PackedVector4Array<class_PackedVector4Array>`{.interpreted-text
role="ref"} **PackedVector4Array**()
`🔗<class_PackedVector4Array_constructor_PackedVector4Array>`{.interpreted-text
role="ref"}

Constructs an empty **PackedVector4Array**.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-constructor
:::

`PackedVector4Array<class_PackedVector4Array>`{.interpreted-text
role="ref"} **PackedVector4Array**(from:
`PackedVector4Array<class_PackedVector4Array>`{.interpreted-text
role="ref"})

Constructs a **PackedVector4Array** as a copy of the given
**PackedVector4Array**.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-constructor
:::

`PackedVector4Array<class_PackedVector4Array>`{.interpreted-text
role="ref"} **PackedVector4Array**(from:
`Array<class_Array>`{.interpreted-text role="ref"})

Constructs a new **PackedVector4Array**. Optionally, you can pass in a
generic `Array<class_Array>`{.interpreted-text role="ref"} that will be
converted.

\*\*Note:\*\* When initializing a **PackedVector4Array** with elements,
it must be initialized with an `Array<class_Array>`{.interpreted-text
role="ref"} of `Vector4<class_Vector4>`{.interpreted-text role="ref"}
values:

    var array = PackedVector4Array([Vector4(12, 34, 56, 78), Vector4(90, 12, 34, 56)])

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_PackedVector4Array_method_append}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **append**(value:
`Vector4<class_Vector4>`{.interpreted-text role="ref"})
`🔗<class_PackedVector4Array_method_append>`{.interpreted-text
role="ref"}

Appends an element at the end of the array (alias of
`push_back<class_PackedVector4Array_method_push_back>`{.interpreted-text
role="ref"}).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedVector4Array_method_append_array}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**append_array**(array:
`PackedVector4Array<class_PackedVector4Array>`{.interpreted-text
role="ref"})
`🔗<class_PackedVector4Array_method_append_array>`{.interpreted-text
role="ref"}

Appends a **PackedVector4Array** at the end of this array.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedVector4Array_method_bsearch}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **bsearch**(value:
`Vector4<class_Vector4>`{.interpreted-text role="ref"}, before:
`bool<class_bool>`{.interpreted-text role="ref"} = true)
`🔗<class_PackedVector4Array_method_bsearch>`{.interpreted-text
role="ref"}

Finds the index of an existing value (or the insertion index that
maintains sorting order, if the value is not yet present in the array)
using binary search. Optionally, a `before` specifier can be passed. If
`false`, the returned index comes after all existing entries of the
value in the array.

\*\*Note:\*\* Calling
`bsearch<class_PackedVector4Array_method_bsearch>`{.interpreted-text
role="ref"} on an unsorted array results in unexpected behavior.

\*\*Note:\*\* Vectors with
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} elements don\'t behave the same as other vectors. Therefore,
the results from this method may not be accurate if NaNs are included.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedVector4Array_method_clear}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_PackedVector4Array_method_clear>`{.interpreted-text
role="ref"}

Clears the array. This is equivalent to using
`resize<class_PackedVector4Array_method_resize>`{.interpreted-text
role="ref"} with a size of `0`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedVector4Array_method_count}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **count**(value:
`Vector4<class_Vector4>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedVector4Array_method_count>`{.interpreted-text
role="ref"}

Returns the number of times an element is in the array.

\*\*Note:\*\* Vectors with
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} elements don\'t behave the same as other vectors. Therefore,
the results from this method may not be accurate if NaNs are included.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedVector4Array_method_duplicate}
::: {.rst-class}
classref-method
:::
::::

`PackedVector4Array<class_PackedVector4Array>`{.interpreted-text
role="ref"} **duplicate**()
`🔗<class_PackedVector4Array_method_duplicate>`{.interpreted-text
role="ref"}

Creates a copy of the array, and returns it.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedVector4Array_method_fill}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **fill**(value:
`Vector4<class_Vector4>`{.interpreted-text role="ref"})
`🔗<class_PackedVector4Array_method_fill>`{.interpreted-text role="ref"}

Assigns the given value to all elements in the array. This can typically
be used together with
`resize<class_PackedVector4Array_method_resize>`{.interpreted-text
role="ref"} to create an array with a given size and initialized
elements.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedVector4Array_method_find}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **find**(value:
`Vector4<class_Vector4>`{.interpreted-text role="ref"}, from:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedVector4Array_method_find>`{.interpreted-text role="ref"}

Searches the array for a value and returns its index or `-1` if not
found. Optionally, the initial search index can be passed.

\*\*Note:\*\* Vectors with
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} elements don\'t behave the same as other vectors. Therefore,
the results from this method may not be accurate if NaNs are included.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedVector4Array_method_get}
::: {.rst-class}
classref-method
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **get**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_PackedVector4Array_method_get>`{.interpreted-text
role="ref"}

Returns the `Vector4<class_Vector4>`{.interpreted-text role="ref"} at
the given `index` in the array. This is the same as using the `[]`
operator (`array[index]`).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedVector4Array_method_has}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has**(value:
`Vector4<class_Vector4>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_PackedVector4Array_method_has>`{.interpreted-text
role="ref"}

Returns `true` if the array contains `value`.

\*\*Note:\*\* Vectors with
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} elements don\'t behave the same as other vectors. Therefore,
the results from this method may not be accurate if NaNs are included.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedVector4Array_method_insert}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **insert**(at_index:
`int<class_int>`{.interpreted-text role="ref"}, value:
`Vector4<class_Vector4>`{.interpreted-text role="ref"})
`🔗<class_PackedVector4Array_method_insert>`{.interpreted-text
role="ref"}

Inserts a new element at a given position in the array. The position
must be valid, or at the end of the array (`idx == size()`).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedVector4Array_method_is_empty}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_empty**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedVector4Array_method_is_empty>`{.interpreted-text
role="ref"}

Returns `true` if the array is empty.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedVector4Array_method_push_back}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **push_back**(value:
`Vector4<class_Vector4>`{.interpreted-text role="ref"})
`🔗<class_PackedVector4Array_method_push_back>`{.interpreted-text
role="ref"}

Inserts a `Vector4<class_Vector4>`{.interpreted-text role="ref"} at the
end.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedVector4Array_method_remove_at}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_at**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedVector4Array_method_remove_at>`{.interpreted-text
role="ref"}

Removes an element from the array by index.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedVector4Array_method_resize}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **resize**(new_size:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedVector4Array_method_resize>`{.interpreted-text
role="ref"}

Sets the size of the array. If the array is grown, reserves elements at
the end of the array. If the array is shrunk, truncates the array to the
new size.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedVector4Array_method_reverse}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **reverse**()
`🔗<class_PackedVector4Array_method_reverse>`{.interpreted-text
role="ref"}

Reverses the order of the elements in the array.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedVector4Array_method_rfind}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **rfind**(value:
`Vector4<class_Vector4>`{.interpreted-text role="ref"}, from:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedVector4Array_method_rfind>`{.interpreted-text
role="ref"}

Searches the array in reverse order. Optionally, a start search index
can be passed. If negative, the start index is considered relative to
the end of the array.

\*\*Note:\*\* Vectors with
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} elements don\'t behave the same as other vectors. Therefore,
the results from this method may not be accurate if NaNs are included.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedVector4Array_method_set}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **set**(index:
`int<class_int>`{.interpreted-text role="ref"}, value:
`Vector4<class_Vector4>`{.interpreted-text role="ref"})
`🔗<class_PackedVector4Array_method_set>`{.interpreted-text role="ref"}

Changes the `Vector4<class_Vector4>`{.interpreted-text role="ref"} at
the given index.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedVector4Array_method_size}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedVector4Array_method_size>`{.interpreted-text role="ref"}

Returns the number of elements in the array.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedVector4Array_method_slice}
::: {.rst-class}
classref-method
:::
::::

`PackedVector4Array<class_PackedVector4Array>`{.interpreted-text
role="ref"} **slice**(begin: `int<class_int>`{.interpreted-text
role="ref"}, end: `int<class_int>`{.interpreted-text role="ref"} =
2147483647)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedVector4Array_method_slice>`{.interpreted-text
role="ref"}

Returns the slice of the **PackedVector4Array**, from `begin`
(inclusive) to `end` (exclusive), as a new **PackedVector4Array**.

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

:::: {#class_PackedVector4Array_method_sort}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **sort**()
`🔗<class_PackedVector4Array_method_sort>`{.interpreted-text role="ref"}

Sorts the elements of the array in ascending order.

\*\*Note:\*\* Vectors with
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} elements don\'t behave the same as other vectors. Therefore,
the results from this method may not be accurate if NaNs are included.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedVector4Array_method_to_byte_array}
::: {.rst-class}
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**to_byte_array**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedVector4Array_method_to_byte_array>`{.interpreted-text
role="ref"}

Returns a `PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"} with each vector encoded as bytes.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Operator Descriptions

:::: {#class_PackedVector4Array_operator_neq_PackedVector4Array}
::: {.rst-class}
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`PackedVector4Array<class_PackedVector4Array>`{.interpreted-text
role="ref"})
`🔗<class_PackedVector4Array_operator_neq_PackedVector4Array>`{.interpreted-text
role="ref"}

Returns `true` if contents of the arrays differ.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedVector4Array_operator_sum_PackedVector4Array}
::: {.rst-class}
classref-operator
:::
::::

`PackedVector4Array<class_PackedVector4Array>`{.interpreted-text
role="ref"} **operator +**(right:
`PackedVector4Array<class_PackedVector4Array>`{.interpreted-text
role="ref"})
`🔗<class_PackedVector4Array_operator_sum_PackedVector4Array>`{.interpreted-text
role="ref"}

Returns a new **PackedVector4Array** with contents of `right` added at
the end of this array. For better performance, consider using
`append_array<class_PackedVector4Array_method_append_array>`{.interpreted-text
role="ref"} instead.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedVector4Array_operator_eq_PackedVector4Array}
::: {.rst-class}
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`PackedVector4Array<class_PackedVector4Array>`{.interpreted-text
role="ref"})
`🔗<class_PackedVector4Array_operator_eq_PackedVector4Array>`{.interpreted-text
role="ref"}

Returns `true` if contents of both arrays are the same, i.e. they have
all equal `Vector4<class_Vector4>`{.interpreted-text role="ref"}s at the
corresponding indices.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedVector4Array_operator_idx_int}
::: {.rst-class}
classref-operator
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **operator
\[\]**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedVector4Array_operator_idx_int>`{.interpreted-text
role="ref"}

Returns the `Vector4<class_Vector4>`{.interpreted-text role="ref"} at
index `index`. Negative indices can be used to access the elements
starting from the end. Using index out of array\'s bounds will result in
an error.
