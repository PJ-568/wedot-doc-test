github_url

:   hide

# JavaClassWrapper {#class_JavaClassWrapper}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

Provides access to the Java Native Interface.

::: {.rst-class}
classref-introduction-group
:::

## Description

The JavaClassWrapper singleton provides a way for the Godot application
to send and receive data through the [Java Native
Interface](https://developer.android.com/training/articles/perf-jni)
(JNI).

\*\*Note:\*\* This singleton is only available in Android builds.

    var LocalDateTime = JavaClassWrapper.wrap("java.time.LocalDateTime")
    var DateTimeFormatter = JavaClassWrapper.wrap("java.time.format.DateTimeFormatter")

    var datetime = LocalDateTime.now()
    var formatter = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss")

    print(datetime.format(formatter))

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

:::: {#class_JavaClassWrapper_method_wrap}
::: {.rst-class}
classref-method
:::
::::

`JavaClass<class_JavaClass>`{.interpreted-text role="ref"}
**wrap**(name: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_JavaClassWrapper_method_wrap>`{.interpreted-text role="ref"}

Wraps a class defined in Java, and returns it as a
`JavaClass<class_JavaClass>`{.interpreted-text role="ref"}
`Object<class_Object>`{.interpreted-text role="ref"} type that Godot can
interact with.

\*\*Note:\*\* This method only works on Android. On every other
platform, this method does nothing and returns an empty
`JavaClass<class_JavaClass>`{.interpreted-text role="ref"}.
