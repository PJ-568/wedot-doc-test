github_url

:   hide

# PackedDataContainerRef {#class_PackedDataContainerRef}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

An internal class used by
`PackedDataContainer<class_PackedDataContainer>`{.interpreted-text
role="ref"} to pack nested arrays and dictionaries.

::: {.rst-class}
classref-introduction-group
:::

## Description

When packing nested containers using
`PackedDataContainer<class_PackedDataContainer>`{.interpreted-text
role="ref"}, they are recursively packed into **PackedDataContainerRef**
(only applies to `Array<class_Array>`{.interpreted-text role="ref"} and
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}). Their
data can be retrieved the same way as from
`PackedDataContainer<class_PackedDataContainer>`{.interpreted-text
role="ref"}.

    var packed = PackedDataContainer.new()
    packed.pack([1, 2, 3, ["abc", "def"], 4, 5, 6])

    for element in packed:
        if element is PackedDataContainerRef:
            for subelement in element:
                print("::", subelement)
        else:
            print(element)

    # Prints:
    # 1
    # 2
    # 3
    # ::abc
    # ::def
    # 4
    # 5
    # 6

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

:::: {#class_PackedDataContainerRef_method_size}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedDataContainerRef_method_size>`{.interpreted-text
role="ref"}

Returns the size of the packed container (see
`Array.size<class_Array_method_size>`{.interpreted-text role="ref"} and
`Dictionary.size<class_Dictionary_method_size>`{.interpreted-text
role="ref"}).
